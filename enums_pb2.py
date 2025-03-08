# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: enums.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'enums.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_base_pb2 as steammessages__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65nums.proto\x1a\x18steammessages_base.proto*\x80\n\n\x17\x45PublishedFileQueryType\x12)\n%k_PublishedFileQueryType_RankedByVote\x10\x00\x12\x34\n0k_PublishedFileQueryType_RankedByPublicationDate\x10\x01\x12\x42\n>k_PublishedFileQueryType_AcceptedForGameRankedByAcceptanceDate\x10\x02\x12*\n&k_PublishedFileQueryType_RankedByTrend\x10\x03\x12\x46\nBk_PublishedFileQueryType_FavoritedByFriendsRankedByPublicationDate\x10\x04\x12\x44\n@k_PublishedFileQueryType_CreatedByFriendsRankedByPublicationDate\x10\x05\x12\x35\n1k_PublishedFileQueryType_RankedByNumTimesReported\x10\x06\x12J\nFk_PublishedFileQueryType_CreatedByFollowedUsersRankedByPublicationDate\x10\x07\x12(\n$k_PublishedFileQueryType_NotYetRated\x10\x08\x12=\n9k_PublishedFileQueryType_RankedByTotalUniqueSubscriptions\x10\t\x12\x32\n.k_PublishedFileQueryType_RankedByTotalVotesAsc\x10\n\x12,\n(k_PublishedFileQueryType_RankedByVotesUp\x10\x0b\x12/\n+k_PublishedFileQueryType_RankedByTextSearch\x10\x0c\x12\x32\n.k_PublishedFileQueryType_RankedByPlaytimeTrend\x10\r\x12\x32\n.k_PublishedFileQueryType_RankedByTotalPlaytime\x10\x0e\x12\x39\n5k_PublishedFileQueryType_RankedByAveragePlaytimeTrend\x10\x0f\x12<\n8k_PublishedFileQueryType_RankedByLifetimeAveragePlaytime\x10\x10\x12:\n6k_PublishedFileQueryType_RankedByPlaytimeSessionsTrend\x10\x11\x12=\n9k_PublishedFileQueryType_RankedByLifetimePlaytimeSessions\x10\x12\x12?\n;k_PublishedFileQueryType_RankedByInappropriateContentRating\x10\x13\x12\x34\n0k_PublishedFileQueryType_RankedByBanContentCheck\x10\x14\x12\x34\n0k_PublishedFileQueryType_RankedByLastUpdatedDate\x10\x15*\xbc\x01\n#EPublishedFileInappropriateProvider\x12\x31\n-k_EPublishedFileInappropriateProvider_Invalid\x10\x00\x12\x30\n,k_EPublishedFileInappropriateProvider_Google\x10\x01\x12\x30\n,k_EPublishedFileInappropriateProvider_Amazon\x10\x02*\xd5\x02\n!EPublishedFileInappropriateResult\x12\x32\n.k_EPublishedFileInappropriateResult_NotScanned\x10\x00\x12\x34\n0k_EPublishedFileInappropriateResult_VeryUnlikely\x10\x01\x12\x30\n,k_EPublishedFileInappropriateResult_Unlikely\x10\x1e\x12\x30\n,k_EPublishedFileInappropriateResult_Possible\x10\x32\x12.\n*k_EPublishedFileInappropriateResult_Likely\x10K\x12\x32\n.k_EPublishedFileInappropriateResult_VeryLikely\x10\x64*\xb1\x03\n\x11\x45PersonaStateFlag\x12\'\n#k_EPersonaStateFlag_HasRichPresence\x10\x01\x12&\n\"k_EPersonaStateFlag_InJoinableGame\x10\x02\x12\x1e\n\x1ak_EPersonaStateFlag_Golden\x10\x04\x12*\n&k_EPersonaStateFlag_RemotePlayTogether\x10\x08\x12&\n!k_EPersonaStateFlag_ClientTypeWeb\x10\x80\x02\x12)\n$k_EPersonaStateFlag_ClientTypeMobile\x10\x80\x04\x12*\n%k_EPersonaStateFlag_ClientTypeTenfoot\x10\x80\x08\x12%\n k_EPersonaStateFlag_ClientTypeVR\x10\x80\x10\x12*\n%k_EPersonaStateFlag_LaunchTypeGamepad\x10\x80 \x12-\n(k_EPersonaStateFlag_LaunchTypeCompatTool\x10\x80@*\xb0\x02\n\x15\x45\x43ontentCheckProvider\x12#\n\x1fk_EContentCheckProvider_Invalid\x10\x00\x12-\n)k_EContentCheckProvider_Google_DEPRECATED\x10\x01\x12\"\n\x1ek_EContentCheckProvider_Amazon\x10\x02\x12!\n\x1dk_EContentCheckProvider_Local\x10\x03\x12*\n&k_EContentCheckProvider_GoogleVertexAI\x10\x04\x12(\n$k_EContentCheckProvider_GoogleGemini\x10\x05\x12&\n\"k_EContentCheckProvider_SteamLearn\x10\x06*\x93\t\n\x19\x45ProfileCustomizationType\x12&\n\"k_EProfileCustomizationTypeInvalid\x10\x00\x12\x36\n2k_EProfileCustomizationTypeRareAchievementShowcase\x10\x01\x12,\n(k_EProfileCustomizationTypeGameCollector\x10\x02\x12+\n\'k_EProfileCustomizationTypeItemShowcase\x10\x03\x12,\n(k_EProfileCustomizationTypeTradeShowcase\x10\x04\x12%\n!k_EProfileCustomizationTypeBadges\x10\x05\x12+\n\'k_EProfileCustomizationTypeFavoriteGame\x10\x06\x12\x31\n-k_EProfileCustomizationTypeScreenshotShowcase\x10\x07\x12)\n%k_EProfileCustomizationTypeCustomText\x10\x08\x12,\n(k_EProfileCustomizationTypeFavoriteGroup\x10\t\x12-\n)k_EProfileCustomizationTypeRecommendation\x10\n\x12+\n\'k_EProfileCustomizationTypeWorkshopItem\x10\x0b\x12)\n%k_EProfileCustomizationTypeMyWorkshop\x10\x0c\x12.\n*k_EProfileCustomizationTypeArtworkShowcase\x10\r\x12,\n(k_EProfileCustomizationTypeVideoShowcase\x10\x0e\x12%\n!k_EProfileCustomizationTypeGuides\x10\x0f\x12\'\n#k_EProfileCustomizationTypeMyGuides\x10\x10\x12+\n\'k_EProfileCustomizationTypeAchievements\x10\x11\x12)\n%k_EProfileCustomizationTypeGreenlight\x10\x12\x12+\n\'k_EProfileCustomizationTypeMyGreenlight\x10\x13\x12%\n!k_EProfileCustomizationTypeSalien\x10\x14\x12\x35\n1k_EProfileCustomizationTypeLoyaltyRewardReactions\x10\x15\x12\x34\n0k_EProfileCustomizationTypeSingleArtworkShowcase\x10\x16\x12\x38\n4k_EProfileCustomizationTypeAchievementsCompletionist\x10\x17\x12%\n!k_EProfileCustomizationTypeReplay\x10\x18*\xc8\x01\n\x1b\x45PublishedFileStorageSystem\x12(\n$k_EPublishedFileStorageSystemInvalid\x10\x00\x12,\n(k_EPublishedFileStorageSystemLegacyCloud\x10\x01\x12&\n\"k_EPublishedFileStorageSystemDepot\x10\x02\x12)\n%k_EPublishedFileStorageSystemUGCCloud\x10\x03*\x97\x01\n\x19\x45\x43loudStoragePersistState\x12(\n$k_ECloudStoragePersistStatePersisted\x10\x00\x12(\n$k_ECloudStoragePersistStateForgotten\x10\x01\x12&\n\"k_ECloudStoragePersistStateDeleted\x10\x02*\xe8\x01\n\x12\x45SDCardFormatStage\x12 \n\x1ck_ESDCardFormatStage_Invalid\x10\x00\x12!\n\x1dk_ESDCardFormatStage_Starting\x10\x01\x12 \n\x1ck_ESDCardFormatStage_Testing\x10\x02\x12!\n\x1dk_ESDCardFormatStage_Rescuing\x10\x03\x12#\n\x1fk_ESDCardFormatStage_Formatting\x10\x04\x12#\n\x1fk_ESDCardFormatStage_Finalizing\x10\x05*\x95\x02\n\x13\x45StorageFormatStage\x12!\n\x1dk_EStorageFormatStage_Invalid\x10\x00\x12$\n k_EStorageFormatStage_NotRunning\x10\x01\x12\"\n\x1ek_EStorageFormatStage_Starting\x10\x02\x12!\n\x1dk_EStorageFormatStage_Testing\x10\x03\x12\"\n\x1ek_EStorageFormatStage_Rescuing\x10\x04\x12$\n k_EStorageFormatStage_Formatting\x10\x05\x12$\n k_EStorageFormatStage_Finalizing\x10\x06*\x84\x01\n\x15\x45SystemFanControlMode\x12\"\n\x1ek_SystemFanControlMode_Invalid\x10\x00\x12#\n\x1fk_SystemFanControlMode_Disabled\x10\x01\x12\"\n\x1ek_SystemFanControlMode_Default\x10\x02*\xaa\x01\n\x14\x45StartupMovieVariant\x12\"\n\x1ek_EStartupMovieVariant_Invalid\x10\x00\x12\"\n\x1ek_EStartupMovieVariant_Generic\x10\x01\x12#\n\x1fk_EStartupMovieVariant_DeckBlue\x10\x02\x12%\n!k_EStartupMovieVariant_DeckOrange\x10\x03*\x8b\x01\n\x13\x45\x43olorGamutLabelSet\x12 \n\x1ck_ColorGamutLabelSet_Default\x10\x00\x12$\n k_ColorGamutLabelSet_sRGB_Native\x10\x01\x12,\n(k_ColorGamutLabelSet_Native_sRGB_Boosted\x10\x02*}\n\x14\x45WindowStackingOrder\x12\"\n\x1ek_EWindowStackingOrder_Invalid\x10\x00\x12\x1e\n\x1ak_EWindowStackingOrder_Top\x10\x01\x12!\n\x1dk_EWindowStackingOrder_Bottom\x10\x02*\xc0\x03\n\x14\x45\x42luetoothDeviceType\x12!\n\x1dk_BluetoothDeviceType_Invalid\x10\x00\x12!\n\x1dk_BluetoothDeviceType_Unknown\x10\x01\x12\x1f\n\x1bk_BluetoothDeviceType_Phone\x10\x02\x12\"\n\x1ek_BluetoothDeviceType_Computer\x10\x03\x12!\n\x1dk_BluetoothDeviceType_Headset\x10\x04\x12$\n k_BluetoothDeviceType_Headphones\x10\x05\x12\"\n\x1ek_BluetoothDeviceType_Speakers\x10\x06\x12$\n k_BluetoothDeviceType_OtherAudio\x10\x07\x12\x1f\n\x1bk_BluetoothDeviceType_Mouse\x10\x08\x12\"\n\x1ek_BluetoothDeviceType_Joystick\x10\t\x12!\n\x1dk_BluetoothDeviceType_Gamepad\x10\n\x12\"\n\x1ek_BluetoothDeviceType_Keyboard\x10\x0b*\x80\x01\n\x15\x45SystemAudioDirection\x12\"\n\x1ek_SystemAudioDirection_Invalid\x10\x00\x12 \n\x1ck_SystemAudioDirection_Input\x10\x01\x12!\n\x1dk_SystemAudioDirection_Output\x10\x02*\xf1\x02\n\x13\x45SystemAudioChannel\x12 \n\x1ck_SystemAudioChannel_Invalid\x10\x00\x12#\n\x1fk_SystemAudioChannel_Aggregated\x10\x01\x12\"\n\x1ek_SystemAudioChannel_FrontLeft\x10\x02\x12#\n\x1fk_SystemAudioChannel_FrontRight\x10\x03\x12\x1c\n\x18k_SystemAudioChannel_LFE\x10\x04\x12!\n\x1dk_SystemAudioChannel_BackLeft\x10\x05\x12\"\n\x1ek_SystemAudioChannel_BackRight\x10\x06\x12$\n k_SystemAudioChannel_FrontCenter\x10\x07\x12 \n\x1ck_SystemAudioChannel_Unknown\x10\x08\x12\x1d\n\x19k_SystemAudioChannel_Mono\x10\t*\xc9\x01\n\x14\x45SystemAudioPortType\x12!\n\x1dk_SystemAudioPortType_Invalid\x10\x00\x12!\n\x1dk_SystemAudioPortType_Unknown\x10\x01\x12\"\n\x1ek_SystemAudioPortType_Audio32f\x10\x02\x12 \n\x1ck_SystemAudioPortType_Midi8b\x10\x03\x12%\n!k_SystemAudioPortType_Video32RGBA\x10\x04*\x90\x01\n\x19\x45SystemAudioPortDirection\x12&\n\"k_SystemAudioPortDirection_Invalid\x10\x00\x12$\n k_SystemAudioPortDirection_Input\x10\x01\x12%\n!k_SystemAudioPortDirection_Output\x10\x02*\x83\x01\n\x13\x45SystemServiceState\x12%\n!k_ESystemServiceState_Unavailable\x10\x00\x12\"\n\x1ek_ESystemServiceState_Disabled\x10\x01\x12!\n\x1dk_ESystemServiceState_Enabled\x10\x02*\xe1\x01\n\x19\x45GraphicsPerfOverlayLevel\x12&\n\"k_EGraphicsPerfOverlayLevel_Hidden\x10\x00\x12%\n!k_EGraphicsPerfOverlayLevel_Basic\x10\x01\x12&\n\"k_EGraphicsPerfOverlayLevel_Medium\x10\x02\x12$\n k_EGraphicsPerfOverlayLevel_Full\x10\x03\x12\'\n#k_EGraphicsPerfOverlayLevel_Minimal\x10\x04*\xe5\x01\n\x14\x45GPUPerformanceLevel\x12\"\n\x1ek_EGPUPerformanceLevel_Invalid\x10\x00\x12\x1f\n\x1bk_EGPUPerformanceLevel_Auto\x10\x01\x12!\n\x1dk_EGPUPerformanceLevel_Manual\x10\x02\x12\x1e\n\x1ak_EGPUPerformanceLevel_Low\x10\x03\x12\x1f\n\x1bk_EGPUPerformanceLevel_High\x10\x04\x12$\n k_EGPUPerformanceLevel_Profiling\x10\x05*\xbb\x01\n\x0e\x45ScalingFilter\x12\x1c\n\x18k_EScalingFilter_Invalid\x10\x00\x12\x18\n\x14k_EScalingFilter_FSR\x10\x01\x12\x1c\n\x18k_EScalingFilter_Nearest\x10\x02\x12\x1c\n\x18k_EScalingFilter_Integer\x10\x03\x12\x1b\n\x17k_EScalingFilter_Linear\x10\x04\x12\x18\n\x14k_EScalingFilter_NIS\x10\x05*\xbb\x01\n\x13\x45SplitScalingFilter\x12!\n\x1dk_ESplitScalingFilter_Invalid\x10\x00\x12 \n\x1ck_ESplitScalingFilter_Linear\x10\x01\x12!\n\x1dk_ESplitScalingFilter_Nearest\x10\x02\x12\x1d\n\x19k_ESplitScalingFilter_FSR\x10\x03\x12\x1d\n\x19k_ESplitScalingFilter_NIS\x10\x04*\xdd\x01\n\x13\x45SplitScalingScaler\x12!\n\x1dk_ESplitScalingScaler_Invalid\x10\x00\x12\x1e\n\x1ak_ESplitScalingScaler_Auto\x10\x01\x12!\n\x1dk_ESplitScalingScaler_Integer\x10\x02\x12\x1d\n\x19k_ESplitScalingScaler_Fit\x10\x03\x12\x1e\n\x1ak_ESplitScalingScaler_Fill\x10\x04\x12!\n\x1dk_ESplitScalingScaler_Stretch\x10\x05*}\n\x12\x45GamescopeBlurMode\x12!\n\x1dk_EGamescopeBlurMode_Disabled\x10\x00\x12#\n\x1fk_EGamescopeBlurMode_IfOccluded\x10\x01\x12\x1f\n\x1bk_EGamescopeBlurMode_Always\x10\x02*\xa6\x01\n\nESLSHelper\x12\x18\n\x14k_ESLSHelper_Invalid\x10\x00\x12\x19\n\x15k_ESLSHelper_Minidump\x10\x01\x12\x16\n\x12k_ESLSHelper_Kdump\x10\x02\x12\x18\n\x14k_ESLSHelper_Journal\x10\x03\x12\x14\n\x10k_ESLSHelper_Gpu\x10\x04\x12\x1b\n\x17k_ESLSHelper_SystemInfo\x10\x05*\xc5\x01\n\x11\x45HDRVisualization\x12\x1c\n\x18k_EHDRVisualization_None\x10\x00\x12\x1f\n\x1bk_EHDRVisualization_Heatmap\x10\x01\x12 \n\x1ck_EHDRVisualization_Analysis\x10\x02\x12\'\n#k_EHDRVisualization_HeatmapExtended\x10\x03\x12&\n\"k_EHDRVisualization_HeatmapClassic\x10\x04*\x81\x01\n\x13\x45HDRToneMapOperator\x12!\n\x1dk_EHDRToneMapOperator_Invalid\x10\x00\x12#\n\x1fk_EHDRToneMapOperator_Uncharted\x10\x01\x12\"\n\x1ek_EHDRToneMapOperator_Reinhard\x10\x02*|\n\x0c\x45\x43PUGovernor\x12\x1a\n\x16k_ECPUGovernor_Invalid\x10\x00\x12\x17\n\x13k_ECPUGovernor_Perf\x10\x01\x12\x1c\n\x18k_ECPUGovernor_Powersave\x10\x02\x12\x19\n\x15k_ECPUGovernor_Manual\x10\x03*\xe2\x01\n\x0c\x45UpdaterType\x12\x1a\n\x16k_EUpdaterType_Invalid\x10\x00\x12\x19\n\x15k_EUpdaterType_Client\x10\x01\x12\x15\n\x11k_EUpdaterType_OS\x10\x02\x12\x17\n\x13k_EUpdaterType_BIOS\x10\x03\x12\x1d\n\x19k_EUpdaterType_Aggregated\x10\x04\x12\x18\n\x14k_EUpdaterType_Test1\x10\x05\x12\x18\n\x14k_EUpdaterType_Test2\x10\x06\x12\x18\n\x14k_EUpdaterType_Dummy\x10\x07*\x97\x02\n\rEUpdaterState\x12\x1b\n\x17k_EUpdaterState_Invalid\x10\x00\x12\x1c\n\x18k_EUpdaterState_UpToDate\x10\x02\x12\x1c\n\x18k_EUpdaterState_Checking\x10\x03\x12\x1d\n\x19k_EUpdaterState_Available\x10\x04\x12\x1c\n\x18k_EUpdaterState_Applying\x10\x05\x12(\n$k_EUpdaterState_ClientRestartPending\x10\x06\x12(\n$k_EUpdaterState_SystemRestartPending\x10\x07\x12\x1c\n\x18k_EUpdaterState_RollBack\x10\x08*\xe1\x01\n\x18\x45StorageBlockContentType\x12&\n\"k_EStorageBlockContentType_Invalid\x10\x00\x12&\n\"k_EStorageBlockContentType_Unknown\x10\x01\x12)\n%k_EStorageBlockContentType_FileSystem\x10\x02\x12%\n!k_EStorageBlockContentType_Crypto\x10\x03\x12#\n\x1fk_EStorageBlockContentType_Raid\x10\x04*\xc3\x01\n\x1b\x45StorageBlockFileSystemType\x12)\n%k_EStorageBlockFileSystemType_Invalid\x10\x00\x12)\n%k_EStorageBlockFileSystemType_Unknown\x10\x01\x12&\n\"k_EStorageBlockFileSystemType_VFat\x10\x02\x12&\n\"k_EStorageBlockFileSystemType_Ext4\x10\x03*\xd0\x01\n\x16\x45StorageDriveMediaType\x12$\n k_EStorageDriveMediaType_Invalid\x10\x00\x12$\n k_EStorageDriveMediaType_Unknown\x10\x01\x12 \n\x1ck_EStorageDriveMediaType_HDD\x10\x02\x12 \n\x1ck_EStorageDriveMediaType_SSD\x10\x03\x12&\n\"k_EStorageDriveMediaType_Removable\x10\x04*\xb3\x01\n\x1f\x45SystemDisplayCompatibilityMode\x12-\n)k_ESystemDisplayCompatibilityMode_Invalid\x10\x00\x12*\n&k_ESystemDisplayCompatibilityMode_None\x10\x01\x12\x35\n1k_ESystemDisplayCompatibilityMode_MinimalBandwith\x10\x02*\xe3\x01\n\x1f\x45SteamDeckCompatibilityCategory\x12-\n)k_ESteamDeckCompatibilityCategory_Unknown\x10\x00\x12\x31\n-k_ESteamDeckCompatibilityCategory_Unsupported\x10\x01\x12.\n*k_ESteamDeckCompatibilityCategory_Playable\x10\x02\x12.\n*k_ESteamDeckCompatibilityCategory_Verified\x10\x03*\xd0\x02\n(ESteamDeckCompatibilityResultDisplayType\x12\x38\n4k_ESteamDeckCompatibilityResultDisplayType_Invisible\x10\x00\x12<\n8k_ESteamDeckCompatibilityResultDisplayType_Informational\x10\x01\x12:\n6k_ESteamDeckCompatibilityResultDisplayType_Unsupported\x10\x02\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Playable\x10\x03\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Verified\x10\x04*\x9a\x02\n!ESteamDeckCompatibilityTestResult\x12/\n+k_ESteamDeckCompatibilityTestResult_Invalid\x10\x00\x12\x35\n1k_ESteamDeckCompatibilityTestResult_NotApplicable\x10\x01\x12,\n(k_ESteamDeckCompatibilityTestResult_Pass\x10\x02\x12,\n(k_ESteamDeckCompatibilityTestResult_Fail\x10\x03\x12\x31\n-k_ESteamDeckCompatibilityTestResult_FailMinor\x10\x04*w\n\x08\x45\x41\x43State\x12\x16\n\x12k_EACState_Unknown\x10\x00\x12\x1b\n\x17k_EACState_Disconnected\x10\x01\x12\x18\n\x14k_EACState_Connected\x10\x02\x12\x1c\n\x18k_EACState_ConnectedSlow\x10\x03*\x85\x01\n\rEBatteryState\x12\x1b\n\x17k_EBatteryState_Unknown\x10\x00\x12\x1f\n\x1bk_EBatteryState_Discharging\x10\x01\x12\x1c\n\x18k_EBatteryState_Charging\x10\x02\x12\x18\n\x14k_EBatteryState_Full\x10\x03*\xfe\x01\n\tEOSBranch\x12\x17\n\x13k_EOSBranch_Unknown\x10\x00\x12\x17\n\x13k_EOSBranch_Release\x10\x01\x12 \n\x1ck_EOSBranch_ReleaseCandidate\x10\x02\x12\x14\n\x10k_EOSBranch_Beta\x10\x03\x12\x1d\n\x19k_EOSBranch_BetaCandidate\x10\x04\x12\x17\n\x13k_EOSBranch_Preview\x10\x05\x12 \n\x1ck_EOSBranch_PreviewCandidate\x10\x06\x12\x14\n\x10k_EOSBranch_Main\x10\x07\x12\x17\n\x13k_EOSBranch_Staging\x10\x08*\xc6\x03\n\x11\x45\x42rowserGPUStatus\x12\x1f\n\x1bk_EBrowserGPUStatus_Invalid\x10\x00\x12\x1f\n\x1bk_EBrowserGPUStatus_Enabled\x10\x01\x12\'\n#k_EBrowserGPUStatus_DisabledUnknown\x10\x02\x12*\n&k_EBrowserGPUStatus_DisabledCrashCount\x10\x04\x12)\n%k_EBrowserGPUStatus_DisabledBlocklist\x10\x05\x12)\n%k_EBrowserGPUStatus_DisabledJSRequest\x10\x06\x12+\n\'k_EBrowserGPUStatus_DisabledCommandLine\x10\x07\x12-\n)k_EBrowserGPUStatus_DisabledRuntimeDetect\x10\x08\x12\x30\n,k_EBrowserGPUStatus_DisabledChildCommandLine\x10\t\x12\x36\n2k_EBrowserGPUStatus_DisabledCompositingCommandLine\x10\n*\xe3\x04\n\x15\x45\x42rowserFeatureStatus\x12#\n\x1fk_EBrowserFeatureStatus_Invalid\x10\x00\x12$\n k_EBrowserFeatureStatus_NotFound\x10\x01\x12#\n\x1fk_EBrowserFeatureStatus_Unknown\x10\x02\x12,\n(k_EBrowserFeatureStatus_DisabledSoftware\x10\x03\x12\'\n#k_EBrowserFeatureStatus_DisabledOff\x10\x04\x12)\n%k_EBrowserFeatureStatus_DisabledOffOk\x10\x05\x12/\n+k_EBrowserFeatureStatus_UnavailableSoftware\x10\x06\x12*\n&k_EBrowserFeatureStatus_UnavailableOff\x10\x07\x12,\n(k_EBrowserFeatureStatus_UnavailableOffOk\x10\x08\x12+\n\'k_EBrowserFeatureStatus_EnabledReadback\x10\t\x12(\n$k_EBrowserFeatureStatus_EnabledForce\x10\n\x12#\n\x1fk_EBrowserFeatureStatus_Enabled\x10\x0b\x12%\n!k_EBrowserFeatureStatus_EnabledOn\x10\x0c\x12*\n&k_EBrowserFeatureStatus_EnabledForceOn\x10\r*\x9f\x05\n\x0c\x45GpuDriverId\x12\x1a\n\x16k_EGpuDriverId_Invalid\x10\x00\x12\x1a\n\x16k_EGpuDriverId_Unknown\x10\x01\x12!\n\x1dk_EGpuDriverId_AmdProprietary\x10\x02\x12 \n\x1ck_EGpuDriverId_AmdOpenSource\x10\x03\x12\x1b\n\x17k_EGpuDriverId_MesaRadv\x10\x04\x12$\n k_EGpuDriverId_NvidiaProprietary\x10\x05\x12\"\n\x1ek_EGpuDriverId_IntelPropietary\x10\x06\x12\x1c\n\x18k_EGpuDriverId_MesaIntel\x10\x07\x12&\n\"k_EGpuDriverId_QualcommProprietary\x10\x08\x12!\n\x1dk_EGpuDriverId_ArmProprietary\x10\t\x12$\n k_EGpuDriverId_GoogleSwiftshader\x10\n\x12&\n\"k_EGpuDriverId_BroadcomProprietary\x10\x0b\x12\x1f\n\x1bk_EGpuDriverId_MesaLLVMPipe\x10\x0c\x12\x1b\n\x17k_EGpuDriverId_MoltenVK\x10\r\x12\x1d\n\x19k_EGpuDriverId_MesaTurnip\x10\x0e\x12\x1c\n\x18k_EGpuDriverId_MesaPanVK\x10\x0f\x12\x1c\n\x18k_EGpuDriverId_MesaVenus\x10\x10\x12\x1c\n\x18k_EGpuDriverId_MesaDozen\x10\x11\x12\x1a\n\x16k_EGpuDriverId_MesaNVK\x10\x12\x12!\n\x1dk_EGpuDriverId_MesaHoneyKrisp\x10\x13*\xdd\x05\n\x13\x45\x43ommunityItemClass\x12!\n\x1dk_ECommunityItemClass_Invalid\x10\x00\x12\x1f\n\x1bk_ECommunityItemClass_Badge\x10\x01\x12\"\n\x1ek_ECommunityItemClass_GameCard\x10\x02\x12+\n\'k_ECommunityItemClass_ProfileBackground\x10\x03\x12\"\n\x1ek_ECommunityItemClass_Emoticon\x10\x04\x12%\n!k_ECommunityItemClass_BoosterPack\x10\x05\x12$\n k_ECommunityItemClass_Consumable\x10\x06\x12!\n\x1dk_ECommunityItemClass_GameGoo\x10\x07\x12)\n%k_ECommunityItemClass_ProfileModifier\x10\x08\x12\x1f\n\x1bk_ECommunityItemClass_Scene\x10\t\x12$\n k_ECommunityItemClass_SalienItem\x10\n\x12!\n\x1dk_ECommunityItemClass_Sticker\x10\x0b\x12$\n k_ECommunityItemClass_ChatEffect\x10\x0c\x12/\n+k_ECommunityItemClass_MiniProfileBackground\x10\r\x12%\n!k_ECommunityItemClass_AvatarFrame\x10\x0e\x12(\n$k_ECommunityItemClass_AnimatedAvatar\x10\x0f\x12/\n+k_ECommunityItemClass_SteamDeckKeyboardSkin\x10\x10\x12/\n+k_ECommunityItemClass_SteamDeckStartupMovie\x10\x11*\xd9\x01\n\x1f\x45SteamDeckCompatibilityFeedback\x12+\n\'k_ESteamDeckCompatibilityFeedback_Unset\x10\x00\x12+\n\'k_ESteamDeckCompatibilityFeedback_Agree\x10\x01\x12.\n*k_ESteamDeckCompatibilityFeedback_Disagree\x10\x02\x12,\n(k_ESteamDeckCompatibilityFeedback_Ignore\x10\x03*\x9f\x01\n\x1e\x45ProvideDeckFeedbackPreference\x12*\n&k_EProvideDeckFeedbackPreference_Unset\x10\x00\x12(\n$k_EProvideDeckFeedbackPreference_Yes\x10\x01\x12\'\n#k_EProvideDeckFeedbackPreference_No\x10\x02*\xb1\x03\n\rETouchGesture\x12\x17\n\x13k_ETouchGestureNone\x10\x00\x12\x18\n\x14k_ETouchGestureTouch\x10\x01\x12\x16\n\x12k_ETouchGestureTap\x10\x02\x12\x1c\n\x18k_ETouchGestureDoubleTap\x10\x03\x12\x1d\n\x19k_ETouchGestureShortPress\x10\x04\x12\x1c\n\x18k_ETouchGestureLongPress\x10\x05\x12\x1a\n\x16k_ETouchGestureLongTap\x10\x06\x12\x1f\n\x1bk_ETouchGestureTwoFingerTap\x10\x07\x12\x1f\n\x1bk_ETouchGestureTapCancelled\x10\x08\x12\x1d\n\x19k_ETouchGesturePinchBegin\x10\t\x12\x1e\n\x1ak_ETouchGesturePinchUpdate\x10\n\x12\x1b\n\x17k_ETouchGesturePinchEnd\x10\x0b\x12\x1d\n\x19k_ETouchGestureFlingStart\x10\x0c\x12!\n\x1dk_ETouchGestureFlingCancelled\x10\r*\x8c\x01\n\x13\x45SessionPersistence\x12*\n\x1dk_ESessionPersistence_Invalid\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fk_ESessionPersistence_Ephemeral\x10\x00\x12$\n k_ESessionPersistence_Persistent\x10\x01*\xd9\x01\n\x1a\x45NewSteamAnnouncementState\x12(\n$k_ENewSteamAnnouncementState_Invalid\x10\x00\x12(\n$k_ENewSteamAnnouncementState_AllRead\x10\x01\x12\x30\n,k_ENewSteamAnnouncementState_NewAnnouncement\x10\x02\x12\x35\n1k_ENewSteamAnnouncementState_FeaturedAnnouncement\x10\x03*\xfe\x01\n\nEForumType\x12\x18\n\x14k_EForumType_Invalid\x10\x00\x12\x18\n\x14k_EForumType_General\x10\x01\x12\x1e\n\x1ak_EForumType_ReportedPosts\x10\x02\x12\x19\n\x15k_EForumType_Workshop\x10\x03\x12\x1e\n\x1ak_EForumType_PublishedFile\x10\x04\x12\x18\n\x14k_EForumType_Trading\x10\x05\x12\x19\n\x15k_EForumType_PlayTest\x10\x06\x12\x16\n\x12k_EForumType_Event\x10\x07\x12\x14\n\x10k_EForumType_Max\x10\x08*\x8b\x07\n\x12\x45\x43ommentThreadType\x12\x1f\n\x1bk_ECommentThreadTypeInvalid\x10\x00\x12-\n)k_ECommentThreadTypeScreenshot_Deprecated\x10\x01\x12\x31\n-k_ECommentThreadTypeWorkshopAccount_Developer\x10\x02\x12.\n*k_ECommentThreadTypeWorkshopAccount_Public\x10\x03\x12/\n+k_ECommentThreadTypePublishedFile_Developer\x10\x04\x12,\n(k_ECommentThreadTypePublishedFile_Public\x10\x05\x12\x1c\n\x18k_ECommentThreadTypeTest\x10\x06\x12\"\n\x1ek_ECommentThreadTypeForumTopic\x10\x07\x12&\n\"k_ECommentThreadTypeRecommendation\x10\x08\x12(\n$k_ECommentThreadTypeVideo_Deprecated\x10\t\x12\x1f\n\x1bk_ECommentThreadTypeProfile\x10\n\x12 \n\x1ck_ECommentThreadTypeNewsPost\x10\x0b\x12\x1c\n\x18k_ECommentThreadTypeClan\x10\x0c\x12(\n$k_ECommentThreadTypeClanAnnouncement\x10\r\x12!\n\x1dk_ECommentThreadTypeClanEvent\x10\x0e\x12+\n\'k_ECommentThreadTypeUserStatusPublished\x10\x0f\x12+\n\'k_ECommentThreadTypeUserReceivedNewGame\x10\x10\x12\x32\n.k_ECommentThreadTypePublishedFile_Announcement\x10\x11\x12(\n$k_ECommentThreadTypeModeratorMessage\x10\x12\x12&\n\"k_ECommentThreadTypeClanCuratedApp\x10\x13\x12$\n k_ECommentThreadTypeQAndASession\x10\x14\x12\x1b\n\x17k_ECommentThreadTypeMax\x10\x15*\xd7\x01\n\x14\x45\x42roadcastPermission\x12\"\n\x1ek_EBroadcastPermissionDisabled\x10\x00\x12(\n$k_EBroadcastPermissionFriendsApprove\x10\x01\x12(\n$k_EBroadcastPermissionFriendsAllowed\x10\x02\x12 \n\x1ck_EBroadcastPermissionPublic\x10\x03\x12%\n!k_EBroadcastPermissionSubscribers\x10\x04*f\n\x18\x45\x42roadcastEncoderSetting\x12\"\n\x1ek_EBroadcastEncoderBestQuality\x10\x00\x12&\n\"k_EBroadcastEncoderBestPerformance\x10\x01*y\n\x14\x45\x43loudGamingPlatform\x12\x1e\n\x1ak_ECloudGamingPlatformNone\x10\x00\x12\x1f\n\x1bk_ECloudGamingPlatformValve\x10\x01\x12 \n\x1ck_ECloudGamingPlatformNVIDIA\x10\x02*\x9a\x02\n\x18\x45\x43ompromiseDetectionType\x12#\n\x1fk_ECompromiseDetectionType_None\x10\x00\x12)\n%k_ECompromiseDetectionType_TradeEvent\x10\x01\x12*\n&k_ECompromiseDetectionType_ApiCallRate\x10\x02\x12%\n!k_ECompromiseDetectionType_Manual\x10\x03\x12+\n\'k_ECompromiseDetectionType_TicketAction\x10\x04\x12.\n*k_ECompromiseDetectionType_MaliciousRefund\x10\x05*\xd6\x01\n\x1a\x45\x41syncGameSessionUserState\x12\x30\n#k_EAsyncGameSessionUserStateUnknown\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x30\n,k_EAsyncGameSessionUserStateWaitingForOthers\x10\x00\x12.\n*k_EAsyncGameSessionUserStateReadyForAction\x10\x01\x12$\n k_EAsyncGameSessionUserStateDone\x10\x02*\xc4\x01\n\x1f\x45\x41syncGameSessionUserVisibility\x12;\n7k_EAsyncGameSessionUserVisibilityEnvelopeAndSessionList\x10\x00\x12\x34\n0k_EAsyncGameSessionUserVisibilitySessionListOnly\x10\x01\x12.\n*k_EAsyncGameSessionUserVisibilityDismissed\x10\x02*\xd4\x01\n\x12\x45GameRecordingType\x12 \n\x1ck_EGameRecordingType_Unknown\x10\x00\x12%\n!k_EGameRecordingType_NotRecording\x10\x01\x12(\n$k_EGameRecordingType_ManualRecording\x10\x02\x12,\n(k_EGameRecordingType_BackgroundRecording\x10\x03\x12\x1d\n\x19k_EGameRecordingType_Clip\x10\x04*\\\n\x0c\x45\x45xportCodec\x12\x1a\n\x16k_EExportCodec_Default\x10\x00\x12\x17\n\x13k_EExportCodec_H264\x10\x01\x12\x17\n\x13k_EExportCodec_H265\x10\x02*\xea\x03\n\rEProtoAppType\x12\x15\n\x11k_EAppTypeInvalid\x10\x00\x12\x12\n\x0ek_EAppTypeGame\x10\x01\x12\x19\n\x15k_EAppTypeApplication\x10\x02\x12\x12\n\x0ek_EAppTypeTool\x10\x04\x12\x12\n\x0ek_EAppTypeDemo\x10\x08\x12\x17\n\x13k_EAppTypeDeprected\x10\x10\x12\x11\n\rk_EAppTypeDLC\x10 \x12\x13\n\x0fk_EAppTypeGuide\x10@\x12\x15\n\x10k_EAppTypeDriver\x10\x80\x01\x12\x15\n\x10k_EAppTypeConfig\x10\x80\x02\x12\x17\n\x12k_EAppTypeHardware\x10\x80\x04\x12\x18\n\x13k_EAppTypeFranchise\x10\x80\x08\x12\x14\n\x0fk_EAppTypeVideo\x10\x80\x10\x12\x15\n\x10k_EAppTypePlugin\x10\x80 \x12\x19\n\x14k_EAppTypeMusicAlbum\x10\x80@\x12\x16\n\x10k_EAppTypeSeries\x10\x80\x80\x01\x12\x15\n\x0fk_EAppTypeComic\x10\x80\x80\x02\x12\x14\n\x0ek_EAppTypeBeta\x10\x80\x80\x04\x12\x1a\n\x12k_EAppTypeShortcut\x10\x80\x80\x80\x80\x04\x12 \n\x13k_EAppTypeDepotOnly\x10\x80\x80\x80\x80\xf8\xff\xff\xff\xff\x01*\x96\x01\n\x19\x45\x43hildProcessQueryCommand\x12\'\n#k_EChildProcessQueryCommand_Invalid\x10\x00\x12+\n\'k_EChildProcessQueryCommand_GpuTopology\x10\x01\x12#\n\x1fk_EChildProcessQueryCommand_Max\x10\x02*\xf6\x02\n\x1a\x45\x43hildProcessQueryExitCode\x12(\n$k_EChildProcessQueryExitCode_Success\x10\x00\x12:\n-k_EChildProcessQueryExitCode_ErrorCommandline\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x34\n\'k_EChildProcessQueryExitCode_ErrorOther\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12<\n/k_EChildProcessQueryExitCode_ErrorUnimplemented\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x37\n*k_EChildProcessQueryExitCode_ErrorFileSave\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x45\n8k_EChildProcessQueryExitCode_ErrorNotSupportedByPlatform\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xf2\x01\n EWindowsUpdateInstallationImpact\x12\x37\n*k_EWindowsUpdateInstallationImpact_Unknown\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12-\n)k_EWindowsUpdateInstallationImpact_Normal\x10\x00\x12,\n(k_EWindowsUpdateInstallationImpact_Minor\x10\x01\x12\x38\n4k_EWindowsUpdateInstallationImpact_ExclusiveHandling\x10\x02*\xf2\x01\n\x1c\x45WindowsUpdateRebootBehavior\x12\x33\n&k_EWindowsUpdateRebootBehavior_Unknown\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x33\n/k_EWindowsUpdateRebootBehavior_NeverNeedsReboot\x10\x00\x12\x34\n0k_EWindowsUpdateRebootBehavior_AlwaysNeedsReboot\x10\x01\x12\x32\n.k_EWindowsUpdateRebootBehavior_MightNeedReboot\x10\x02*\xfe\x01\n\x16\x45\x45xternalSaleEventType\x12$\n k_EExternalSaleEventType_Unknown\x10\x00\x12&\n\"k_EExternalSaleEventType_Publisher\x10\x01\x12%\n!k_EExternalSaleEventType_Showcase\x10\x02\x12#\n\x1fk_EExternalSaleEventType_Region\x10\x03\x12\"\n\x1ek_EExternalSaleEventType_Theme\x10\x04\x12&\n\"k_EExternalSaleEventType_Franchise\x10\x05\x42\tH\x01\x80\x01\x01\x80\xb5\x18\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\001\200\265\030\001'
  _globals['_EPUBLISHEDFILEQUERYTYPE']._serialized_start=42
  _globals['_EPUBLISHEDFILEQUERYTYPE']._serialized_end=1322
  _globals['_EPUBLISHEDFILEINAPPROPRIATEPROVIDER']._serialized_start=1325
  _globals['_EPUBLISHEDFILEINAPPROPRIATEPROVIDER']._serialized_end=1513
  _globals['_EPUBLISHEDFILEINAPPROPRIATERESULT']._serialized_start=1516
  _globals['_EPUBLISHEDFILEINAPPROPRIATERESULT']._serialized_end=1857
  _globals['_EPERSONASTATEFLAG']._serialized_start=1860
  _globals['_EPERSONASTATEFLAG']._serialized_end=2293
  _globals['_ECONTENTCHECKPROVIDER']._serialized_start=2296
  _globals['_ECONTENTCHECKPROVIDER']._serialized_end=2600
  _globals['_EPROFILECUSTOMIZATIONTYPE']._serialized_start=2603
  _globals['_EPROFILECUSTOMIZATIONTYPE']._serialized_end=3774
  _globals['_EPUBLISHEDFILESTORAGESYSTEM']._serialized_start=3777
  _globals['_EPUBLISHEDFILESTORAGESYSTEM']._serialized_end=3977
  _globals['_ECLOUDSTORAGEPERSISTSTATE']._serialized_start=3980
  _globals['_ECLOUDSTORAGEPERSISTSTATE']._serialized_end=4131
  _globals['_ESDCARDFORMATSTAGE']._serialized_start=4134
  _globals['_ESDCARDFORMATSTAGE']._serialized_end=4366
  _globals['_ESTORAGEFORMATSTAGE']._serialized_start=4369
  _globals['_ESTORAGEFORMATSTAGE']._serialized_end=4646
  _globals['_ESYSTEMFANCONTROLMODE']._serialized_start=4649
  _globals['_ESYSTEMFANCONTROLMODE']._serialized_end=4781
  _globals['_ESTARTUPMOVIEVARIANT']._serialized_start=4784
  _globals['_ESTARTUPMOVIEVARIANT']._serialized_end=4954
  _globals['_ECOLORGAMUTLABELSET']._serialized_start=4957
  _globals['_ECOLORGAMUTLABELSET']._serialized_end=5096
  _globals['_EWINDOWSTACKINGORDER']._serialized_start=5098
  _globals['_EWINDOWSTACKINGORDER']._serialized_end=5223
  _globals['_EBLUETOOTHDEVICETYPE']._serialized_start=5226
  _globals['_EBLUETOOTHDEVICETYPE']._serialized_end=5674
  _globals['_ESYSTEMAUDIODIRECTION']._serialized_start=5677
  _globals['_ESYSTEMAUDIODIRECTION']._serialized_end=5805
  _globals['_ESYSTEMAUDIOCHANNEL']._serialized_start=5808
  _globals['_ESYSTEMAUDIOCHANNEL']._serialized_end=6177
  _globals['_ESYSTEMAUDIOPORTTYPE']._serialized_start=6180
  _globals['_ESYSTEMAUDIOPORTTYPE']._serialized_end=6381
  _globals['_ESYSTEMAUDIOPORTDIRECTION']._serialized_start=6384
  _globals['_ESYSTEMAUDIOPORTDIRECTION']._serialized_end=6528
  _globals['_ESYSTEMSERVICESTATE']._serialized_start=6531
  _globals['_ESYSTEMSERVICESTATE']._serialized_end=6662
  _globals['_EGRAPHICSPERFOVERLAYLEVEL']._serialized_start=6665
  _globals['_EGRAPHICSPERFOVERLAYLEVEL']._serialized_end=6890
  _globals['_EGPUPERFORMANCELEVEL']._serialized_start=6893
  _globals['_EGPUPERFORMANCELEVEL']._serialized_end=7122
  _globals['_ESCALINGFILTER']._serialized_start=7125
  _globals['_ESCALINGFILTER']._serialized_end=7312
  _globals['_ESPLITSCALINGFILTER']._serialized_start=7315
  _globals['_ESPLITSCALINGFILTER']._serialized_end=7502
  _globals['_ESPLITSCALINGSCALER']._serialized_start=7505
  _globals['_ESPLITSCALINGSCALER']._serialized_end=7726
  _globals['_EGAMESCOPEBLURMODE']._serialized_start=7728
  _globals['_EGAMESCOPEBLURMODE']._serialized_end=7853
  _globals['_ESLSHELPER']._serialized_start=7856
  _globals['_ESLSHELPER']._serialized_end=8022
  _globals['_EHDRVISUALIZATION']._serialized_start=8025
  _globals['_EHDRVISUALIZATION']._serialized_end=8222
  _globals['_EHDRTONEMAPOPERATOR']._serialized_start=8225
  _globals['_EHDRTONEMAPOPERATOR']._serialized_end=8354
  _globals['_ECPUGOVERNOR']._serialized_start=8356
  _globals['_ECPUGOVERNOR']._serialized_end=8480
  _globals['_EUPDATERTYPE']._serialized_start=8483
  _globals['_EUPDATERTYPE']._serialized_end=8709
  _globals['_EUPDATERSTATE']._serialized_start=8712
  _globals['_EUPDATERSTATE']._serialized_end=8991
  _globals['_ESTORAGEBLOCKCONTENTTYPE']._serialized_start=8994
  _globals['_ESTORAGEBLOCKCONTENTTYPE']._serialized_end=9219
  _globals['_ESTORAGEBLOCKFILESYSTEMTYPE']._serialized_start=9222
  _globals['_ESTORAGEBLOCKFILESYSTEMTYPE']._serialized_end=9417
  _globals['_ESTORAGEDRIVEMEDIATYPE']._serialized_start=9420
  _globals['_ESTORAGEDRIVEMEDIATYPE']._serialized_end=9628
  _globals['_ESYSTEMDISPLAYCOMPATIBILITYMODE']._serialized_start=9631
  _globals['_ESYSTEMDISPLAYCOMPATIBILITYMODE']._serialized_end=9810
  _globals['_ESTEAMDECKCOMPATIBILITYCATEGORY']._serialized_start=9813
  _globals['_ESTEAMDECKCOMPATIBILITYCATEGORY']._serialized_end=10040
  _globals['_ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE']._serialized_start=10043
  _globals['_ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE']._serialized_end=10379
  _globals['_ESTEAMDECKCOMPATIBILITYTESTRESULT']._serialized_start=10382
  _globals['_ESTEAMDECKCOMPATIBILITYTESTRESULT']._serialized_end=10664
  _globals['_EACSTATE']._serialized_start=10666
  _globals['_EACSTATE']._serialized_end=10785
  _globals['_EBATTERYSTATE']._serialized_start=10788
  _globals['_EBATTERYSTATE']._serialized_end=10921
  _globals['_EOSBRANCH']._serialized_start=10924
  _globals['_EOSBRANCH']._serialized_end=11178
  _globals['_EBROWSERGPUSTATUS']._serialized_start=11181
  _globals['_EBROWSERGPUSTATUS']._serialized_end=11635
  _globals['_EBROWSERFEATURESTATUS']._serialized_start=11638
  _globals['_EBROWSERFEATURESTATUS']._serialized_end=12249
  _globals['_EGPUDRIVERID']._serialized_start=12252
  _globals['_EGPUDRIVERID']._serialized_end=12923
  _globals['_ECOMMUNITYITEMCLASS']._serialized_start=12926
  _globals['_ECOMMUNITYITEMCLASS']._serialized_end=13659
  _globals['_ESTEAMDECKCOMPATIBILITYFEEDBACK']._serialized_start=13662
  _globals['_ESTEAMDECKCOMPATIBILITYFEEDBACK']._serialized_end=13879
  _globals['_EPROVIDEDECKFEEDBACKPREFERENCE']._serialized_start=13882
  _globals['_EPROVIDEDECKFEEDBACKPREFERENCE']._serialized_end=14041
  _globals['_ETOUCHGESTURE']._serialized_start=14044
  _globals['_ETOUCHGESTURE']._serialized_end=14477
  _globals['_ESESSIONPERSISTENCE']._serialized_start=14480
  _globals['_ESESSIONPERSISTENCE']._serialized_end=14620
  _globals['_ENEWSTEAMANNOUNCEMENTSTATE']._serialized_start=14623
  _globals['_ENEWSTEAMANNOUNCEMENTSTATE']._serialized_end=14840
  _globals['_EFORUMTYPE']._serialized_start=14843
  _globals['_EFORUMTYPE']._serialized_end=15097
  _globals['_ECOMMENTTHREADTYPE']._serialized_start=15100
  _globals['_ECOMMENTTHREADTYPE']._serialized_end=16007
  _globals['_EBROADCASTPERMISSION']._serialized_start=16010
  _globals['_EBROADCASTPERMISSION']._serialized_end=16225
  _globals['_EBROADCASTENCODERSETTING']._serialized_start=16227
  _globals['_EBROADCASTENCODERSETTING']._serialized_end=16329
  _globals['_ECLOUDGAMINGPLATFORM']._serialized_start=16331
  _globals['_ECLOUDGAMINGPLATFORM']._serialized_end=16452
  _globals['_ECOMPROMISEDETECTIONTYPE']._serialized_start=16455
  _globals['_ECOMPROMISEDETECTIONTYPE']._serialized_end=16737
  _globals['_EASYNCGAMESESSIONUSERSTATE']._serialized_start=16740
  _globals['_EASYNCGAMESESSIONUSERSTATE']._serialized_end=16954
  _globals['_EASYNCGAMESESSIONUSERVISIBILITY']._serialized_start=16957
  _globals['_EASYNCGAMESESSIONUSERVISIBILITY']._serialized_end=17153
  _globals['_EGAMERECORDINGTYPE']._serialized_start=17156
  _globals['_EGAMERECORDINGTYPE']._serialized_end=17368
  _globals['_EEXPORTCODEC']._serialized_start=17370
  _globals['_EEXPORTCODEC']._serialized_end=17462
  _globals['_EPROTOAPPTYPE']._serialized_start=17465
  _globals['_EPROTOAPPTYPE']._serialized_end=17955
  _globals['_ECHILDPROCESSQUERYCOMMAND']._serialized_start=17958
  _globals['_ECHILDPROCESSQUERYCOMMAND']._serialized_end=18108
  _globals['_ECHILDPROCESSQUERYEXITCODE']._serialized_start=18111
  _globals['_ECHILDPROCESSQUERYEXITCODE']._serialized_end=18485
  _globals['_EWINDOWSUPDATEINSTALLATIONIMPACT']._serialized_start=18488
  _globals['_EWINDOWSUPDATEINSTALLATIONIMPACT']._serialized_end=18730
  _globals['_EWINDOWSUPDATEREBOOTBEHAVIOR']._serialized_start=18733
  _globals['_EWINDOWSUPDATEREBOOTBEHAVIOR']._serialized_end=18975
  _globals['_EEXTERNALSALEEVENTTYPE']._serialized_start=18978
  _globals['_EEXTERNALSALEEVENTTYPE']._serialized_end=19232
# @@protoc_insertion_point(module_scope)
