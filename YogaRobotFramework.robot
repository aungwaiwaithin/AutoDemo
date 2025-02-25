*** Settings ***
Library                 SeleniumLibrary

*** Variables ***
${url}                                   https://webfront-uat.yogamovement.com/
${browser}                               Firefox
${close_alert}                           //html/body/div/div/aside/div/div[2]/button
#/html/body/div/div/aside/div/div[2]/button
#css:.modal__btn-close.click-efx.circle.animated
${register}                              //html/body/div/div/header/div/div/div/nav[1]/ul/li[1]/a

${register_btn}                          //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button
${femal}                                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div
${lastname}                              //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input
${country}                               //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div
${contry_search}                         //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input
${myanmar}                               //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]

${year}                                     1998
${month}                                    10
${day}                                 //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]
${country_img}                          xpath:img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]

${signin_link}                       //html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[2]/a
${signin_btn}                       //html/body/div/div/aside/div/div[2]/div/div/div[2]/form/div/button
${siginalaert}                      //html/body/div/div/aside/div/div[2]/button
${buy_aclass}                       //html/body/div/div/header/div[2]/a[2]/div/button[1]
${allaccess}                        //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[2]/a
${allaccess_pack}                   //html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[3]
${allaccess_pack_btn}               //html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[3]/div[4]/button
${order_next}                       //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button
${choose_one}                       //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/label/div/div/div/div[1]
${east_coast}                      //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/label/div/div/div/div[1]/div[1]
${img1}                             C:/Users/DELL/Pictures/flower1.jpg

${payment_change}                 //html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/button

${image_upload}                 //html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/label/input

${card_number}                  //html/body/div/form/span[2]/div/div/div[2]/span/input

${card_exp_date}               //html/body/div/form/span[2]/div/span/input

${card_cvc}                     //html/body/div/form/span[2]/div/span/input

${paynow}                      //html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/button

*** Keywords ***
Register User
     Sleep                           3
     Click Element                   xpath=//html/body/div/div/header/div/div/div/nav[1]/ul/li[1]/a
     Sleep                           3
     Input Text                      name:email              wai21@yopmail.com
     Sleep                           3
     Input Text                      name:password            wai123
     Sleep                           3
     Click Button                   ${register_btn}
     Sleep                           5
     Input Text                     name:firstname                QA
     Sleep                            4
     Input Text                     ${lastname}                 Wai Wai
     Sleep                           3
     Click Element                  ${country}
     Sleep                            3
     Input Text                     ${contry_search}            Myanmar
     Sleep                           3
     Click Element                  ${myanmar}
     Sleep                           2
     Input Text                     name:mobile                 988766565
     Sleep                            2
     Click Element                 id:dob
     Sleep                          2
     #year
     Click Element                 xpath://select[2]/option[@value='${year}']
     Sleep                          2
     Select From List By Value     xpath://select[2]            ${year}
     Sleep                          2
     Select From List By Value    xpath://select[1]             ${month}
     Sleep                          2
    Click Element                ${day}
     Sleep                          3
     Click Element               ${femal}
    Sleep                           2
    Click Element               class:css-egispl
    Sleep                           2
    Click Element               xpath://img[@src="https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-th.png"]
    Sleep                           2
    Click Button                //html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button


Singin
    Click Element               ${signin_link}
    Sleep                       3
    Input Text                  name:email                      aung100@yopmail.com
    Sleep                       3
    Input Text                  name:password                   P@ssw0rd
    Sleep                       3
    Click Button                ${signin_btn}
    Sleep                       3
    Click Button                ${siginalaert}
    Sleep                       3
    Click Button                ${buy_aclass}
    Sleep                       3
    Click Element               ${allaccess}
    Sleep                       3
    Click Element               ${allaccess_pack}
    Sleep                       3
    Click Button                ${allaccess_pack_btn}
    Sleep                       3
    Click Button                ${order_next}
    Sleep                       3
    Click Element               ${choose_one}
    Sleep                       3
    Click Element               xpath://*[text()="East Coast"]
    Sleep                       3

  #Imge
  Execute JavaScript            document.querySelector('input[type="file"]').classList.remove('d-none')
  Sleep                         3
  Choose File                   xpath://input[@type='file']                     ${img1}
  Sleep                         3

  #Iframe Payment
  Click Button                          xpath=//button[text()='Change']
  Sleep                                 3
  Wait Until Element Is Visible        CSS=iframe[name^='__privateStripeFrame']          timeout=10s
  Select Frame                          CSS=iframe[name^='__privateStripeFrame'][title="Secure card number input frame"]
  Sleep                                 3

  Input Text                            ${card_number}                  4111111111111111
  Unselect Frame

  Select Frame                          CSS=iframe[name^='__privateStripeFrame'][title="Secure expiration date input frame"]
  Sleep                                 3
  Input Text                            ${card_exp_date}                12/26
  Unselect Frame

  #CVC
   Select Frame                          CSS=iframe[name^='__privateStripeFrame'][title="Secure CVC input frame"]
    Sleep                                 3
    Input Text                            ${card_cvc}                123
    Unselect Frame
    Sleep                                  3
    Click Button                        ${paynow}




*** Test Cases ***
Main
    Open Browser                ${url}                      ${browser}
    Maximize Browser Window
    Sleep                       5
    Click Button                xpath=//html/body/div/div/aside/div/div[2]/button
    Sleep                       5
    Register User
    Sleep                       5
    Singin
    Sleep                       5
