import requests
from .. import errors
from ..utils import formatCommas

class rbx:
    """Handler for Roblox functions"""

    def __init__(self, username:str):
        user = rbx.get(self, url=f"https://api.roblox.com/users/get-by-username?username={username}")
        self.name = username
        self.id = user.id

    def getid(self):
        """
        Get a Roblox user from their ID
        Parameters
        -----------
        username: :class:`str`
            The Roblox username to fetch
        Raises
        ------
        :exc:`.rbxError`
            If an error occurs with the request.
        """
        res = rbx.get(f"https://api.roblox.com/users/get-by-username?username={self.username}")
        return res.Id

    def get(self, url):
        req = requests.get(url).json()
        res = rbx.rattr(_dict=req)
        try:
            if not res.success: raise errors.rbxError(res.errorMessage, self.username)
        except AttributeError: 
            pass
        try:
            if res.errors:
                res.errors = rbx.rattr(_dict=res.errors[0])
                raise errors.rbxError(res.errors.message)
        except AttributeError:
            pass
        return res


    def url_as(self, circular, size, format):
        """Arg check for "_as" functions"""
        sizes = [48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720]
        if format == None:
            format = "png"
        format = format.lower()
        if format != ("png" or "jpeg"):
            raise ValueError(f'Argument format must be "png" or "jpg", not {format}')
        if not isinstance(circular, bool):
            raise TypeError(f"Argument circular must be of type bool, not {type(circular)}")
        if size not in sizes:
            raise ValueError("Invalid Size. Acceptable Sizes: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720.")
        return

    class rattr(object):
        """convert :class:`dict` to :class:`class`"""
        def __init__(self, _dict):
            _dict = {k[0].lower()+k[1:]: v for k, v in _dict.items()}
            for key in _dict:
                if key == "isOnline": _key = "online"
                else: _key = key
                if _dict[key] is not None: setattr(self, _key, _dict[key])

    class status(object):
        """Class for status subproperties"""
        def __init__(self, outerself):
            outerself = outerself.__dict__
            for key in outerself:
                setattr(self, key[1:], outerself[key])

        @property
        def online(self):
            """If user is online.\n
            Returns :class:`bool`"""
            res = rbx.get(self, url=f"https://api.roblox.com/users/{self.id}/onlinestatus/")
            return res.online

        @property
        def lastLocation(self):
            """Returns what the user was doing when it was last online. (Playing, creating, etc.)\n
            Returns :class:`str`
            """
            res = rbx.get(self, url=f"https://api.roblox.com/users/{self.id}/onlinestatus/")
            return res.lastLocation

        @property
        def lastOnline(self):
            """Returns time and date the user was last offline.\n
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://api.roblox.com/users/{self.id}/onlinestatus/")
            return res.lastOnline

    class thumbnails(object):
        """Class for thumbnail subproperties"""
        def __init__(self, outerself):
            outerself = outerself.__dict__
            for key in outerself:
                setattr(self, key[1:], outerself[key])
            
        @property
        def avatar_bust(self):
            """Returns avatar-bust image url of user.\n
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar-bust?userIds={self.id}&size=48x48&format=Png&isCircular=false")
            res.data = rbx.rattr(_dict=res.data[0])
            return res.data.imageUrl

        @property
        def avatar_headshot(self):
            """Returns avatar-headshot image url of user.\n
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={self.id}&size=48x48&format=Png&isCircular=false")
            res.data = rbx.rattr(_dict=res.data[0])
            return res.data.imageUrl

        def avatar_bust_as(self, circular=False, size=48, format=None):
            """
            Returns avatar-bust image url for user.
            Parameters
            -----------
            circular: :class:`bool`
                If the image is circular. Defaults to False.
            size: :class:`int`
                Width and height of image. Must be one of: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720. Defaults to 48.
            format: :class:`str`
                If the image should be a png or jpeg. Defaults to png.
            Raises
            ------
            :exc:`TypeError`
                If circular is not a :class:`bool`.
            :exc:`ValueError`
                If format is not "png" or "jpeg".
            :exc:`.ValueError`
                If an invalid size is passed.
            """
            if format == None: format = "png"
            rbx.url_as(self, circular, size, format)
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar-bust?userIds={self.id}&size={size}x{size}&format={format}&isCircular={str(circular)}")
            res = rbx.rattr(res.data[0])
            return res.imageUrl

        def avatar_headshot_as(self, circular=False, size=48, format=None):
            """
            Returns avatar-headshot image url for user.
            Parameters
            -----------
            circular: :class:`bool`
                If the image is circular. Defaults to False.
            size: :class:`int`
                Width and height of image. Must be one of: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720. Defaults to 48.
            format: :class:`str`
                If the image should be a png or jpeg. Defaults to png.
            Raises
            ------
            :exc:`TypeError`
                If circular is not a :class:`bool`.
            :exc:`ValueError`
                If format is not "png" or "jpeg".
            :exc:`.ValueError`
                If an invalid size is passed.
            """
            if format == None: format = "png"
            rbx.url_as(self, circular, size, format)
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={self.id}&size={size}x{size}&format={format}&isCircular={str(circular)}")
            res = rbx.rattr(res.data[0])
            return res.imageUrl


    class user(object):
        """Represents a Roblox user.
    Attributes
    -----------
    id: :class:`int`
        Returns id of current user.
    name :class:`str`
        Returns name of current user.
    about: :class:`str`
        Returns the about section of current user.
    created: :class:`str`
        Returns creation date of current user.
    displayName: :class:`str`
        Returns the display name of current user.
    friendcount: :class:`int`
        Returns friend count of current user.
    avatar: :class:`str`
        Returns image url of current user.
    followers: :class:`int`
        Returns followers of current user.
    following: :class:`int`
        Returns followings of current user.
    prevnames: :class:`list`
        Returns a list of current user's previous usernames. (Max 25)
    favgames: :class:`list`
        Returns a list of the current user's favorite games.
    createdgames: :class:`list`
        Returns a list of the current user's created games.
    groups: :class:`list`
        Returns a list of the current user's joined groups.
    rap: :class:`int`
        Returns the total Recent Average Price of all current user's limiteds.
    """
        def __init__(self, username:str):  
            user = rbx.get(self, url=f"https://api.roblox.com/users/get-by-username?username={username}")
            self._name = username
            self._id = user.id
            self.thumbnails = rbx.thumbnails(self)
            self.status = rbx.status(self)

        @property
        def id(self):
            """Returns id of current user
            Returns :class:`int`"""
            return self._id

        @property
        def name(self):
            """Returns the name of current user.
            Returns :class:`str`"""
            return self._name

        @property
        def about(self):
            """Returns the about section of current user.
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://users.roblox.com/v1/users/{self.id}")
            return res.description

        @property
        def created(self):
            """Returns creation date for current user.
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://users.roblox.com/v1/users/{self.id}")
            return res.created

        @property
        def displayName(self):
            """Returns display name of user.
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://users.roblox.com/v1/users/{self.id}")
            return res.displayName

        @property
        def friendcount(self):
            """Returns friend count of user.
            Returns :class:`int`"""
            res = rbx.get(self, url=f"https://friends.roblox.com/v1/users/{self.id}/friends/count")
            res = res['count']
            return res

        @property
        def avatar(self):
            """Returns avatar url of user.
            Returns :class:`str`"""
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar?userIds={self.id}&size=150x150&format=Png&isCircular=false")
            return res
        
        @property
        def followers(self):
            """Returns follower count of user.
            Returns :class:`int`"""
            count = rbx.get(self, url=f"https://friends.roblox.com/v1/users/{self.id}/followers/count")
            count = formatCommas(count.count)
            return count

        @property
        def following(self):
            """Returns following count of user.
            Returns :class:`int`"""
            count = rbx.get(self, url=f"https://friends.roblox.com/v1/users/{self.id}/followings/count")
            count = formatCommas(count.count)
            return count

        @property
        def prevnames(self):
            """Returns previous usernames of user. (Max 25)\n
            Returns :class:`list`"""
            newres = []
            res = rbx.get(self, url=f"https://users.roblox.com/v1/users/{self.id}/username-history?limit=25")
            res = res.data
            for i in range(0, len(res)):
                res[i] = rbx.rattr(res[i])
                newres.append(res[i].name)
            return newres

        @property
        def favgames(self):
            """Returns favorite games of user.
            Returns :class:`list`"""
            res = rbx.get(self, url=f"https://games.roblox.com/v2/users/{self.id}/favorite/games?")
            res = res.data
            for i in range(0, len(res)):
                res[i] = rbx.rattr(res[i])
                res[i].creator = rbx.rattr(res[i].creator)
                res[i].rootPlace = rbx.rattr(res[i].rootPlace)
            return res

        @property
        def createdgames(self):
            """Returns created games of user.
            Returns :class:`list`"""
            res = rbx.get(self, url=f"https://games.roblox.com/v2/users/{self.id}/games?")
            res = res.data
            for i in range(0, len(res)):
                res[i] = rbx.rattr(res[i])
                res[i].creator = rbx.rattr(res[i].creator)
                res[i].rootPlace = rbx.rattr(res[i].rootPlace)
            return res

        @property
        def groups(self):
            """Returns groups that user is in\n
            Returns :class:`list`"""
            res = rbx.get(self, url=f"https://groups.roblox.com/v2/users/{self.id}/groups/roles")
            res = res.data
            for i in range(0, len(res)):
                res[i] = rbx.rattr(res[i])
                res[i].group = rbx.rattr(res[i].group)
                res[i].role = rbx.rattr(res[i].role)

            return res

        @property
        def rap(self):
            """Returns Recent Average Price for user
            Returns :class:`int`"""
            therap = 0
            res = rbx.get(self, url=f"https://inventory.roblox.com/v1/users/{self.id}/assets/collectibles?sortOrder=Asc&limit=100")
            rap = res.data
            rapitems = len(rap)
            for i in range(0, rapitems):
                rap[i] = rbx.rattr(_dict=rap[i])
                try: rap[i].recentAveragePrice
                except AttributeError: continue
                if i == 0: therap = rap[i].recentAveragePrice
                else: therap += rap[i].recentAveragePrice
            return formatCommas(therap)

        def avatar_as(self, circular=False, size=48, format=None):
            """
            Returns avatar image url for user.
            Parameters
            -----------
            circular: :class:`bool`
                If the image is circular. Defaults to False.
            size: :class:`int`
                Width and height of image. Must be one of: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720. Defaults to 48.
            format: :class:`str`
                If the image should be a png or jpeg. Defaults to png.
            Raises
            ------
            :exc:`TypeError`
                If circular is not a :class:`bool`.
            :exc:`ValueError`
                If format is not "png" or "jpeg".
            :exc:`.ValueError`
                If an invalid size is passed.
                """
            if format == None: format = "png"
            rbx.url_as(self, circular, size, format)
            res = rbx.get(self, url=f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={self.id}&size={size}x{size}&format={format}&isCircular={str(circular)}")
            res = rbx.rattr(res.data[0])
            return res.imageUrl