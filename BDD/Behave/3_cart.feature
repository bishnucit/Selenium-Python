Feature: Cart page checks

    Scenario: Set display Z-A and add to cart the 2nd item of the list and then go to cart page and remove the item
        Given open test site
        When I enter valid username and password
        Then I change option of display to z to a
        Then I add "2" nd product on the list to cart from inventory page
        Then I click on the cart button
        Then I remove the product from cart
        And I go back to inventory page from cart page
        And I logout and close browser
