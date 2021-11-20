
import logging
import requests
import json
import xmltodict

from requests import status_codes

#from ovlic.sonos.household import Household
Household = "This variable is going to get removed from this file bwahaha"

from . import errors
from . import abc
from . import config

logger = logging.getLogger(__name__)

def raise_err(response):
    """
    Raise an error if the Sonos API returned an error.
    """
    """Example:
    [<Response [400]>, {'errorCode': 'ERROR_BAD_REQUEST', 'reason': 'command body contains invalid JSON'}]
    """

    status_code = response.status_code
    data = response.json()
    try:
        errorCode = data["errorCode"]
        reason = data["reason"]
    except KeyError:
        try:
            errorCode = data['fault']["detail"]["errorcode"]
            reason = data['fault']["faultstring"]
        except KeyError:
            pass

    # HTTP Errors
    if errorCode == "ERROR_BAD_REQUEST" or status_code == 400:
        raise errors.BadRequest(reason)
    elif errorCode == "ERROR_UNAUTHORIZED" or status_code == 401:
        raise errors.Unauthorized(reason)
    elif errorCode == "ERROR_FORBIDDEN" or status_code == 403:
        raise errors.Forbidden(reason)
    elif errorCode == "ERROR_NOT_FOUND" or status_code == 404:
        raise errors.NotFound(reason)
    elif errorCode == "ERROR_GONE" or status_code == 410:
        raise errors.Gone(reason)
    elif errorCode == "ERROR_TOO_MANY_REQUESTS" or status_code == 429:
        raise errors.RateLimitExceeded(reason)
    elif errorCode == "ERROR_INTERNAL_SERVER_ERROR" or status_code == 500:
        raise errors.InternalServerError(reason)
    elif errorCode == "ERROR_SERVICE_UNAVAILABLE" or status_code == 503:
        raise errors.ServiceUnavailable(reason)
    elif errorCode == "ERROR_NOT_IMPLEMENTED" or status_code == 501:
        raise errors.NotImplemented(reason)

    elif status_code == 499:
        # Other Custom Errors

        # Global Errors
        if errorCode == "ERROR_MISSING_PARAMETERS":
            raise errors.MissingParameters(reason)
        elif errorCode == "ERROR_INVALID_SYNTAX":
            raise errors.InvalidSyntax(reason)
        elif errorCode == "ERROR_UNSUPPORTED_NAMESPACE":
            raise errors.UnsupportedNamespace(reason)
        elif errorCode == "ERROR_UNSUPPORTED_COMMAND":
            raise errors.UnsupportedCommand(reason)
        elif errorCode == "ERROR_INVALID_PARAMETER":
            raise errors.InvalidParameter(reason)
        elif errorCode == "ERROR_INVALID_OBJECT_ID":
            raise errors.InvalidObjectId(reason)
        elif errorCode == "ERROR_COMMAND_FAILED":
            raise errors.CommandFailed(reason)
        elif errorCode == "ERROR_NOT_CAPABLE":
            raise errors.NotCapable(reason)
    
    else:
        # Unknown Error
        raise errors.SonosError(reason)

    
def get(endpoint, **kwargs):
    """
    Get a request from the Sonos API.
    """
    logger.debug("Getting request from Sonos API.")
    url = "https://api.ws.sonos.com/control/api/v1{}".format(endpoint)
    if kwargs.get('access_token'):
        access_token = kwargs.get('access_token')
    else:
        access_token = config.access_token
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logger.debug("Successfully got request from Sonos API.")
        return response.json()
    else:
        logger.error("Failed to get request from Sonos API.")
        print(response.text)
        print(response.status_code)
        raise_err(response)


