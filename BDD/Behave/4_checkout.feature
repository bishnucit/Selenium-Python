#noinspection CucumberUndefinedStep
Feature: checkout page checks for https://www.saucedemo.com/

    Scenario: Navigate to checkout page and cancel the checkout
      Given I am at checkout page
      When  I click on Continue button without entering any text
      Then I can see error message
      But If i click on cancel, it takes me back to previous page
      Then I click on Checkout button again and i am at checkout page
      But If i enter First Name, Last name, Zip code and click on Continue button
      Then I am navigated to finish checkout page
      Then I click on cancel, it takes me to inventory page
      And I logout and close browser

    Scenario: Navigate to checkout page and complete the checkout
      Given I am at checkout page
      Then If i enter First Name, Last name, Zip code and click on Continue button
      Then I am navigated to finish checkout page
      Then I click on finish button to complete the checkout
      Then I can see the thank you page and i go back to inventory page
      And I logout and close browser
