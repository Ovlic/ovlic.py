
class SonosError(Exception):
    """Base Exception for errors raised from Sonos."""
    def __init__(self, message=""):
        self.message = message
        #super().__init__(f"{self.message}")


class AuthorizationException(SonosError):
    """Exception that's thrown when an operation in the :class:`Authorization` fails."""
    def __init__(self, message=""):
        self.message = message
        super().__init__(f"{self.message}")


class GlobalError(SonosError):
    """Exception that's thrown when an operation in the :class:`control` fails."""
    def __init__(self, message=""):
        self.message = message
        super().__init__(f"{self.message}")


class HTTPError(SonosError):
    """Exception that's thrown when the Sonos API returns a status code other than :int:`200`."""
    def __init__(self, message=""):
        self.message = message
        #super().__init__(f"{self.message}")


class InvalidClient(AuthorizationException):
    """Raised when client token provided doesn’t correspond to client that generated auth code"""
    pass

class InvalidAuthentication(AuthorizationException):
    """Raised when :param:`client_id` or :param:`client_secret` parameter is invalid"""
    pass

class InvalidRedirectUri(AuthorizationException):
    """Raised when redirect URI provided doesn’t match redirect URI registered with client"""
    pass

class InvalidCode(AuthorizationException):
    """Raised when authorization code provided is invalid or expired"""
    pass

class InvalidGrant(AuthorizationException):
    """Raised when grant type is invalid or unsupported"""
    pass

class UnsupportedGrantType(AuthorizationException):
    """Raised when an unsupported grant type is sent"""
    pass


class MissingParameters(GlobalError):
    """Raised when required parameters are missing."""
    pass

class InvalidSyntax(GlobalError):
    """Raised when a malformed JSON is sent to a speaker."""
    pass

class UnsupportedNamespace(GlobalError):
    """Raised when a namespace is not recognized by the speaker."""
    pass

class UnsupportedCommand(GlobalError):
    """Raised when an unsupported command is sent to a speaker."""
    pass

class InvalidParameter(GlobalError):
    """Raised when an invalid parameter is sent to a speaker."""
    pass

class InvalidObjectId(SonosError):
    """Raised when an incorrect object identifier is sent to a speaker."""
    pass

class CommandFailed(GlobalError):
    """Raised when a player returns an internal error"""
    pass

class NotCapable(GlobalError):
    """Raised when targetted speaker does not support the command."""
    pass


class BadRequest(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`400`."""
    pass

class Unauthorized(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`401`."""
    pass

class Forbidden(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`403`."""
    pass

class NotFound(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`404`."""
    pass

class MethodNotAllowed(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`405`."""
    pass

class Gone(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`410`."""
    pass

class RateLimitExceeded(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`429`."""
    pass

class InternalServerError(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`500`."""
    pass

class NotImplemented(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`501`."""
    pass

class BadGateway(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`502`."""
    pass

class ServiceUnavailable(HTTPError):
    """Raised when the Sonos API returns a status code of :int:`503`."""
    pass



class InvalidRequest(SonosError):
    """Raised when an invalid request is sent"""
    pass

class InvalidMethod(SonosError):
    """Raised when wrong HTTP method is used"""
    pass

class InvalidAccessToken(SonosError):
    """Raised when access token is invalid"""
    pass

class InvalidRefreshToken(SonosError):
    """Raised when refresh token is invalid"""
    pass

class DefaultError(SonosError):
    """Default Sonos Error. (Will be removed once all other errors are done.)"""
    def __init__(self, err_type=f"invalid_request"):
        self.err_type = f"{err_type}"

        if self.err_type == "invalid_request":
            self.message = f"Invalid request."
        elif self.err_type == "unsupported_grant_type":
            self.message = f"Unsupported grant type."
        elif self.err_type == "invalid_client":
            self.message = f"Invalid client token."
        elif self.err_type == "invalid_redirect_uri":
            self.message = f"Invalid redirect uri."
        elif self.err_type == "invalid_code":
            self.message = f"Expired authorization code."
        elif self.err_type == "invalid_grant":
            self.message = f"Invalid grant."
        elif self.err_type == "invalid_method":
            self.message = f"Wrong HTTP method used."
        elif self.err_type == "Authentication required":
            self.message = f"'client_id' or 'client_secret' parameters aren’t valid."
        elif self.err_type == "ERROR_INVALID_SYNTAX":
            self.message = f"Malformed JSON sent to player."
        elif self.err_type == "ERROR_UNSUPPORTED_COMMAND":
            self.message = f"Unsupported command."
        elif self.err_type == "ERROR_COMMAND_FAILED":
            self.message = f"Command failed."
        elif self.err_type == "ERROR_NOT_CAPABLE":
            self.message = f"Player not capable of command."

        else:
            self.message = f"An Unknown Error, '{self.err_type}' Occured."

        super().__init__(f"{self.message}")