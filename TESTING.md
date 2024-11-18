# Testing

## Validator Testing

Wawa Land has be thoroughly tested. All the code has been run through the [W3C html Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JSHint JavaScript Validator](https://jshint.com/). 

HTML

| Page                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| Home                    |![Home Page](static/images/screenshots/html-index.png)                                  | PASS     |
| Blog - logged out       |![Blog - Logged Out](static/images/screenshots/html-blog-loggedout.png)                 | PASS     |
| Blog - logged in        |![Blog - Logged In](static/images/screenshots/html-)                 | PASS     |
| Blog Post - logged out  |![Blog - Logged Out](static/images/screenshots/html-)                 | PASS     |
| Blog Post - logged in   |![Blog - Logged In](static/images/screenshots/html-)                 | PASS     |
| Event List              |![Event](static/images/screenshots/html-event-list.png)                 | PASS     |
| Event Listing           |![Event](static/images/screenshots/html-event-listing.png)                 | The code the validator is referring to is code which has been integrated by Django for the review functionality and not written by me. The id is specific to each review and the '<p>' tag cannot be deleted by me.   |
| Blog - logged out       |![Blog - Logged Out](static/images/screenshots/html-blog-loggedout.png)                 | PASS     |


The HTML W3C Validator Results:
![HTML W3C Validator](media/html-validator.png)

The CSS Validator Results:
![CSS Validator](media/css-validator.png)

The JSHINT Validator Results for Both Pages:
- script.js:
![JSHint Validator for script.js](media/js-script.png)

- quiz.js:
![JSHint Validator for quiz.js](media/js-quiz.png)


## Manual Testing
- Manual testing was carried out on local and deployed sites.

| Location     | Feature         | Expected Outcome                               | Pass/Fail| Notes                   |
|--------------|--------------   |------------------------------------------------|----------|-------------------------|
| Header       | Home button     | Takes user to home                             |  PASS    |
| Header       | Log-in button   | Takes user to log-in page on click             |  PASS    | If user is not logged in, the register and log-in buttons will be displayed, but if they are logged in, only the log-out button will appear |
| Header       | Register button  | Takes user to registration page on click                                       | PASS      |                                                                                                           |
| Header       | Logout button    | Takes user to log-out page on click                                            | PASS      |                                                                                                           |
| Log-in page  | Log-in function  | When user enters an unknown username, the user will not be logged in           | PASS      |                                                                                                           |
| Log-in page  | Log-in function  | When user enters an unknown password, the user will not be logged in           | PASS      |                                                                                                           |
| Log-in page  | Log-in function  | When user enters a known username AND password, the user will be logged in     | PASS      |                                                                                                           |

