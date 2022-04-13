# SleepioUITests

Currently set up to run against Chrome browser. Need to add multi-browser testing(will use config.json)
Currently, only have the tests steps directly without feature files. Have BDD style but in comments

NOTE FOR E2E TEST:
Make sure to manually update the email address before running the test since if the email address already exists, the account doesn't get created and the assertion would fail

To run the tests run the following commands:

pipenv run python -m pytest -k landing -v <br />
pipenv run python -m pytest -k improveyoursleep -v <br />
pipenv run python -m pytest -k howlongproblemwithsleep -v <br />
pipenv run python -m pytest -k whatstopsfromsleepingmostoften -v <br />
pipenv run python -m pytest -k whatextent -v <br />
pipenv run python -m pytest -k e2e_multiple_assertions -v <br />
