"""
API Wrapper for Sonos.
"""

__title__ = 'sonos'
__author__ = 'Ovlic'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present Ovlic'
__version__ = '0.0.1'



# import logging
from . import errors
from . import utils
from . import abc
from .auth import Authorization
from .client import Client
from .group import Group
from .household import Household
from .player import Player
from .subscription import Subscription, subscribe, unsubscribe


# from . import config
# from .control import Control

#class sonos:

    #def __init__(self, client_id, client_secret, redirect_uri, **kwargs):
"""
        self.logger = logging.getLogger(__name__)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        if "access_token" in kwargs:
            self.access_token = kwargs["access_token"]
            config.access_token = self.access_token
        else:
            self.access_token = None
        if "refresh_token" in kwargs:
            self.refresh_token = kwargs["refresh_token"]
        else:
            self.refresh_token = None"""
            
        #self.authorization = Authorization(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, access_token=self.access_token, refresh_token=self.refresh_token)
        #self.control = Control(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri)
        
        #self.logger.info("Sonos API Wrapper initialized.")


"""class config:
    
    def __init__(self, client_id, client_secret, **kwargs):
        config.client_id = client_id
        config.client_secret = client_secret

        if "access_token" in kwargs:
            config.access_token = kwargs['access_token']
            
        if "refresh_token" in kwargs:
            config.access_token = kwargs['refresh_token']"""