[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/organization/repository)

<h1 align="center">Hide & Chic</h1>
<h2 align="center">Serving Your Leather Obsession</h2>

###### Code Institute MS4 / Full Stack Frameworks With Django

<img src="" width="800">

[View the live project here.]()

---

## INDEX

- <a href="#context">Context</a>
  - <a href="#ux-overview">Project Overview/Strategy</a>
  - <a href="#ux">User Experience</a>
  - <a href="#ux-strategy">Strategy</a>
  - <a href="#ux-scope">Scope</a>
  - <a href="#ux-structure">Structure</a>
- <a href="#skeleton">Skeleton</a>
- <a href="#surface">Surface</a>
  - <a href="#features-existing">Existing Features</a>
  - <a href="#features-future">Desirable Features</a>
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

## USER EXPERIENCE (UX)

Hide & Chic is an online retail store solely dedicated to the sale of fine leather products. Dedicated to providing customers with unique and hard-to-find, quality leather treasures, it offers a carefully curated selection of the finest leather goods - all in one place.

It offers shoppers a gender-inclusive retail experience - product categories are not gender-specific and include a range of both gender-fluid and gender-neutral collections. Products are simply categorised according to function. In the case where size may be applicable to a product - a universal, standard sizing range is available for selection.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<span id="ux"></span>

- ## USER STORIES

| **As a...**                          | **I want to...**                                                 | **So I can...**                                                                                          |
| :----------------------------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **_ VIEWING AND NAVIAGTION _**       |
| Shopper                              | Immediately understand the purpose of the site                   | Decide whether to stay                                                                                   |
|                                      | View a list of products                                          | Select some to purchase                                                                                  |
|                                      | View individual product details                                  | Identify the price, description, product rating, product image, available sizes and read product reviews |
|                                      | Easily identify deals and sale items                             | Take advantage of special savings on products I'd like to purchase                                       |
|                                      | Easily view the total of my cart contents/purchases              | Avoid spending too much                                                                                  |
| **_ REGISTRATION & USER ACCOUNTS _** |
|                                      | Easily register for an account                                   | Access a personal account and view my profile                                                            |
|                                      | Easily log in and out                                            | Access my personal account info                                                                          |
|                                      | Easily recover password if forgotten                             | Regain access to my account                                                                              |
|                                      | Receive email confirmation upon registering                      | Verify account successful registration                                                                   |
|                                      | Have a personalized user profile                                 | View my order confirmation, history, wishlist and view/update personal delivery details                  |
| **_ SORTING & SEARCHING _**          |
|                                      | Sort the list of available products                              | Easily identify products by rating, price and category                                                   |
| Sort a specific cateogry             | Identify products by rating, price within a category             |
|                                      | Add a juice to my favourites list                                | Quickly find a product I'd like to purchase again                                                        |
|                                      | Search for a product by name/keyword                             | Find a specific product to purchase                                                                      |
|                                      | View what I've searched for plus the results                     | See if the product is available                                                                          |
| **_ PURCHASING & CHECKOUT _**        |
|                                      | Easily select the size and quantity of a product when purchasing | Can be assured I'm selecting size and quantity I want                                                    |
|                                      | View items in my cart to be purchased                            | Identify the total cost of my purchase and items to be received                                          |
|                                      | Adjust the quantity of items in my cart                          | Easily make changes before checking out                                                                  |
|                                      | Feel my personal and payment info is processed securely          | Make purchases confidently                                                                               |
|                                      | View order confirmation upon checkout                            | Verify my order                                                                                          |
|                                      | Receive an email confirmation upon checkout                      | I have a personal record of my order                                                                     |
| **_ PURCHASING & CHECKOUT _**        |
|                                      | Add a product                                                    | Add new items to my store                                                                                |
|                                      | Edit/update a product                                            | Change product prices, descriptions, images and other related fields                                     |
|                                      | Delete a product                                                 | Remove items no longer on sale or out of stock                                                           |
|                                      | Delete customer product reviews                                  | In the instance of offensive commentary                                                                  |

> # **SCOPE**

**Minimum Viable Product** for the website will include:

