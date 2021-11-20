
import logging

from . import config
from . import control
from . import errors
from .household import Household


class Client:
    """
    Represents a client connection to Sonos
    """
    def __init__(self, access_token, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.access_token = access_token
        self.refresh_token = kwargs.get('refresh_token')
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.redirect_uri = kwargs.get('redirect_uri')

        self.logger.info('Verifying access token...')
        try:
            control.verify_access_token(self.access_token)
        except errors.InvalidAccessToken:
            self.logger.info('Access token is invalid, refreshing...')
            if self.refresh_token is None:
                self.logger.error('No refresh token provided, cannot refresh access token')
                raise errors.InvalidAccessToken
            try:
                refr = control.refresh_access_token()
                self.access_token = refr['access_token']
            except:
                self.logger.error('Failed to refresh access token')
                raise errors.InvalidRefreshToken

            self.logger.info('Access token refreshed')
            self.logger.debug('Access token: %s', self.access_token)
        
        self.logger.info('Access token verified')
        config.access_token = self.access_token


    def getHouseholds(self):
        """
        Returns a list of households
        """
        self.logger.info("Getting households..")
        req = control.get(endpoint="/households")
        res = []
        for household in req['households']:
            res.append(Household(household))
        return res


    def getHousehold(self):
        """
        Returns the first household found.
        """
        self.logger.info("Getting household ...")
        req = control.get(endpoint="/households")
        return Household(req['households'][0])