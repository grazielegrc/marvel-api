@stories
Feature: Listing stories

@positive
Scenario: List stories with limit equal to 5
  Given I have an access token
  When I perform a GET operation for "/v1/public/stories"
  Then I verify the response code is "200"
  And it was returned only 5 registers
