
def bracket(message):
    from .src.bracket import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def glitch(message):
    from .src.glitch import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def bubbletext(message):
    from .src.bubbletext import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def fancy(message):
    from .src.fancy import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def emojify(message):
    from .src.emojifytext import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def franktur(message):
    from .src.franktur import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def spoiler(message):
    from .src.spoilertext import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def strike(message):
    """Needs to be fixed"""
    return
    #return f"~~{message}~~"

def subscript(message):
    from .src.subscript import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def superscript(message):
    from .src.superscript import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def varied(message):
    from .src.varied import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg

def upsidedown(message):
    from .src.upside_down import font
    table = message.maketrans(font)
    msg = message.translate(table)
    return msg