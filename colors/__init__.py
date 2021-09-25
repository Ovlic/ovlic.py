"""
HOW TO USE:
In a string, put the color you want first, with the first item and the second item at the emd. (Example: _str = f"{green[0]}Green!{green[1]}"
"""


reset = [str(u"\u001b[0m"), str(u"\u001b[0m")]

bold = [str(u"\u001b[1m"), str(u"\u001b[22m")]
dim = [str(u"\u001b[2m"), str(u"\u001b[22m")]
italic = [str(u"\u001b[3m"), str(u"\u001b[23m")]
underline = [str(u"\u001b[4m"), str(u"\u001b[24m")]
inverse = [str(u"\u001b[7m"), str(u"\u001b[27m")]
hidden = [str(u"\u001b[8m"), str(u"\u001b[28m")]
strikethrough = [str(u"\u001b[9m"), str(u"\u001b[29m")]

black = [str(u"\u001b[30m"), str(u"\u001b[39m")]
red = [str(u"\u001b[31m"), str(u"\u001b[39m")]
green = [str(u"\u001b[32m"), str(u"\u001b[39m")]
yellow = [str(u"\u001b[33m"), str(u"\u001b[39m")]
blue = [str(u"\u001b[34m"), str(u"\u001b[39m")]
magenta = [str(u"\u001b[35m"), str(u"\u001b[39m")]
cyan = [str(u"\u001b[36m"), str(u"\u001b[39m")]
white = [str(u"\u001b[37m"), str(u"\u001b[39m")]
gray = [str(u"\u001b[90m"), str(u"\u001b[39m")]
grey = [str(u"\u001b[90m"), str(u"\u001b[39m")]

brightRed = [str(u"\u001b[91m"), str(u"\u001b[39m")]
brightGreen = [str(u"\u001b[92m"), str(u"\u001b[39m")]
brightYellow = [str(u"\u001b[93m"), str(u"\u001b[39m")]
brightBlue = [str(u"\u001b[94m"), str(u"\u001b[39m")]
brightMagenta = [str(u"\u001b[95m"), str(u"\u001b[39m")]
brightCyan = [str(u"\u001b[96m"), str(u"\u001b[39m")]
brightWhite = [str(u"\u001b[97m"), str(u"\u001b[39m")]

bgBlack = [str(u"\u001b[40m"), str(u"\u001b[49m")]
bgRed = [str(u"\u001b[41m"), str(u"\u001b[49m")]
bgGreen = [str(u"\u001b[42m"), str(u"\u001b[49m")]
bgYellow = [str(u"\u001b[43m"), str(u"\u001b[49m")]
bgBlue = [str(u"\u001b[44m"), str(u"\u001b[49m")]
bgMagenta = [str(u"\u001b[45m"), str(u"\u001b[49m")]
bgCyan = [str(u"\u001b[46m"), str(u"\u001b[49m")]
bgWhite = [str(u"\u001b[47m"), str(u"\u001b[49m")]
bgGray = [str(u"\u001b[100m"), str(u"\u001b[49m")]
bgGrey = [str(u"\u001b[100m"), str(u"\u001b[49m")]

bgBrightRed = [str(u"\u001b[101m"), str(u"\u001b[49m")]
bgBrightGreen = [str(u"\u001b[102m"), str(u"\u001b[49m")]
bgBrightYellow = [str(u"\u001b[103m"), str(u"\u001b[49m")]
bgBrightBlue = [str(u"\u001b[104m"), str(u"\u001b[49m")]
bgBrightMagenta = [str(u"\u001b[105m"), str(u"\u001b[49m")]
bgBrightCyan = [str(u"\u001b[106m"), str(u"\u001b[49m")]
bgBrightWhite = [str(u"\u001b[107m"), str(u"\u001b[49m")]

# legacy styles for colors pre v1.0.0
blackBG = [str(u"\u001b[40m"), str(u"\u001b[49m")]
redBG = [str(u"\u001b[41m"), str(u"\u001b[49m")]
greenBG = [str(u"\u001b[42m"), str(u"\u001b[49m")]
yellowBG = [str(u"\u001b[43m"), str(u"\u001b[49m")]
blueBG = [str(u"\u001b[44m"), str(u"\u001b[49m")]
magentaBG = [str(u"\u001b[45m"), str(u"\u001b[49m")]
cyanBG = [str(u"\u001b[46m"), str(u"\u001b[49m")]
whiteBG = [str(u"\u001b[47m"), str(u"\u001b[49m")]


def rainbow(_str):
    arr = [char for char in _str]
    rainbowcount = 1
    for i in range(0, len(arr)):
        if arr[i] == " ": continue
        if rainbowcount == 1: arr[i] = red[0]+arr[i]+red[1]
        if rainbowcount == 2: arr[i] = yellow[0]+arr[i]+yellow[1]
        if rainbowcount == 3: arr[i] = green[0]+arr[i]+green[1]
        if rainbowcount == 4: arr[i] = blue[0]+arr[i]+blue[1]
        if rainbowcount == 5: arr[i] = magenta[0]+arr[i]+magenta[1]
        rainbowcount += 1
        if rainbowcount == 6: rainbowcount = 1
    arr = "".join(arr)
    return f"{bold[0]}{arr}{bold[1]}"