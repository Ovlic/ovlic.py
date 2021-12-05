
import logging

from . import abc
from . import control
from .group import Group
from .player import Player


class groups(object):
    """
    Represents the current set of logical players and groups in the household.
    """
    def __init__(self, data):
        self._groups = []
        self._players = []
        for i in range(0, len(data['groups'])):
            self._groups.append(Group(data['groups'][i]))

        for i in range(0, len(data['players'])):
            self._players.append(Player(data['players'][i]))

    @property
    def groups(self) -> list:
        "A list of :class:`Group` objects in this household."
        return self._groups

    @property
    def players(self) -> list:
        "A list of :class:`Player` objects in this household."
        return self._players


class Household(abc.BaseHousehold):
    """
    Represents a household of Sonos devices.
    """
    def __init__(self, data):
        self.logger = logging.getLogger(__name__)
        self._id = data['id']
    
    def __repr__(self) -> str:
        return "<Household id={0._id}>".format(self)


    @property
    def id(self) -> str:
        """
        Get the ID of the household.\n
        :return: The ID of the household.
        """
        return self._id


    def getGroups(self) -> groups:
        "Get all groups."
        self.logger.info("Getting groups..")
        res = control.get(endpoint="/households/{}/groups".format(self.id))
        return groups(res)

    def createGroup(self, player_ids:list):
        """
        Create a group.\n
        :param player_ids: List of player ids to be added to the group.
        """
        self.logger.info("Creating group..")
        res = control.post(endpoint="/households/{}/groups/createGroup".format(self.id), data={"playerIds": player_ids})
        return res


    def getFavorites(self):
        "Get all favorites of a household."
        self.logger.info("Getting favorites..")
        res = control.get(endpoint="/households/{}/favorites".format(self.id))
        for i in range (0, len(res['items'])):
            res['items'][i] = abc.Favorite(res['items'][i])
        return res

    def loadFavorite(self, favorite_id:str, playOnCompletion:bool=False, action:abc.QueueAction=abc.QueueAction.append(), playModes:str=None):
        "Load a favorite."
        self.logger.info("Loading favorite..")
        data = {
            "favoriteId": favorite_id,
            "playOnCompletion": playOnCompletion,
            "action": action
        }
        if playModes is not None:
            data["playModes"] = playModes
            
        res = control.post(endpoint="/households/{}/favorites".format(self.id), params=data)
        return res