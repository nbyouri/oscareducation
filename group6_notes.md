# Notes of Group 6   

## About Testing Env

### General Setup and Requirements
- If you use Posix, install requirements-group6.txt. See further for Windows
- Make sure you have PhantomJS installed and in your path environment variable! 
- In your Postgres, please allow user oscar to drop and create databases as the testing framework use an alternative db
- Add a configuration selecting "Behave"
- If you want to run the tests in PyCharm, go in Settings/Language & Framework/BDD and select Behave

### MacOS Setup 

### Windows Setup
- Launch requirements-group6_wind.txt
- You might be forced to restart your computer after adding PhantomJS in your path   

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
