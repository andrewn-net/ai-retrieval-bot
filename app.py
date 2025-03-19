"""
This software is provided "as is," without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a particular
purpose and noninfringement. In no event shall the authors or copyright holders be
liable for any claim, damages or other liability, whether in an action of contract,
tort or otherwise, arising from, out of or in connection with the software or the use
or other dealings in the software.

Limitation of Liability: In no event shall the authors or copyright holders be liable for any indirect, incidental, special, or consequential damages.

External Libraries: If this code relies on external libraries, please consult the disclaimers provided by those libraries.

License: MIT License.

Intended Use: This code is intended for educational purposes.
"""

import os
import constants

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

# Slack tokens from constants.py
SLACK_BOT_TOKEN = constants.SLACK_BOT_TOKEN
SLACK_SIGNING_SECRET = constants.SLACK_SIGNING_SECRET
SLACK_APP_TOKEN = constants.SLACK_APP_TOKEN

# OpenAI API key from constants.py
os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY

# Initialize the Bolt app with your app token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
)

# Load your data
loader = DirectoryLoader("data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# Define a listener to process user messages and respond with the result
@app.message()
def process_query(message, say):
    query = message['text']

    response = index.query(query)
    say(response)

if __name__ == "__main__":
    # Start the Bolt app using Socket Mode
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
