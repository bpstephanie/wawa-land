# Testing

## Validator Testing

Wawa Land has been thoroughly tested. All the code has been run through the [W3C HTML Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JSHint JavaScript Validator](https://jshint.com/). 

- ### HTML

| Page                    | Screenshot                                                                             | Notes    |
|-------------------------|----------------------------------------------------------------------------------------|----------|
| Home                    |![Home Page](static/images/screenshots/html-index.png)                                  | PASS     |
| Blog - Logged out       |![Blog - Logged Out](static/images/screenshots/html-blog-loggedout.png)                 | PASS     |
| Blog - Logged in        |![Blog - Logged In](static/images/screenshots/html-blog-loggedin.png)                 | PASS     |
| Blog Post - Logged out  |![Blog - Logged Out](static/images/screenshots/html-blog-post-loggedout.png)          | The code the validator is referring to is code which has been integrated by Django for the comment functionality and not written by me. The '<p>' tag cannot be deleted by me.     |
| Blog Post - Logged in   |![Blog - Logged In](static/images/screenshots/html-blog-post-logged-in.png)                 | The code the validator is referring to is code which has been integrated by Django for the comment functionality and not written by me. The id is specific to each review and the '<p>' tag cannot be deleted by me.     |
| Event List             |![Event](static/images/screenshots/html-event-list.png)                 | PASS     |
| Event Listing - Logged out          |![Event](static/images/screenshots/html-event-listing.png)                 | The code the validator is referring to is code which has been integrated by Django for the review functionality and not written by me. The id is specific to each review and the '<p>' tag cannot be deleted by me.   |
| Event Listing - Logged in          |![Event](static/images/screenshots/html-event-listing-loggedout.png)                 | The code the validator is referring to is code which has been integrated by Django for the review functionality and not written by me. The '<p>' tag cannot be deleted by me.   |
| Add Post      |![Add Post](static/images/screenshots/add-post-1.png) ![Add Post](static/images/screenshots/add-post-2.png)                | The code validator is referring to errors in code that have been integrated by Django that add Summernote to the body field. I cannot amend this code.      |
| Profile       |![Profile](static/images/screenshots/html-profile.png)                 | The code the validator is referring to is code which has been integrated by Django for the posts and comments functionality and not written by me. The '<p>' tag cannot be deleted by me.     |
| Edit Post       |![Edit Post](static/images/screenshots/html-edit-post-1.png) ![Edit Post](static/images/screenshots/html-edit-post-2.png)               | The code validator is referring to errors in code that have been integrated by Django that add Summernote to the body field. I cannot amend this code.     |
| Login          |![Login](static/images/screenshots/html-log-in.png)                                  | PASS     |
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
| Login                    | Desktop    | ![Login Desktop](static/images/screenshots/login-desktop.png)                    |
| Login                    | Mobile     | ![Login Mobile](static/images/screenshots/login-mobile.png)                      |
| Logout                   | Desktop    | ![Logout Desktop](static/images/screenshots/logout-desktop.png)                 |
| Logout                   | Mobile     | ![Logout Mobile](static/images/screenshots/logout-mobile.png)                   |


#### Future Improvements for Lighthouse Testing




## Manual Testing
- Manual testing was carried out on local and deployed sites.

| Location     | Feature                              | Expected Outcome                                 | Pass/Fail|
|--------------|--------------------------------------|--------------------------------------------------|----------|
| Header       | Home button                          | Takes user to home                               |  PASS    |
| Header       | Blog button                          | Takes user to blog                               |  PASS    |
| Header       | Events button                        | Takes user to events page                        |  PASS    |
| Header       | Register button                      | Takes user to sign up page                       |  PASS    |
| Header       | Login button                         | Takes user to login page                        |  PASS    |
| Header       | Logout button (for logged in users) | Takes user to logout page                       |  PASS    |
| Header       | Profile button (for logged in users) | Takes user to profile page                       |  PASS    |
| Home page    | Hero section - sign up link (for logged out users)         | Takes user to sign up page                       |  PASS    |
| Home page    | Read our blogs (link)..              | Takes user to blog page                          |  PASS    |
| Home page    | Attend our events (link)..           | Takes user to events page                        |  PASS    |
| Blog page    | Log in to write a post (for logged out users)          | Takes user to login page                        |  PASS    |
| Blog page    | Add post button                      | Takes user to add post page                      |  PASS    |
| Blog page    | Post listings                        | When a post title is clicked it takes user to individual blog post page                        |  PASS    |
| Blog page    | Next button                        | If there are more than 6 posts then a 'next' button will appear for users to click through different post pages                        |  PASS    |
| Blog page    | Prev button                        | If there are more than 6 posts, on page 2 and onwards a 'prev' button will appear for users to click through different post pages                        |  PASS    |
| Blog Detail page    | Like button                      | When clicked, a like is registered and success message is shown to user                      |  PASS    |
| Blog Detail page    | Like button                      | If the user has previously liked, When clicked again, a like removal is registered and error message is shown to the user                      |  PASS    |
| Blog Detail page    | Comment counter                      | When any user's comment has been approved, the comment counter increases by one                      |  PASS    |
| Blog Detail page    | Leave comment field empty                    | If the user leaves an empty comment but clicks the submit button, the user is prompted to fill in the comment                      |  PASS    |
| Blog Detail page    | Leave comment                      | When the user leaves a comment, the comment can be seen in the comments section on the left                      |  PASS    |
| Blog Detail page    | Unapproved comments                      | The user can see their unapproved comments faded out                      |  PASS    |
| Blog Detail page    | Approved comments                      | All users can see their approved comments from all users                      |  PASS    |
| Blog Detail page    | Edit button on comments                      | When clicked, the user can update their own comments and see the reflected change instantly                      |  PASS    |
| Blog Detail page    | Delete button modal on comments                      | When clicked, a delete confirmation modal is shown to the user confirming whether or not they would like to delete their comment                      |  PASS    |
| Blog Detail page    | Delete button in modal                     | When clicked, the users' comment is permanently deleted from the database                      |  PASS    |
| Add Post page    | Leave title field empty                     | If the user leaves an empty title but clicks the submit button, the user is prompted to fill in the title                     |  PASS    |
| Add Post page    | Leave body field empty                     | If the user fills in the title field but leaves an empty body and clicks the submit button, the user is shown an error message at the top and 'This field is required' appears on the form                     |  PASS    |
| Add Post page    | Add image                     | If the user adds their own image to the post, it is shown on the blog post when the post has been approved by the administration                     |  PASS    |
| Events page      | Event listings                    | When an event name is clicked it takes user to individual event listing page                     |  PASS    |
| Events page    | Next button                        | If there are more than 9 event listings then a 'next' button will appear for users to click through different event pages                        |  PASS    |
| Events page    | Prev button                        | If there are more than 9 event listings, on page 2 and onwards a 'prev' button will appear for users to click through different event pages                        |  PASS    |
| Event Detail page    | Review counter                      | When any user's review has been approved, the review counter increases by one                      |  PASS    |
| Event Detail page    | Leave review                      | When the user leaves a review, the review can be seen in the reviews section on the left                      |  PASS    |
| Event Detail page    | Unapproved reviews                      | The user can see their unapproved reviews faded out                      |  PASS    |
| Event Detail page    | Approved reviews                      | All users can see their approved reviews from all users                      |  PASS    |
| Event Detail page    | Edit button on reviews                      | When clicked, the user can update their own reviews and see the reflected change instantly                      |  PASS    |
| Event Detail page    | Delete button Modal on reviews                      | When clicked, a delete confirmation modal is shown to the user confirming whether or not they would like to delete their review                      |  PASS    |
| Event Detail page    | Delete button in modal                     | When clicked, the users' review is permanently deleted from the database                      |  PASS    |
| Profile page    | Published posts section                     | All the users' published posts are listed in this section                      |  PASS    |
| Profile page    | Unpublished posts section                     | All the users' unpublished posts are listed in this section                      |  PASS    |
| Profile page    | Approved comments section                     | All the users' approved comments are listed in this section                      |  PASS    |
| Profile page    | Comments awaiting approval section                   | All the users' comments awaiting approval are listed in this section                      |  PASS    |
| Profile page    | Likes section                 | All the users' likes on posts are listed in this section                      |  PASS    |
| Profile page    | Post edit button                 | When clicked, the user is taken to the edit post page                      |  PASS    |
| Profile page    | Post delete button                 | When clicked, the delete confirmation modal is opened and the user can confirm permanent deletion of the post                      |  PASS    |
| Profile page    | Comment edit button                 | When clicked, the edit comment modal is opened and the user can update their comment                      |  PASS    |
| Profile page    | Edit comment modal save changes button                 | When clicked, the user is taken to the post the comment was made on                      |  PASS    |
| Profile page    | Comment delete button                 | When clicked, the delete confirmation modal is opened and the user can confirm permanent deletion of the comment and is then taken to the post the comment was made on                     |  PASS    |
| Edit Post page    | Empty title field                     | If the user leaves an empty title but clicks the submit button, the user is prompted to fill in the title                     |  PASS    |
| Edit Post page    | Empty body field                     | If the user fills in the title field but leaves an empty body and clicks the submit button, the user is shown an error message at the top and 'This field is required' appears on the form                     |  PASS    |
| Edit Post page    | Add image                     | If the user adds their own image to the post, it is shown on the blog post when the post has been approved by the administration                     |  PASS    |
| Login page    | Sign in button                    | If the user clicks the sign in button with an unknown/wrong username or password, the user will be prompted to enter a correct username/password combination                     |  PASS    |
| Login page    | Sign in button                    | If the user clicks the sign in button with an known username and password, the user will be signed in                    |  PASS    |
| Register page    | Sign up button                    | If the user clicks the sign up button with an unknown/wrong username or password, the user will be prompted to enter a correct username/password combination                     |  PASS    |
| Register page    | Sign up button                    | If the user enters a username which doesn't comply with the criteria they will not be registered and will be prompted to enter a password which does comply                    |  PASS    |
| Register page    | Sign up button                    | If the user enters a username and password which complies with the criteria they will be registered                    |  PASS    |
| Logout page    | Logout button                    | If the user clicks the logout button they will be logged out                    |  PASS    |


## User Story Testing
| User Story                                                                                                       | Pass/Fail|
|------------------------------------------------------------------------------------------------------------------|----------|
| As a **developer** I can **design wireframes** so that I can **see the project's layout and use it as a reference when designing pages.** | PASS     |
| As a **user** I can **sign up to the site** so that I can **view the content available to users.**               | PASS     |
| As a **user** I can **login to my account** so that I can **view the content available to users.**               | PASS     |
| As a **user** I can **click on blog** so that I can **see all the blog posts.**                                  | PASS     |
| As a **user** I can **click on any blog post snippet** so that I can **read all the content.**                   | PASS     |
| As a **site admin** I can **create, read, update and delete posts** so that I can **manage my blog content.**    | PASS     |
| As a **site admin** I can **create, read, update and delete events** so that I can **manage my events content.** | PASS     |
| As a **developer** I can **deploy my project to Heroku** so that it **can be accessed by users on the internet.**| PASS     |
| As a **user** I can **click on events** so that I can **see all the events listed.**                             | PASS     |
| As a **user** I can **click on any event listing** so that I can **read all the details.**                       | PASS     |
| As a **user** I can **see what other users' opinions of events** so that I can **judge what type of events to go to.**| PASS     |
| As a **site user** I can **leave comments on a post** so that I can **be involved in the conversation.**         | PASS     |
| As a **site user** I can **leave reviews on an event** so that I can **be involved in the conversation.**        | PASS     |
| As a **user** I can **add my own blog post** so that I can **share my knowledge with the community.**            | PASS     |
| As a **user** I can **delete my draft blog post** so that I can **remove it so it is not shared with the community.**| PASS     |
| As a **user** I can **see all the posts I have written, published and unpublished, all my comments, reviews and likes** so that I can **keep track of all my interactions with the site.**| PASS     |

## Additional Testing
The site was also tested using [Wave](https://wave.webaim.org/). There are no errors howvever there are 4 alerts including three possible headings in the footer and a redundant link. These have not be changed because the footer is not intended to have headings and the redundant link is an alternative home link to the logo link. The results were as follows:

![Wave Summary](static/images/screenshots/wave-summary.png)
![Wave Details and Heading Alerts](static/images/screenshots/wave-alerts-1.png)
![Wave Redundant Link Alert](static/images/screenshots/wave-alerts-2.png)



## Bugs

### Fixed Bugs
- When a user wanted to edit their review on an event, both the title and body fields content were being populated in both fields. This was due to an error in my JavaScript code where both elements were under the same variable meaning they were indistinguishable. That has been fixed now and is no longer a problem.

- The Summernote field on the Add Post/Edit Post pages was not responsive on smaller screens. Code was added to the setting.py file to make this field responsive.

### Known Bugs
On the register page, when a user's password does not comply with the criteria, the error message is not centered. The same bug occurs on the login page, the error message when a user's credentials don't match those on the system is not centered.

[Go Back To README.md](README.md)



