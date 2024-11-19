# Testing

## Validator Testing

Wawa Land has be thoroughly tested. All the code has been run through the [W3C html Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JSHint JavaScript Validator](https://jshint.com/). 

- ### HTML

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


- ### CSS
The CSS Validator Results:
![CSS Validator](static/images/screenshots/css.png)

- ### Python and Django
The CI Python Linter Validator
| File                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| Blog - Admin            |![Blog-Admin](static/images/screenshots/blog-admin.png)                                 | PASS     |
| Blog - Apps             |![Blog-Apps](static/images/screenshots/blog-app.png)                                   | PASS     |
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
| Wawaland - Settings     |![Wawaland - Settings](static/images/screenshots/wawaland-settings.png)                 | PASS     |
| Wawaland - Urls         |![Wawaland - Urls](static/images/screenshots/wawaland-urls.png)                         | PASS     |
| Wawaland - Wsgi         |![Wawaland - Wsgi](static/images/screenshots/wawaland-wsgi.png)                         | PASS     |


- ### JavaScript
The JSHINT Validator
| File                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| comments.js             |![comments.js](static/images/screenshots/comments-jshint.png)                           | PASS     |
| posts.js                |![posts.js](static/images/screenshots/posts-jshint.png)                                | PASS     |
| profile.js              |![profile.js](static/images/screenshots/profile-jshint.png)                             | PASS     |
| reviews.js              |![reviews.js](static/images/screenshots/reviews-jshint.png)                             | PASS     |


- ### Lighthouse
| Page                      | Device     | Screenshot                                                                       |
|---------------------------|------------|----------------------------------------------------------------------------------|
| Home                      | Desktop    | ![Home Desktop](static/images/screenshots/home-desktop.png)                      |
| Home                      | Mobile     | ![Home Mobile](static/images/screenshots/home-mobile.png)                        |
| Blog - Logged In          | Desktop    | ![Blog Desktop](static/images/screenshots/blog-li-desktop.png)                   |
| Blog - Logged In          | Mobile     | ![Blog Mobile](static/images/screenshots/blog-li-mobile.png)                     |
| Blog - Logged Out         | Desktop    | ![Blog Desktop](static/images/screenshots/blog-logout-desktop.png)               |
| Blog - Logged Out         | Mobile     | ![Blog Mobile](static/images/screenshots/blog-logout-mobile.png)                 |
| Blog Post - Logged In     | Desktop    | ![Blog Post Desktop](static/images/screenshots/blog-post-li-desktop.png)         |
| Blog Post - Logged In     | Mobile     | ![Blog Post Mobile](static/images/screenshots/blog-post-li-mobile.png)           |
| Blog Post - Logged Out    | Desktop    | ![Blog Post Desktop](static/images/screenshots/blog-post-logout-desktop.png)     |
| Blog Post - Logged Out    | Mobile     | ![Blog Post Mobile](static/images/screenshots/blog-post-lo-mobile.png)           |
| Event Page                | Desktop    | ![Event Desktop](static/images/screenshots/event-desktop.png)                    |
| Event Page                | Mobile     | ![Event Mobile](static/images/screenshots/event-mobile.png)                      |
| Event Listing - Logged In | Desktop    | ![Event Listing Desktop](static/images/screenshots/event-listing-li-desktop.png) |
| Event Listing - Logged In | Mobile     | ![Event Listing Mobile](static/images/screenshots/event-listing-li-mobile.png)   |
| Event Listing - Logged Out| Desktop    | ![Event Listing Desktop](static/images/screenshots/event-listing-lo-desktop.png) |
| Event Listing - Logged Out| Mobile     | ![Event Listing Mobile](static/images/screenshots/event-listing-lo-mobile.png)   |
| Add New Post              | Desktop    | ![Add Post Desktop](static/images/screenshots/add-post-desktop.png)              |
| Add New Post              | Mobile     | ![Add Post Mobile](static/images/screenshots/add-post-mobile.png)                |
| Edit Post                 | Desktop    | ![Edit Post Desktop](static/images/screenshots/edit-post-desktop.png)            |
| Edit Post                 | Mobile     | ![Edit Post Mobile](static/images/screenshots/edit-post-mobile.png)              |
| Profile                   | Desktop    | ![Profile Desktop](static/images/screenshots/profile-desktop.png)                |
| Profile                   | Mobile     | ![Profile Mobile](static/images/screenshots/profile-mobile.png)                  |
| Register                  | Desktop    | ![Register Desktop](static/images/screenshots/register-desktop.png)              |
| Register                  | Mobile     | ![Register Mobile](static/images/screenshots/register-mobile.png)                |
| Log In                    | Desktop    | ![Login Desktop](static/images/screenshots/login-desktop.png)                    |
| Log In                    | Mobile     | ![Login Mobile](static/images/screenshots/login-mobile.png)                      |
| Log Out                   | Desktop    | ![Log Out Desktop](static/images/screenshots/logout-desktop.png)                 |
| Log Out                   | Mobile     | ![Log Out Mobile](static/images/screenshots/logout-mobile.png)                   |




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

