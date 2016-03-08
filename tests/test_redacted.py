import pytest
from redacted import Redacted, REDACTED_STR, SecureSink


def test_as_string_is_redacted():
    a = Redacted('my-secret')
    assert str(a) != 'my-secret'
    assert str(a) == REDACTED_STR


def test_repr_is_redacted():
    a = Redacted('my-secret')
    assert repr(a) != 'my-secret'
    assert repr(a) == REDACTED_STR


def test_formating_with_redacted_raise_ValueError():
    a = Redacted('my-secret')
    with pytest.raises(ValueError):
        '{}'.format(a)


def test_using_secure_sink_secret_is_available():
    secret = Redacted('my-secret')
    with SecureSink() as sink:
        sink.unwrap(secret)
