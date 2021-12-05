from PIL import Image
from io import BytesIO
from discord import File
import pyperclip

async def ad(avatar):
    ad = Image.open("src/assets/ad.png")
    data = BytesIO(await avatar.read())
    pfp = Image.open(data)
    pfp = pfp.resize((230, 230))
    ad.paste(pfp, (155, 75))

    buffer_output = BytesIO()
    ad.save(buffer_output, format='PNG')    
    buffer_output.seek(0) 
    return File(buffer_output, 'myimage.png')

async def delete(avatar):
    ad = Image.open("src/assets/delete.png")
    data = BytesIO(await avatar.read())
    pfp = Image.open(data)
    pfp = pfp.resize((230, 230))
    ad.paste(pfp, (155, 75))

    buffer_output = BytesIO()
    ad.save(buffer_output, format='PNG')    
    buffer_output.seek(0) 
    return File(buffer_output, 'myimage.png')
