*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  test_user
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  tu
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Page Should Contain  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  test_user
    Set Password  asd123
    Set Password Confirmation  asd123
    Click Button  Register
    Page Should Contain  Password should be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  test_user
    Set Password  password
    Set Password Confirmation  password
    Click Button  Register
    Page Should Contain  Password should have non-letter characters

Register With Nonmatching Password And Password Confirmation
    Set Username  test_user
    Set Password  password123
    Set Password Confirmation  password456
    Click Button  Register
    Page Should Contain  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Page Should Contain  User with username kalle already exists

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page