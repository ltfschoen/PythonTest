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
```

Run Apps
-------
- Written in Python 2.7
- Copy your present working directory `pwd` and paste it into below to add directory to $PYTHONPATH, since Python does not add the current directory to sys.path
```
export PYTHONPATH=$PYTHONPATH:<paste_pwd>
```

```
python ./break_time.py
python ./file_handler.py
python ./movie_set/main.py
```

Run Unit Tests
-------
- Using [PyTest library](http://doc.pytest.org/)
```
pytest -v
```