# SleepioUITests

These tests have been set up to run against chrome browser. 
The chrome browser version is 100.0.4896.88 and chrome driver version is 100.0.4896.60

To run the tests run the following commands from the root folder:

pipenv run python -m pytest -k sleepiolanding -v <br />
pipenv run python -m pytest -k improveyoursleep -v <br />
pipenv run python -m pytest -k howlongproblemwithsleep -v <br />
pipenv run python -m pytest -k whatstopsfromsleepingmostoften -v <br />
pipenv run python -m pytest -k whatextent -v <br />
pipenv run python -m pytest -k e2e_multiple_assertions -v <br />


NOTE FOR E2E TEST:
Make sure to manually update the email address before running the test since if the email address already exists, the account doesn't get created and the assertion would fail
