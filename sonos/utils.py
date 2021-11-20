


from .household import Household


def getPlayerById(household:Household, id:str):
    """
    Returns the player with the given id.
    """
    data = Household.getGroups()
    for i in range(0, len(data.players)):
        if data.players[i].id == id:
            return data.players[i]
    raise ValueError("Invalid player id.")