# Created by sekoyahicks at 8/28/24
Feature: Create the test case

  Scenario: User can filter by sale status High Demand
    Given Open the main page
    When log in to the page
    And Click on "off plan" at the left side menu
    And Verify the right page opens
    And Click on Filters
    And Filter by sale status of "High Demand"
    Then Verify each product contains the High Demand tag
