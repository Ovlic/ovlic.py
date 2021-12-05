
from . import abc
from . import control
from . import errors
from . import playback
import logging


class Group(abc.BaseGroup):
    def __init__(self, data):
        self.logger = logging.getLogger(__name__)
        self.data = data
        self._id = self.data['id']
        self._name = self.data['name']
        self._coordinatorId = self.data['coordinatorId']
        self._playbackState = self.data['playbackState']
        self._playerIds = self.data['playerIds']

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def coordinatorId(self) -> str:
        return self._coordinatorId

    @property
    def playbackState(self) -> str:
        return self._playbackState

    @property
    def playerIds(self) -> list:
        return self._playerIds
        

    def getVolume(self) -> abc.Volume:
        """
        Get the volume of the group.
        """
        self.logger.info("Getting group volume..")
        res = control.get(self, endpoint="/groups/{}/groupVolume".format(self._id))
        return res

    def setMute(self, mute:bool) -> bool:
        """
        Mutes the group.
        """
        self.logger.info("Muting group..")
        res = control.post(self, endpoint="/groups/{}/groupVolume/mute".format(self._id), params={"muted":mute})
        self.logger.info("Muted group.")
        return res

    def setRelativeVolume(self, volume:int) -> bool:
        """
        Sets the relative volume of the group.
        """
        if volume < -100 or volume > 100:
            raise errors.SonosError("Volume must be between -100 and 100.")
        
        self.logger.info("Setting relative group volume..")
        res = control.post(self, endpoint="/groups/{}/groupVolume/relative".format(self._id), params={"volumeDelta":volume})
        return res


    def setVolume(self, volume: int) -> bool:
        """
        Sets the absolute volume of the group.
        """
        if volume < 0 or volume > 100:
            raise errors.SonosError("Volume must be between 0 and 100.")
        
        self.logger.info("Setting absolute group volume..")
        res = control.post(self, endpoint="/groups/{}/groupVolume".format(self._id), params={"volume": volume})
        return res
        
    
    def getPlaybackStatus(self) -> abc.PlaybackStatus:
        """
        Get the playback status of the group.
        """
        self.logger.info("Getting group playback status..")
        res = control.get(self, endpoint="/groups/{}/playback".format(self._id))
        return res

    def loadLineIn(self) -> bool:
        """
        Loads the line-in into the group.
        """
        self.logger.info("Loading line-in into group..")
        res = control.post(self, endpoint="/groups/{}/playback/lineIn".format(self._id), data={})
        return res

    def pause(self) -> bool:
        """
        Pauses the group.
        """
        self.logger.info("Pausing group..")
        res = control.post(self, endpoint="/groups/{}/playback/pause".format(self._id), data={})
        return res

    def play(self) -> bool:
        """
        Plays the group.
        """
        self.logger.info("Playing group..")
        res = control.post(self, endpoint="/groups/{}/playback/play".format(self._id), data={})
        return res

    def seek(self, time:int) -> bool:
        """
        Seeks the group.
        """
        self.logger.info("Seeking group..")
        res = control.post(self, endpoint="/groups/{}/playback/seek".format(self._id), data={"positionMillis": time})
        return res

    def seekRelative(self, time:int) -> bool:
        """
        Relative-Seeks the group.
        """
        self.logger.info("Seeking group..")
        res = control.post(self, endpoint="/groups/{}/playback/seekRelative".format(self._id), data={"deltaMillis": time})
        return res

    def setPlayMode(self, playMode:abc.PlayMode) -> bool:
        """
        Sets the play mode of the group.
        """
        self.logger.info("Setting group play mode..")
        res = control.post(self, endpoint="/groups/{}/playback/playMode".format(self._id), data={"playMode": playMode})
        return res

    def repeat(self) -> bool:
        """
        Repeats the group.
        """
        self.logger.info("Repeating group..")
        res = control.post(self, endpoint="/groups/{}/playback/playMode".format(self._id), data={"playMode": "repeat"})
        return res

    def repeatOne(self) -> bool:
        """
        Repeats the group indefinetly.
        """
        self.logger.info("Setting group to repeat indefinetly..")
        res = control.post(self, endpoint="/groups/{}/playback/playMode".format(self._id), data={"playMode": "repeatOne"})
        return res

    def shuffle(self) -> bool:
        """
        Shuffles the group.
        """
        self.logger.info("Shuffling group..")
        res = control.post(self, endpoint="/groups/{}/playback/playMode".format(self._id), data={"playMode": "shuffle"})
        return res

    def crossfade(self) -> bool:
        """
        Crossfades the group.
        """
        self.logger.info("Crossfading group..")
        res = control.post(self, endpoint="/groups/{}/playback/playMode".format(self._id), data={"playMode": "crossfade"})
        return res

    def skipToNext(self) -> bool:
        """
        Skips to the next track in the group.
        """
        self.logger.info("Skipping to next track in group..")
        res = control.post(self, endpoint="/groups/{}/playback/skipToNextTrack".format(self._id), data={})
        return res

    def skipToPrevious(self) -> bool:
        """
        Skips to the previous track in the group.
        """
        self.logger.info("Skipping to previous track in group..")
        res = control.post(self, endpoint="/groups/{}/playback/skipToPreviousTrack".format(self._id), data={})
        return res

    def togglePlayPause(self) -> bool:
        """
        Toggles the play/pause state of the group.
        """
        self.logger.info("Toggling play/pause state of group..")
        res = control.post(self, endpoint="/groups/{}/playback/togglePlayPause".format(self._id), data={})
        return res

    def getMetadataStatus(self) -> abc.PlaybackMetadata:
        """
        Get the metadata status of the group.
        """
        self.logger.info("Getting group metadata status..")
        res = control.get(self, endpoint="/groups/{}/playbackMetadata".format(self._id))
        return res

    def playbackSubscribe(self):
        """
        Subscribe to the group's playback events.
        """
        self.logger.info("Subscribing to group playback events..")
        res = control.post(self, endpoint="/groups/{}/playback/subscription".format(self._id), params={})
        return res

    
    