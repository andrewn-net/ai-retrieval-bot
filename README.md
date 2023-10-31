# AI Retrieval Bot

![opena-langchain-slack](https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/78996d00-8c69-4edd-beca-407b834c8edb)

This Slack bot allows users to ask questions and receive AI-generated responses based on documents located within a specified directory. This functionality is made possible through Retrieval-augmented generation (RAG), a framework provided by Langchain. You can find more information about RAG in the Langchain documentation [here](https://github.com/langchain-ai/langchain).

## Setup
### Create Slack App
This high-level walkthrough will give you the basics to create a bot and Slack app using the Slack Bolt framework.  If you don't already have a Slack workspace, sign-up at [slack.com](https://www.slack.com/).
Then [create a Slack app](https://api.slack.com/apps/new) and give it a name, icon, and description.

![image](https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/a0d3f51b-7074-4a51-b39f-2f170d8428d4)

#### Tokens
Navigate to OAuth & Permissions (left hand side menu) and in the Bot Token Scopes section add the scopes `chat:write` and `app_mentions:read`

Next, navigate to Install App and install it to your workspace. This will generate an OAuth Token beginning with `xoxb` which is needed later.

From the left hand menu there is another section called Basic Information. Here you'll find a Signing Secret which is also needed for later.

#### Enabling Socket Mode

This code uses a Slack feature called [Socket Mode](https://api.slack.com/apis/connections/socket). It is alternative to using HTTP as your bot's communication protocol. If you prefer to use HTTP head over to [this tutorial](https://slack.dev/bolt-python/tutorial/getting-started-http) to make the appropriate code changes.

From the menu select Socket Mode and toggle the feature on. Ensure Interactivity is also enabled.

<img width="834" alt="image" src="https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/c877c8b6-9a29-4289-a9fd-19137ac285cd">

That's it for creating the Slack app. You'll need to refer back to this later to get tokens.

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

You can now chat with the bot in Slack. Ask it questions and recieve AI-generated responses based on the documents.

<img width="711" alt="image" src="https://github.com/andrewn-net/ai-retrieval-bot/assets/27248499/e9667fba-4f9e-4864-8265-103e061bac8e">
