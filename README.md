# Development environment

## Group 6 Status

[![Build Status](https://travis-ci.org/nbyouri/oscareducation.svg?branch=master)](https://travis-ci.org/nbyouri/oscareducation)
[![Coverage Status](https://coveralls.io/repos/github/nbyouri/oscareducation/badge.svg?branch=coverage)](https://coveralls.io/github/nbyouri/oscareducation?branch=coverage)

See further for information about our part of the project.

## Installation

### Database
First, install PostgreSQL version 9.4 or above
(installation instructions depends on your OS).
Then we advise you to install a tool such as
`pgAdmin` to administrate the database, `DbVisualizer`
visualize the database schema and
`PyCharm Community Edition` a python IDE. By default,
as it is stated in `oscar/settings.py`, the database
name is 'oscar', accessible from `localhost:5432`, with
the user 'oscar' and the password 'oscar'. So, create a
PostgreSQL server with a database, with the parameters 
you chose or the default parameters stated above if you 
do not intend to change the `oscar/settings.py`.

### Django
You only need to perform these commands once:
Install `virtualenv`, clone the repository, and
create a new virtual environment in it. Python
will be used in version 2.7. `ve` is the folder
where the virtual environment will be stored
```sh
$ apt-get install python-virtualenv
$ git clone https://github.com/ioune1993/oscareducation.git
$ cd oscareducation
$ virtualenv --python=/usr/bin/python2.7 ve
```

Then, enter in the virtual environment, and install
all the requirements
```sh
$ source ve/bin/activate
$ pip install -r requirements-oscar2.txt
```
Then adding fields into your database
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
If the second command does not create the fields, and report 
that there are missing relations, use the `makemigrations.sh` 
script to make the migrations for each app one by one (and then 
do the second command). This is unfortunate, but this a known 
bug in Django that can happen.

Then optionally with `pgAdmin` 
import the SQL data file 'oscar-data.sql' to obtain a sample 
of data in order to test the website.

Finally create a superuser account
```sh
$ python manage.py createsuperuser
```
and follow the steps

Once all the steps above done, run the server with:
```sh    
$ python manage.py runserver
```

You can now access the website: `http://127.0.0.1:8000`.

The administration is on `http://127.0.0.1:8000/admin`. You can
create a new "Professor" (green +) (and later, Students the same way), there, click on "green +" again to start a 
popup in which you'll create a new user (for example "prof" with password "prof"),
validate, select field is auto field, validate, you now have a prof user.
Then, edit this professor by providing him/her an email address (because
you need to confirm his/her email, you can use a temporary address in your tests).
Log out and go back on "/" to log.

Now, whenever you want to run the website again, you
only need to enter in you virtual environment and run
the Django server:
```sh
$ source ve/bin/activate
$ python manage.py runserver
```

## Documentation
To consult the Oscar documentation, open the
`documentation/build/html/index.html` file.

In order to generate the documentation, the `sphinx`
is used with .rst files. Examples of code documentation
can be found in `doc-example.py`. These conventions must
be respected to allow the proper documentation generation.

To generate the HTML documentation, run this command being in
the `documentation` folder:
```sh
$ make html
```

When you add code files to the project, they must be added to
the modules described in the .rst files, located in the
`documentation/source` folder.

The `conf.py` file in the `documentation/source` contains the
configuration for the `sphinx` tool.

# Notes of Group 6

## About Testing Env

### General Setup and Requirements
- If you use Posix, install requirements-group6.txt. See further for Windows
- Make sure you have PhantomJS installed and in your path environment variable!
- In your Postgres, please allow user oscar to drop and create databases as the testing framework use a disposable testing db
- Add a configuration selecting "Behave"
- If you want to run the tests in PyCharm, go in Settings/Language & Framework/BDD and select Behave

## Feature testing

Here is a small explanation of the feature testing environment

### Framework and tools

Behave has been selected as the feature testing framework. It lets you define
testing scenarios from desired user stories.
For example, you chose a simple login user stories, and then define
a scenario for a user logging in with "Given, Then, When" keywords.

In order to run those test, we use Selenium and the headless browser PhantomJS.
This way, the test are ran in background and you're not bothered with a browser popping
on your computer and executing the tests.

### How the tests are written and organized

- *environment.py* file defines some parameters of the test environment, such as what happen
between two tests, before each steps, etc...
- *browser.py* file defines the characteristics of the browser, such as the size of the screen,
some methods to let us take screenshots and dump an html file in case of test fail, and other things
- *specs/*.features* files are the scenarios. Each features represents a user story, with multiple
scenarios linked to this user story. For example we have the login user story, with the scenario of a
successful login, unsuccessful login, etc.
Each scenario is divided in *steps*, each step representing an action.
- *steps/* files. These files are just the implementation of each steps we talked before
using the framework. For example, in the login scenario we used the "*Then I enter my username*" step. That
step will then use the login page object to really input the username in the test instance of the website.
- *pages/* files are internal representation of the website pages using a Domain Specific Language. Again,
for our login page, we will define a page object that knows that the real login page has two inputs for
username and password and also a submit button, and will provide methods to interact with theses.

To summarize the execution flow :

- The framework reads each scenario
- For each steps, it looks up in the steps files for its definition
- Each steps use a page object to execute the action on the website test instance
- If it fails, the scenarios stops and the browser saves a screenshot and dumps an html file
of where the test failed so you can debug easier
- If it succeeds, the framework goes on the next step and so on

## Usage

Just run your tests with Behave within Pycharm or run `behave` in your terminal in the project's root.

### BDD Testing Framework
Behave is the testing framework used.
See http://pythonhosted.org/behave/ for further documentation.

### POM DSL
Still not found, but should be highly interesting to find an equivalent of
the combination Capybara-SitePrism of Rails in order to abstract the test steps.

### Integrity errors - FactoryBoy
Please be careful when creating factories with FactoryBoy, respect the integrity constraints
by using SubFactories or other RelatedFactories.
http://factoryboy.readthedocs.io/en/latest/
