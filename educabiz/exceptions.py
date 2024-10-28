class ClientError(Exception):
    """base class for any error in educabiz.client.Client"""


class LoginFailedError(ClientError):
    """Login invalid"""
