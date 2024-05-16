# checkout-codekata-agrichain

A code kata to demonstrate programming skills in python3. This is an exercise by AgriChain

## App set-up and execution - Local

### Set-up

1. **Clone the git repo** in a new & clean folder on your system.
2. Ensure that python3 is available on your system. This project was built with python 3.11.4. Ideally, we should be executing python apps in a virtual environment so let's create that.
3. **Create a python virtual environment** in the project root folder and activate it. You can use `python -m venv .venv` command to create a virtual environment with the name '.venv'.
4. **Once activated, install the dependencies** in the .venv environment with the help of 'requirements.txt' present in the root folder. Run `pip install -r requirements.txt` command for the same.
5. With the virtual environment activated and dependencies installed, you are good to go! **Start by running the tests** and validating if everything is alright?

### Running Tests

The application includes comprehensive tests to ensure that the behavior of utility is intact all the time. The tests are written in pytest and you can easily run these tests using the IDE tools. if you are playing around with this app using terminal, **run either of the commands stated** to see if all the test cases pass? `python -m pytest` or `pytest .\tests\test_checkout.py`

### Running the application

As your application is all set and tests are passing, we are sure that the app is ready for use. let's try it out with the command! `python .\main.py`

## App set-up and execution - Docker

This application can also be used as a containerized application with docker. Assuming that you already have docker installed on your machine, you can simply bring up the app in docker with the command `docker compose up --build`. The compose.yaml file has the port and other details already.

Alternatively, you can also use the more usual command of creating a Docker image of the application first and then running an instance of that image, the commands for that would be

1. `docker build -t checkout-agrichain .` - This will build a docker image based upon the dockerfile and tag it with the name 'checkout-agrichain'.
2. Once the image is successful, you can verify that using the `docker images` command, you should see the latest image of 'checkout-agrichain' listed there.
3. Now the last step would be to run a container based on the image. Use `docker run --name checkout-app -p 8000:8080 checkout-agrichain` command for that.

## Areas of improvement

The final solution must demonstrate

-   Documentation / Comments
-   Logging if possible / print statements at least.
-   Exception handling
-   Read price / Offer from external files, so that they can be modified
-   using configs
-   A readme file that's comprehensive enough to tell from design to usage.
