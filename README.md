#### Ian's Pokeapp
# To run this application on your local machine
1. git clone this repository into your project directory
2. create a virtual environment: $ python3 -m venv venv 
    to enter your venv: $ source venv/bin/activate 
3. install dependencies : $ pip3 install -r requirements.txt
4. You will need to create environmental variables in your .env file
    $ touch .env
    The two variables you need are DATABASE_URL and SECRET_KEY
5. create pokeapp database : $ psql -f pokeapp.sql
6. open application @ http:localhost:5000: $ flask run 

#### Features and Inspiration
This application is w.i.p while I job search.
This application 
  -  is a static site
  -  features the ability to login/sign up and logout 
  -  using Flask WTForms and bcrypt authentication
  -  utilizes the PokeAPI to retrieve Pokemon data
