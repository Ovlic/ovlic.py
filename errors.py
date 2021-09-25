from .colors import red, bold
class Error(Exception): 
    "Base exception"
    def __init__ (self, message):
        super().__init__(red[0] + message + red[1])
    #pass

class ImageError(Error):
    "Errors raised from issues in image_gen"
    def __init__(self, message="An Error Occured."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class AvatarError(Error):
    "Error raised when an invalid avatar is passed in for image_gen"
    def __init__(self, message="Invalid avatar."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class obError(Error):
    "Error raised from bot"
    def __init__(self, message="An Error Occured."):
        self.message = message
        super().__init__(f"{self.message}")

    def __str__(self):
        return f"{red[0]}{self.message}{red[1]}"

    def __dir__(self):
        return super().__dir__()

    