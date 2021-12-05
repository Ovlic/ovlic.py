import abc
from . import playback

class BasePlayer(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def id(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def apiVersion(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def minApiVersion(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def softwareVersion(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def websocketUrl(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def isUnregistered(self) -> bool:
        pass
    @property
    @abc.abstractmethod
    def capabilities(self) -> list:
        pass
    @property
    @abc.abstractmethod
    def deviceIds(self) -> list:
        pass

class BaseGroup(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def id(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def coordinatorId(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def playbackState(self) -> str:
        pass
    @property
    @abc.abstractmethod
    def playerIds(self) -> list:
        pass

class BaseHousehold(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def id(self) -> str:
        pass

class AudioClipType(str):
  """
  Indicates the type of sound that Sonos should play.
  """
  def __init__(self, mode):
    upperMode = mode.upper()
    if upperMode != "CHIME" and upperMode != "CUSTOM":
      raise ValueError("Invalid audio clip type: {}".format(mode))

class AudioClipState:
  """
  Represents the state of an audio clip.
  """
  class active:
      "Currently playing."
      def __name__(self):
        return "active"
  class dismissed:
      "Dismissed."
      def __name__(self):
        return "dismissed"
  class done:
      "Playback complete."
      def __name__(self):
        return "done"
  class error:
      "Playback encountered an error."
      def __name__(self):
        return "error"
  class interrupted:
      "Playback interrupted, for example, by a high priority audio clip."
      def __name__(self):
        return "interrupted"

  def determineState(_state):
    "Determine the state of an audio clip"
    state = _state.upper()
    if state == "ACTIVE":
      return AudioClipState.active()
    elif state == "DISMISSED":
      return AudioClipState.dismissed()
    elif state == "DONE":
      return AudioClipState.done()
    elif state == "ERROR":
      return AudioClipState.error()
    elif state == "INTERRUPTED":
      return AudioClipState.interrupted()
    else:
      raise ValueError("Unknown state: " + state)

class Priority:
  """
  Indicates the priority of an audio clip.
  """
  class low:
    def __name__(self):
      return "LOW"
    pass
  class high:
    def __name__(self):
      return "HIGH"
    pass
  class default:
    def __name__(self):
      return "LOW"

class AudioClip:
  """
  Represents an audio clip.
  """
  def __init__(self, data):
    self._appId = data['appId']
    try:
      self._clipType = AudioClipType(data['clipType'])
    except KeyError:
      self._clipType = "CHIME"
    self._id = data['id']
    self._name = data['name']
    try:
      if data['priority'] == "LOW":
        self._priority = Priority.low()
      elif data['priority'] == "HIGH":
        self._priority = Priority.high()
    except KeyError:
      self._priority = Priority.low()
    self.status = AudioClipState.determineState(data['state'])

  @property
  def appId(self):
    "This string identifies the app that created the audioClip. Companies should use their reversed Internet domain name as the identifier, similar to com.acme.app."
    return self._appId

  @property
  def clipType(self) -> AudioClipType:
    "Sonos plays a built-in sound when this option is provided. The default value is `CHIME`."
    return self._clipType

  @property
  def id(self) -> str:
    "Sonos generates this unique identifier and assigned to the audio clip."
    return self._id

  @property
  def name(self) -> str:
    "User identifiable string."
    return self._name

  @property
  def priority(self) -> Priority.low()or Priority.high():
    "Clip priority. Clips are `low` priority by default."
    return self._priority

  @property
  def state(self) -> AudioClipState.active() or AudioClipState.dismissed() or AudioClipState.done() or AudioClipState.error() or AudioClipState.interrupted():
    "The current state of the audio clip."
    return self.status

class Volume(object):
    """
    Represents data returned from the Sonos API for volume.
    """
    def __init__(self, data):
        self.muted = data['muted']
        self.fixed = data['fixed']
        self.volume = data['volume']

    @property
    def muted(self) -> bool:
        return self.muted

    @property
    def fixed(self) -> bool:
        return self.fixed

    @property
    def volume(self) -> int:
        return self.volume

class PlayModes(object):
    """
    Represents data returned from the Sonos API for play modes.
    """
    def __init__(self, data):
        self._repeat = data['repeat']
        self._repeatOne = data['repeatOne']
        self._crossfade = data['crossfade']
        self._shuffle = data['shuffle']

    @property
    def repeat(self) -> bool:
        return self._repeat

    @property
    def repeatOne(self) -> bool:
        return self._repeatOne

    @property
    def crossfade(self) -> bool:
        return self._crossfade

    @property
    def shuffle(self) -> bool:
        return self._shuffle

class PlaybackState(str):
  """
  Represents a Player's current state
  """
  def __init__(self, state):
    upperState = state.upper
    if upperState != "PLAYBACK_STATE_BUFFERING" and upperState != "PLAYBACK_STATE_IDLE" and upperState != "PLAYBACK_STATE_PAUSED" and upperState != "PLAYBACK_STATE_PLAYING":
      raise ValueError("Invalid playback state: " + state)


class PlayMode(str):
  """
  Represents player playmodes: `repeat`, `repeatOne`, `shuffle`, `crossfade`.
  """
  def __init__(self, mode):
    if mode != "repeat" and mode != "repeatOne" and mode != "shuffle" and mode != "crossfade":
      raise ValueError("Invalid play mode: " + mode)

class PlaybackActions(object):
    """
    Represents data returned from the Sonos API for available playback actions.
    """
    def __init__(self, data):
        self._canSkip = data['canSkip']
        self._canSkipBack = data['canSkipBack']
        self._canSeek = data['canSeek']
        self._canRepeat = data['canRepeat']
        self._canRepeatOne = data['canRepeatOne']
        self._canCrossfade = data['canCrossfade']
        self._canShuffle = data['canShuffle']

    @property
    def canSkip(self) -> bool:
        return self._canSkip

    @property
    def canSkipBack(self) -> bool:
        return self._canSkipBack

    @property
    def canSeek(self) -> bool:
        return self._canSeek

    @property
    def canRepeat(self) -> bool:
        return self._canRepeat

    @property
    def canRepeatOne(self) -> bool:
        return self._canRepeatOne

    @property
    def canCrossfade(self) -> bool:
        return self._canCrossfade

    @property
    def canShuffle(self) -> bool:
        return self._canShuffle

class PlaybackStatus(object):
    """
    Represents data returned from the Sonos API for playback status.
    """
    def __init__(self, data):
        self._playbackState = PlaybackState(data['playbackState'])
        self._positionMillis = data['positionMillis']
        self._itemId = data['itemId']
        self._queueVersion = data['queueVersion']
        self._previousItemId = data['previousItemId']
        self._previousPositionMillis = data['previousPositionMillis']
        self._playModes = PlayModes(data['playModes'])
        self._availablePlaybackActions = PlaybackActions(data['availablePlaybackActions'])

    @property
    def playbackState(self) -> PlaybackState:
        return self._playbackState

    @property
    def positionMillis(self) -> int:
        return self._positionMillis

    @property
    def itemId(self) -> str:
        return self._itemId

    @property
    def queueVersion(self) -> str:
        return self._queueVersion

    @property
    def previousItemId(self) -> str:
        return self._previousItemId

    @property
    def previousPositionMillis(self) -> int:
        return self._previousPositionMillis

    @property
    def playModes(self) -> PlayModes:
        return self._playModes

class PlaybackItem(object):
    """
    Represents data returned from the Sonos API for metadata.
    """
    def __init__(self, data):
      self.track = playback.Track(data['track'])

class PlaybackMetadata(object):
    """
    Represents data returned from the Sonos API for playback metadata.
    """
    def __init__(self, data):
      self.container = playback.PlaybackContainer(data['container'])
      self.currentItem = PlaybackItem(data['currentItem'])
      self.nextItem = PlaybackItem(data['nextItem'])
      try:
          self.streamInfo = data['streamInfo']
      except KeyError:
          self.streamInfo = None

class Favorite(object):
    """
    Represents data returned from the Sonos API for favorites.
    """
    def __init__(self, data):
      self._id = data['id']
      self._name = data['name']
      try:
        self.description = data['description']
      except KeyError:
        self.description = None
      # self._type = data['type']  NOT IMPLEMENTED IN THE SONOS API
      try:
        self.imageUrl = data['imageUrl']
      except KeyError:
        self.imageUrl = None
      try:
        self.imageCompilation = data['imageCompilation']
      except KeyError:
        self.imageCompilation = None
      try:
        self.service = playback.Service(data['service'])
      except KeyError:
        self.service = None

    @property
    def id(self) -> str:
      return self._id

    @property
    def name(self) -> str:
      return self._name

class Playlist(object):
    """
    Represents data returned from the Sonos API for playlists.
    """
    def __init__(self, data):
      self._id = data['id']
      self._name = data['name']
      self._type = data['type']
      self._trackCount = data['trackCount']

    @property
    def id(self) -> str:
      return self._id

    @property
    def name(self) -> str:
      return self._name

    @property
    def type(self) -> str:
      return self._type
    
    @property
    def trackCount(self) -> int:
      return self._trackCount

class PlayerSettings(object):
  """
  Represents a player's settings.
  """
  def __init__(self, data):
    self._volumeMode = data['name']
    self._volumeScalingFactor = data['volumeScalingFactor']
    self._monoMode = data['monoMode']
    self._wifiDisable = data['wifiDisable']

  @property
  def volumeMode(self) -> str:
    return self._volumeMode

  @property
  def volumeScalingFactor(self) -> float:
    return self._volumeScalingFactor

  @property
  def monoMode(self) -> bool:
    return self._monoMode

  @property
  def wifiDisable(self) -> bool:
    return self._wifiDisable

class MusicServiceAccount(object):
  """
  Represents a music service account.
  """
  def __init__(self, data):
    self._userIdHashCode = data['userIdHashCode']
    self._nickname = data['nickname']
    self._id = data['id']
    self._isGuest = data['isGuest']
    self.service = playback.Service(data['service'])

  @property
  def userIdHashCode(self) -> str:
    "Opaque hash of the user account sent by the service in the `match` command."
    return self._userIdHashCode

  @property
  def nickname(self) -> str:
    "The name for the music service account presented to the user when they view their account from the Sonos app."
    return self._nickname

  @property
  def id(self) -> str:
    "The account ID for the music service account."
    return self._id

  @property
  def isGuest(self) -> bool:
    "Indicates whether the account is a guest account or not. If :bool:`True`, the account is a guest account. If :bool:`False`, it is not."
    return self._isGuest

class Capabilities(object):
  """
  Represents a player's capabilities.
  """
  def __init__(self, data):
    self._playback = True if 'PLAYBACK' in data else False
    self._cloud = True if 'CLOUD' in data else False
    self._HTPlayback = True if 'HT_PLAYBACK' in data else False
    self._HTPowerState = True if 'HT_POWER_STATE' in data else False
    self._airplay = True if 'AIRPLAY' in data else False
    self._lineIn = True if 'LINE_IN' in data else False
    self._audioClip = True if 'AUDIO_CLIP' in data else False
    # Not yet implemented in the Sonos API
    # self._voice = True if 'VOICE' in data else False
    self._speakerDetection = True if 'SPEAKER_DETECTION' in data else False
    self._fixedVolume = True if 'FIXED_VOLUME' in data else False


  @property
  def playback(self) -> bool:
    "The player can produce audio. You can target it for playback."
    return self._playback

  @property
  def cloud(self) -> bool:
    "The player can send commands and receive events over the internet."
    return self._cloud

  @property
  def HTPlayback(self) -> bool:
    "The player is a home theater source. It can reproduce the audio from a home theater system, typically delivered by S/PDIF or HDMI."
    return self._HTPlayback

  @property
  def HTPowerState(self) -> bool:
    "The player can control the power state of a home theater system."
    return self._HTPowerState

  @property
  def airplay(self) -> bool:
    "The player can host AirPlay streams."
    return self._airplay

  @property
  def lineIn(self) -> bool:
    "The player has an analog line-in."
    return self._lineIn

  @property
  def audioClip(self) -> bool:
    "The device is capable of playing audio clip notifications."
    return self._audioClip

  # Not yet implemented in the Sonos API
  # @property
  # def voice(self) -> bool:
    # "The device supports the voice namespace"
    # return self._voice

  @property
  def speakerDetection(self) -> bool:
    "The component device is capable of detecting connected speaker drivers."
    return self._speakerDetection

  @property
  def fixedVolume(self) -> bool:
    "The device supports fixed volume."
    return self._fixedVolume


class QueueAction:
  """
  Represents how to load content into the queue.
  """
  def append():
    return "APPEND"
    
  def insert():
    return "INSERT"
    
  def insertNext():
    return "INSERT_NEXT"

  def replace():
    return "REPLACE"