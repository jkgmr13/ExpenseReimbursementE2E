Feature: Manager approves or denies reimbursements
  Background:
    Given The manager is logged in
    Given The manager has clicked the view button
    Scenario: Approve a reimbursement
      When The manager clicks approve
      Then The manager should be prompted for a reason
      When The manger completes the prompt
      Then The approved request should be removed from the table
      Scenario: Deny a reimbursement
        When The manager clicks deny
        Then The manager should be prompted for a reason
        When The manger completes the prompt
        Then The denied request should be removed from the table
