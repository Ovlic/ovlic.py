import random
import re
import requests
import urllib

nytlogo = "https://i.pinimg.com/originals/5e/af/20/5eaf20e1a08c73f59d40ab3ba5bffaae.png"

randomcolor = random.randint(0, 0xFFFFFF)

formatmonth = lambda rDateMonth: "January" if rDateMonth == "01" else "February" if rDateMonth == "02" else "March" if rDateMonth == "03" else "April" if rDateMonth == "04" else "May" if rDateMonth == "05" else "June" if rDateMonth == "06" else "July" if rDateMonth == "07" else "August" if rDateMonth == "08" else "September" if rDateMonth == "09" else "October" if rDateMonth == "10" else "November" if rDateMonth == "11" else "December" if rDateMonth == "12" else None

toTuple = lambda _dict: [(k, v) for k, v in _dict.items()]

remove_special_methods= lambda d: [a for a in d if not a.startswith('__')]

formatdate = lambda m, d, y: f"{m}/{d}/{y}"

formatCommas = lambda s: "{:,}".format(s)

formatnum = lambda n: int(n) if n%1 == 0 else n

factorcheck = lambda f, n: True if isinstance(formatnum(n/f), int) else False

ismultiple = lambda m, n: True if m % n == 0 else False

def url_shorten(link):
	data = requests.get(f"https://tinyurl.com/api-create.php?url={urllib.parse.quote(link)}").text
	return data

def is_url(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

def is_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats: return True
    return False

def comma(num:int):
    numString = str(num)
    #if numString.index() != -1: numString = str(numString)
    numString = numString.split().reverse()
    numString = "".join(numString)
    numStringWithCommas = ""
    numStringLength = numString.length
    for i in range(0, numStringLength):
        toPrepend = numString[i]
        if i != numStringLength - 1 and ((i + 1) % 3) == 0: toPrepend = "," + toPrepend
        numStringWithCommas = toPrepend + numStringWithCommas
    return numStringWithCommas