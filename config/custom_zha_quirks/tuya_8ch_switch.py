from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Basic, Groups, Identify, OnOff, Scenes, Time, Ota, GreenPowerProxy
from zigpy.profiles import zgp
from zhaquirks.tuya import TuyaSwitch
from zhaquirks.tuya.mcu import TuyaMCUCluster, TuyaOnOff

# Extended TuyaMap class with all attributes required by ZHA, including 'dp_converter'.
class TuyaMap:
    def __init__(self, name, endpoint_id):
        self.ep_attribute = name
        self.attribute_name = name
        self.endpoint_id = endpoint_id
        self.dp_converter = None

# Custom MCU cluster with hardcoded DP mapping
class CustomTuyaMCU(TuyaMCUCluster):
    """Custom MCU cluster for 8 gang switch."""
    
    # Static mapping that ZHA cannot lose
    dp_to_attribute = {
        1: [TuyaMap("on_off", 1)],
        2: [TuyaMap("on_off", 2)],
        3: [TuyaMap("on_off", 3)],
        4: [TuyaMap("on_off", 4)],
        5: [TuyaMap("on_off", 5)],
        6: [TuyaMap("on_off", 6)],
        7: [TuyaMap("on_off", 7)],
        8: [TuyaMap("on_off", 8)],
    }

    data_point_handlers = {
        1: "_dp_2_attr_update",
        2: "_dp_2_attr_update",
        3: "_dp_2_attr_update",
        4: "_dp_2_attr_update",
        5: "_dp_2_attr_update",
        6: "_dp_2_attr_update",
        7: "_dp_2_attr_update",
        8: "_dp_2_attr_update",
    }

# OnOff cluster without Manufacturer ID
class TuyaOnOffNM(TuyaOnOff):
    """Tuya OnOff cluster with No Manufacturer ID."""
    pass

# Main device definition
class Custom8GangSwitch(TuyaSwitch):
    """Tuya TS0601 8-gang switch quirk."""
    
    signature = {
        "models_info": [("_TZE204_adlblwab", "TS0601")],
        "endpoints": {
            1: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.SMART_PLUG,
                "input_clusters": [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaMCUCluster.cluster_id,
                ],
                "output_clusters": [Time.cluster_id, Ota.cluster_id],
            },
            242: {
                "profile_id": zgp.PROFILE_ID,
                "device_type": zgp.DeviceType.PROXY_BASIC,
                "input_clusters": [],
                "output_clusters": [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        "endpoints": {
            # Endpoint 1: CustomTuyaMCU + TuyaOnOffNM (primary)
            1: {
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    CustomTuyaMCU,
                    TuyaOnOffNM,
                ],
                "output_clusters": [Time.cluster_id, Ota.cluster_id],
            },
            # Endpoints 2-8
            2: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            3: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            4: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            5: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            6: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            7: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
            8: {
                "profile_id": zha.PROFILE_ID,
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [TuyaOnOffNM],
                "output_clusters": [],
            },
        }
    }