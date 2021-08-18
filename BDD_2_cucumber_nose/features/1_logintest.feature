Feature: Login verification for https://www.saucedemo.com/
  Scenario: Navigate to test site
    Given user is on login page
    When I enter valid username and password
    Then I am successfully logged in

  Scenario: Do an unsuccessful login
    Given user is on login page
    When I enter invalid username and password
    Then I am not logged in
