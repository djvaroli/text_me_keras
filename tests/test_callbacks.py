# not sure how to test Callback without a set of real credentials so test imports

from text_me_keras.callbacks import TextMeCallback
from text_me_keras.messaging import TextMessage


def test_check_credentials_are_set():
    creds_set = TextMessage._are_credentials_set()
    assert not creds_set, "Credentials should not be set in test environment."



