# Notes of Group 6


## About Testing

### Requirements 
- Make sure you have PhantomJS install and in your path ! 
- Update your VE with added requirements
- In your Postgres, please allow user oscar to drop and create databases as the testing framework use an alternative db

### Usage 

Just run your tests with ```python manage.py behave```  and enjoy.

#### BDD Testing Framework
**Django_Behave** is making it easier to use Behave 
http://behave-django.readthedocs.io/en/stable/

#### POM DSL
Still not found, but should be highly interesting to find an equivalent of 
the combination Capybara-SitePrism of Rails in order to abstract the test steps.

#### Integrity errors - FactoryBoy
Please be careful when creating factories with FactoryBoy, respect the integrity constraints 
by using SubFactories or other RelatedFactories.
http://factoryboy.readthedocs.io/en/latest/
