## Table of Content
1. [Bugs](#bugs)
2. [Validator Testing](#validator-testing)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Lighthouse](#lighthouse)
3. [Browser Testing](#browser-testing)
4. [Device Testing](#device-testing)
5. [Automated testing](#automated-testing)
6. [Manual Testing](#manual-testing)
    1. [Site Navigation](#site-navigation)
    2. [Home Page](#home-page)
    3. [Post detail page](#post-detail-page)
    4. [Booknow page](#booknow-page)
    5. [Booking Dashboard page ](#booking-dashboard-page)
    6. [Contact page](#contact-page)
    7. [Login page](#login-page)
    8. [Sign up page](#sign-up-page)
    9. [Logout page](#logout-page)

Extensive testing was done to make sure all the features work as expected. I did both the automated test and the manual test.

## Bugs

|  Bug |  Solution  |Status   |
|--|--|--|
|  
User can book a consultation at the same date and time as another user | Add to the views.py file Booking.objects.filter(date=date, time=time).exists() | fixed |
|  
Form to change booking does not appear | add 'form': form to the views.py file  | fixed |
|  
Menu on mobile devices is positioned incorrectly | fixed CSS style   | fixed |
|  
Daterange filter doesn't work on admin panel | delete wrong version and install new   | fixed |

## Validator Testing

### HTML
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. 
There were errors and warnings in the reports about unclosed elements and tags, incorrect values ​​and types of elements, unnecessary trailing slashes. All errors and warnings have been fixed, the project's HTML code has been re-checked without errors.
<details><summary>base.html</summary>
<img src="static/validation/validation-html-base.png">
</details>

<details><summary>index.html</summary>
<img src="static/validation/validation-html-index.png">
</details>

<details><summary>about.html</summary>
<img src="static/validation/validation-html-about.png">
</details>

<details><summary>blog.html</summary>
<img src="static/validation/validation-html-blog.png">
</details>

<details><summary>post_detail.html</summary>
<img src="static/validation/validation-html-post-detail.png">
</details>

<details><summary>booknow.html</summary>
<img src="static/validation/validation-html-booknow.png">
</details>

<details><summary>bookings.html</summary>
<img src="static/validation/validation-html-bookings.png">
</details>

<details><summary>delete-booking.html</summary>
<img src="static/validation/validation-html-delete-booking.png">
</details>

<details><summary>change-booking.html</summary>
<img src="static/validation/validation-html-change-booking.png">
</details>

<details><summary>contact-us.html</summary>
<img src="static/validation/validation-html-contact.png">
</details>

<details><summary>message-received.html</summary>
<img src="static/validation/validation-html-message-received.png">
</details>

<details><summary>login.html</summary>
<img src="static/validation/validation-html-login.png">
</details>

<details><summary>logout.html</summary>
<img src="static/validation/validation-html-logout.png">
</details>

<details><summary>signup.html</summary>
<img src="static/validation/validation-html-signup.png">
</details>
<br>

### CSS 
The website CSS style has successfully passed the [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). 
<details><summary>style.css</summary>
<img src="static/validation/validation_css.png">
</details>
<br>

### Python

All Python code was manually checked using [CI Python Linter](https://pep8ci.herokuapp.com/). 

#### Blog app
<details><summary>admin.py</summary>
<img src="static/validation/validation-python-blog-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-blog-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-blog-models.png">
</details>
<details><summary>tests_admin.py</summary>
<img src="static/validation/validation-python-blog-tests_admin.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-blog-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-blog-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-blog-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-blog-views.png">
</details>
<br>

#### Booking app

<details><summary>admin.py</summary>
<img src="static/validation/validation-python-booking-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-booking-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-booking-models.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-booking-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-booking-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-booking-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-booking-views.png">
</details>
<br>

#### Contact app
<details><summary>admin.py</summary>
<img src="static/validation/validation-python-contact-admin.png">
</details>
<details><summary>forms.py</summary>
<img src="static/validation/validation-python-contact-forms.png">
</details>
<details><summary>models.py</summary>
<img src="static/validation/validation-python-contact-models.png">
</details>
<details><summary>tests_models.py</summary>
<img src="static/validation/validation-python-contact-tests_models.png">
</details>
<details><summary>tests_views.py</summary>
<img src="static/validation/validation-python-contact-tests_views.png">
</details>
<details><summary>urls.py</summary>
<img src="static/validation/validation-python-contact-urls.png">
</details>
<details><summary>views.py</summary>
<img src="static/validation/validation-python-contact-views.png">
</details>
<br>



### Lighthouse

## Browser Testing

Testing has been carried out on the  following browsers: 
  - Google Chrome
  - Firefox
  - Microsoft Edge

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience.
The available functionality and user experience is reflected in the table below.


| Goals/actions  | As a guest | As a logged user  | Result | Comment |
|--|:--:|:--:|:--:|--|
| I can use menu and navigating through pages | &check; | &check; | Pass | |
| I can see the home page | &check; | &check; | Pass | |
| I can see the Sign Up page | &check; |&check;  |  Pass| |
| I can see the Login page  | &check; |&check;  |  Pass| |
| I can see the Logout page  | &cross; |&check;  |  Pass| This function is available only to authorized users|
| I can see the blog | &check; |&check;  |  Pass| |
| I can see the post detail page | &check; |&check;  |  Pass| |
| I can leave comment | &cross; |&check;  |  Pass|This function is available only to authorized users|
| I can leave like | &cross; |&check;  |  Pass| This function is available only to authorized users|
| I can see the Booknow page when I click on Book Now button| &cross; | &check;  | Pass |Redirects to the page with a message that the user must register or log in for guest or shows up form for authorized user |
| I can fill fields in the form the Booknow page | &cross; | &check;  | Pass |This page and form are available only to authorized users |
| I can see the Bookings dashboard page   | &cross; | &check;  | Pass | This page is available only to an authorized users|
| I can edit booking in the form on the Change booking page  | &cross;  | &check;  | Pass |This page is available only to authorized users |
| I can see the Change booking page  | &cross;  | &check;  | Pass | This page is available only to authorized users|
| I can see the Delete booking page  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| I can see the Contact page  | &cross;  | &check;  | Pass | This page is available only to authorized users|

<br/>

## Device Testing
The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.
The following devices have been tested:

- Nest HubMax (Desktop)
- iPad Pro (Tablet)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- Galaxy Tab S4 (Tablet)
- Nexus 7 (Mobile)
- Nokia N9 (Mobile)
- iPhone 5/SE (Mobile)
- iPhone 4 (Mobile)
## Automated testing
Testing was done using the built in Django module, unittest.
Coverage was also usesd to generate a report

***Contact app:***
<details><summary>Contact app tests_views.py </summary>
<img src="">
</details>
<details><summary>Contact app tests_models.py</summary>
<img src="">
</details>
<br>
<details><summary>Coverage Contact app</summary>
<img src="">
</details>
<br>

***Booking app:***

<details><summary>Booking app tests_views.py </summary>
<img src="">
</details>
<details><summary>Booking app tests_models.py</summary>
<img src="">
</details>
<br>
<details><summary>Coverage Booking app</summary>
<img src="">
</details>
<br>

***Blog app:***

<details><summary>Blog app tests_views.py </summary>
<img src="">
</details>
<details><summary>Blog app tests_models.py</summary>
<img src="">
</details>
<details><summary>Blog app tests_admin.py</summary>
<img src="">
</details>
<br>
<details><summary>Coverage Blog app</summary>
<img src="">
</details>
<br>

## Manual Testing
### Site Navigation
### Home Page
### Post detail page
### Booknow page
### Booking Dashboard page
### Contact page
### Login page
### Sign up page
### Logout page


