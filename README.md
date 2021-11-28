# Mofatesh Bot
Sharif Courseware Subscriber / Telegram Publisher

## What?
In Computer Engineering department of Sharif University of Technology some courses use [this](http://ce.sharif.edu/programs-and-courses#Courses) as their courseware. Unfortunately this system doesn't send any notification to the students so there's a high chance of missing some course news.

Mofatesh is a Telegram bot; It checks the courseware periodically and whenever it finds something new collects it. On the other hand students can use this bot to subscribe to a course, so whenever the bot finds something new it notifies them.

## How?
### Setup
In order to setup this project one needs to install python requirements and then config the project. It's quite straightforward:

```bash
pip install -r requirements.txt
```

and then create a file named `local_config.py` containing:

```python
# Required
BOT_TOKEN = 'YOUR_BOT_TOKEN'
ALLOWED_COURSES = [
	'00-01_1_ce242-1',
	# Place allowed courses here
]

# Optional
BOT_SLEEP_TIME = 10		# check users status time interval
COLLECTOR_SLEEP_TIME = 60 # check courseware time interval
```

The course ID can be extracted from the URL of course homepage. Just replace each `/` with a `_`.

### Run
There are 2 services you should run. A collector service and a publisher service.

Just run each of the following commands in a different terminal session.

```bash
python collector
python publisher
```

### Usage
Just add the Telegram bot to the group of course or directly message it.

There are 4 commands:

```
/start
/listen <course ID>
/deafen <course ID>
/help
```
smmh was here!
