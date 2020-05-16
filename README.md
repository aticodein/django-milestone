
# Fullstack Django-milestone project
[![Build Status](https://travis-ci.org/aticodein/django-milestone.svg?branch=master)](https://travis-ci.org/aticodein/django-milestone)

Frequently used shortcuts on gitpod:
alias run='python3 manage.py runserver'
alias col='python3 manage.py collectstatic'
alias mak='python3 manage.py makemigrations'
alias mig='python3 manage.py migrate'

## Project 

This project is an online webshop for electronics. 
Selected products held in shopping cart for one session.
Login, logout authentication for shopping with stripe payments.


 [Heroku Link to the application](https://milestone-4-django-project.herokuapp.com),
 [Github repository](https://github.com/aticodein/django-milestone)

## UX

A very simple presentation of a working webshop, easily attached to a technichal blog for introduce new products to readers.
Its simplicity good for around 50 items easily browsing with category and pagination.

A blog reader when got some new information about a new released electronic product on the market,
usually have to go to an other website to buy that product. Links to that website probably working with affiliate systems.

The blog owner with this application of the blog website, can sell products without go to other online webshop.

## Features

Landing page with slider, link for products and menubar. Very short visual representation of the products.
Next is the product page all item with pagination, below main menubar a category shearch option and a back to all items button.
Site bar for a few other kind of group and information to represent. 
Below products delivery information and footer with social media links.
The main menubar have the registration page link, login and shopping cart link. After registration
user can login and registration part of the menu change to a profile link and login turns a logout of course.

### Existing Features

Logged in or out warning sign.
Product panel has information for products from database.
Number of items can put in shopping cart after login.
Adjust products quantity at shopping cart and go to checkout.
Shopping via Stripe.

### Features Left to Implement

Site bar links to suggested groups or information.
Detailed and bigger product panel.
Auction page for certain product with a bidding system.

## Technologies Used

This project uses HTML, CSS, JavaScript and Python computer languages.
JQuery, Bootstrap, Django frameworks. 
SQLite and AWS databases.
Gitpod for developing, Github repositories for store code and Heroku deployment.

- AWS buckets stores data for Heroku
- Django with Python
  - Back-end framework very useful inbuilt fetures specially Admin site.
- Gitpod cloud developing
  - Found easy to use   

## Testing

During developing I have the debug function on (true) at online_auction.settings.py in Django app
so when I run the application it show immediately some of the problems.

Later I have set up [Travis](https://travis-ci.org/github/aticodein/django-milestone), all my github push was 
automaticly tested by this service.

I have used google developer tool to inspect my website many times, not only for checking the responsiveness 
in different devices but the error messages in console.

Friends and family tested the deployed version for me all links are clickable and menubar item working at all kind of devices.
However I have to used google more tools for clearing browsing data for checking all my CSS changes working.
This is the reason for some of inline style coding in HTML, but some are necessary for getting other styling at particular 
HTML item.

## Deployment

This project was deployed at [Heroku](https://milestone-4-django-project.herokuapp.com/)

I have folloewd this processduring deployment:

- Create new Heroku app at [Heroku/Home](https://www.heroku.com/home)
- The app name must be all lowercase caracter no space only dash can be used.
- Heroku uses Postgres database, so first I did add-on with free option
  - at setting Config Vars: the SECTRET_KEY and DATABASE_URL must be set for every project.
  - in developer terminal with pip must be installed psycopg2
  - this for the Heroku database connection 
   `Pip freeze > requirements.txt`
- Then in settings.py I have database:
 `DATABASE = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
- And the location for files:
 `STATICFILES_LOCATION = 'static'`
 `STATICFILES_STORAGE = 'custom_storages.StaticStorage'`
 `STATIC_URL = '/static/'`
 `STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)`
- Have to create a Procfile and install gunicorn
- In settings.py Heroku should be at allowed host with Heroku project name: 
  - ALLOWED_HOSTS = [os.environ.get('GITPOD_HOSTNAME','localhost'), 'milestone-4-django-project.herokuapp.com']
- For database changhe during development:
  - I have used an " if else " statement between AWS and SQLite 
  - Important to use "collectstatic" command after static file changes to find these at AWS database

### Differences
Database contet different in Gitpod to Heroku, Heroku uses AWS buckets for images and products details.  

## Credits

### Media and Content

The photos and text for products used in this site were obtained from [Buyitdirect](https://www.buyitdirect.ie/),
[eBay](https://www.ebay.ie/)

### Acknowledgements

Thanks to Ali Ashik, my mentor at Code Institute for support and the useful knowledge and ideas.
My second mentor during this project was Aaron Sinnott who helped to finalise.

When I got stuck tutor support helped me many times with quick answers to my questions.
Great support throughout the course with mentors, tutors, leads and friends at Slack!

THANK YOU!  
