#noinspection CucumberUndefinedStep
Feature: Inventory Manipulation for https://www.saucedemo.com/

    Scenario Outline: After login successfully, change display rule for the products
        Given open test site
        When I enter valid username and password
        Then I click on the dropdown to select "<display>" option to see "<item>" first
        And I logout and close browser

        Examples: TypeList
            | display       | item                |
            | az            | item_4_title_link   |
            | za            | item_3_title_link   |
            | lohi          | item_2_title_link   |
            | hilo          | item_5_title_link   |

    Scenario: Open product detail page to verify proper navigation
        Given open test site
        When I enter valid username and password
        Then I click on the first product and can see the product detail page
        And I navigate back to inventory page from product detail page
        And I logout and close browser

    Scenario: Select the lowest product's detail page and add the product to cart
        Given open test site
        When I enter valid username and password
        Then I change option of display to low to high
        Then I click on the first product and can see the product detail page
        Then I add the product to cart
        And I navigate back to inventory page from product detail page
        And I logout and close browser

    Scenario: Select the highest product's detail page and add the product to cart
        Given open test site
        When I enter valid username and password
        Then I change option of display to high to low
        Then I click on the first product and can see the product detail page
        Then I add the product to cart
        And I navigate back to inventory page from product detail page
        And I logout and close browser

    Scenario: Add the lowest and highest product to cart from product detail page and navigate to cart to verify
        Given open test site
        When I enter valid username and password
        Then I change option of display to high to low
        Then I click on the first product and can see the product detail page
        Then I add the product to cart
        And I navigate back to inventory page from product detail page
        Then I change option of display to low to high
        Then I click on the first product and can see the product detail page
        Then I add the product to cart
        Then I navigate back to inventory page from product detail page
        Then I click on the cart button
        Then I verify "2" items are displaying in cart
        Then I go back to inventory page from cart page
        And I logout and close browser
