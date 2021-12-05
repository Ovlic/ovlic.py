
import logging
from .control import subscribe

class SubscribeType(str):
    """
    Represents a Player's current state
    """
    def __init__(self, _type):
        types = [
            'audioClip',
            'favorites',
            'groups',
            'groupVolume',
            'playback',
            'playbackMetadata',
            'playbackSession',
            'playerVolume',
            'playlists',
        ]
        if _type not in types:
            raise ValueError("Invalid subscription type: " + _type)

class Subscription:
    """
    
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    class AudioClip:
        """
        
        """
        def __init__(self, player_id):
            self.endpoint = '/players/{}/audioClip/subscription'.format(player_id)

        def __name__(self):
            return 'audioClip'

    class Favorites:
        """
        
        """
        def __init__(self, household_id):
            self.endpoint = '/households/{}/favorites/subscription'.format(household_id)

        def __name__(self):
            return 'favorites'

    class Groups:
        """
        
        """
        def __init__(self, household_id):
            self.endpoint = '/households/{}/groups/subscription'.format(household_id)

        def __name__(self):
            return 'groups'

    class GroupVolume:
        """
        
        """
        def __init__(self, group_id):
            self.endpoint = '/groups/{}/groupVolume/subscription'.format(group_id)

        def __name__(self):
            return 'groupVolume'

    class Playback:
        """
        
        """
        def __init__(self, group_id):
            self.endpoint = '/groups/{}/playback/subscription'.format(group_id)

        def __name__(self):
            return 'playback'

    class PlaybackMetadata:
        """
        
        """
        def __init__(self, group_id):
            self.endpoint = '/groups/{}/playbackMetadata/subscription'.format(group_id)

        def __name__(self):
            return 'playbackMetadata'

    class PlaybackSession:
        """
        
        """
        def __init__(self, session_id):
            self.endpoint = '/playbackSessions/{}/playbackSession/subscription'.format(session_id)

        def __name__(self):
            return 'playbackSession'

    class PlayerVolume:
        """
        
        """
        def __init__(self, player_id):
            self.endpoint = '/players/{}/playerVolume/subscription'.format(player_id)

        def __name__(self):
            return 'playerVolume'

    class Playlists:
        """
        
        """
        def __init__(self, household_id):
            self.endpoint = '/households/{}/playlists/subscription'.format(household_id)

        def __name__(self):
            return 'playlists'



def subscribe(to:Subscription):
    """
    Subscribe to events from a namespace.
    """
    logger = logging.getLogger(__name__)
    logger.debug("Subscribing to event: %s", to.__name__)
    subscribe(namespace=to.__name__, endpoint=to.endpoint)
    
    
def unsubscribe(to:Subscription):
    """
    Unsubscribe from events from a namespace.
    """
    logger = logging.getLogger(__name__)
    logger.debug("Unsubscribing from event: %s", to.__name__)
    subscribe(namespace=to.__name__, endpoint=to.endpoint)
        
    



