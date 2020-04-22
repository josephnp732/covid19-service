from flask import Flask, request, redirect, jsonify
from slack_webhook import Slack
import requests
import webbrowser

slackWebhook = ''  # TODO: Add Slack Webhook here
slack = Slack(url=slackWebhook)

app = Flask(__name__)

# All Data
@app.route("/all", methods=['GET'])
def all():

    url = 'http://covid19-all:3001/all'
    r = requests.get(url)

    if r.status_code == 500:
        slack.post(attachments=[
            {
                "fallback": "Plain-text summary of the attachment.",
                "color": "#FF0000",
                "pretext": "HTTP 500 - Internal Server Error",
                "author_name": "Covid19 - Backbone",
                "title": "Microservices - All",
                "text": "`Visit AWS CloudWatch logs`",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": False
                    }
                ]
            }
        ])
        return "Server Down. Please try again after sometime"

    return jsonify(r.json())

# All Countries
@app.route("/countries", methods=['GET'])
def countries():

    url = 'http://covid19-countries:3002/countries'
    r = requests.get(url)

    if r.status_code == 500:
        slack.post(attachments=[
            {
                "fallback": "Plain-text summary of the attachment.",
                "color": "#FF0000",
                "pretext": "HTTP 500 - Internal Server Error",
                "author_name": "Covid19 - Backbone",
                "title": "Microservices - All Countries",
                "text": "`Visit AWS CloudWatch logs`",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": False
                    }
                ]
            }
        ])
        return "Server Down. Please try again after sometime"

    return jsonify(r.json())

# Country Specific
@app.route("/countries/<country>", methods=['GET'])
def specific_country(country):

    url = 'http://covid19-country-specific:3003/countries/' + country
    r = requests.get(url)

    if r.status_code == 500:
        slack.post(attachments=[
            {
                "fallback": "Plain-text summary of the attachment.",
                "color": "#FF0000",
                "pretext": "HTTP 500 - Internal Server Error",
                "author_name": "Covid19 - Backbone",
                "title": "Microservices - Specific Country",
                "text": "`Visit AWS CloudWatch logs`",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": False
                    }
                ]
            }
        ])
        return "Server Down. Please try again after sometime"

    return jsonify(r.json())

# grafana
@app.route("/admin", methods=['GET'])
def grafana():
    webbrowser.open("http://grafana.monitoring:3000", new=0, autoraise=True)
    return "Admin Dashboard Opened in new Tab"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
