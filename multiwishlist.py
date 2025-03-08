import requests
import base64
import steammessages_storebrowse.steamclient_pb2 as storebrowse_pb2
from google.protobuf.json_format import MessageToDict
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

app = Flask(__name__)

GET_ITEMS_REQUEST_LIMIT = 50
BASE_URL = "https://api.steampowered.com"

load_dotenv()
STEAM_API_KEY = os.getenv('STEAM_API_KEY')

# obtener uint64 de usuario
def get_steam_id_from_vanityUrl(vanityUrl):
    try:
        response = requests.get(
            f"{BASE_URL}/ISteamUser/ResolveVanityURL/v1",
            params ={
                "key": STEAM_API_KEY,
                "vanityurl": vanityUrl
            }
        )
        response.raise_for_status()
        data = response.json()
        if data['response']['success'] == 1:
            steamid = data['response']['steamid']
            return steamid
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al resolver vanityUrl: {e}")
        return None
    
# obtener datos de usuario
def get_steam_user_details(steamid):
    try:
        response = requests.get(
            f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v2",
            params ={
                "key": STEAM_API_KEY,
                "steamid": steamid
            }
        )
        response.raise_for_status()
        data = response.json()
        player = data['response']['players'][0]

        personaname = player.get('personaname')
        country = player.get('loccountrycode')
        avatar = player.get('avatar')

        return {
            'personaname': personaname,
            'loccountrycode': country,
            'avatar': avatar
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener detalles del usuario: {e}")
        return None

# obtener la wishlist
def get_wishlist(steamid):
    try:
        response = requests.get(
            f"{BASE_URL}/IWishlistService/GetWishlist/v1/", 
            params={"steamid": steamid}
        )
        response.raise_for_status()
        data = response.json()
        wishlist_items = data.get("response", {}).get("items", [])
        return wishlist_items
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la wishlist: {e}")
        return []

# obtener los items
def get_items_info(app_ids, country_code):
    items = []

    for i in range(0, len(app_ids), GET_ITEMS_REQUEST_LIMIT):
        requested_app_ids = app_ids[i:i + GET_ITEMS_REQUEST_LIMIT]
        get_items_request = storebrowse_pb2.CStoreBrowse_GetItems_Request(
            ids=[storebrowse_pb2.StoreItemID(appid=app_id) for app_id in requested_app_ids],
            context=storebrowse_pb2.StoreBrowseContext(
                language="english",
                country_code=country_code
            ),
            data_request=storebrowse_pb2.StoreBrowseItemDataRequest(
                include_release=True,
                include_basic_info=True,
                include_all_purchase_options=True,
                include_assets=True
            ),
        )
        get_items_request_buffer = get_items_request.SerializeToString()
        input_protobuf_encoded = base64.b64encode(get_items_request_buffer).decode("utf-8")

        try:
            response = requests.get(
                f"{BASE_URL}/IStoreBrowseService/GetItems/v1",
                params={"input_protobuf_encoded": input_protobuf_encoded},
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            get_items_response = storebrowse_pb2.CStoreBrowse_GetItems_Response()
            get_items_response.ParseFromString(response.content)
            get_items_response_object = MessageToDict(get_items_response)
            items.extend(get_items_response_object['storeItems'])

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los items: {e}")
            return None
        
    return items

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        wishlist_items = get_wishlist(get_steam_id_from_vanityUrl(request.form.get('input')))
        app_ids = [item['appid'] for item in wishlist_items if 'appid' in item]
        country_code = "AR"

        items = get_items_info(app_ids, country_code)
        items_info = []
        #!!!!!!!! LO DEJÉ ACÁ 
        #último pensamiento: hacer una matriz dodne usuario 1-datosUser1 2-datosUser2.. etc , de la misma manera tal vez deba hacer con los juegos.
        user_details = []

        for item in items:
            appid = item.get('appid')
            name = item.get('name')

            # Si el juego ya no existe, assets lanza error.
            assets = item.get('assets', {})
            header_image_filename = assets.get('header')
            if header_image_filename:
                base_url = "https://steamcdn-a.akamaihd.net"
                image_url = f"{base_url}/steam/apps/{appid}/{header_image_filename}?t=1739400994"
            else:
                image_url = None

            is_free = item.get('isFree')
            normal_price = None
            sale_price = None
            discount_pct = None
            
            for option in item.get('purchaseOptions', []):
                if 'packageid' in option:
                    if 'formattedOriginalPrice' not in option:
                        normal_price = option.get('formattedFinalPrice')
                        break
                    else:
                        normal_price = option.get('formattedOriginalPrice')
                        sale_price = option.get('formattedFinalPrice')
                        discount_pct = option.get('discountPct')
                        break

            if sale_price == None or is_free:
                sale_price = "-"

            items_info.append({
                'appid': appid,
                'name': name,
                'header_image': image_url,
                'is_free': is_free,
                'normal_price': normal_price,
                'sale_price': sale_price,
                'discount_pct': discount_pct,
                #'shared_wish': 
            })
        return render_template('index.html', items_info=items_info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
