README
============

About
-------
- Purpose: Learning Python 2.7 and 3.5.
- Integrated:

* [x] PyDash library (similar to Lodash for JS)
* [x] PyTest unit testing framework
* [x] Travis CI (continuous integration)
* [x] Multiple files
* [x] Guidance from Programming Foundations at Udacity

Travic CI Build Status: [![Build Status](https://api.travis-ci.org/ltfschoen/PythonTest.svg)](https://travis-ci.org/ltfschoen/PythonTest)

Setup
-------
- [Install Python 2 or 3 from download or with Homebrew](https://www.python.org/downloads/)
- Python 2.7 installation with Homebrew (note that `brew install python` installs Python 2.7)
```
brew search python
brew install python
```

- Python 3.5.2 installation with Homebrew
```
brew install python3
brew linkapps python3
```
- Note: Python 3.5.2 and Pip and setuptools are installed with following commands available
```
pip3 install --upgrade pip setuptools
```
- Globally install Python 3.5.2 packages into the site-package `/usr/local/lib/python3.5/site-packages`:
```
pip3 install <package>
```

- Install codebase
```
git clone https://github.com/ltfschoen/PythonTest && cd PythonTest
pip install --upgrade pip
```

- Install dependencies 
```
pip install -r requirements.txt
```

Switch to Relevant Virtualenv
-----------------------------
* List Virtualenvs previously created
```
ls $WORKON_HOME
```

* Switch to a listed Virtualenv that you have created, i.e.
```
workon python_test_env_3.6.0
```

Run Apps
-------
- **Important Note**: All programs written in Python 2.7. Only break_time.py has been converted to support both Python 2.7 and 3.5 so far.
- Copy your present working directory `pwd` and paste it into below to add directory to $PYTHONPATH, since Python does not add the current directory to sys.path. If you do not do this you may get an error like `ImportError: No module named helpers` when you run a program
```
export PYTHONPATH=$PYTHONPATH:<paste_pwd>
echo $PYTHONPATH
```

```
python ./break_time.py
python ./file_handler.py
python ./movie_set/main.py
python profanity_detector/main.py
python movie_finder/entertainment_center.py
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

Known bugs
----------
- Running profanity_detector/main.py with Python 3.5 instead of 2.7 gives HTTP request error
- Running test_file_handler_util_remove_numbers_from_filename_and_append_rand_int() currently only working for Python 2.7