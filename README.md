# Lockio Flask Server

## Building the Docker image
Be carefull, to create the docker image you need to change inside app.py the BACK_URL to DOCKER_URL.
After making those changes, you can build the docker image with the following command:
```bash
docker build -t lockio/lockio-block:latest .