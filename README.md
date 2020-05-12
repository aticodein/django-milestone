# Fullstack Django-milestone project
[![Build Status](https://travis-ci.org/aticodein/django-milestone.svg?branch=master)](https://travis-ci.org/aticodein/django-milestone)
Django online store
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

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.



