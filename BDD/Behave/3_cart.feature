#noinspection CucumberUndefinedStep
Feature: Cart page checks for https://www.saucedemo.com/

    Scenario: Set display Z-A and add to cart the 2nd item of the list and then go to cart page and remove the item
        Given open test site
        When I enter valid username and password
        Then I change option of display to z to a
        Then I add product number "2" on the list to cart from inventory page
        Then I click on the cart button
        Then I remove the product from cart
        And I go back to inventory page from cart page
        And I logout and close browser

    Scenario: Add every 4th item of all display types to cart from inventory page and then verify the number of items
        in the cart page. If an item is already added to cart then it should not add it again.
        Given open test site
        When I enter valid username and password
        Then I add product number "4" on the list to cart from inventory page
        Then I change option of display to z to a
        Then I add product number "4" on the list to cart from inventory page
        Then I change option of display to low to high
        Then I add product number "4" on the list to cart from inventory page
        Then I change option of display to high to low
        Then I add product number "4" on the list to cart from inventory page
        Then I click on the cart button
        Then I verify "3" items are displaying in cart
        Then I go back to inventory page from cart page
        And I logout and close browser

    Scenario: Add 6th product of all types of display option and verify the cart icon count at cart page.
        Given open test site
        When I enter valid username and password
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to z to a
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to low to high
        Then I add product number "6" on the list to cart from inventory page
        Then I change option of display to high to low
        Then I add product number "6" on the list to cart from inventory page
        Then I click on the cart button
        Then I can see the count of the cart icon to be "4"
        Then I go back to inventory page from cart page
        And I logout and close browser
