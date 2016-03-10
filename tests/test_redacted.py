import pytest
from redacted import Secret, REDACTED_STR, SecureSink, DataLeak


@pytest.fixture
def secret():
    return Secret('my-secret')


def test_as_string_is_redacted(secret):
    assert str(secret) != 'my-secret'
    assert str(secret) == REDACTED_STR


def test_repr_is_redacted(secret):
    assert repr(secret) != 'my-secret'
    assert repr(secret) == REDACTED_STR


def test_formating_with_redacted_raise_ValueError(secret):
    with pytest.raises(DataLeak):
        '{}'.format(secret)


def test_using_secure_sink_secret_is_available(secret):
    with SecureSink() as sink:
        assert sink.unwrap(secret) == 'my-secret'


def test_secret_is_not_leaked_on_dir(secret):
    assert 'my-secret' not in secret.__dict__.values()


def test_accessing_secret_outside_secure_sink_raises(secret):
    with pytest.raises(DataLeak):
        secret.secret
