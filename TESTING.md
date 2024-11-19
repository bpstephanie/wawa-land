# Testing

## Validator Testing

Wawa Land has be thoroughly tested. All the code has been run through the [W3C html Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JSHint JavaScript Validator](https://jshint.com/). 

HTML

| Page                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| Home                    |![Home Page](static/images/screenshots/html-index.png)                                  | PASS     |
| Blog - logged out       |![Blog - Logged Out](static/images/screenshots/html-blog-loggedout.png)                 | PASS     |
| Blog - logged in        |![Blog - Logged In](static/images/screenshots/html-blog-loggedin.png)                 | PASS     |
| Blog Post - logged out  |![Blog - Logged Out](static/images/screenshots/html-blog-post-loggedout.png)          | The code the validator is referring to is code which has been integrated by Django for the comment functionality and not written by me. The '<p>' tag cannot be deleted by me.     |
| Blog Post - logged in   |![Blog - Logged In](static/images/screenshots/html-blog-post-logged-in.png)                 | The code the validator is referring to is code which has been integrated by Django for the comment functionality and not written by me. The id is specific to each review and the '<p>' tag cannot be deleted by me.     |
| Event List             |![Event](static/images/screenshots/html-event-list.png)                 | PASS     |
| Event Listing - logged out          |![Event](static/images/screenshots/html-event-listing.png)                 | The code the validator is referring to is code which has been integrated by Django for the review functionality and not written by me. The id is specific to each review and the '<p>' tag cannot be deleted by me.   |
| Event Listing - logged in          |![Event](static/images/screenshots/html-event-listing-loggedout.png)                 | The code the validator is referring to is code which has been integrated by Django for the review functionality and not written by me. The '<p>' tag cannot be deleted by me.   |
| Add Post      |![Add Post](static/images/screenshots/add-post-1.png) ![Add Post](static/images/screenshots/add-post-2.png)                | The code validator is referring to errors in code with have been integrated by Django that add summernote to the body field. I cannot amend this code.      |
| Profile       |![Profile](static/images/screenshots/html-profile.png)                 | The code the validator is referring to is code which has been integrated by Django for the posts and comments functionality and not written by me. The '<p>' tag cannot be deleted by me.     |
| Edit Post       |![Edit Post](static/images/screenshots/html-edit-post-1.png) ![Edit Post](static/images/screenshots/html-edit-post-2.png)               | The code validator is referring to errors in code with have been integrated by Django that add summernote to the body field. I cannot amend this code.     |
| Log In          |![Log In](static/images/screenshots/html-log-in.png)                                  | PASS     |
| Register        |![Register](static/images/screenshots/html-register.png)                                  | The code the validator is referring to is integrated by Django and not written by me.     |
| Sign Out        |![Sign Out](static/images/screenshots/html-sign-out.png)                                  | PASS     |


CSS

The CSS Validator Results:
![CSS Validator](static/images/screenshots/css.png)

The CI Python Linter Validator
| Page                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| Blog - Admin            |![Blog-Admin](static/images/screenshots/blog-admin.png)                                 | PASS     |
| Blog - Apps             |![Blog-Apps](static/images/screenshots/blog-apps.png)                                   | PASS     |
| Blog - Forms            |![Blog-Forms](static/images/screenshots/blog-forms.png)                                 | PASS     |
| Blog - Models           |![Blog-Models](static/images/screenshots/blog-models.png)                               | PASS     |
| Blog - Urls             |![Blog-Urls](static/images/screenshots/blog-urls.png)                                   | PASS     |
| Blog - Views            |![Blog-Views](static/images/screenshots/blog-views.png)                                 | PASS     |
| Event - Admin           |![Blog-Admin](static/images/screenshots/event-admin.png)                                | PASS     |
| Event - Apps            |![Event-Apps](static/images/screenshots/event-apps.png)                                 | PASS     |
| Event - Forms           |![Event-Forms](static/images/screenshots/event-forms.png)                               | PASS     |
| Event - Models          |![Event-Models](static/images/screenshots/event-models.png)                             | PASS     |
| Event - Urls            |![Event-Urls](static/images/screenshots/event-urls.png)                                 | PASS     |
| Event - Views           |![Event-Views](static/images/screenshots/event-views.png)                               | PASS     |
| Wawaland - Settings     |![EWawaland - Settings](static/images/screenshots/wawaland-settings.png)                | PASS     |
| Wawaland - Urls         |![EWawaland - Urls](static/images/screenshots/wawaland-urls.png)                        | PASS     |



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

