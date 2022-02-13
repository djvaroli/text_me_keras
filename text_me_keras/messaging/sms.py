"""Functions that assist in building and sending text messages.
"""
from inspect import Attribute
import os
from logging import getLogger, WARNING
from twilio.rest import Client

logger = getLogger()
logger.setLevel(WARNING)


class TextMessage:
    
    def __init__(self) -> None:
        self._check_if_credentials_set()
        self.message_lines = []
    
    def __repr__(self) -> str:
        return f"TextMessage(\n\t{self.message}\n)"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __length__(self) -> int:
        return len(self.message)
    
    def _check_if_credentials_set(self, action="warning"):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        warning_or_error_message = "To send messages please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN."
        
        if account_sid is None or auth_token is None:
            if action == "warning":
                logger.warning(warning_or_error_message)
            elif action == "error":
                raise Exception(warning_or_error_message)
            else:
                raise Exception(f"Invalid action {action}.")
    
    @property
    def message(self) -> str:
        return "\n\t".join(self.message_lines)

    def add_line(self, text: str) -> "TextMessage":
        """Adds a line of text to the text message.

        Args:
            text (str): Line of text to be added to the message.
        """
        self.message_lines.append(text)
        return self

    def reset_message(self) -> "TextMessage":
        """Resets the contents of the text message.
        """
        self.message = ""
        
    def send(self, to: str, from_: str):
        """Sends the text message to the specified number.

        Args:
            to (str): Number to send message to.
            from_ (str): Number the message is sent from. Should be your active Twilio number.
        """
        self._check_if_credentials_set(action="error")
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        return client.messages.create(
            to, 
            body=self.message,
            from_=from_
        )
        