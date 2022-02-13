from cgitb import text
from tensorflow.python.keras.callbacks import Callback


class TextMeCallback(Callback):

    def __init__(
        self,
        text_to: str,
        frequency: int,
        round_to: int = 4
    ):
        """TensorFlow callback that enables sending SMS messages during model training.

        Args:
            text_to (str): Number of the person to text model metrics to.
            frequency (int): Number of epochs between successive text mesages.
            round_to (int, optional): Number of digits to round metrics to. Defaults to 4.
        """
        super(TextMeCallback, self).__init__()
        self.text_to = text_to
        self.frequency = frequency
        self.round_to = round_to
        self.seen_epochs = 0
        
    def on_epoch_end(self, epoch, logs=None):
        pass