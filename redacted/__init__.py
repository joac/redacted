EXCEPTION_ON_LEAK = False  # Instead of printing, raise an exception on insecure access to data
TRACE_SECRET_ACCESS = False  # Log stack traces of secure access to secret
REDACTED_STR = "<REDACTED>"


class Redacted(object):
    """Encapsulates binary sensitive data"""

    def __init__(self, secret):
        pass

    def __repr__(self):
        return REDACTED_STR

    def __format__(self, *args, **kwargs):
        raise ValueError("Redacted Objects can't be unsafe formatted")

    def __str__(self):
        return REDACTED_STR


class SecureFormatter(object):
    """Provides pythonesque string formating, returning a Redacted"""


class SecureSink(object):
    """Provides a way to access stored secret"""
