

"""
Create an exception class when user does not provide a valid url or key.
"""
class ConfigurationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
