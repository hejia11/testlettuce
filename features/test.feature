# Created by X-8 at 2019/12/25
#Enter feature name here
Feature: Calculation
  # Enter feature description here
  Input two number,then compare result
# Enter scenario name here
  Scenario: Do a simple add method
    # Enter steps here
    Given I have two number:1 and 5
    When Do add method
    Then I get result:6

  Scenario: Do a simple add method
    # Enter steps here
    Given I have two number:2 and 5
    When Do add method
    Then I get result:7
