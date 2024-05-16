# checkout-codekata-agrichain

A code kata to demonstrate programming skills in python3. **This is an exercise by AgriChain**
The goal of the exercise is to implement the code for a supermarket checkout process that calculates the total price of items added in the cart by the customer. In the store, they use individual letters of the alphabet (A, B, C, and so on) to represent items. Products can be purchased at their individual pricing or at a discounted price when purchased in groups as listed below: 

![image](https://github.com/AngeshBhardwaj/checkout-codekata-agrichain/assets/13464654/b0ee3bc3-179f-4619-a3fe-cd50385a0d9d)

For example, item ‘A’ might cost $50 individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you $130.

Comprehensive test cases have been added to validate that the checkout accepts items in any order, so that if we scan product B, then product A, and then another product B, we’ll recognize the two B’s and price them at a discounted price of $45 instead of individual pricing of $30, which brings the Total order pricing to Rs 95. Below example cases have been validated by automated test cases included in the application:

![image](https://github.com/AngeshBhardwaj/checkout-codekata-agrichain/assets/13464654/0d380d1c-49a0-40b0-afe5-13823a213d6c)

## Application Features
The application is ready to use and can be ran on a local maching having python3 or in a container. The app has below main features:
- **An informational greetings message** that talks about the products and offers available for the week (in screen shot above).
- **An interactive menu** supported to test out the app functionality easily.
- Automated test cases built to ensure the behavior of app doesn't change with updates. **This app is built using BDD and TDD principles**.
- The app has been built by following the best practices for cleaner, simpler while reusable code.
- The app has configurable and centralized logging and config support.
  
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

This application can also be used as a containerized application with docker. Assuming that you already have docker installed on your machine, you can simply bring up the app in docker with the command `docker compose up --build`. The compose.yaml file has the port and other details already. _[As our application requires interactive terminal, this command will give '' error and terminate. **you will need to run it manually in interactive mode using `docker run -ti checkout-codekata-agrichain-server` command.**]_

Alternatively, you can also use the more usual command of creating a Docker image of the application first and then running an instance of that image, the commands for that would be

1. `docker build -t checkout-codekata-agrichain-server .` - This will build a docker image based upon the dockerfile and tag it with the name 'checkout-agrichain'.
2. Once the image is successful, you can verify that using the `docker images` command, you should see the latest image of 'checkout-agrichain' listed there.
3. Now the last step would be to run a container based on the image. Use `docker run -ti --name checkout-app -p 8000:8080 checkout-codekata-agrichain-server` command for that.

## Areas of improvement

The application can be further enhanced to

-   Read price / Offer from external file (csv/text), so that they can be modified externally.
-   Option for cancelling Cart or having more detailed / incremental total price with visible savings due to offers.
-   Using fixtures and stubs for test so that test data also gets read from data files and are independent of actual offers available.
-   Log file rotation and better logging can be introduced.
-   The application will struggle to handle large item list as of now, if the requirement arises, a different data structure can be considered.
-   Environment control can be added for better validation in different lifecycles.
-   Asynchronous programming can be introduced for better scaling, not needed as of now.
