README
============

About
-------
- Purpose: Learning Python 2.7.
- Integrated:

* [x] PyDash library (similar to Lodash for JS)
* [x] PyTest unit testing framework
* [x] Travis CI (continuous integration)
* [x] Multiple files
* [x] Guidance from Programming Foundations at Udacity

Travic CI Build Status: [![Build Status](https://api.travis-ci.org/ltfschoen/PythonTest.svg)](https://travis-ci.org/ltfschoen/PythonTest)

Setup
-------
- Install codebase and dependencies
```
git clone https://github.com/ltfschoen/PythonTest && cd PythonTest
brew install python
pip install pydash
pip install -U pytest
pip install twilio
pip install -U python-dotenv
```

Run Apps
-------
- Written in Python 2.7
- Copy your present working directory `pwd` and paste it into below to add directory to $PYTHONPATH, since Python does not add the current directory to sys.path
```
export PYTHONPATH=$PYTHONPATH:<paste_pwd>
echo $PYTHONPATH
```

```
python ./break_time.py
python ./file_handler.py
python ./movie_set/main.py
python profanity_detector/main.py
```

- Create a file .env and add contents 
```
LIVE_TWILIO_ACCOUNT_SID="<insert_your_sid_from_twilio_account>"
LIVE_TWILIO_AUTH_TOKEN="<insert_your_auth_token_from_twilio_account>"
TWILIO_PHONE_NUMBER="<insert_your_twilio_phone_number>"
RECIPIENT_PHONE_NUMBER="<insert_recipient_phone_number>"
```

```
python ./twilio_sms/main.py
```

Run Unit Tests
-------
- Using [PyTest library](http://doc.pytest.org/)
```
pytest -v
```