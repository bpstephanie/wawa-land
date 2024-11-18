# Wawa Land

Wawa Land is a community blog and events page for families with babies and children. Users can review events and leave comments on blog posts. Not only that, but users can also add their own blog posts to the site and are visible once they have been approved by the Wawa Land administration.

The inspiration of the name 'Wawa Land' is from the Quechua language word for 'child', 'baby', or 'infant'.

Welcome to <a href="https://wawa-land-04eebd0de719.herokuapp.com/">Wawa Land</a>

## Contents
* [**User Experience UX**](<#user-experience-ux>)
  * [Agile Methodology](<#agile-methodology>)
  * [User Stories](<#user-stories>)
  * [Site Structure](<#site-structure>)
  * [Design Choices](<#design-choices>)
    * [Typography](<#typography>)
    * [Colour Scheme](<#colour-scheme>)
    * [Wireframes](<#wireframes>)
* [**Features**](<#features>)
  * [Existing Features](<#existing-features>)
    * [Navigation Bar](<#navigation-bar>)
    * [Logged In Banner](<#logged-in-banner>)
    * [Footer](<#footer>)
    * [Messages](<#messages>)
    * [Home Page](<#home-page>)
    * [Blog](<#blog>)
      * [Add New Blog Post](<#add-new-blog-post>)
      * [Blog Post](<#blog-post>)
        * [Likes](<#likes>)
        * [Comments](<#comments>)
    * [Events Page](<#add-new-expense>)
      * [Event Detail](<#event-detail>)
        * [Reviews](<#reviews>)
    * [Profile](<#profile>)
      * [Edit Blog Post](<#edit-blog-post>)
    * [Register](<#register>)
    * [Log In](<#log-in>)
    * [Sign Out](<#sign-out>)
    * [Error Pages](<#error-pages>)
    * [Admin Panel](<#admin-panel>)
  * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Database**](<#database>)
* [**Testing**](<#testing>)
  * [Testing User Stories](<#testing-user-stories>)
    * [Site Owner](<#site-owner>) 
  * [Validation](<#validation>)
  * [Additional Testing](<#additional-testing>)
  * [Known Bugs](<#known-bugs>)
    * [Unresolved Bugs](<#unresolved-bugs>)
* [**Deployment**](<#deployment>)
  * [**To Deploy on Heroku**](<#to-deploy-on-heroku>)
  * [**To Deploy Locally on GitHub**](<#to-deploy-locally-on-github>)
  * [**To Fork the Project**](<#to-fork-the-project>)
  * [**To Clone the Project**](<#to-clone-the-project>)
  * [**Cloudinary**](<#cloudinary>)
  * [**PostgreSQL**](<#postgresql>)
* [**Credits**](<#credits>)
  * [**Content**](<#content>)
* [**Acknowledgements**](<#acknowledgements>)

# Features
  ## Existing Features

  - ## Site Wide Features

    - ### Navigation Bar
      Featured on all pages, the fully responsive navigation bar includes links to the Home page, Blog page, Events page, Log in and Register pages when the user is not logged in. Once the user logs in the Log in and Register links change to Sign Out and a user Profile page is made available. The nav bar allows the user to easily navigate to the main pages across the site.

      A decision was made to not put the Add Post page into the navigation bar as I wanted to make it clear that the Add Post function was only available for the blog.
    
      <details><summary>Navigation Bar whilst user is logged out - Desktop View</summary>

      ![Desktop view](static/images/screenshots/desktop-nav.png)

      </details>
      <details><summary>Navigation Bar whilst user is logged out - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-nav.png)

      </details>

      <details><summary>Navigation Bar whilst user is logged in - Desktop View</summary>

      ![Desktop view](static/images/screenshots/navbar-logged-in.png)

      </details>
      <details><summary>Navigation Bar whilst user is logged in - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-navbar-logged-in.png)

      </details>

      [Back To Top](<#contents>)
    
    - ### Logged In Banner
      Once a user has logged in, there is visual feedback in the form of a message stating their logged in status in a banner that is a slightly light shade than the navbar.

      <details><summary>Logged In Banner - Desktop View</summary>

      ![Desktop view](static/images/screenshots/loggedin-banner.png)

      </details>
      <details><summary>Logged In Banner - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-loggedin-banner.png)

      </details>

      [Back To Top](<#contents>)

    - ### Footer
      The footer section has 4 sections which include 'About', which explains a bit about the site, 'Social Media', with links to the relevant social media sites for Wawa Land, 'Contact Us', which includes a link to send us an email and the 'Copyright' section. The footer can be seen across all pages and is fully responsive.

      <details><summary>Footer - Desktop View</summary>

      ![Desktop view](static/images/screenshots/desktop-footer.png)

      </details>
      <details><summary>Footer - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-footer.png)

      </details>

      [Back To Top](<#contents>)

    - ### Messages
      Messages have been utilized to give users instant feedback for action they take. Success messages and error messages are distinguishable by their colour; green has been used for success and red for error messages.

      <details><summary>Success Messages - Desktop View</summary>

      ![Desktop view](static/images/screenshots/desktop-success-message.png)

      </details>
      <details><summary>Success Messages - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-success-message.png)

      </details>

      <details><summary>Error Messages - Desktop View</summary>

      ![Desktop view](static/images/screenshots/desktop-error-message.png)

      </details>
      <details><summary>Error Messages - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-error-message.png)

      </details>

      [Back To Top](<#contents>)


  - ## Pages

    - ### Home Page
      The homepage is the first page a user sees when coming to Wawa Land. The hero section includes a welcome message and a call to action to sign up. Below the hero section, the user can find out what to use Wawa Land for with navigable links to the Blog and the Event page. The cursor style changes when a user hovers over the respective sections, letting them know they are both links.

      <details><summary>Home Page - Desktop View</summary>

      ![Desktop view](static/images/screenshots/homepage-hero.png)
      ![Desktop view](static/images/screenshots/desktop-homepage.png)

      </details>
      <details><summary>Home Page - Mobile View</summary>

      ![Mobile view](static/images/screenshots/mobile-homepage-hero.png)
      ![Mobile view](static/images/screenshots/mobile-homepage.png)

      </details>

      [Back To Top](<#contents>)


    - ### Blog
      When a user clicks the 'Blog' in the navbar they are taken to the blog list page. At the top of the page there is a prompt for the user to add their own post. The button to take them to write their own post only appears to users who are logged in, if they are not they will be prompted to log in.
      
      Below, the user can see all the posts that are available to read on the site. The blog posts can be from any user and are displayed here once they have been approved by the Wawa Land administration. They are ordered with the newest appearing first. Users of the site (logged in or not) can click on a blog post title to be taken to read the full article. Only 6 posts will appear per page, users will be able to navigate through the pages of the blog to see all the content available.

      <details><summary>Add Post Prompt</summary>

      ![Logged in](static/images/screenshots/add-new-post.png)
      ![Logged out](static/images/screenshots/add-new-post-logged-out.png)

      </details>

      <details><summary>Blog Article List</summary>

      ![Blog Article List](static/images/screenshots/blog-posts.png)

      </details>

      [Back To Top](<#contents>)


      - #### Add New Blog Post
        To reach this page, a user needs to have clicked on 'Add Post' on the blog page. The user is prompted to add their own blog post by a form. They must give their post a title and a body. If a user attempts to submit a post without a title or a body an error message appears at the top as well as visual feedback that the fields are required.

        <details><summary>Add New Post Form</summary>

        ![Desktop](static/images/screenshots/desktop-add-post.png)
        ![Mobile](static/images/screenshots/mobile-add-post.png)

        </details>

        <details><summary>Visual Feedback for Invalid Form</summary>

        ![Invalid Title](static/images/screenshots/invalid-title.png)
        ![Invalid Feedback](static/images/screenshots/addpost-error-message.png)
        ![Invalid Feedback](static/images/screenshots/field-required.png)

        </details>
        
        [Back To Top](<#contents>)


      - #### Blog Post
        Each blog post is rendered on it's own page. All posts have the same format of an image, placeholder or user uploaded, the title, the author and date and time the post was written or updated. Underneath the blog post the user can 'like' or 'unlike' the post. Below the likes section and comment counter, the user can leave their own comment.

        <details><summary>Individual Blog Post</summary>

        ![Individual Blog Post](static/images/screenshots/post-detail.png)

        </details>
        
        [Back To Top](<#contents>)

        - ##### Likes
          Only logged-in users can 'like' or 'unlike' posts. For a successful 'like' a green success error message is shown at the top of the page. If a user 'unlikes' a post a red error message is shown. A red error message for 'unliking' was chosen as it may have been a mistake that the user clicked on the heart again, therefore I wanted to make the user aware the action they have taken. The likes show without the need for the page to be refreshed.

          Within the likes section, there is also a comment counter. The number of approved comments is shown.

          <details><summary>Likes and Comment Counter Section</summary>

          ![Likes and Comment Count Section](static/images/screenshots/likes-and-comment-count.png)

          </details>
          
          [Back To Top](<#contents>)

        - ##### Comments
          Only logged-in users can comment on a post. If the user is not logged-in, they are prompted to log in to leave a comment. The 'log in' is a link to take the user to the log in page.

          Once a user is logged in, they can view all users comments as well as their own unapproved comments. There are 'Edit' and 'Delete' buttons under the user's own comments. If they choose to edit their comment, the 'Leave Comment' section is populated with the user's comment they wish to change. Once the user clicks update, the comment is shown on the left side. If the user chooses to update a comment that was already approved, it will need to be approved again by the Wawa Land admin. The 'Delete' button will bring up a modal message confirming if the user would like to delete it. This is a precaution as the user may have accidentally clicked the delete button. If this is the case the user can close the delete confirmation message and nothing will happen. If the user chooses to delete the comment, it will be deleted from the database. This action cannot be undone.

          <details><summary>Comments Section</summary>

          ![Comments](static/images/screenshots/comments.png)

          </details>
          <details><summary>Edit Comment</summary>

          ![Delete Comment](static/images/screenshots/update-comment.png)

          </details>
          <details><summary>Delete Comment Modal</summary>

          ![Delete Comment](static/images/screenshots/delete-comment.png)

          </details>

          [Back To Top](<#contents>)

    - ### Events Page
      The events page show all events endorsed by Wawa Land. From the event list page users can see the name of the event, the age range it is suitable for and the date of the event. The events are in descending order where upcoming events are listed first. Users can click on the name of an event to be taken to the event detail page to read more about it.

      <details><summary>Events List</summary>

      ![Events List](static/images/screenshots/event-list.png)

      </details>

      [Back To Top](<#contents>)

      - #### Event Detail Page
        Each event listing is rendered on it's own page. All events have the same format of an image, the name, more information about the event, the price, the time and the date of the event. Currently all events can only be added by the Wawa Land administration. This is due to security, as events are for babies and children, it waws decided that user-added events could pose a risk. Underneath the event listing the user can leave a review for the event.

        <details><summary>Events Listing</summary>

        ![Events Listing](static/images/screenshots/event-detail.png)

        </details>

        [Back To Top](<#contents>)

        - ##### Reviews
          Only logged-in users can review an event. If the user is not logged-in, they are prompted to log in to leave a review. The 'log in' is a link to take the user to the log in page.

          Once a user is logged in, they can view all users reviews as well as their own unapproved reviews. There are 'Edit' and 'Delete' buttons under the user's own reviews. If they choose to edit their review, the 'Leave a Review' section is populated with the user's review they wish to change. Once the user clicks update, the review is shown on the left side. If the user chooses to update a review that was already approved, it will need to be approved again by the Wawa Land admin. The 'Delete' button will bring up a modal message confirming if the user would like to delete it. This is a precaution as the user may have accidentally clicked the delete button. If this is the case the user can close the delete confirmation message and nothing will happen. If the user chooses to delete the review, it will be deleted from the database. This action cannot be undone.

          <details><summary>Review Section</summary>

          ![Comments](static/images/screenshots/reviews.png)

          </details>
          <details><summary>Edit Review</summary>

          ![Delete Comment](static/images/screenshots/update-review.png)

          </details>
          <details><summary>Delete Review Modal</summary>

          ![Delete Comment](static/images/screenshots/delete-review.png)

          </details>

    - ### Profile
      The profile page is where the user can see all the posts they have written, published or unpublished, all their comments on posts, approved or awating approval and all their likes. It is from the profile page that a user can edit a post, update a comment or delete either.

      <details><summary>Profile Page - Posts Section</summary>

      ![Profile Page](static/images/screenshots/profile.png)

      </details>
      <details><summary>Profile Page - Comments Section</summary>

      ![Profile Page - Comments Section](static/images/screenshots/profile-2.png)

      </details>
      <details><summary>Profile Page - Likes Section</summary>

      ![Profile Page - Likes Section](static/images/screenshots/profile-likes.png)

      </details>

      [Back To Top](<#contents>)

        - #### Edit Blog Post
          The user is taken to this edit blog post page from the profile page. The title and body sections are pre-populated with the content of the post they want to edit. The user can use summernote features such as using 'bold' or 'italics' to name but a few. Once they have updated the post the user is redirected to the profile page.

          <details><summary>Edit Blog Post</summary>

          ![Edit Blog Post](static/images/screenshots/edit-blog-post.png)

          </details>

          [Back To Top](<#contents>)

    - ### Register
      On the Register page the user can create an account, optionally inputting their email address. If the user already has an account and visits this page they can navigate to the login page via a link.

      <details><summary>Register Page</summary>

      ![Register Page](static/images/screenshots/sign-up.png)

      </details>

      [Back To Top](<#contents>)

    - ### Log In
      On this page, users who have already created an account can log in. They can toggle to have their details remembered to avoid having to enter the information again.

      <details><summary>Login Page</summary>

      ![Login Page](static/images/screenshots/login.png)

      </details>

      [Back To Top](<#contents>)

    - ### Sign Out
      When a user clicks the log out in the navigation bar , the user is taken to this page where they can confirm they want to log out.

      <details><summary>Logout Page</summary>

      ![Logout Page](static/images/screenshots/logout.png)

      </details>

      [Back To Top](<#contents>)

    - ### Error Pages
      If a page is not found, the user will be shown this page.

      <details><summary>404 Error Page</summary>

      ![404 Error Page](static/images/screenshots/404-error.png)

      </details>

      [Back To Top](<#contents>)

    - ### Admin Panel
      The admin panel can be accessed by the superuser. Here in the admin panel, the superuser can view all users, blog posts, comments, events and reviews. It is via the admin panel that the Wawa Land team can approve comments and reviews and publish blog posts.

      The posts can be ordered by title, slug, status or created on date. The events can be ordered by title, slug or age-range.

      <details><summary>Admin Page</summary>

      ![Admin Page](static/images/screenshots/admin-page.png)

      </details>

      <details><summary>Admin - Posts Page</summary>

      ![Posts Page](static/images/screenshots/admin-posts.png)

      </details>

      <details><summary>Admin - Events Page</summary>

      ![Events Page](static/images/screenshots/admin-events.png)

      </details>

      [Back To Top](<#contents>)

  ## Future Features
  There are many more feature that I wanted to include in this project for ease of users.
  - Social Login
    Enhance the user sign-up experience by integrating social login options for example; Google and Facebook. This not only would decrease the sign up time but also boosts the chances of users completing their registration.

  - Search Bar
    This would most likely be the next functionality to add. Currently users have to click through the pages to asee all posts and events, however adding a search field would allow users to look for specific posts and/or events.

  - Tags 
    Adding category tags to events and posts would allow users to search for a category and see everything relating to that category.

  - Calendar View
    The events page would benefit fom having a calendar, whereby users would be able to select a date and be shown all the events happening on that day.
  
  - Saved Events / Saved Posts
    It would be benefical for users to be able to save posts they are interested in or want to read at a later date in their profile. It would also be beneficial for users to be able to save events to their profile. If these capabilities were added to Wawa Land, other users would also be able to see how many saves each post or event had which would indicate popularity.

  - Thumbs Up / Thumbs Down
    Similar to the like functionality on the blog posts, Wawa Land could have a 'thumbs up', 'thumbs down' rating system where users can let Wawa Land know what sorts of events they like more than others. This will help Wawa Land in the future to list more events the users of the site are interested in.

  - Tickets
    On each event, users would be able to click a link to buy a ticket on their respective site. The events that are listed by Wawa Land are a mixture of their own events and events in the local area they trust, therefore tickets to certain events need to be purchased elsewhere but by having a link on the event detail page, users would easily be able to purchase tickets.

  - Email Notifications
    Whenever a user saves an event they would recieve an email letting them know the event is coming up.

    [Back To Top](<#contents>)

# Technologies Used

* [Python3 + Django](https://www.python.org/)
* [HTML5](https://html.spec.whatwg.org/)
* [CSS](https://www.w3.org/Style/CSS/specs.en.html)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [PostgreSQL](https://www.postgresql.org/)
* [Cloudinary](https://cloudinary.com/) - used for online storage of static files.
* [Gitpod](https://www.gitpod.io/#get-started) - used for writing code, committing and pushing to [Github](https://github.com/).
* [Github](https://github.com/) - used for storing the repository and for version control.
* [Heroku](https://dashboard.heroku.com/) - used to deploy and host the project.
* [Lucid](https://dashboard.heroku.com/) - used to create the ERD model for Wawa Land.
* [CloudConvert](https://cloudconvert.com/png-to-webp) - used to convert images to  webp.
* [TinyPNG](https://tinypng.com/) - used to optimize images.
* [PEP8](https://peps.python.org/pep-0008/) - used to validate python code.


[Back To Top](<#contents>)

# Database
- I used Code Institute's PostgreSQL database for Wawa Land.
- I created an Entity Relationshop Diagram (ERD) using [Lucid](https://dashboard.heroku.com/) to plan my database.

![Entity Relationship Model for Wawa Land](static/images/screenshots/erd-model.png)

# Deployment

  ## To Deploy on Heroku
  The site was developed using [Gitpod](https://www.gitpod.io/#get-started). All commit messages were pushed to [Github](https://github.com/) using the GitPod terminal. The finished project was deployed in [Heroku](https://dashboard.heroku.com/).

  Before starting the process on [Heroku](https://dashboard.heroku.com/), you first need to enter 'pip3 freeze > requirements.txt' in the terminal in your IDE. This adds a list of dependencies to your requirements.txt file needed for deployment. Commit these changes and push to GitHub before you deploy.

  -  You can also update your 'requirements.txt' file once you have already deployed to Heroku, by entering 'pip freeze > requirements.txt'. Don't forget to commit your changes and push to GitHub.

  The process of deploying to [Heroku](https://dashboard.heroku.com/) is as follows:

  1. Log into [Heroku](https://dashboard.heroku.com/) (or create an account).

  <details><summary>Heroku Step 1</summary>
  
  ![Heroku Step 1](static/images/screenshots/heroku_one.png)

  </details>

  2. In the top right hand corner there is a button 'New' that releases a dropdown menu, where you need to click 'Create a new app'.

  <details><summary>Heroku Step 2</summary>
  
  ![Heroku Step 2](static/images/screenshots/heroku_two.png)

  </details>

  3. On the next page, you will need to add a name for your app and input what region you are in. Bear in mind that each app name is unique therefore you may need to try some different options out. Once you have decided on an app name and selected which region you are in. Click 'Create app'

  <details><summary>Heroku Step 3</summary>
  
  ![Heroku Step 3](static/images/screenshots/heroku_three.png)

  </details>

  4. On the next page, click the 'Settings' tab. Once you have clicked on the settings tab, click 'Reveal Config Vars' in the 'Config Vars' section. Next you will need to add values. For Wawa Land, three key value pairs were added:
      - KEY = "DISABLE_COLLECTSTATIC", VALUE = "1" Once the key and value input fields have been filled you have to click 'Add'.
      - KEY = "DATABASE_URL", the value is the url that was emailed to you when creating the databse. Then click 'Add'
      - KEY = "SECRET_KEY", the value is any random secret key containing numbers, letters and characters. You can use [Random Keygen](https://randomkeygen.com/) or invent your own. Then click 'Add'.

  <details><summary>Heroku Step 4 - Settings Tab</summary>
  
  ![Heroku Step 4 - Settings Tab](static/images/screenshots/heroku_four_settings.png)

  </details>

   <details><summary>Heroku Step 4 - Config Vars Section</summary>
  
  ![Heroku Step 4 - Config Vars Section](static/images/screenshots/heroku_four_config.png)

  </details>

  5. In your IDE terminal, you need to type the following code to install the project requirements:
    - pip3 install gunicorn~=20.1
    - pip3 install -r requirements.txt
    - pip3 freeze --local > requirements.txt

  6. Next, create an env.py file at the root level directory, which must containe the following:
    - import os

    - os.environ.setdefault("DATABASE_URL", "CI database URL")
    - os.environ.setdefault("SECRET_KEY", " Your secret key")

  7. Next, create a file at the root level directory called Procfile. In this file enter:
    -  web: gunicorn my_project.wsgi

  8. Next, in your settings.py file, set DEBUG = FALSE
    **YOU SHOULD ALWAYS SET DEBUG TO FALSE BEFORE DEPLOYING FOR SECURITY**

  9. Add ",'.herokuapp.com' " (without the double quotes) to the ALLOWED_HOSTS list in settings.py

  10. Next, add commit and push your code to [Github](https://github.com/).

  11. Next, on [Heroku](https://dashboard.heroku.com/), you need to go to the 'Deploy' tab. For 'Deployment Method', click 'GitHub'. Search for the repository name you want to deploy and then click connect.

  <details><summary>Heroku Step 11 - Deploy Tab</summary>
  
  ![Heroku Step 11 - Deploy Tab](static/images//screenshots/heroku_six.png)

  </details>

  <details><summary>Heroku Step 11 - Deployment Method</summary>
  
  ![Heroku Step 11 - Deployment Method](static/images/screenshots/heroku_six_deployment_meth.png)

  </details>

  <details><summary>Heroku Step 11 - Connect to GitHub</summary>

    Wawa Land has already been connected to Heroku so mine will look a little different from yours. However, where you can see 'App Connected to GitHub' on the image, you will see 'Connect to GitHub, next to that you'll be able to search for the repository you want to connect.

  ![Heroku Step 11 - Connect to Github](static/images/screenshots/heroku_six_connect.png)
  
  </details>


  12. Scroll down to the sections below, called 'Automatic Deploys' and 'Manual Deploy'. Here you need to choose which option best suits your project. Once selected, click 'Deploy Branch'.

  <details><summary>Heroku Step 12 - Deploy</summary>
  
  ![Heroku Step 12 - Deploy](assets/images/heroku_seven.png)

  </details>

  [Back To Top](<#contents>)




  ## To Deploy Locally on GitHub
  ## To Fork the Project
  ## To Clone the Project
  ## Cloudinary
  ## PostgreSQL
    
