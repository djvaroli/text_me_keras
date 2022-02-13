# Text Me Keras

A TensorFlow callback that texts back... to let you know how training is going.


## Usage.

### Clone and Install.
   
`git clone https://github.com/djvaroli/text_me_keras.git && cd text_me_keras/ && pip install -e .`

### Export Twilio Credentials

Python
```
import os

os.environ["TWILIO_ACCOUNT_SID"] = <your_account_sid>
os.environ["TWILIO_AUTH_TOKEN"] = <your_auth_token>
```

Shell
```
export TWILIO_ACCOUNT_SID=<your_account_sid>
export TWILIO_AUTH_TOKEN=<your_auth_token>
```

### Try it Out
```
import os

import numpy as np
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.python.keras.models import Model

from text_me_keras.callbacks.texting import TextMeCallback
# if you haven't set the credentials before hand you'll get a warning

i = Input((100, ))
x = Dense(10)(i)
x = Dense(100)(x)
model = Model(i, x)

model.compile("adam", "mse", metrics=["accuracy"])

# if you haven't set the creds by this point, an exception will be raised
cbck = TextMeCallback(
    to=<to_number>, 
    from_=<from_number>,  # must be a number attached to your twilio account 
    frequency=2,  # num epochs between texts
    run_id="Test Run"
)

x = np.random.random((32, 100))
model.fit(x, x, batch_size=16, callbacks=[cbck], epochs=5)
```

