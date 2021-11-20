
from . import control
from . import abc
import logging
import json
import xmltodict

class Player(abc.BasePlayer):
    """
    Represents a Sonos player.
    """
    def __init__(self, data):
        print(data)
        self.logger = logging.getLogger(__name__)
        self._apiVersion = data['apiVersion']
        self._deviceIds = data['deviceIds']
        self._icon = data['icon'] if 'icon' in data else None
        self._id = data['id']
        self._minApiVersion = data['minApiVersion']
        self._name = data['name']
        self._softwareVersion = data['softwareVersion']
        self._websocketUrl = data['websocketUrl']
        self._capabilities = data['capabilities']
        self._ip = self._websocketUrl.split("//")[1].split(":")[0]
        info = control.get_device_info(self._ip)['root']['device']
        self._macAddress['MACAddress']
        self._serialNumber['serialNum']
        self._model['modelName']
        self._modelNumber['modelNumber']
        self._displayName['displayName']
        self._softwareVersion['softwareVersion']
        self._hardwareVersion['hardwareVersion']


        "http://192.168.1.26:1400/xml/device_description.xml"

        # TODO: Add more properties from json below 
        """
   {
   "root":{
      "@xmlns":"urn:schemas-upnp-org:device-1-0",
      "specVersion":{
         "major":"1",
         "minor":"0"
      },
      "device":{
         "deviceType":"urn:schemas-upnp-org:device:ZonePlayer:1",
         "friendlyName":"192.168.1.26 - Sonos One SL",
         "manufacturer":"Sonos, Inc.",
         "manufacturerURL":"http://www.sonos.com",
         "modelNumber":"S22",
         "modelDescription":"Sonos One SL",
         "modelName":"Sonos One SL",
         "modelURL":"http://www.sonos.com/products/zoneplayers/S22",
         "softwareVersion":"65.1-21040",
         "swGen":"2",
         "hardwareVersion":"1.28.1.6-1.2",
         "serialNum":"48-A6-B8-AC-A9-60:9",
         "MACAddress":"48:A6:B8:AC:A9:60",
         "UDN":"uuid:RINCON_48A6B8ACA96001400",
         "iconList":{
            "icon":{
               "id":"0",
               "mimetype":"image/png",
               "width":"48",
               "height":"48",
               "depth":"24",
               "url":"/img/icon-S22.png"
            }
         },
         "minCompatibleVersion":"64.0-00000",
         "legacyCompatibleVersion":"58.0-00000",
         "apiVersion":"1.25.1",
         "minApiVersion":"1.1.0",
         "displayVersion":"13.3",
         "extraVersion":"None",
         "nsVersion":"27",
         "roomName":"Justin's Room",
         "displayName":"One SL",
         "zoneType":"24",
         "feature1":"0x00000000",
         "feature2":"0x01418332",
         "feature3":"0x0001580e",
         "seriesid":"A100",
         "variant":"2",
         "internalSpeakerSize":"5",
         "bassExtension":"#BASS_EXT#",
         "satGainOffset":"#SAT_GAIN_OFFSET#",
         "memory":"512",
         "flash":"512",
         "ampOnTime":"10",
         "retailMode":"0",
         "SSLPort":"1443",
         "securehhSSLPort":"1843",
         "serviceList":{
            "service":[
               {
                  "serviceType":"urn:schemas-upnp-org:service:AlarmClock:1",
                  "serviceId":"urn:upnp-org:serviceId:AlarmClock",
                  "controlURL":"/AlarmClock/Control",
                  "eventSubURL":"/AlarmClock/Event",
                  "SCPDURL":"/xml/AlarmClock1.xml"
               },
               {
                  "serviceType":"urn:schemas-upnp-org:service:MusicServices:1",
                  "serviceId":"urn:upnp-org:serviceId:MusicServices",
                  "controlURL":"/MusicServices/Control",
                  "eventSubURL":"/MusicServices/Event",
                  "SCPDURL":"/xml/MusicServices1.xml"
               },
               {
                  "serviceType":"urn:schemas-upnp-org:service:DeviceProperties:1",
                  "serviceId":"urn:upnp-org:serviceId:DeviceProperties",
                  "controlURL":"/DeviceProperties/Control",
                  "eventSubURL":"/DeviceProperties/Event",
                  "SCPDURL":"/xml/DeviceProperties1.xml"
               },
               {
                  "serviceType":"urn:schemas-upnp-org:service:SystemProperties:1",
                  "serviceId":"urn:upnp-org:serviceId:SystemProperties",
                  "controlURL":"/SystemProperties/Control",
                  "eventSubURL":"/SystemProperties/Event",
                  "SCPDURL":"/xml/SystemProperties1.xml"
               },
               {
                  "serviceType":"urn:schemas-upnp-org:service:ZoneGroupTopology:1",
                  "serviceId":"urn:upnp-org:serviceId:ZoneGroupTopology",
                  "controlURL":"/ZoneGroupTopology/Control",
                  "eventSubURL":"/ZoneGroupTopology/Event",
                  "SCPDURL":"/xml/ZoneGroupTopology1.xml"
               },
               {
                  "serviceType":"urn:schemas-upnp-org:service:GroupManagement:1",
                  "serviceId":"urn:upnp-org:serviceId:GroupManagement",
                  "controlURL":"/GroupManagement/Control",
                  "eventSubURL":"/GroupManagement/Event",
                  "SCPDURL":"/xml/GroupManagement1.xml"
               },
               {
                  "serviceType":"urn:schemas-tencent-com:service:QPlay:1",
                  "serviceId":"urn:tencent-com:serviceId:QPlay",
                  "controlURL":"/QPlay/Control",
                  "eventSubURL":"/QPlay/Event",
                  "SCPDURL":"/xml/QPlay1.xml"
               }
            ]
         },
         "deviceList":{
            "device":[
               {
                  "deviceType":"urn:schemas-upnp-org:device:MediaServer:1",
                  "friendlyName":"192.168.1.26 - Sonos One SL Media Server",
                  "manufacturer":"Sonos, Inc.",
                  "manufacturerURL":"http://www.sonos.com",
                  "modelNumber":"S22",
                  "modelDescription":"Sonos One SL Media Server",
                  "modelName":"Sonos One SL",
                  "modelURL":"http://www.sonos.com/products/zoneplayers/S22",
                  "UDN":"uuid:RINCON_48A6B8ACA96001400_MS",
                  "serviceList":{
                     "service":[
                        {
                           "serviceType":"urn:schemas-upnp-org:service:ContentDirectory:1",
                           "serviceId":"urn:upnp-org:serviceId:ContentDirectory",
                           "controlURL":"/MediaServer/ContentDirectory/Control",
                           "eventSubURL":"/MediaServer/ContentDirectory/Event",
                           "SCPDURL":"/xml/ContentDirectory1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-upnp-org:service:ConnectionManager:1",
                           "serviceId":"urn:upnp-org:serviceId:ConnectionManager",
                           "controlURL":"/MediaServer/ConnectionManager/Control",
                           "eventSubURL":"/MediaServer/ConnectionManager/Event",
                           "SCPDURL":"/xml/ConnectionManager1.xml"
                        }
                     ]
                  }
               },
               {
                  "deviceType":"urn:schemas-upnp-org:device:MediaRenderer:1",
                  "friendlyName":"Justin's Room - Sonos One 
SL Media Renderer",
                  "manufacturer":"Sonos, Inc.",
                  "manufacturerURL":"http://www.sonos.com",
                  "modelNumber":"S22",
                  "modelDescription":"Sonos One SL Media Renderer",
                  "modelName":"Sonos One SL",
                  "modelURL":"http://www.sonos.com/products/zoneplayers/S22",
                  "UDN":"uuid:RINCON_48A6B8ACA96001400_MR",
                  "serviceList":{
                     "service":[
                        {
                           "serviceType":"urn:schemas-upnp-org:service:RenderingControl:1",
                           "serviceId":"urn:upnp-org:serviceId:RenderingControl",
                           "controlURL":"/MediaRenderer/RenderingControl/Control",
                           "eventSubURL":"/MediaRenderer/RenderingControl/Event",
                           "SCPDURL":"/xml/RenderingControl1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-upnp-org:service:ConnectionManager:1",
                           "serviceId":"urn:upnp-org:serviceId:ConnectionManager",
                           "controlURL":"/MediaRenderer/ConnectionManager/Control",
                           "eventSubURL":"/MediaRenderer/ConnectionManager/Event",
                           "SCPDURL":"/xml/ConnectionManager1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-upnp-org:service:AVTransport:1",
                           "serviceId":"urn:upnp-org:serviceId:AVTransport",
                           "controlURL":"/MediaRenderer/AVTransport/Control",
                           "eventSubURL":"/MediaRenderer/AVTransport/Event",
                           "SCPDURL":"/xml/AVTransport1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-sonos-com:service:Queue:1",
                           "serviceId":"urn:sonos-com:serviceId:Queue",
                           "controlURL":"/MediaRenderer/Queue/Control",
                           "eventSubURL":"/MediaRenderer/Queue/Event",
                           "SCPDURL":"/xml/Queue1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-upnp-org:service:GroupRenderingControl:1",
                           "serviceId":"urn:upnp-org:serviceId:GroupRenderingControl",
                           "controlURL":"/MediaRenderer/GroupRenderingControl/Control",
                           "eventSubURL":"/MediaRenderer/GroupRenderingControl/Event",
                           "SCPDURL":"/xml/GroupRenderingControl1.xml"
                        },
                        {
                           "serviceType":"urn:schemas-upnp-org:service:VirtualLineIn:1",
                           "serviceId":"urn:upnp-org:serviceId:VirtualLineIn",
                           "controlURL":"/MediaRenderer/VirtualLineIn/Control",
                           "eventSubURL":"/MediaRenderer/VirtualLineIn/Event",
                           "SCPDURL":"/xml/VirtualLineIn1.xml"
                        }
                     ]
                  },
                  "X_Rhapsody-Extension":{
                     "@xmlns":"http://www.real.com/rhapsody/xmlns/upnp-1-0",
                     "deviceID":"urn:rhapsody-real-com:device-id-1-0:sonos_1:RINCON_48A6B8ACA96001400",
                     "deviceCapabilities":{
                        "interactionPattern":{
                           "@type":"real-rhapsody-upnp-1-0"
                        }
                     }
                  },
                  "qq:X_QPlay_SoftwareCapability":{
                     "@xmlns:qq":"http://www.tencent.com",
                     "#text":"QPlay:2"
                  },
                  "iconList":{
                     "icon":{
                        "mimetype":"image/png",
                        "width":"48",
                        "height":"48",
                        "depth":"24",
                        "url":"/img/icon-S22.png"
                     }
                  }
               }
            ]
         }
      }
   }
}
        """

    @property
    def apiVersion(self) -> str:
        "The highest API version supported by the player."
        return self._apiVersion

    @property
    def deviceIds(self) -> list:
        "The IDs of all bonded devices corresponding to this logical player."
        return self._deviceIds

    @property
    def icon(self) -> str:
        """
        An identifier for the player icon. Set when the user chooses a pre-defined room for the player. You can map this to an icon to display in your app for the player. Values include any of the following:
        Note: Sonos sends `generic` if the user set up a custom room in the Sonos app.
        + bathroom
        + bedroom
        + den
        + diningroom
        + familyroom
        + foyer
        + garage
        + garden
        + generic
        + guestroom
        + hallway
        + kitchen
        + library
        + livingroom
        + masterbedroom
        + mediaroom
        + office
        + patio
        + playroom
        + pool
        + tvroom
        + portable
        """
        return self._icon

    @property
    def id(self) -> str:
        "The ID of the player."
        return self._id

    @property
    def minApiVersion(self) -> str:
        "The lowest API version supported by the player."
        return self._minApiVersion

    @property
    def name(self) -> str:
        "The display name for the player. For example, “Living Room”, “Kitchen”, or “Dining Room”."
        return self._name

    @property
    def softwareVersion(self) -> str:
        "The version of the software running on the device."
        return self._softwareVersion

    @property
    def websocketUrl(self) -> str:
        "The URL for the Websocket connection."
        return self._websocketUrl

    @property
    def capabilities(self) -> abc.Capabilities:
        "The capabilities of the player."
        return self._capabilities

        
    """def playerVolumeSubscribe(self):
        \"""
        Subscribe to the players's playerVolume events.
        \"""
        from ovlic.sonos import control

        self.logger.info("Subscribing to player's playerVolume events..")
        res = control.post(self, endpoint="/players/{}/playerVolume/subscription".format(self._id), params={})
        return res"""

    def loadAudioClip(self, name:str, appId="com.ovlic.app", clipType:abc.AudioClipType="CHIME", httpAuthorization:str=None, priority:abc.Priority=abc.Priority.default(), streamUrl:str=None, volume:int=None) -> abc.AudioClip:
        """
        Load an audio clip into the player.
        """
        params = {
            "name": name,
            "appId": appId,
            "clipType": clipType,
            "priority": priority,
        }

        if httpAuthorization is not None:
            params["httpAuthorization"] = httpAuthorization

        if streamUrl is not None:
            params["streamUrl"] = streamUrl

        if volume is not None:
            params["volume"] = volume

        self.logger.info("Loading audio clip..")
        res = control.post(self, endpoint="/players/{}/loadAudioClip".format(self._id), params=params)
        return res
    
    

