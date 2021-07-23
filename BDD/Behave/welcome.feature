Feature: Test Something
  Scenario: verify image
    Given launch chrome browser
    When open test site
    Then verify that the webpage has some content
    And close browser

  Scenario: Do a successful login
    Given open test site
    When I enter valid username and password
    Then I am successfully logged in
    And close browser

  Scenario: Do an unsuccessful login
    Given open test site
    When I enter invalid username and password
    Then I can see the error message
    And close browser

  Scenario: Logout from the site after successfully login
    Given open test site
    When I enter valid username and pas sword
    Then I am successfully logged in
    And I logout and close browser
