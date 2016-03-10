import threading

from . _redacted import SecretContainer

EXCEPTION_ON_LEAK = False  # Instead of printing, raise an exception on insecure access to data
TRACE_SECRET_ACCESS = False  # Log stack traces of secure access to secret
REDACTED_STR = "<REDACTED>"

__LOCAL_DATA = threading.local()

# __LOCAL_DATA.unlocked =


class DataLeak(Exception):
    """Raised when you are leaking data"""


class Secret(SecretContainer):
    """Encapsulates binary sensitive data"""

    def __init__(self, secret):
        self.secret = secret
        self.locked = True

    def __repr__(self):
        return REDACTED_STR

    def __format__(self, *args, **kwargs):
        raise DataLeak("Redacted Objects can't be unsafe formatted")

    def __str__(self):
        return REDACTED_STR


class SecureFormatter(object):
    """Provides pythonesque string formating, returning a Secret"""


class SecureSink(object):
    """Provides a way to access stored secret"""

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def unwrap(self, secret):
        secret.locked = False
        return secret.secret
