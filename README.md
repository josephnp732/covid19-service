# covid19-service
Flask API Services deployed on Docker <br/>
_NOTE:_ API Services used in Covid19-Backend Repository (https://github.com/josephnp732/Covid19-Backend.git)

### Requires Python 3 and pip3

To install requirements, run: `pip3 install -r requirements.txt` in their respective repos directories

### Adding New Slack API Webhook to the backbone/backbone.py file:

Follow these instructions: https://api.slack.com/messaging/webhooks

### Find Docker Images here: https://hub.docker.com/u/josephnp732

#### Docker Image Pull commands:

* `docker pull josephnp732/covid19_backbone:tag`
* `docker pull josephnp732/covid19_all:tag`
* `docker pull josephnp732/covid19_countries:tag`
* `docker pull josephnp732/covid19_country_specific:tag`
