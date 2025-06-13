# Simple Telegram message sender using a bot session.

This simple python code can create a Fastapi webservice api that can be used to send messages to a known telegram id number contact. The purpose is not to used to send spam, the main goal is to use it to send alerts for specific events of interest, like finished tasks in server, backups or failing services.

A Dockerfile is provided to make ease to implement the bot message sender using Docker.

Just clone the repo and next:

1. Create a .env file in the directory root with the example data given in .env.sample file.

2. Build the docker image with: docker build -t tg_bot .

3. Next you can create a docker container:

docker run --name my-tg-bot -it -dp 8000:8000 tg_bot

You can test if is working making a cURL request for example:

curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{"chat_id": "123123123", "content": "Say hello to my little friend. Atte: Tony Montana."}' http://x.x.x.x:8000/send-msg/send-msg

Enjoy!