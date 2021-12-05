


class Artist(object):
    """
    Represents data returned from the Sonos API for an artist.
    """
    def __init__(self, data):
        self._name = data['name']

        try:
          self.id = data['id']
        except KeyError:
          self.id = None
        try:
          self.imageUrl = data['imageUrl']
        except KeyError:
          self.imageUrl = None
        
        try:
          self.tags = data['tags']
        except KeyError:
          self.tags = None

    @property
    def name(self) -> str:
        return self._name


class Album(object):
  """
    Represents data returned from the Sonos API for an artist.
  """
  def __init__(self, data):
      self._name = data['name']

      try:
        self.id = data['id']
      except KeyError:
        self.id = None
      try:
        self.artist = data['artist']
      except KeyError:
        self.artist = None
      try:
        self.imageUrl = data['imageUrl']
      except KeyError:
        self.imageUrl = None
      
      try:
        self.tags = data['tags']
      except KeyError:
        self.tags = None

  @property
  def name(self) -> str:
    return self._name


class PlaybackContainer(object):
    """
    Represents data returned from the Sonos API for playback.
    """
    def __init__(self, data):
        self._name = data['name']
        self._type = data['type']
        self.id = MusicObjectId(data['id'])
        self.service = Service(data['service'])
        self._imageUrl = data['imageUrl']
        self._tags = data['tags']

    @property
    def name(self) -> str:
      return self._name
    
    @property
    def type(self) -> str:
      return self._type

    @property
    def imageUrl(self) -> str:
      return self._imageUrl

    @property
    def tags(self) -> list:
      return self._tags


class MusicObjectId(object):
    """
    Represents data returned from the Sonos API for music object ids.
    """
    def __init__(self, data):
        self.objectId = data['objectId']
        try:
          self.serviceId = data['serviceId']
        except KeyError:
          self.serviceId = None
        try:
          self.accountId = data['accountId']
        except KeyError:
          self.accountId = None


class Policies: pass # Somehow removed need to be readded


class PositionInformation(object):
  """
  Represents data returned from the Sonos API for position information.
  """
  def __init__(self, data):
    self.itemId = data['itemId']
    try:
      self.positionMillis = data['positionMillis']
    except KeyError:
      self.positionMillis = None


class Service(object):
  """
  Represents a music service identifier.
  """
  def __init__(self, data):
    self.name = data['name']
    try:
      self.id = data['id']
    except KeyError:
      self.id = None
    try:
      self.imageUrl = data['imageUrl']
    except KeyError:
      self.imageUrl = None


class Track(object):
    """
    Represents data returned from the Sonos API for tracks.
    """

    def __init__(self, data):
        self._name = data['name']
        self._type = data['type']
        self._imageUrl = data['imageUrl']
        self._tags = data['tags']
        self.album = Album(data['album'])
        self.artist = Artist(data['artist'])
        self.id = MusicObjectId(data['id'])
        self.service = Service(data['service'])
        try:
          self.durationMillis = data['durationMillis']
        except KeyError:
          self.durationMillis = None

    @property
    def name(self) -> str:
      return self._name
    
    @property
    def type(self) -> str:
      return self._type
    
    @property
    def imageUrl(self) -> str:
      return self._imageUrl
    
    @property
    def tags(self) -> list:
      return self._tags