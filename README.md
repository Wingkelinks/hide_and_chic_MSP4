[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://github.com/Wingkelinks/hide_and_chic_MSP4)

<h1 align="center">Hide & Chic</h1>
<h2 align="center">Serving Your Leather Obsession</h2>

<h5 align="center">
Code Institute MS4 / Full Stack Frameworks With Django</h5>

<img src="" width="800">

[Click here to view the live project]()

---

## INDEX

- <a href="#context">Context</a>
  - <a href="#ux-overview">Project Overview/Strategy</a>
  - <a href="#ux">User Experience</a>
  - <a href="#ux-scope">Scope</a>
  - <a href="#ux-structure">Structure</a>
- <a href="#skeleton">Skeleton</a>
- <a href="#surface">Surface</a>
- <a href="#db-model">Database Model</a>
  - <a href="#features-existing">Existing Features</a>
  - <a href="#features-future">Future Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Development and Deployment</a>
- <a href="#credits">Credits</a>

---

> # **CONTEXT**

<span id="context"></span>

Hide & Chic is my fourth and final milestone project as a Code Institute student working towards a Diploma in Full Stack Software Development. It forms part of the Full Stack Frameworks module. The final project is not intended for commercial use - education pursposes only.

The project purpose is outlined as follows:

"... build a full-stack site based around business logic used to control a centrally-owned dataset."

"... set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service."

<span id="ux-overview"></span>
<span id="ux"></span>

> # **PROJECT OVERVIEW**

Hide & Chic is an Australian based business that focusses on a niche retail market, as well as a commitment to being accessible to a broad audience within its unique industry.

>## USER EXPERIENCE (UX)

Hide & Chic is an online retail store solely dedicated to the sale of fine leather products. Dedicated to providing customers with unique and hard-to-find, quality leather treasures, it offers a carefully curated selection of the finest leather goods - all in one place.

It offers shoppers a gender-inclusive retail experience - product categories are not gender-specific and include a range of both gender-fluid and gender-neutral collections. Products are simply categorised according to function. In the case where size may be applicable to a product - a universal, standard sizing range is available for selection.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<span id="ux"></span>

## USER STORIES

|| **As a...**  | **I want to...** | **So I can...** |
| :------------| :----------------| :-------------- |:-------------- |
|**VIEWING & NAVIGATION**|
||*SHOPPER* | Immediately understand the purpose of the site | Decide whether to stay |
|||View a list of products without having to register | Select some to purchase
|||View individual product details  | Identify the price, description, product rating, product image, available sizes and read product reviews |
|||Easily identify deals and sale items  | Take advantage of special savings on products I'd like to purchase |
|||Easily view the total of my cart contents/purchases | Keep track of expenditure  |
| **REGISTRATION & USER ACCOUNTS** |**As a...**| **I want to...** | **So I can...** |
||*SHOPPER*| Easily register for an account | Access a personal account and view my profile |
|||Easily log in and out | Access my personal account info |
||| Easily recover password if forgotten | Regain access to my account |
||| Receive email confirmation upon registering | Verify successful registration |
||| Have a personalized user profile | View my order confirmation, history, wishlist, reviews and view/update personal delivery details |
| **SORTING & SEARCHING** |**As a...**| **I want to...** | **So I can...** |
||*SHOPPER* | Sort the list of available products|Easily identify products by category, name, rating and price |
|||Sort a specific category | Identify products by name, rating and price within a category |
|||Add a product to my wishlist | Quickly find a product I've saved or purchase again|
|||Search for a product by name/keyword | Find a specific product to purchase |
|||View what I've searched for plus the results| See if the product is available |
| **PURCHASING & CHECKOUT** |**As a...**| **I want to...** | **So I can...** |
||*SHOPPER*| Easily select the size and quantity of a product when purchasing | Can be assured I'm selecting size and quantity I want|
||| View items in my cart to be purchased | Identify the total cost of my purchase and items to be received |
||| Adjust the quantity of items in my cart | Easily make changes before checking out |
||| Feel my personal and payment info is processed securely | Make purchases confidently |
||| View order confirmation upon checkout | Verify my order |
||| Receive an email confirmation upon checkout  | I have a personal record of my order |
| **ADMIN PRIVILEGES** |**As an...**| **I want to...** | **So I can...** |
||*OWNER/ADMIN* | Add a product | Add new items to my store |
||| Edit/update a product| Change product prices, descriptions, images and other related fields  |
||| Delete a product | Remove items no longer on sale or out of stock |
|||Delete customer product reviews | In the instance of offensive commentary|

> <span id="ux-scope"></span>
> # **SCOPE**

**Minimum Viable Product** for the website will include:

- Mobile first design
- Easy to navigate
- Intuitive design
- Visually appealing
- Secure

> # **SKELETON**

## WIREFRAMES
<span id="ux-structure"></span>
<span id="skeleton"></span>

- Click [here](wireframes/final_wireframes.pdf) to view the final wireframes
- Preliminary sketches:

<img src="/wireframes/prelim_wireframe1.jpeg" width="400">
<img src="/wireframes/prelim_wireframe2.jpeg" width="400">


> # **SURFACE**
>
> <span id="surface"></span>

## DESIGN

- #### Theme and Colour Scheme

Naturally, the theme and colour palette is inspired by leather and an associated earthiness. In striving to maintain good contrast across the site, a bold orangey-red color was selected as a starting point. From then on [Coolors](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff-4dec38-000000) and [ColorHexa](https://www.colorhexa.com/d3d3d3) were used to search for appealing tones and contrasting colours, resulting in the two colour palettes as shown below. These were incorporated as root classes in the CSS file, to be easily called upon directly from the HTML files.

Take a closer look at the colour schemes:

  - Palette 1
  <img src="/testing/images/hideandchic_color1.png" width="400">

  - Palette 2
  <img src="/testing/images/hideandchic_color2.png" width="400">
  
  | Palette 1| Palette 2|
  |:------------|:------------|
  |*Left to right*|*Left to right*|
  |**platinum**: #e5e5e|**orange-soda**: #f15c37|
  |**muted**: #6c757d|**coral**: #f67b53|
  |**blue-black**: #011014|**salmon**: #fb996f|
  |**cyan**: #37ccf1|**rosso**: #d42912|
  |**granny-smith**: #c8f6a7|**blue-black**: #011014|

- #### Typography

- ##### [Google Fonts](https://fonts.google.com/)

  - [IM Fell Great Primer SC](https://fonts.google.com/specimen/IM+Fell+Great+Primer+SC?preview.text=Hide%20%26%20Chic&preview.text_type=custom&sort=alpha&query=im+fell+#standard-styles) was selected for the Hide & Chic logo and makes an appearance in selected headings and messages throughout the site. It has an old style printing appeal which seemed an appropriate styling choice.
  - [Josefin Sans](https://fonts.google.com/specimen/Josefin+Sans?preview.text=Hide%20%26%20Chic&preview.text_type=custom&sort=alpha&query=josefin+sans) was chosen for the body of the site. It has a an elegant, vintage feeling and pairs nicely with IM Fell Great Primer SC.

- #### Imagery

  - All images were individually sourced from [Unsplash](https://unsplash.com/) and are free to use.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<span id="db-model"></span>

## DATABASE MODEL

A relational database is utilised for this project as there are a number of relationships between the tables. SQLite was used during development and then Heroku Postgres in production. The diagram below illustrates the database logic:

- Click [here](wireframes/db_diagram.pdf) to view the database schema.

#### Key models

**Category**
+ Stores product category details
+ Sends information to product model to categorize a product

**Product**
+ Stores all product details:
  + SKU
  + Category
  + Name
  + Description
  + Color
  + Size - if applicble
  + Price
  + Sale - if applicable
  + Sale price - if applicable
  + Rating
  + Review - if applicable
  + Image + URL 

+ Links information from the category model by ForeignKey
+ Sends information to the OrderLineItem model to instantiate a purchase

**ProductReview**
- Links a review to a registered user and product by foreign key
- Checks whether a user has previously reviewed the same product

**Order**
- Handles order information:
  -  User profile
  -  Order number
  -  Delivery details
  -  Total cost
- Uses signals to update line-item changes

**OrderLineItem**
- Stores individual order information
- Uses information from the Product model by ForeignKey
- Sends information to the Order model through ForeignKey

**UserProfile**
- Maintains users default delivery information and order history
- Linked to the Order model by ForeignKey to attach order information to a user's profile

> # **FEATURES**
<span id="features-existing"></span>

## CURRENT

### Site-wide

#### **Responsiveness**

Using Bootstrap's grid system and additional media queries, the site is responisive across a range of devices.

#### **Accessibility**

Accesbility standards are met by following common best practices:
  - one `<h1>` per page
  - using sub-headings
  - ensuring links and call-to-action prompts are clear
  - the presence of aria-labels
  - strong colour contrasting across the site (particularly in navigation)
  - images have ALT attributes

#### **Navigation**

The navigation menu assists the user in finding their way across the site.

Navigation options are updated depending on a user's status:
- whether they are registered and logged in or not
- and if they are logged in as admin, certain privileges are made available


#### **Footer**

The footer is visible on all pages, and gives users additional navigation options.

#### **Search Functionality**

The search bar can be accessed via the navbar and the footer. It allows users to submit search queries to filter products in the database.

#### **Toasts**

In the form of pop-up messaging, toasts communicate confirmation of certain actions to a user, for example upon login/logout, checkout success, any warnings or error messages etc.
  
#### **User registration - not a requirement to shop**

If a user would prefer not to create an account, they are still able to shop and make a purchase.

#### **User profile creation**

Users can register and create an account if they want to. 
The registration process requires:
+ Username
+ Email address
+ Password
 
User Profiles allow users to: 
+ View their order history
+ Save their default delivery information to their profile from the checkout page.
+ Update their default delivery information to their profile.
+ Post product reviews
+ Edit their product reviews
+ Save favourite products to a wishlist - listed on their profile page

---

### Page-specific

#### **Home**

- A striking hero image and slogan draws potential customers in 
- A call-to-action links straight to the products page
- A scroll down button with a subtle wobble animation invites further exploration of the home page inlcuding,
- A collections section of cards showcasing product categories,
- A featured collection section inviting the user to explore the stores latest collection,
- A carousel displaying positive customer reviews

#### **Products Page**

All users can browse through available products.
Products can be viewed by category:
+ All Products
+ Footwear
+ Jackets
+ Bags
+ Accessories
+ Sale

All users can also sort products (ascending & descending) according to:
+ Price
+ Rating
+ Name
  
From here, a registered user in session:
  - can add the product to their wishlist

From here, admin have the ability to:
  - add, edit/delete a product

To view a product in more detail, users can click on the selected product and navigate to the product details page.

#### **Product Details Page**

The product details page offers:
+ Product name
+ Product category
+ Product description 
+ Product price 
+ Product rating
+ Product reviews
+ Sale information

From here, users can add the selected product to their cart, add it to their wishlist or simply navigate back to the all products page.

From here, admin have the ability to:
  - add, edit/delete a product
  - add, edit/delete a review

#### **Cart**

**Cart Modal**
A user can quickly view their cart via a modal from the navbar at any point to see what items they have chosen and what the cart total is. From here, they can choose to navigate to the cart page, where they can view a detailed breakdown of their cart.

**Cart Page**
From here a user can update product quantities, remove items from the cart or navigate to the checkout page.
If the cart total is less than the free delivery threshold, the user is informed as to how much they still need to spend to qualify for free delivery.


#### **Checkout**

The checkout page allows users to:

+ Use their default delivery address (if registered, logged in and selected to save their details)
+ Input new delivery information if necessary or because they checking out as a guest
+ Update their profile with the new delivery information (if they registered and logged in)
+ Checkout and pay securely via the Stripe Payment system
+ Upon checkout, a loading screen appears to notify the user that their payment is being processed
+ A checkout success page is displayed, detailing the order information
+ If an error occurs during the payment process, e.g. a user closes the browser, Stripe still creates an order
+ An email is sent to the user providing them with their order confirmation

#### **Profile**

  *Registered users only*
- Details:
  - default contact and delivery info
  - ability to update to make future checkouts quicker
- Orders:
  - view previous orders
- Wishlist:
  - a list of products saved with links to each
- Reviews:
  - Displays a link to the reviewed product page

--- 
### Security & Defensive Programming

#### **Secure accounts**
Account security is ensured by Django's allauth.

#### **Deletion Confirmation**
When users request to delete a product or review, a modal pops up to confirm they wish to do so to prevent accidental deletion.

#### **Access Protection**

Django's `@login_required` route decorators are used  to secure the database from being tampered with by non-admin/superusers. 

#### **Static and image file hosting**

Static and image files are served from an Amazon S3 Bucket.

#### **404 and 500 error handling**

404 and 500 error pages help to keep the user on the site when something goes wrong, allowing them to navigate back to the home page.

#### **CRUD functionality**

All users can
- View all products
- Make a purchase as a guest

Registered session users can:
- Post product reviews
- Edit product reviews
- Update their delivery details
- Save and update their wishlist

Admin/superusers can:
  - Add, update and delete products
  - Add, update and delete product reviews

<span id="features-future"></span>
## FUTURE FEATURES

- Pagination
- Contact page
- Advanced payment features eg. AfterPay, Google and Apple Pay
- A blog app 

---

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>
<span id="technologies"></span>

> # **TECHNOLOGIES USED**

## LANGUAGES

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

## FRAMEWORKS AND LIBRARIES

- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)

## DATABASE
- [Heroku Postgres](https://www.heroku.com/postgres)

## EXTENSIONS AND PACKAGES

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [django-countries](https://pypi.org/project/django-countries/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Stripe](https://stripe.com/docs)

## PROJECT MANAGEMENT

- [Visual Studio Code](https://code.visualstudio.com/) - Coding Editor
- [Pipenv](https://pypi.org/project/pipenv/) - Python Virtual Environment & Package Manager
- [Git](https://git-scm.com/) - Version Control
- [GitHub](https://github.com/) - Repository Storage
- [Imgbot](https://github.com/marketplace/imgbot)
  > A Github app that optimizes images (free for open source projects).
  > Imgbot sends an auto pull request with images optimized. The pull request is merged and Imgbot keeps working as changes are made to the repository.
- [Heroku](https://www.heroku.com/about) - Hosting
- [Balsamiq](https://balsamiq.com/) - Wireframes, Site Map

## TOOLS

- [Google Fonts](https://fonts.google.com/)
- [Material Icons by Google Fonts](https://fonts.google.com/icons)
- [Font Awesome](https://fontawesome.com/)
- [Am I Responsive?](http://ami.responsivedesign.is/)
- [DB Diagram](https://dbdiagram.io/)
---

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>
<span id="deployment"></span>

> # **DEVELOPMEMNT AND DEPLOYMENT**

The deployed version of Hide & Chic has been created using the master branch.

## LOCAL DEVELOPMENT

The following is required to run this project in your local environment:

- [Python 3](https://www.python.org/downloads/) - to run the code
- [Pipenv](https://pypi.org/project/pipenv/)  - package installation and virtual environment 
- [Git](https://git-scm.com/) - used for version control
- [Amazon AWS S3 Bucket](https://aws.amazon.com/) - to host static and media files
- [Visual Studio Code](https://code.visualstudio.com/) - or your own choice of IDE

>**To run Hide & Chic locally, follow these steps:**

1. Visit this [Repository link](https://github.com/Wingkelinks/hide_and_chic_MSP4) and click on the Clone or Download button to copy the link provided.

  <img src="/testing/images/repo-clone.png" width="400">

2. In your IDE of choice, open a terminal window and navigate to the directory that you want to copy the project to:

    `Git clone "your copied link"`

    Hit enter to clone it to your directory.

    *OR - Download the zipped file, decompress it and use your IDE of choice to access it.*

3. Make sure you either have access to your email server settings and credentials or to your cloud based email, such as [Gmail](https://accounts.google.com/b/0/AddMailService).

4. Install [Pipenv](https://pipenv.pypa.io/en/latest/). 
(This project was developed on a Mac, therefore [Homebrew](https://brew.sh/) was used to install pipenv `brew install pipenv`).

5. NB: Create a virtual environment by typing:

   `pipenv shell`

6. Install all of the package dependencies in the pipfile by using:

   `pipenv install`

7. Make sure to have a test account on [Stripe]("https://stripe.com/en-nl")

8. Create a file called `env.py` to hold your app's environment variables, which should contain the following:


    ```console
      import os
   
      os.environ("SECRET_KEY", "<app secret key of your choice>")
      os.environ("DEVELOPMENT", "True")
      os.environ('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
      os.environ('STRIPE_SECRET_KEY', '<key generated by Stripe>')
      os.environ('STRIPE_WH_SECRET', '<key generated by Stripe for individual webhook endpoint>')
    ```
    - To find your Stripe keys, login and under the **Developers** tab look for the 'Publishable Key' and 'Secret Key'

    - The webhook secret key can be found under **Webhooks** once you have created an endpoint, which should be set to receive all events and match this url structure:

    ***Values for the env.py environment variables and Heroku Config Vars used below are unique to each SQLlite, Postgres and S3 Bucket created. Please refer to their respective documentation for further details.***


9.  Run migrations by:

    `python3 manage.py makemigrations --dry-run`
    `python3 manage.py makemigrations`
    `python3 manage.py migrate --plan`
    `python3 manage.py migrate`

10. Create a superuser by typing in terminal `python3 manage.py createsuperuser`

11. Run the app locally by typing `python3 manage.py runserver`.


### Heroku

Hide & Chic is deployed on [Heroku](https://id.heroku.com/login) from the master branch. To do this, the following steps were taken:

<p>
<details>
<summary>Heroku Deployment Instructions</summary>
<p>

1. **Log In** to [Heroku](https://id.heroku.com/login)

2. [Gunicorn](https://gunicorn.org/), a Python WSGI HTTP Serve, is a necessary installed dependency
3. Create a file called **Procfile** and include the following:
```
web: gunicorn hide_and_chic.wsgi:application
```
Be careful not to leave a blank line underneath!
3. Add the hostname of your Heroku app to settings.py
```
ALLOWED_HOSTS = ['hide_and_chic.herokuapp.com', 'localhost']
```
4. Select **Create new app** in the Heroku dashboard and give it a unique name
3. Link the app to the GitHub repository by going to the **Deploy** tab in the main app menu
4. Under **Connect to Github** enter your details and connect your repository
5. Under **Resources** search for and add **Heroku-Postgres** to the app
6. Next, go to settings and select **Config Vars** and then **Reveal Config Vars**

|**Key**|**Value**|
|:-----|:-----|
|AWS_ACCESS_KEY_ID|`<your variable here>`|
|AWS_SECRET_ACCESS_KEY|`<your variable here>`|
|DATABASE_URL|`<added by Heroku when Postgres installed>`|
|DISABLE_COLLECTSTATIC|`1` NB this variable will be deleted later|
|EMAIL_HOST_PASS|`<your variable here>`|
|EMAIL_HOST_USER|`<your variable here>`|
|SECRET_KEY|`<your variable here>`|
|STRIPE_PUBLIC_KEY|`<your variable here>`|
|STRIPE_SECRET_KEY|`<your variable here>`|
|STRIPE_WH_SECRET|`<different from env.py>`|
|USE_AWS|True|
</details>

### Amazon S3
Create an [AWS S3 bucket]("https://s3.console.aws.amazon.com/s3/home")

<p>
<details>
<summary>S3 Bucket Setup Instructions</summary>
<p>

1. Create an [Amazon AWS](aws.amazon.com) account
2. Search for **S3** and create a new bucket
- Allow public access
- Acknowledge
3. Under **Properties > Static** website hosting
- Enable
- Index.html as index document
- Save
4. Under **Permissions > CORS** use:
```
		[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under **Permissions > Bucket Policy**:
- Generate Bucket Policy and record the **Bucket ARN**
- Choose **S3 Bucket Policy** Policy Type
- For **Principal**, enter `*`
- Enter **ARN** from above
- **Add Statement**
- **Generate Policy**
- Copy **Policy JSON Document**
- Paste policy into **Edit Bucket policy** on the previous tab
- Save
6. Under **Access Control List (ACL)**:
- For **Everyone (public access)**, tick **List**
- Accept that the bucket will be made public
- Save

</details>

### AWS IAM (Identity and Access Management)


<p>
<details>
<summary>AWS IAM Setup Instructions</summary>
<p>

1. From the **IAM dashboard** within AWS, select **User Groups**:
- Create new group e.g. `manage-hide-and-chic`
- Click through without adding a policy
- **Create Group**
2. Select **Policies**:
- Create policy
- Under **JSON** tab, click **Import managed policy**
- Choose **AmazongS3FullAccess**
- Edit the resource to include the **Bucket ARN** noted earlier when creating the Bucket Policy:
```
			"Resource": [
			                "arn:aws:s3:::hide-and-chic",
			                "arn:aws:s3:::hide-and-chic/*"
            ]
```
- Click **next step** and go to **Review policy**
- Give the policy a name e.g. `hide-and-chic-policy` and description
- **Create policy**
3. Go back to **User Groups** and choose the group created earlier
- Under **Permissions > Add permissions**, choose **Attach Policies** and select the one just created
- **Add permissions**
4. Under **Users**:
- Choose a user name e.g. `hide-and-chic-staticfiles-user`
- Select **Programmatic access** as the **Access type**
- Click Next
- Add the user to the Group just created
- Click Next and **Create User**
5. **Download the `.csv` containing the access key and secret access key. This will NOT be available to download again**
6. Add the values from the `.csv` you downloaded to your Heroku Cvars under Settings:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```
7. Delete the `DISABLE_COLLECTSTATIC` variable from your Config Vars and deploy your Heroku app

</details>


### Please note:

1. As mentioned, this project used [Pipenv](https://pipenv.pypa.io/en/latest/) for its virtual environment - this automatically creates a pipfile and includes all dependencies needed for the project to run 
2.  The pipfile renders the file 'requirements.txt' unnecessary, but one was included in this project in the event someone not using Pipenv might need it
3. A `Procfile` is a Heroku requirement 
4. During deployment, Heroku accesses the pipfile and installs the dependencies
5. I also reads the Procfile and the Config Variables

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---

<span id="testing"></span>

> # **TESTING**

Click [here](TESTING.md) to view testing details. 

---

<span id="credits"></span>

> # **CREDITS**

## TUTORIALS AND RESOURCES

- [Boutique Ado Django Walkthrough Project by Chris Zielinksi](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Guide to markdown on .md files.
- [CSS Tricks](https://css-tricks.com/) - convenient CSS resources. Regularly referenced their **Flexbox** tutorial.
- [Stack Overflow](https://stackoverflow.com/) - general questions and problem solving.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) - general questions and problem solving.
- Code Institute **Slack** channel
  
## REFERENCED AND MODIFIED CODE SOURCES

- [Code Snippet for bootstrap banner above fixed-top nav](https://stackoverflow.com/questions/44526926/show-bootstrap-banner-at-the-top-before-navbar/44530320)

- [Scroll down button animation](https://codepen.io/nelledejones/pen/gOOPWrK)

- [Centering a Material Icon in a div](https://newbedev.com/mat-icon-does-not-center-in-its-div)

## CONTENT AND MEDIA

- All text content is original
- Images obtained from [Unsplash](https://unsplash.com/) & [Pexels](https://www.pexels.com/)


## ACKNOWLEDGEMENTS

- Thanks to my Mentor, Sebastian Immel for his humour, guidance and support.
- Thank you to the Code Institute and the top quality course content.
- Thank you to the Code Institue Slack community - a great place to check in and learn from others.
- Thank you to Chris Zielinksi for his thorough Full Stack Django example (Boutique Ado), as well as for sharing his insights and expertise on the CI Slack channel

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>