def post(endpoint, params:dict):
    """
    Post a request to the Sonos API.
    endpoint: The endpoint to post to. (Anything after /control/api/v1/)
    params: The parameters to post.
    """
    logger.debug("Posting request to Sonos API.")
    url = "https://api.ws.sonos.com/control/api/v1/{}".format(endpoint)
    headers = {
        "Authorization": "Bearer {}".format(config.access_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    paramsJson = json.dumps(params)
    response = requests.post(url, headers=headers, data=paramsJson)
    if response.status_code == 200:
        logger.debug("Successfully posted request to Sonos API.")
        return response.json()
    else:
        logger.error("Failed to post request to Sonos API.")
        print(response.status_code)
        print(response.text)
        raise_err(response)

def subscribe(namespace, endpoint):
    """
    Subscribe to events from a namespace.
    :str:`namespace`: The namespace to subscribe to.
    :str:`endpoint`: The subscription url in the namespace to subscribe to.
    """
    logger.info("Subscribing to {} events...".format(namespace))
    url = "https://api.ws.sonos.com/control/api/v1{}".format(endpoint)
    headers = {
        "Authorization": "Bearer {}".format(config.access_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        logger.debug("Successfully subscribed to {}.".format(namespace))
        return response.json()
    else:
        logger.error("Failed to subscribe to {}.".format(namespace))
        raise_err(response)

def unsubscribe(namespace, endpoint):
    """
    Unsubscribe to events from a namespace.
    :str:`namespace`: The namespace to unsubscribe to.
    :str:`endpoint`: The subscription url in the namespace to unsubscribe to.
    """
    logger.info("Unsubscribing to {} events...".format(namespace))
    url = "https://api.ws.sonos.com/control/api/v1{}".format(endpoint)
    headers = {
        "Authorization": "Bearer {}".format(config.access_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        logger.debug("Successfully unsubscribed to {}.".format(namespace))
        return response.json()
    else:
        logger.error("Failed to unsubscribe to {}.".format(namespace))
        raise_err(response)


def get_device_info(ip):
    """
    Get player info.
    :str:`ip`: The IP address of the player.
    """
    logger.debug("Getting device info...")
    url = "http://{}:1400/xml/device_description.xml".format(ip)
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug("Successfully got device info.")
        return json.loads(json.dumps(xmltodict.parse(response.text)))
    else:
        logger.error("Failed to get device info.")
        raise_err(response)


def verify_access_token(access_token):
    """
    Verify that the access token is valid.
    """
    logger.debug("Verifying access token.")
    url = "https://api.ws.sonos.com/control/api/v1/households/"
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logger.debug("Successfully verified access token.")
        return response.json()
    else:
        logger.error("Failed to verify access token.")
        raise_err(response)


def refresh_access_token(refresh_token, auth_key):
    """
    Refresh an access token from Sonos.
    """
    logger.info("Refreshing access token...")
    headers = {
        "Authorization": "Basic "+auth_key,
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post("https://api.sonos.com/login/v3/oauth/access", headers=headers, data=data)
    if response.status_code == 200:
        logger.debug("Successfully refreshed access token.")
        return response.json()
    else:
        logger.error("Failed to refresh access token.")
        raise_err(response)



class Control:
    """
    Control API for Sonos.
    """
    def __init__(self, client_id, client_secret, redirect_uri):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing Sonos Control..")
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = config.access_token
        #self.player_name = player_name
        # self.auth_key = auth_key
        self.logger.info("Initialized Sonos Control.")
        self.audioClip = self.audioClip(self)

        

    def get_households(self):
        """
        Get all households.
        """
        self.logger.info("Getting households..")
        
        req = get(self, endpoint="/households")
        res = []

        for i in range(0, len(req['households'])):
            res.append(Household(req['households'][i]))

        return res

    def get_household(self):
        """
        Get the first households.
        """
        self.logger.info("Getting households..")
        res = get(self, endpoint="/households")
        return Household(res['households'][0])


    
    class audioClip:
        """

        """
        def __init__(self, control):
            self.control = control
            self.access_token = self.control.access_token
            self.client_id = self.control.client_id
            self.client_secret = self.control.client_secret
            self.redirect_uri = self.control.redirect_uri
            self.logger = self.control.logger
            self.logger.info("Initializing AudioClip..")
            self.logger.info("Initialized AudioClip.")

    class groups:
        def __init__(self, control):
            self.control = control
            self.access_token = self.control.access_token
        
            self.logger = self.control.logger
            self.logger.info("Initializing groups..")
            self.logger.info("Initialized groups.")

        def getGroups(self):
            """
            Get all groups.
            """
            self.logger.info("Getting groups..")
            headers = {"Authorization": "Bearer "+self.access_token, "Content-Type": "application/json"}
            sonoswait =  "Not correct"#requests.get("https://api.ws.sonos.com/control/api/v1/households/"+self.h_id+"/groups", headers=headers).json()
            try:
                if sonoswait['fault']: # If there is a fault, return the fault.
                    self.logger.error("Fault: "+sonoswait['fault']['message'])
                    return sonoswait['fault']
                else:
                    self.logger.info("Groups: "+str(sonoswait))
                    return sonoswait
            except KeyError: 
                return sonoswait
            self.logger.info("Got groups.")
            return

    class groupVolume:
            
        def __init__(self, access_token, group):
            self.group = group
            self.access_token = access_token
            self.logger.info("Initializing groupVolume..")
            self.logger.info("Initialized groupVolume.")

        def getVolume(self) -> abc.Volume:
            """
            Get the volume of the group.
            """
            self.logger.info("Getting group volume..")
            url = "https://api.sonos.com/control/api/v1/groups/{}/groupVolume".format(self.group.id)
            headers = {
                "Authorization": "Bearer {}".format(self.access_token),
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.logger.info("Got group volume.")
                return abc.Volume(response.json())
            else:
                self.logger.error("Failed to get group volume.")
                raise errors.SonosError(response.status_code, response.text)

        def setMute(self, mute: bool) -> bool:
            """
            Mutes the group.
            """
            self.logger.info("Muting group..")
            url = "https://api.sonos.com/control/api/v1/groups/{}/groupVolume/mute".format(self.groupId)
            headers = {
                "Authorization": "Bearer {}".format(self.self.group.id),
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.logger.info("Set group mute.")
                return True
            else:
                self.logger.error("Failed to set group mute.")
                raise errors.SonosError(response.status_code, response.text)

        def setRelativeVolume(self, volume:int) -> bool:
            """
            Sets the relative volume of the group.
            """
            if volume < -100 or volume > 100:
                raise errors.SonosError("Volume must be between -100 and 100.")
            
            self.logger.info("Setting relative group volume..")
            url = "https://api.sonos.com/control/api/v1/groups/{}/groupVolume/relative".format(self.group.id)
            headers = {
                "Authorization": "Bearer {}".format(self.access_token),
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            data = {
                "volumeDelta": volume
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                self.logger.info("Set relative group volume to {}".format(volume))
                return True
            else:
                self.logger.error("Failed to set group volume.")
                raise errors.SonosError(response.status_code, response.text)


        def setVolume(self, volume: int) -> bool:
            """
            Sets the absolute volume of the group.
            """
            if volume < 0 or volume > 100:
                raise errors.SonosError("Volume must be between 0 and 100.")
            
            self.logger.info("Setting absolute group volume..")
            url = "https://api.sonos.com/control/api/v1/groups/{}/groupVolume".format(self.group.id)
            headers = {
                "Authorization": "Bearer {}".format(self.access_token),
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            data = {
                "volume": volume
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                self.logger.info("Set absolute group volume to {}".format(volume))
                return True
            else:
                self.logger.error("Failed to set group volume.")
                raise errors.SonosError(response.status_code, response.text)


    class households:
        def __init__(self, control):
            self.control = control
            self.access_token = self.control.access_token
            self.logger = self.control.logger
            self.logger.info("Initializing households..")
            self.logger.info("Initialized households.")

        
    
    class playback:
        """

        """
        def __init__(self, control):
            self.control = control
            self.player = self.control.player
            self.access_token = self.control.access_token
            self.player = self.control.player
            self.logger = self.control.logger
            self.logger.info("Initializing Playback..")
            self.logger.info("Initialized Playback.")

        def getPlaybackStatus(self):
            """
            Get the current playback status.
            """
            self.logger.info("Getting playback status..")
            self.logger.info("Got playback status.")
            return "playback status"

        def loadLineIn(self):
            """
            Load line-in.
            """
            self.logger.info("Loading line-in..")
            self.logger.info("Loaded line-in.")
            return "line-in"

        def pause(self):
            """
            Pause playback.
            """
            self.logger.info("Pausing playback..")
            self.logger.info("Paused playback.")
            return "paused"

        def play(self):
            """
            Resume playback.
            """
            self.logger.info("Resuming playback..")

            headers = {"Authorization": "Bearer "+self.access_token, "Content-Type": "application/json"}
            
            sonoswait =  requests.get(f"https://api.ws.sonos.com/control/api/v1/groups/{self.player.groupId()}/playback/play", headers=headers).json()
            try:
                if sonoswait['fault']: # If there is a fault, return the fault.
                    self.logger.error("Fault: "+sonoswait['fault']['message'])
                    return sonoswait['fault']
                else:
                    self.logger.info("Groups: "+str(sonoswait))
                    return sonoswait
            except KeyError: 
                return sonoswait

            self.logger.info("Resumed playback.")
            return "playing"

        def seek(self, position):
            """
            Seek to a position.
            """
            self.logger.info("Seeking to position..")
            self.logger.info("Seeked to position.")
            return "seeked"

        def seekRelative(self, position):
            """
            Seek relative to the current position.
            """
            self.logger.info("Seeking relative to position..")
            self.logger.info("Seeked relative to position.")
            return "seeked relative"

        def setPlayMode(self, play_mode):
            """
            Set the play mode.
            """
            self.logger.info("Setting play mode..")
            self.logger.info("Set play mode.")
            return "set play mode"

        def skipToNext(self):
            """
            Skip to the next track.
            """
            self.logger.info("Skipping to next track..")
            self.logger.info("Skipped to next track.")
            return "skipped to next track"

        def skipToPrevious(self):
            """
            Skip to the previous track.
            """
            self.logger.info("Skipping to previous track..")
            self.logger.info("Skipped to previous track.")
            return "skipped to previous track"

        def subscribe(self):
            """
            Subscribe to the playback status.
            """
            self.logger.info("Subscribing to playback status..")
            self.logger.info("Subscribed to playback status.")
            return "subscribed to playback status"

        def togglePlayPause(self):
            """
            Toggle play/pause.
            """
            self.logger.info("Toggling play/pause..")
            self.logger.info("Toggled play/pause.")
            return "toggled play/pause"

        def unsubscribe(self):
            """
            Unsubscribe from the playback status.
            """
            self.logger.info("Unsubscribing from playback status..")
            self.logger.info("Unsubscribed from playback status.")
            return "unsubscribed from playback status"
