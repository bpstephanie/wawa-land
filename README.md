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
      * [Blog Post](<#blog-post>)
        * [Likes](<#likes>)
        * [Comments](<#comments>)
      * [Add New Blog Post](<#add-new-blog-post>)
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
  * [Languages](<#languages>)
  * [Frameworks, Libraries and Packages](<#frameworks-libraries-and-packages>)
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

  - ### Navigation Bar
    Featured on all pages, the fully responsive navigation bar includes links to the Home page, Blog page, Events page, Log in and Register pages when the user is not logged in. Once the user logs in the Log in and Register links change to Sign Out and a user Profile page is made available. The nav bar allows the user to easily navigate to the main pages across the site.

    A decision was made to not put the Add Post page into the navigation bar as I wanted to make it clear that the Add Post function was only available for the blog.
  
    <details><summary>Navigation Bar whilst user is logged out:</summary>
    
    ![Desktop view](static/images/screenshots/desktop-nav.png)
    ![Mobile view](static/images/screenshots/mobile-nav.png)
    
    </details>

    <details><summary>Navigation Bar whilst user is logged in:</summary>
    
    ![Desktop view](static/images/screenshots/navbar-logged-in.png)
    ![Mobile view](static/images/screenshots/mobile-navbar-logged-in.png)
    
    </details>

    [Back To Top](<#contents>)
  
  - ### Logged In Banner
    Once a user has logged in, there is visual feedback in the form of a message stating their logged in status in a banner that is a slightly light shade than the navbar.

    <details><summary>Logged In Banner</summary>
    
    ![Desktop view](static/images/screenshots/loggedin-banner.png)
    ![Mobile view](static/images/screenshots/mobile-loggedin-banner.png)
    
    </details>

    [Back To Top](<#contents>)

  - ### Footer
    The footer section has 4 sections which include 'About', which explains a bit about the site, 'Social Media', with links to the relevant social media sites for Wawa Land, 'Contact Us', which includes a link to send us an email and the 'Copyright' section. The footer can be seen across all pages and is fully responsive.

    <details><summary>Footer</summary>
    
    ![Desktop view](static/images/screenshots/desktop-footer.png)
    ![Mobile view](static/images/screenshots/mobile-footer.png)
    
    </details>

    [Back To Top](<#contents>)

  - ### Messages
    Messages have been utilized to give users instant feedback for action they take. Success messages and error messages are distinguishable by their colour; green has been used for success and red for error messages.

    <details><summary>Success Messages</summary>
    
    ![Desktop view](static/images/screenshots/desktop-success-message.png)
    ![Mobile view](static/images/screenshots/mobile-success-message.png)
    
    </details>

    <details><summary>Error Messages</summary>
    
    ![Desktop view](static/images/screenshots/desktop-error-message.png)
    ![Mobile view](static/images/screenshots/mobile-error-message.png)
    
    </details>

    [Back To Top](<#contents>)

  - ### Home Page
    The homepage is the first page a user sees when coming to Wawa Land. The hero section includes a welcome message and a call to action to sign up. Below the hero section, the user can find out what to use Wawa Land for with navigable links to the Blog and the Event page. The cursor style changes when a user hovers over the respective sections, letting them know they are both links.

    <details><summary>Home page</summary>

    ![Desktop view](static/images/screenshots/homepage-hero.png)
    ![Desktop view](static/images/screenshots/desktop-homepage.png)
    ![Mobile view](static/images/screenshots/mobile-homepage-hero.png)
    ![Mobile view](static/images/screenshots/mobile-homepage.png)
    
    </details>

    [Back To Top](<#contents>)

  - ### Blog
    When a user clicks the 'Blog' in the navbar they are taken to the blog list page. At the top of the page there is a prompt for the user to add their own post. The button to take them to write their own post only appears to users who are logged in, if they are not they will be prompted to log in.
    
    Below, the user can see all the posts that are available to read on the site. The blog posts can be from any user and are displayed here once they have been approved by the Wawa Land administration. They are ordered with the newest appearing first. Only 6 posts will appear per page, users will be able to navigate through the pages of the blog to see all the content available.

    <details><summary>Add Post Prompt</summary>

    ![Logged in](static/images/screenshots/add-new-post.png)
    ![Logged out](static/images/screenshots/add-new-post-logged-out.png)
    </details>

    <details><summary>Blog Article List</summary>

    ![Blog Article List](static/images/screenshots/blog-posts.png)
    </details>

    [Back To Top](<#contents>)

  - ### Events Page 
  [Back To Top](<#contents>)

  - ### Profile
  [Back To Top](<#contents>)

  - ### Register
  [Back To Top](<#contents>)

  - ### Log In
  [Back To Top](<#contents>)

  - ### Sign Out
  [Back To Top](<#contents>)

  - ### Error Pages
  [Back To Top](<#contents>)

  - ### Admin Panel
  [Back To Top](<#contents>)