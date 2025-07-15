# Autotest portfolio

This is a portfolio used to display automated testing cases.

## author 

Benjamin Defays

## Important points 

* All tests will use Python

* Tests with Playwright need to use async

* Automated tests will use Playwright

* Performance tests will use Locust

* To limit time consuming error, type checking is set at strict and can be changed in the settings by searching for python.analysis.typeCheckingMode 

### websites

* Most of the tests will be based on the test website `https://www.saucedemo.com/` for now

## to begin (only need to be done once)
1. Open your terminal, navigate to the project directory, and run this command to give the script permission to execute `chmod +x setup.sh`
2. Execute the script by running `./setup.sh`
3. activate the virtual environment in your terminal each time you open a new session by running `source venv/bin/activate`