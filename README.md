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

**Header** 

Consists of a logo, navigation menu and call to action all of which allow the user to get a feel of the site, access its different pages and most importantly create an account. 

**Footer**

Gives the user opportunity to check out Post{it} social media accounts as well as contact information. 









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
