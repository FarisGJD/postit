# POST{it}

[View Live Website Here](https://postit-fd.herokuapp.com/)

***
# Introduction
POSTIT is a social media, internet/discussion forum or message board where users can hold conversations in the form of posted messages.  Each post acts as an interactive digital channel that facilities the creation and sharing of information, ideas, interests and other forms of expression through virtual communities and networks. This differs from chat rooms which allow you to communicate with people in real time whereas forums are suited for discussion where not all the participants have to be online at the same time. 

POSTIT uses a hierarchical or tree-like structure where a user creates an initial post to start a discussion. In this case a post is a user-submitted message enclosed into a block containing the user’s details, information about said post such as text and the date and time it was submitted. The original post otherwise known as a thread starter is then responded to by other users through posts of their own. 

These collections of messages then form a thread otherwise known as a topic, where posts appear as block one after another from oldest to newest. A thread is defined by a title, an additional description that may summarise the intended discussion and an opening or original post which opens whatever dialogue or make whatever announcement or reply to said post. Posts that follow in the thread are meant to continue discussion about the original post, or respond to other replies. 

The users of POSTIT can be divided into registered and guest accounts. The latter can only read posts/threads whereas the former in addition to can create, update and delete their own archived posts. Logged in users can also like/dislike and comment on other posts. Finally, admins will be able to moderate posts as to filter out objectionable content. 

***
# Development Planes 
## Strategy

POST{it} is intended to be used as a platform for discussion between strangers, friends and communities. Users will be able to see the latest site-wide posts on the home page while having a more detailed look and the ability to comment on other people’s posts when clicked on. Furthermore, each user has a unique profile page in which their own posts are stored. All these features are in a bid to make POST{it} the new ‘town square’ and place for discussion. 

**The Sites Ideal User** 
-	People who want to share their ideas with a broader community 
-	People who want to discuss topics in a relaxed and non-time sensitive manner (.i.e. not instant messaging)
-	People who want a place where they can store their ideas
-	

**Site Goals** 
-	Provide users with a place for friendly and safe discussion 
-	Provide users the ability to share their own thoughts 
-	Provide users the ability to connect with one another 

**EPICS & User Stories** 

A total of 9 epics were created which branched off into 15 user stories each with several tasks. The details for each epic, user story and task can be found within the projects tab of the Postit repository in GitHub. 

***
# The Scope Plane 
POST{it} initial public offering is to deploy  a minimal viable product in terms of creating, reading, updating and deleting posts. The strategy was devised through an agile methodology based on the aforementioned epics and user stories. 

**Content Requirements & Funtional Specifications**
-	Kitschy design based around the name Postit therefore the background will be a cork board and each post is presented as a postit note 
-	Users can create and manage their accounts, each with its own constraints and privileges 
-	Profile page where users can store and manage their posts 
-	Site must allow the user to navigate through intuitively 
-	Site must allow users to perform basic crud functionality 
-	Site must allow users to comment on posts 
-	Site must allow users to view a detailed post 
-	All view functionality must link to the appropriate URL 
-	Accessible to variety of users through a miraid of devices 

***
# Structure

From the users side the site will implement a hierarchical tree structure but from the developers side a Model View Template architecture is used to create and connect all the components. This is in a bid to offer the user a seamless and enjoyable experience.  

***
# Skeleton 
Balsamic was used to create wireframes that acted as the visual foudnation to the site which informed the logical steps that needed to be taken. Since an MVT structure was used each part of the framework was interconected thus determining the skeletons potential. 

**Database Schema** 

Since this was phase one of the sites roll out strategy only two models were used to keep things simple, one to handle the users posts and the other comments. Since allauth was used, the need to build a custom user model was forgone since it handled that side on its own. The database schema was formulated using DrawSQL. 

***
# Surface

**Design** 

As previously stated, the design behind Post{it} comes from its namesake. This made the overall theme and styling simple, making the user immediately aware of the core concept behind it. 

**Typography** 

The main fonts used for the site were Cabin Sketch and Lorinda Sketch which are a free hand, drawing style font. This means that it could have some device/browser compatibility issues which is why the fallback fonts of Raleway, Roboto and sans-serif were also used. 

**Imagery**

To give the feel of a cork board a high resolution image of one was used as the background for the entire site. Postit notes and pins were created using custom CSS and a border was added as a garnish for the create-post form. 

***
# Features

**Base.html** 

***Header*** 

Consists of a logo, navigation menu and call to action all of which allow the user to get a feel of the site, access its different pages and most importantly create an account. 

***Footer***

Gives the user opportunity to check out Post{it} social media accounts as well as contact information. 

**index.html** 

This is the home page where the user can read the latest posts. It is important as it sets the stage for the next feature which is one of the most important. 

**full-thread.html**

Allows the user to get a detailed view of the post they are interested in as well as creating a dialogue between individuals which is the main goal behind Post{it}


**create-postit.html** 

Another one of the most important parts of the site which allows users to engage with the site itself thus setting them up for communication between other users. 

**profile.html**

Allows the user to view and manage the posts they have created which gives them 50% of the CRUD functionality 

***update.html***

Redirects the user to a prepopulated form in which they can edit the post they have chosen to update. 

***delete***

Although not a template in its own right, it gives the user the ability to easily delete its respective post. 

**allauth**

Another important features which allows the user to create and manage their account with Post{it} which in turns gives them more or less access to the overall site. 

**Features To Implement**

-	Likes 
-	Image, video & audio uploads 
-	Organise posts through user generated categories such as NSFV, MEME, GIFS etc…
-	Search bar to sift through posts 
-	Increased functionality in the profile page 

***
# Technologies Used 
**Languages** 
- HTML5
- CSS3 
- JavaScript 
- Python 

**Framewroks**
- Django
    - allauth
    - gunicorn 
    - psycopg2 
    - dj-database 

**Database** 
- Heroku Postgres

**Tool** 
- Cloudinary 
- Heroku 
- Gitpod 
- Git 
- GitHub
- Balsamic 
- Favicon 
- Lighthouse 
- W3C Markup 
- W3C Validators 
- W3C Jigsaw 
- PEP8 

***
# Search Engine Optimization
SEO techniques wwere used to improve the quality and quanitity of traffic towards POST{it} such as: 
- Keywords and Meta Description tags within the base.html temaplte creating better relationships between the site pages and serach engies.
- Crawlable Links. 

***
# Bugs & Issues

Using an MVT framework coupled with an Agile methodology proved to be extremely successful in the development of the site since few  bugs & issues were encountered. This coupled with Django’s in-built debugger made for a rapid and enjoyable creations process. If any issues were to be brought up it would be a lack of experience with templating languages. 

***
# Testing 

Both manual and automated tests were implemented to test the logic, responsiveness, compatibility, validation, feedback and confirmation during and after completion. Automated tests were implemented using test cases within project. Manual tests consisted of device and cross browsers compatibility as well as asking others. 

**HTML Validation** 

W3C Markup Validation Service was implementd to validate the HTML/tempaltes of the websites. The only errors that came about were due to tempalte variables being inlcuded in the HTML and the use of a base.html import which meant all but one of the pages had head tags. 

**CSS Validation** 

W3C Jigsaw was used to validate the CSS and returned no errors. 

**JavaScript Validation** 

JSHint Analysis Tool was used for the JavaScript and not significant issues were found except for missing semi colons and the use of ES6 arrow function. 

***
# Deployment


The app was deployed on Heroku by following these steps: 

**Heroku**

1.	Create Heroku app 
-	Head to the Heroku Website
-	Create an account by entering the specified details such as email address and password 
-	Activate account through email authentication 
-	Head back to Heroku and click new button which will reveal a drop down menu, select new app from there 
-	Enter a unique app name and select the region closest to you 
-	Click on create app 
2.	Creating The Database
-	In the dashboard head over to the resource tab. 
-	Scroll down and click on Add-Ons, searching for and selecting the Heroku Postgres database in this case
3.	Setting Environment Variables
-	Heading to the settings tab and scroll down to Reveal Config Vars section where you will input your environment variables 
4.	Add Heroku Hostname to Allowed_Hosts  in your workspace settings.py file 
5.	Set up Cloudinary for media and static files storage 
-	Create cloudinary account and copy you’re your API  environment variable and paste it into the Config Vars in Heroku with the key type of CLOUDINARY_URL. 
6.	Create Procfile in top level directory
7.	Heroku Deployment 
-	Click on deply tab on Heroku 
-	For deployment method click GitHub and connect your GitHub account. 
-	In the search box search for your repository name and then link the two
-	Optional you can either choose manual deployment from Heroku or automatic which will deploy based on your workspace git pushes
8.	Final Deployment 
-	When you have completed the development process in the settings.py file change DEBUG to False. 

**Forking The Repositroy** 
-	Navigate to the repository on GitHub
-	 Click on the fork button in the upper right-hand corner

**Cloning The Repository** 
-	Navigate to the repository on GitHub 
-	Click the code dropdown menu 
-	Selecting your cloning preference such as HTTPS, SSH, or GitHub CLI and then click copy to copy the URL to your clipboard
-	Open Git Bash 
-	Change the currently working directory to one which you want the cloned one. 
-	Type git clone and paste the URL from the clipboard 
-	Enter to create your clone.

***
# Credits
- CI DBMS walkthrough Project 
- CI Hello Django walktrhough Project 
- CI I Think Before I Blog Walkthrough Project 

# Notes 

Unfortunately, my GitPod workspace which had 90% of my work completed was corrupted meaning I lost a huge amount of work in terms of my project and README as you will be able to tell from my repo commits and pushes. I have had to restart all over again and complete everything within a week. 

