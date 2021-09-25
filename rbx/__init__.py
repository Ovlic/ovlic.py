import requests

async def commaNumber(num):
    numString = str(num)
    if numString.index("e") != -1: numString = str(numString)
    numString = numString.split("").reverse()
    numstring = "".join(numString)
    numStringWithCommas = ""
    numStringLength = numString.length
    for i in range(0, numStringLength):
        toPrepend = numString[i]
        if i != numStringLength - 1 and ((i + 1) % 3) == 0: toPrepend = "," + toPrepend
        numStringWithCommas = toPrepend + numStringWithCommas
    return numStringWithCommas


async def getid(input):
    thejson = requests.get("https://api.roblox.com/users/get-by-username?username=" + input).json()
    return thejson

async def userdetails(input):
    thejson = requests.get("https://users.roblox.com/v1/users/" + input).json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def favgames(input):
    thejson = requests.get("https://games.roblox.com/v2/users/" + input + "/favorite/games?").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson
    

async def createdgames(input):
    thejson = requests.get("https://games.roblox.com/v2/users/" + input + "/games?").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def followers(input):
    print(input)
    count = requests.get("https://friends.roblox.com/v1/users/" + input + "/followers/count").json()
    print(count)
    return commaNumber(count)


async def following(input):
    thejson = requests.get("https://friends.roblox.com/v1/users/" + input + "/followings/count").json()['count']
    return thejson

async def prevnames(input):
    thejson = requests.get("https://users.roblox.com/v1/users/" + input + "/username-history?").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def groups(input):
    thejson = requests.get("https://groups.roblox.com/v2/users/" + input + "/groups/roles").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson
    

async def cirthumb(input, circular):
    thelink = ""
    if circular == None:
        thelink = "https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=" + input + "&size=150x150&format=Png&isCircular=false"
    else:
        thelink = "https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds= " + input + "&size=150x150&format=Png&isCircular=true"
    #size options: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720
    #format options: Png, Jpeg
    #circular options: true, false
    thejson = requests.get(thelink).json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def premium(input):
    thejson = requests.get("https://premiumfeatures.roblox.com/v1/users/"+ input +"/validate-membership").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def onlinestatus(input):
    thejson = requests.get("https://api.roblox.com/users/" + input + "/onlinestatus/").json()
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def rap(input):
    therap = 0
    thejson = requests.get("https://inventory.roblox.com/v1/users/" + input + "/assets/collectibles?sortOrder=Asc&limit=100").json()['data']
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    rap = thejson
    if not rap:
        therap = 0
    else:
        rapitems = len(rap);
        for i in range(0, len(rapitems)):
            if i == 0:
                therap = rap[i].recentAveragePrice
            else: therap = therap + rap[i].recentAveragePrice

    return (await commaNumber(therap))

async def friends(input):
    thejson = requests.get("https://friends.roblox.com/v1/users/" + input + "/friends/count").json()['count']
    #if json.success)if json.success == false) return message.channel.send("Roblox Error: "+json.errorMessage)
    return thejson

async def avatar(input):
    thejson = requests.get("https://thumbnails.roblox.com/v1/users/avatar?userIds=" + input + "&size=150x150&format=Png&isCircular=false").json()
    return thejson

