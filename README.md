# BUY HIVE
## Description
Buy Hive is an online clothing store that focuses on improving online shopping. It comes with unique features that are of benefit to a user. The web application is accessible and easy to navigate.
Buy Hive comes with an enticing user interface and provides a variety of clothing products at the disposal of customers who view the site.

## Features
1. **Displays a variety of products to users**
2. **Shopping cart context management**
3. **Secure user sign up and login**


 ## Technologies used
 1. **React**: The frontend has been built on react.
 2. **Python-Flask**: Backend developing
 3. **SQLite**: Database for storing product and user data.
 4. **Pipenv**: Dependency management tool.
 5. **Flask-RESTFul**: API developing
 6. **JWT**: Use authentication and authorisation

 ## Installation and setting up
 - Fork and clone this repository
 - Installing of dependencies:
    - cd into the frontend directory and run ```npm install``` to install frontend dependencies
    -  once dependecies are installed run ```npm run dev ``` to start the frontend server.
    -  Open another terminal and cd to the backend directory and run ```pipenv install && pipenv shell ``` to install python packages and enter the virtual environment.
    -  Once in the virtual environment run ```export FLASK_APP=app.py``` followed by ```export FLASK_RUN_PORT=5555```
    -  Run ```python app.py``` or ```python3 app.py``` to start the backend server.
    -  Incase of any error while trying to get the backend running use
       ```sh
       pip install --upgrade flask flask-sqlalchemy
       ```
 - Once both servers are running feel free to explore the app in the browser

## Future plans
1. Intergrate a payment system to enable easy transaction while purchasing goods
2. Add a user profile where users can keep track of their order history as well as have control of their data such as username ana the ability to change their password
3. Add seller profile option. This aims at providing a platform for online clothe venders to display as well as sell their products. Seller profile to include features such as
    - order management.
    - inventory management.
    - shipping tracking

## Meet the team
Buy Hive was brought to life by a team of five developers
- **Gideon Rotich**
- **Eric Mutuma**
- **Ian Mugambi**
- **Ignatius Mayaka**
- **Hidaya Vanessa**
        
