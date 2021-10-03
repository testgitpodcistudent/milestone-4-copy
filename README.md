![Logo](/static/readme-assets/logo-readme.png)
# Data-Centric Project | product Website

# Table of Contents

1. [Overview](#overview)
2. [UX](#ux)
    * [Developer Goals](#developer-goals)
    * [User Stories](#user-stories)
    * [Design](#design)
    * [Concept & Font Choice](#concept-and-font-choice)
    * [Colours](#colours)
3. [Features](#existing-features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
    * [Django](#django)
    * [Coding Languages & Libraries](#coding-languages-and-libraries)
    * [Software](#software)
    * [Additional Tools](#additional-tools)
5. [Deployment](#deployment)
    * [GitPod Deployment](#gitpod-deployment)
    * [Heroku](#heroku)
6. [Testing](#testing)
7. [Credits](#credits)
    * [Acknowledgements](#acknowledgements)

<hr>
<hr>

## Overview

Placeholder text

The website is fully responsive, utilizing simple and colourful design language and an intuitive information structure.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# UX

## Developer Goals
* Create an easy-to-use e-commerce website.
* Allow the end-user (customer) to register an account, login, add products to their cart, and purchase them.
* Create an intuitive interface for the site administrator to add, delete and edit products.
* Allow the end user to search products by search term, sort by price and other factors, and view products based on category.
* Provide links to social media pages run by the site owner.
* Create an easy-to-use contact form for customers or potential customers to send messages to the site owner.

<hr> 

## User Stories
1. As a _site administrator_, I want to upload products to the site for the _end-user_ to view and purchase. I want to be able to edit and delete these products if needed.
2. As a _site administrator_, I want to sort the products into separate categories for ease of browsing.
3. As a _site administrator_, I want to ensure that only I can alter the content of the website.
4. As an _end-user_, I want to browse products relevant to me; including searching through them using search terms, sort by price, and view items in specific relevant categories.
5. As an _end-user_, I want to send an e-mail to the site owner about an order (or potential order).
   
### How does the website function to meet the needs of the user, as described in the user stories?
1. The _Add New product_, _Edit_ and _Delete_ functions enable the administrator to fulfill these Create, Update and Delete functions.
2. The site requires administrator _authentication_ to reveal the administrator features. This is done on the _"Admin Login"_ page.
3. The homepage displays all products on the site. The searchbar allows users to search products using a search term. The category links (_All Products, Laptops, Phones, Tablets_) allow users to view by category. The _Sort Products_ dropdown allows users to sort relevant products via different factors including cost.
    A preview of the products is shown; when clicked, the user is directed to the full product page.
4. The *Contact Us* link on the footer of each page directs the user to a functional Contact form which sends an e-mail to the site administrator's inbox.

[⇧ Back to Top](#table-of-contents)

<hr>

## Design
![AmIResponsive Screenshot](/static/readme-assets/responsive-screens.png)

* [Click here to view wireframes.](/static/readme-assets/wireframes.md) <br>

### Concept and Font Choice
The site is designed to appear clean, professional, and uncluttered while also appearing vibrant and welcoming.


- [Hover.CSS](https://ianlunn.github.io/Hover/) - CSS library used for hover effects on site buttons.
- [FontAwesome](https://fontawesome.com/) - Webfont library used for icons throughout the site.

### Colours

![Image scheme](/static/readme-assets/colours.png)

_Some examples of the colours as used throughout the site_

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Existing Features
The site's structure consists of
- **Homepage** which displays all products, as well as search and sort-by-category functionality. When logged in as admin, relevant control panel links are also displayed.
    This uses the *get_products* python function.
- **Admin Login** page which allows the user to authenticate themselves using a username and password, as well as **Logout** buttons.
    These utilize the *admin_login* and *logout* python functions.

    ![Admin Login](/static/readme-assets/admin.png)

    - _The admin-login page can be accessed by clicking the link at the bottom of each page._

    ![Admin features](/static/readme-assets/admin-features.png)
    - _Once logged in as an admin, links to the content-management features are displayed at the top of the product list._
- **product Page** for each product which is loaded when a product is clicked on the homepage..
- **Add New product** - used to add a new product to the database.
- **Delete product** allows the admin to delete the given product.
- **Edit product** allows the admin to edit the selected product.
    ![Edit and delete buttons](/static/readme-assets/edit-delete.png)
    - _Edit and Delete buttons as displayed when logged in as admin_
- **Messages** display a simple message to the user confirming actions such as cart updates, product deletions, login actions etc.
    ![Messages](/static/readme-assets/flash-message.png)

**Developer Notes**
- If you encounter the following error at any point running terminal commands in local deployment: ``` django.db.utils.OperationalError: FATAL:  role "qwmrksyzdlafcq" does not exist ``` , running ``` unset PGHOSTADDR ``` and re-trying the previous command will allow you to continue.

- Ensure your IDE Python linter is set to flake8, or you will encounter false errors related to object models not existing.

<hr>

## Future Features


[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Technologies Used

## Django
The website is built using [Django](https://www.djangoproject.com/).


## Coding Languages and Libraries

* [HTML5](https://www.w3.org/standards/webdesign/htmlcss.html) - Used on all pages for page structure and content.
* [CSS](https://www.w3.org/standards/webdesign/htmlcss.html) - Used on all pages for content styling and placement.
* [BootStrap 4.4.1](https://getbootstrap.com/) - Front end CSS framework.
* [jQuery](https://jquery.com/) - JavaScript library used for intilization of BootStrap features.
* [Python](https://www.python.org/) - used throughout site alongside Flask-PyMongo.

## Software

* [GitPod](https://www.gitpod.io/) - Code editor used throughout development to write code.
* [GIMP Image Editor](https://www.gimp.org/) - Used throughout to crop and edit images.

## Additional Tools

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes in the design process.
* [Responsively](https://responsively.app/) - Used to test site responsiveness throughout development.
* [Am I Responsive](http://ami.responsivedesign.is/) - Browser-based preview any website's responsiveness. Screenshot featured in readme.md 
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Used throughout development to view the website, test features, test JavaScript, and test responsiveness. 
* [ScreenToGif](https://www.screentogif.com/) - Used to create GIF screen-recordings for readme and testing purposes

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Deployment 

**Required:**

- Python3
- [GitHub](https://github.com/) account
- [GitPod](https://gitpod.io/workspaces) account (for local deployment)
- [GitPod browser extension](https://www.gitpod.io/docs/browser-extension/)
- [Heroku](https://id.heroku.com/login) account

[⇧ Back to Top](#table-of-contents)

<hr>

## GitPod Deployment

1. Login to GitHub, and navigate to the [repository](https://github.com/RoryBr1/Milestone-3)
2. Click on the GitPod button at the top right.
3. Install all requirements; in the terminal of your GitPod workspace, type  
   ``` pip3 install -r requirements.txt ```

4. Run the app by typing ``` python3 manage.py runserver --insecure ``` into the terminal. *Note: if you do not add ``` --insecure ``` to the end of the command, images and other static files will fial to load.

[⇧ Back to Top](#table-of-contents)

<hr>

## Heroku

1. In the GitPod terminal, type ``` pip3 freeze -- local > requirements.txt `` . 
2. In the terminal, type ``` python3 app.py > Procfile ``` . This will create a _Procfile_, which tells Heroku which file to run when the site is accessed.
3. In the _Deploy_ tab on Heroku, click "Connect to GitHub" and select the relevant repository. Click "Connect".
4. Go to the _Settings_ page in Heroku and click on "Config Vars". Click on "Reveal Config Vars".
    - Enter the _IP, SECRET_KEY, MONGO_URI,_ and _MONGO_DBNAME_ as contained in your _env.py_ file.
5. Go to the _Deploy_ tab in Heroku, scroll down and click "Enable Automatic Deploys". Click "Deploy Branch".

Once the app is deployed, click "Open App" in Heroku on the project page. The project should be successfully deployed and will update automatically when new GitHub commits are made.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Testing
[Click here](/static/readme-assets/testing.md) to view the Testing.md file.

<hr>


# Credits


[⇧ Back to Top](#table-of-contents)

<hr>


## Acknowledgements



[⇧ Back to Top](#table-of-contents)