# Autotest portfolio

This is a portfolio used to display automated testing cases.

## author 

Benjamin Defays

### websites

* Most of the tests will be based on the test website `https://www.saucedemo.com/`

## Installation

### To begin (only need to be done once)
1. Open your terminal, navigate to the project directory, and run this command to give the script permission to execute `chmod +x setup.sh`
2. Execute the script by running `./setup.sh` and follow the steps provided at the end of the script
3. Install Docker on your computer by following the steps in `https://www.docker.com/get-started/`
4. Launch Docker Desktop

### To build the Docker image 
Run the command `docker build -t autotest .`

### To start the Docker container 
Run the command `docker run -it --rm --init --ipc=host autotest`
This command is based on the good practices mentioned in `https://playwright.dev/docs/docker#recommended-docker-configuration`. Please refer to it when needed.

### To run the tests without Docker 
Run the command `pytest -m [markdown wanted like training]` 

## Notes concerning the project 

* All tests will use Python

* Automated tests will use Playwright

* Performance tests will use Locust

* Tests with Playwright need to use async

* VScode is prefered as the IDE and some commands or behavior are expecting to use it

* To limit time consuming error, type checking for Python is set at strict and can be changed in the settings by searching for python.analysis.typeCheckingMode 
