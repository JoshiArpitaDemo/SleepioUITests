# SleepioUITests

Currently set up to run against Chrome browser. Need to add multi-browser testing(will use config.json)
Currently, only have the tests steps directly without feature files. Have BDD style but in comments

To run the tests run the following commands:

pipenv run python -m pytest -k landing -v
pipenv run python -m pytest -k improveyoursleep -v
pipenv run python -m pytest -k howlongproblemwithsleep -v
pipenv run python -m pytest -k whatstopsfromsleepingmostoften -v
pipenv run python -m pytest -k whatextent -v