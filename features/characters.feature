@characters
Feature: Searching characters

@positive
Scenario: Search by Agents of Atlas
  Given I have an access token
  When I perform a GET operation for "/v1/public/characters/1011198"
  Then I verify the response code is "200"
  And it was returned the "Agents of Atlas" character

@positive
Scenario: Search by Agent Brand
  Given I have an access token
  When I perform a GET operation for "/v1/public/characters/1011297"
  Then I verify the response code is "200"
  And it was returned the "Agent Brand" character

@positive
Scenario: Search by Balder
  Given I have an access token
  When I perform a GET operation for "/v1/public/characters/1011456"
  Then I verify the response code is "200"
  And it was returned the "Balder" character

@negative
Scenario: Search by a nonexistent character
  Given I have an access token
  When I perform a GET operation for "/v1/public/characters/1111111"
  Then I verify the response code is "404"
  And it was returned the message: "We couldn't find that character"