
class Error(Exception): 
    "Base exception"
    def __init__ (self, message):
        super().__init__(message)
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
        return self.message

    def __dir__(self):
        return super().__dir__()

class rbxError(Error):
    """Exception that's raised when an error is returned from Roblox"""
    def __init__(self, message=f"Invalid username.", username=None):
        self.message = f"{message}"
        self.username = username
        super().__init__(f"{self.message}")

    def __str__(self):
        return f"{self.message}"

    def __dir__(self):
        return super().__dir__()

class NYTError(Error):
    """Exception that's raised when an error is returned from the New York Times."""
    def __init__(self, message=f"An Error Occured"):
        self.message = f"{message}"
        super().__init__(f"{self.message}")

    def __str__(self):
        return f"{self.message}"

    def __dir__(self):
        return super().__dir__()

class InvalidKey(Error):
    """Exception that's raised when an invalid api key is passed in."""
    def __init__(self, message=f"Invalid API Key."):
        self.message = f"{message}"
        super().__init__(f"{self.message}")

    def __str__(self):
        return f"{self.message}"

    def __dir__(self):
        return super().__dir__()
        