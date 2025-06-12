# Simple Telegram message sender using a bot session.

This simple python code can create a Fastapi webservice api that can be used to send messages to a known telegram id number contact. The purpose is not to used to send spam, the main goal is to use it to send alerts for specific events of interest, like finished tasks in server, backups or failing services.

A Dockerfile is provided to make ease to implement the bot message sender using Docker.

Just clone the repo and next:

docker build -t tg_bot .

Next you can create a docker container:

docker run --name my-tg-bot -it -dp 8000:8000 tg_bot

Enjoy!

