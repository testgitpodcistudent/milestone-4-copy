[ 🠔 Back to ReadMe ](../readme.md)

# Table of Contents 
1. [Code Validators](#code-validators)
    - [Python](#python)
    - [JavaScript](#javascript)
    - [HTML](#html)
2. [User Stories](#user-stories)
3. [Feedback](#feedback)

<hr>
<hr>

# Code Validators
## Python
* All Python files are PEP8 compliant with a few exceptions. In any case where a PEP8 "Line too long" error is present, this has been left so intentionally as splitting the line causes major development issues.

<hr>

## JavaScript
* The _script.js_ file passed the [JavaScript Validator](https://beautifytools.com/javascript-validator.php) when "jQuery" option is selected, without warnings or errors.

<hr>

## HTML
[W3C HTML validator](https://validator.w3.org/nu/)

* On deployed site, right-click and select "View Page Source". This is the final, rendered HTML. This HTML for each page was put through the HTML validator. Each page's HTML passed with no errors. Some warnings may be present, and a development decision has been made not to fix these at this time.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# User Stories

Each of the user stories was used as a starting point to test each of the features on the site, and ensure that they are accessible and work correctly.
These were tested on both mobile and desktop resolutions.

1. **As a _site administrator_, I want to upload products to the site for the _end-user_ to view and purchase. I want to be able to edit and delete these products if needed.**
    
    ✔  Once logged in, the _Admin_ menu button appears.

    ✔  The _Manage Products_ button directs the user to the relevant page, where an intuitive form allows them to add a new product.

    ✔  Once the form is submitted, a confirmation flash message appears, and the product is successfully added to the site.

    ✔  _Edit_ and _Delete_ buttons are visible overlaying the image of each product when logged in as an admin.

    ✔  The _Edit_ button directs the admin user to the relevant page where they can easily edit the properties of the product.

    ✔  The _Delete_ button deletes the button and a flash message is displayed confirming this to the admin user. (In future developments, a confirmation modal would be highly valuable to prevent accidental deletes).

2. **As a _site administrator_, I want to ensure that only I can alter the content of the website.**

    ✔  At the top of each page when logged in as an admin, the _Admin_ menu link is visible. When not logged in as an admin, these features are not accessible.

3. **As an _end-user_, I want to browse products relevant to me; including searching through them using search terms, or view only products in certain categories.**

    ✔  Products are loaded using products/products.html. The _search_ function is intuitive, functional and finds products according to user search queries. The category buttons successfully load products in the chosen category.

    ✔  When clicked, a new page will load for each product displaying the full details of the product.

4. **As an _end-user_, I want to sort products by their price or rating**

    ✔  On the _Products_ pages, the _Sort By_ dropdown is fully functional and can be used by the customer to sort products according to various factors.

5. **As an _end-user_, I want to add products to my cart and then purchase them**

    ✔ Products can be added to the cart on the individual product pages.

    ✔ When the user clicks on the _cart_ button, they can proceed to view their cart and _Checkout_ if they wish to.

    ✔ Checkout and payment processing is fully functional. **(When testing payments, use the following credit card details: 4242 4242 4242 4242, 04/42, 242 and 42424. These will allow you to run a payment for testing purposes without charging an actual credit card for the payment. Checkout/Payment can currently only be used on the Heroku-deployed version of the site.)**

    ✔ An e-mail confirmation is sent to the user to confirm their purchase details.

6. **As an _end-user_, I want to register an account so that I can save my shipping details and view my order history**.

    ✔ The _Login_ and _Register_ links are both visible when a user is not logged in.

    ✔ _Login_ works successfully for existing users and authenticates them.

    ✔ _Registration_ is fully functional. Users can register, receive an e-mail asking them to confirm their account, and continue to login with that account. (Note: in local deployment, this e-mail will print to the terminal. It is better to test its functionality on the Heroku-deployed site.)

    ✔ Users can save their shipping details when. These can be edited, when logged in, by clicking their _username_ on the navbar and selecting _My Account_.

    ✔ Previous orders can be viewed on the _My Account_ page.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Feedback 

The site was shown to peers and fellow developers who were encouraged to interact with the site and provide their feedback. Overall response from users was positive and no critical bugs were encountered. 

My [CodeInstitute](http://www.codeinstitute.net/) mentor, Arnold Kyeza, returned constructive feedback and advice at multiple stages throughout the project.

[⇧ Back to Top](#table-of-contents)