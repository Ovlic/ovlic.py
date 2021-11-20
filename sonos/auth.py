
import logging
import base64
import requests
import urllib

from . import errors
from . import config


class Authorization:
    """
    Authorization API for Sonos.
    """
    def __init__(self, client_id, client_secret, **kwargs):
        self.logger = logging.getLogger(__name__)
        
        if 'redirect_uri' in kwargs:
            self.redirect_uri = kwargs['redirect_uri']
        else:
            self.redirect_uri = None

        if "access_token" in kwargs:
            self.access_token = kwargs["access_token"]
            config.access_token = self.access_token
        else:
            self.access_token = None
            
        if "refresh_token" in kwargs:
            self.refresh_token = kwargs["refresh_token"]
            config.refresh_token = self.refresh_token
        else:
            self.refresh_token = None

        base_bytes = base64.b64encode(f"{client_id}:{client_secret}".encode('ascii'))
        # print(base_bytes)
        self.auth_key = str(base_bytes.decode())

        self.client_id = client_id
        config.client_id = self.client_id

        self.client_secret = client_secret
        config.client_secret = self.client_secret

        self.logger.info("Sonos Authentication API Wrapper initialized.")

    def raise_err(response, **kwargs):
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
                try:
                    errorCode = data['error']
                except KeyError:
                    pass

        # Authorization errors
        if errorCode == "invalid_request":
            if kwargs.get("refresh_token") == True:
                raise errors.InvalidRefreshToken("Invalid refresh token.")

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

    def post(self, endpoint, data):
        headers = {
            "Authorization": "Basic "+self.auth_key,
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
            }
        
        """data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }"""

        if endpoint is None:
            endpoint = "/login/v3/oauth/access"

        r = requests.post("https://api.sonos.com{}".format(endpoint), headers=headers, data=data).json()
        print(r)
        try:
            if r['error']:
                raise errors.DefaultError(r['error'])
        except KeyError:
            pass
        config.access_token = r['access_token']
        return r


    def create_access_token(self):
        """
        Create an access token from Sonos.
        """
        self.logger.info("Creating access token...")
        headers = {
            "Authorization": "Basic "+self.auth_key,
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
            }
        data = {
            'grant_type': 'authorization_code',
            'code': 'eee',
            'redirect_uri': urllib.parse.quote(str(self.redirect_uri)),
            }

        r = requests.post("https://api.sonos.com/login/v3/oauth/access", headers=headers, data=data).json()
        print(self.auth_key)
        print(r)
        """if r['error']:
            raise errors.DefaultError(r['error'])
        print(r)"""
        return r
        

    def refresh_access_token(self):
        """
        Refresh an access token from Sonos.
        """
        if self.refresh_token is None:
            raise errors.InvalidRequest("No refresh token available.")
        self.logger.info("Refreshing access token...")
        headers = {
            "Authorization": "Basic "+self.auth_key,
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
            }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        r = requests.post("https://api.sonos.com/login/v3/oauth/access", headers=headers, data=data).json()
        print(r)
        try:
            if r['error']:
                raise errors.DefaultError(r['error'])
        except KeyError:
            pass
        config.access_token = r['access_token']
        return r