- Mobile first design
- Easy to navigate
- Intuitive design
- Visually appealing
- Secure

> # **SKELETON**

## WIREFRAMES

<span id="ux-skeleton"></span>

- Wireframes can be viewed [here]()

## SITE MAP

- A site map can be viewed [here]()

> # **SURFACE**
>
> <span id="ux-surface"></span>

## DESIGN

- #### Theme and Colour Scheme

Naturally, the theme and colour palette is inspired by leather and an associated earthiness. In striving to maintain good contrast across the site, a bold orangey-red color was used as a starting point. From then on [Coolors](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff-4dec38-000000) was used search for appealing tones and contrasting colours. The result was the two colour palettes as shown below, which were incorporated as utility classes in the CSS file, to be easily called upon directly from the HTML files.

Take a closer look at the colour schemes:

  <img src="media/Hide&Chic_color1.png" width="400">
  <img src="media/Hide&Chic_color2.png" width="400">

- #### Typography

##### [Google Fonts](https://fonts.google.com/)

- [IM Fell Great Primer SC](https://fonts.google.com/specimen/IM+Fell+Great+Primer+SC?preview.text=Hide%20%26%20Chic&preview.text_type=custom&sort=alpha&query=im+fell+#standard-styles) was selected for the Hide & Chic logo in the Navbar and makes an appearance in selected headings and messages throughout the site. It has an old style printing appeal which I found appropriate.
- [Roboto](https://fonts.google.com/specimen/Josefin+Sans?preview.text=Hide%20%26%20Chic&preview.text_type=custom&sort=alpha&query=josefin+sans) was chosen for the body of the site. It has a an elegant, vintage feeling and pairs nicely with IM Fell Great Primer SC.

- #### Imagery

  - All images were individually sourced from [Unsplash](https://unsplash.com/) and are free to use.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

## DATABASE MODEL

A relational database is utilised for this project as there are a number of relationships between the tables. SQLite was used during development and then Heroku Postgres in production. The diagram below illustrates the database logic:

\*\*\*\* INSERT DB DIAGRAM

> # **FEATURES**

## KEY MODELS AND APPS

- **Category**
- **Product**
- **Product Review**
- **Order**
- **Order Line Item**
- **User Profile**

_Defensive Programming_ Features include **Deletion Confirmation** alerts that appear as a modal, when a user clicks on any 'delete' related button.

## DESIRABLE

<!-- - **Pagination**:
  I would have loved to have included pagination to the site, as I am fully aware that it contributes to a better user experience. Due to time constraints, it was necessary to prioritise other elements/features.

- **Remove Set from Favourites**:
  Again, this is an important companion feature to the 'Add Favourites' feature, however I did not have the time to make it work. -->

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

- [Tachyons](https://tachyons.io/)
- [Google Fonts](https://fonts.google.com/)
- [Material Icons by Google Fonts](https://fonts.google.com/icons)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

## EXTENSIONS AND PACKAGES

- [PIP](https://pypi.org/project/pip/)

## PROJECT MANAGEMENT

- [Visual Studio Code](https://code.visualstudio.com/) - Coding Editor
- [Git](https://git-scm.com/) - Version Control
- [GitHub](https://github.com/) - Repository Storage
- [Imgbot](https://github.com/marketplace/imgbot)
  - A Github app that optimizes images (free for open source projects).
    > Imgbot sends an auto pull request with images optimized. The pull request is merged and Imgbot keeps working as changes are made to the repository.
- [Heroku](https://www.heroku.com/about) - App Hosting
- [Balsamiq](https://balsamiq.com/) - Wireframes, Site Map

---

<span id="testing"></span>

> # **TESTING**

Full testing details can be found [here](TESTING.md)

---

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>
<span id="deployment"></span>

> # **DEVELOPMEMNT AND DEPLOYMENT**

<!-- The deployed version of MySwim has been created using the master branch. -->

## LOCAL DEPLOYMENT

<!-- The following is required to run this project in your local environment:

[Python 3](https://www.python.org/downloads/) - to run the code

[PIP](https://pypi.org/project/pip/) - for package installation

[Git](https://git-scm.com/) - used for version control

[MongoDB or MongoDB Atlas](https://www.mongodb.com/) - for database development

[Visual Studio Code](https://code.visualstudio.com/) - or your own choice of IDE

### First you need to clone MySwim

To clone this project from its [GitHub repository](https://github.com/Wingkelinks/myswim_MSP3):

1. Click on the **Code** button
2. Copy the clone URL for the repository: https://github.com/Wingkelinks/myswim_MSP3.git
3. From within your IDE, open your integrated terminal
4. Make sure you are in the correct folder location
5. Then type **git clone** and paste the URL: https://github.com/Wingkelinks/myswim_MSP3.git
6. From there create an env.py file to store your credentials as follows:

```console
      import os

      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      os.environ.setdefault("SECRET_KEY", "")
      os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
      os.environ.setdefault("MONGO_DBNAME", "my_swim")
```

You can use a random key generator if you wish.

7. This file MUST be hidden in your .gitignore file to keep credentials from being visibly pushed to the repository
8. You should be able to run the app by typing **python3 app.py** into the terminal

- In MongoDB you will need to create a database called MySwim.
- The following collections should be created:
  - sets
  - categories
  - users
- A document in categories should be created with the following fields:

| **Key**       | **Value** | **Type** |
| :------------ | :-------- | :------- |
| category_name | aerobic   | String   |

- The same applies for sets and users, however the sets collection has two fields of arrays:

| **Key**  | **Value** | **Type** |
| :------- | :-------- | :------- |
| pre_set  | []        | Array    |
| main_set | []        | Array    |

### How to deploy to Heroku

MySwim is deployed on Heroku from the master branch. To do this, the following steps were taken:

1. From your terminal, create a **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. Sign up and login to Heroku, **create a new app**
3. Name your app
4. Go to the **Deploy** tab and then **Deployment Method** and select **Github**
5. Under **Connect to Github** enter your details and connect your repository
6. Next, go to **settings** and select **Config Vars** and then **Reveal Config Vars**
7. You need to enter the following variables to match what you have stored in your env.py file

   - **IP** : `0.0.0.0`
   - **PORT** : `5000`
   - **MONGO_URI** : `MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg. mongodb.net/<database_name>?retryWrites=true&w=majority`
   - **SECRET_KEY** : `<app secret key>`

8. Under the **Deploy** tab go to **Automatic Deploys** and enable
9. Under **Manual Deploy**, choose **Master** and click **Deploy Branch**
10. Heroku will begin building the app. When it is ready, you can click **Open app** to launch it. -->

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---

<span id="credits"></span>

> # **CREDITS**

## TUTORIALS AND RESOURCES

<!-- - Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))
- MS3 Strategy and Tips ([Ed Bradley](https://github.com/Edb83))
- Fellow Students MS3 Project ([Ed Bradley](https://github.com/Edb83))
- [Code Institute course material](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) -->

- Code Institute **Slack** channel
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Guide to markdown on .md files.
- [CSS Tricks](https://css-tricks.com/) - convenient CSS resources. Regularly referenced their **Flexbox** tutorial.
- [Stack Overflow](https://stackoverflow.com/) - general questions and problem solving.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) - general questions and problem solving.

## REFERENCED AND MODIFIED CODE SOURCES

<!-- - [CSS3 Animation Notification](https://codepen.io/sugimo/pen/DgLty) - referenced to create custom flash messages
- [Print Page JQuery](https://www.geeksforgeeks.org/how-to-print-a-page-using-jquery/) - to initialise my print functionality
- [Tutorial by Cody Mind](https://www.youtube.com/watch?v=jSSRMC0F6u8) - dynamically add and delete form input fields
- [Dogfalo](https://github.com/Dogfalo/materialize/issues/192) - to customise the Materialize form input fields -->

## CONTENT AND MEDIA

- All initial site content is written by the developer.
- Images obtained from [Unsplash](https://unsplash.com/), an open source photography platform.

## ACKNOWLEDGEMENTS

<!-- - Thanks to my Mentor, Sebastian Immel for his guidance and support.
- Thank you to the Code Institute and the top quality course content.
- Thank you to the Code Institue Slack community - a great place to check in and learn from others. -->

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>
