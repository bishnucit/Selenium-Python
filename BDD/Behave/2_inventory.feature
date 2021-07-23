Feature: Inventory Manipulation

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

