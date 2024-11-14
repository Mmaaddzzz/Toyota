*** Settings ***
Library                             SeleniumLibrary

*** Variables ***

${browser}                          chrome
${url}                              https://www.toyotamobilitysolutions.com   #sample website
${driver_path}                      /bin/chromedriver

${first_name_input}                     //*[@id="firstname"]/form/div/div[1]/input #sample first name input box
${last_name_input}                      //*[@id="lastname"]/form/div/div[2]/input #sample last name input box
${email_input}                          //*[@id="email"]/form/div/div[3]/input #sample email input box
${mobile_number_input}                  //*[@id="mobilenumber"]/form/div/div[4]/input #sample mobile number input box

${submit_button}                        //*[@id="submit"]/form/div/div[1]/button #sample submit button
${login_button}                         //*[@id="submit"]/form/div/div[2]/button #sample login button

${valid_email}                                     valid_user@example.com
${valid_phone_number}                              09088175555


${invalid_email}                                   invalid_user@example
${invalid_phone_number}                            +6390881755556

${special_email}                                     !@#user@#$%^
${special_phone_number}                              !@#user@#$%^

*** Test Cases ***
Navigate to the Register Page
Check Input Fields
Input Valid Username Invalid Password
Input Invalid Username Valid Password 
Clear Input Fields
Special Character Input Valid Fields


*** Keywords ***
Navigate to the Register Page
    open browser                ${url}      ${browser}     #this is for headless robot script options=add_argument("--headless")     options=add_argument("--no-sandbox")     options=add_argument("--disable-gpu")     options=add_argument("--disable-dev-shm-usage")	          executable_path=${driver_path}
    maximize browser window                                #maximize the browser for better viewing 
    sleep    2s

Check Input Fields # STEP 1

    Run Keyword And Continue On Failure    Page Should Contain Element    ${first_name_input}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${last_name_input}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${email_input}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${mobile_number_input}

Input Valid Fields # STEP 2

input text     ${email_input}   ${valid_email} 
input text     ${mobile_number_input}    ${valid_phone_number}  

Input Valid Username Invalid Password #STEP 3 - it shows in the pdf password but I will input the phone number since that is what is shown in the instructions

input text     ${email_input}   ${valid_email} 
input text     ${mobile_number_input}    ${invalid_phone_number}  
element should be visible                                        "Incorrect phone number format. Please try again."


Input Invalid Username Valid Password #STEP 4 -

input text     ${email_input}   ${invalid_email} 
input text     ${mobile_number_input}    ${valid_phone_number}  
element should be visible                                       "Incorrect email format.Please try again."

Clear Input Fields # STEP 5 -
    Clear Element Text    ${first_name_input}
    Clear Element Text    ${last_name_input}
    Clear Element Text    ${email_input}
    Clear Element Text    ${phone_input}


Special Character Input Valid Fields # STEP 6 - this is for the inputting of special characters into the email and phone number input field

input text     ${email_input}   ${special_email} 
input text     ${mobile_number_input}    ${special_phone_number} 
sleep 2
element should be visible                                       "Incorrect email format.Please try again."
refresh

#Other Keywods----------------------------------------------------------------------

refresh
    Execute JavaScript              location.reload(true);