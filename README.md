# AI Retrieval Bot
![opena-langchain-slack](https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/64278101-f0db-4047-8f2c-6a4a9a8c1363)
This Slack bot allows users to ask questions and receive AI-generated responses based on documents located within a specified directory. This functionality is made possible through Retrieval-augmented generation (RAG), a framework provided by Langchain. You can find more information about RAG in the Langchain documentation [here](https://github.com/langchain-ai/langchain)https://github.com/langchain-ai/langchain.
## Setup
### Create Slack App
This high-level walkthrough will give you the basics to create a bot and Slack app using the Slack Bolt framework.  If you don't already have a Slack workspace, sign-up at slack.com.
Then [create a Slack app](https://api.slack.com/apps/new)https://api.slack.com/apps/new and give it a name, icon, and description.
![image](https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/2a49edab-e1cb-46ad-aac7-cd95ea1277f0)
#### Tokens
Navigate to OAuth & Permissions (left hand side menu) and in the Bot Token Scopes section add the scopes `chat:write` and `app_mentions:read`
Next, navigate to Install App and install it to your workspace. This will generate an OAuth Token beginning with `xoxb` which is needed later.
From the left hand menu there is another section based Basic Information. Here you'll find a Signing Secret which is also needed for later.
#### Enabling Socket Mode
This code uses a Slack feature called [Socket Mode](https://api.slack.com/apis/connections/socket)https://api.slack.com/apis/connections/socket. It is alternative to using HTTP as your app's communication protocol. If you prefer to use HTTP head over to [this tutorial](https://slack.dev/bolt-python/tutorial/getting-started-http)https://slack.dev/bolt-python/tutorial/getting-started-http to make the appropriate code changes.
From the menu select Sockt Mode and toggle the feature on. Ensure Interactivity is also enabled.
<img width="815" alt="image" src="https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/62874190-b66b-466b-87aa-b7f8724281b6">
### Install Packages
Install the required packages from OpenAI, Langchain, and Slack (Bolt Framework).
```
pip install openai langchain slack_bolt
```
### Modify constants.py
Create a new secret key from [OpenAI Platform](https://platform.openai.com/account/api-keys) and copy the Bot OAuth Token, Signing Secret, and Socket Mode App Token from Slack.  Note: both the signing secret and app token are found under Basic Information in Slack.
Update the values in the `constants.py` file.
## Data Files
In the project are two sample files in the folder `data` folder. Place any text files you like in this directory.