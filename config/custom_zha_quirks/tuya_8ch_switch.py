from zigpy.profiles import zha, zgp
from zigpy.zcl.clusters.general import Basic, GreenPowerProxy, Groups, Ota, Scenes, Time

from zhaquirks.tuya import TuyaSwitch
from zhaquirks.tuya.mcu import (
    DPToAttributeMapping,
    TuyaMCUCluster,
    TuyaOnOff,
    TuyaOnOffNM,
)


class EightGangTuyaMCU(TuyaMCUCluster):
    """Custom MCU cluster for 8-gang switch."""

    dp_to_attribute = {
        1: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off"),
        2: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=2),
        3: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=3),
        4: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=4),
        5: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=5),
        6: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=6),
        7: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=7),
        8: DPToAttributeMapping(TuyaOnOff.ep_attribute, "on_off", endpoint_id=8),
    }

    data_point_handlers = {dp: "_dp_2_attr_update" for dp in range(1, 9)}


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
            1: {
                "device_type": zha.DeviceType.ON_OFF_SWITCH,
                "input_clusters": [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    EightGangTuyaMCU,
                    TuyaOnOffNM,
                ],
                "output_clusters": [Time.cluster_id, Ota.cluster_id],
            },
            **{
                ep: {
                    "profile_id": zha.PROFILE_ID,
                    "device_type": zha.DeviceType.ON_OFF_SWITCH,
                    "input_clusters": [TuyaOnOffNM],
                    "output_clusters": [],
                }
                for ep in range(2, 9)
            },
        }
    }
