#noinspection CucumberUndefinedStep
Feature: checkout page checks for https://www.saucedemo.com/

    Scenario: Verify error message seen in checkout page if no input is given
      Given I am at checkout page
      When  I click on Continue button without entering any text
      Then I can see error message
      But If i click on cancel, it takes me back to previous page
      Then I click on Checkout button again and i am at checkout page
      But If i enter First Name, Last name, Zip code and click on Continue button
      Then I am navigated to finish checkout page
      Then I click on cancel, it takes me to inventory page
      
