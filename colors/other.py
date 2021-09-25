from .__init__ import *

def loaded_cog(c):
    try:
        return (f'{bold[0]}{cyan[0]}Loaded cog "{c.__name__}"{cyan[1]}{bold[1]}')
    except:
        return (f'{bold[0]}{cyan[0]}Loaded cog "{c}"{cyan[1]}{bold[1]}')

def unloaded_cog(c):
    try:
        return (f'{bold[0]}{cyan[0]}Unloaded cog "{c.__name__}"{cyan[1]}{bold[1]}')
    except:
        return (f'{bold[0]}{cyan[0]}Unloaded cog "{c}"{cyan[1]}{bold[1]}')

def reloaded_cog(c): return (f'{bold[0]}{cyan[0]}Reloaded cog "{c}"{cyan[1]}{bold[1]}')