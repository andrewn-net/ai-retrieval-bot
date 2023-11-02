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
