Back to [README.md](README.md)

## INDEX

- <a href="#user-stories">User Storie - how are they met?</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved Issues</a>
- <a href="#testing-unresolved">Unresolved Issues</a>

---

> # **TESTING**

> <span id="user-stories"></span>

## USER STORY TESTING

### Broadscale User Expectations

**Easy Navigation**

1.  The Navigation is highly contrasted, responsive and easy to understand.
2.  The Navbar and Footer are present on all pages, including Error pages.
3.  The Footer includes top-level navigation links, for when a user is near the bottom of the page.
4.  The title of each page is visible to the user in the browser window, which further indicates which page the user is on.

**Responsiveness**

5.  The site is fully responsive to different screen sizes. This is largely achieved by using Bootstraps grid system in conjunction with varied media queries.

**Appealing Visual Design**

6. The site provides a good visual experience.
7. This is achieved by using a striking, complementary color scheme that is consistent across all pages.
8. The page structure is kept clean and easily readable, by maintaining clear spacing and a simple layout.
9. Two complementing font styles are present across the site. They offer an elegant, vintage feel and provide further consistency to the site's overall appearance.

**Intuitive UX Design**

10. Good UX ensures the user is not left guessing as to what to do, or where to go next.
11. This is assisted by including recognisable icons where user action is required.
12. Alert messages are also present, to let the user know that an action has been performed.
13. Confirmation modals are used to ensure that the user is aware they are about to make an important change to their stored data.

**Security**

14. Allauth provides a robust user account system while Stripe offers secure payments, furthered by use of webhooks to ensure transactions are recorded.

### As a potential customer I want to... 

**Immediately understand the purpose of the site**

1.  A first time visitor will experience a striking home page that contains a hero-image, title and slogan that indicate the site is a retail leather store.
2.  The user is prompted to click an animated 'down arrow', which directs them to the collections and featured collection section, where they can glean further insight into what type of products are on offer.
3.  A carousel showcasing positive customer reviews about products and the store in general, further indicate that the site exists within the retail industry.

**Easily browse through all products**

4. Unregistered users can view all products.
5. Numerous links point to the products page.
6. The navigation bar inludes a 'shop all' dropdown menu which inludes the various categories
7. The search functionality allows the user to find products by name, category or keyword.
8. The sort functionality allows users to order products by name, category, price and rating. 
9. The product cards are simple yet informative - at a glance, the user can tell the name, price, rating and whether the item is on sale or not.

**Experience a convenient and secure registration process**

10. A link to sign up is visible on the home page and is included in the dropdown menu, triggered by clickin the user profile icon in the navbar. 
11. The registration process for new users is straightforward as they are only required to enter a username, email address and password.
12. Upon registration the user is sent a confirmation email which when accessed takes them back to the site where they can log in.

**Shop without registering**

13. Users do not need to register to add items to their cart, or make purchases.

**Read product reviews/ratings**

14. A rating (if applicable) for each product is visible on the products page and product details page.
15. When viewing a product in detail, existing reviews appear below the product image and description.

- **Choose from a range of sizes for certain products**

1. If a product has sizes to choose from, the user can select their preference from the product details page before adding it to their cart. If not specified, the default selection is size medium. 

### As a registered customer I want... 

As well as the above elements (with the exception of registration), returning customers can experience the following:

**A convenient login and logout process**

1. A returning user can easily re-enter the site, by using the simple login process.

**To be able to search for products using appropriate keywords**

2. Search functionality is present that allows users to search products by name, category or keyword.

**To have access to a personal profile**

3. Registered users have access to a personalised profile page where they can view
  - Order confirmation
  - Order history
  - Their wishlist
  - Links to their product reviews
  - Personal delivery details

**To save my default delivery details**

4. Users can either update their details from their account dashboard or by opting to save their details before checking out.
5. Next time they checkout, their details will conveniently be prepoulated into the checkout form. 

**To be able to add a product to a wishlist**

6. Registered users can save their favourite products to a wishlist. These are stored on their profile page.

**To be able to post a review on a product I've bought**

7. Registered users can review any product from the product detail page.
8. They are only able to leave one review per product. 
9. They are not able to delete their reviews, however, they can edit them. 

**Review my cart before checking out**

10. Users can adjust the quantity of an item by clicking the plus/minus buttons in their cart, as well as removing them by clicking the red 'X' icon.

**Receive confirmation of my orders**

1. Upon successfully checking out, users see a pop-up toast informing them their order was successful and that a confirmation email has been sent to their nominated email address. 

**Easily see what products are on sale**

1. Users can easily identify sale items by selecting the sale category from the shop all dropdown menu. 
2. Every product that is on sale, also includes a sale alert badge in the corner of the product image. 
3. And if a product is on sale, the original price is crossed out, and the sale price (in red) can be seen below it.

**Receive free delivery above an order threshold**

1. If an order is $150 (AUD) the delivery fee will be waived.


### As the site owner/admin, I want...

**To have admin privileges to enable me to manage all content (add, edit or delete)**

1. Admin can add new products from the product management link in the navbar.
2. They can change access all relevant fields.
3. The Edit Product page can be accessed from any of the product pages by clicking the edit icon.
4. The form fields are prepopulated with the existing product's details.
5. From the front-end a product can only be deleted via the product details page to avoid accidental deletion (this proofing came as a late addition in the development process, after I had the accident myself).
6. A confirm deletion modal appears to double check the intention.


<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---

<span id="testing-manual"></span>

> # **MANUAL TESTING**

:heavy_check_mark:

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

Manual testing was performed throughout the building process. The following is a breakdown of the different areas/components that have successfully passed manual testing.

#### Navigation

- All links in navigation tested and direct users to the correct pages
  - :heavy_check_mark:
- Correct navigation options are visible to users in session:

  - Logged in user: My Profile & Log Out
  - Admin Logged in: Product Management (includes edit, delete buttons on produts and add new in dropdown), My Profile & Log Out
  - User not logged in: Register & Log In
  - :heavy_check_mark:
- The offcanvas mobile menu displays links as above for different users 
  - :heavy_check_mark:

#### Footer

- The footer displays essential navigation links for different users:

  - Logged in user: Log Out & My Profile
  - User not logged in: Register & Log In
  - :heavy_check_mark:

- Social media links all in working order and direct user to external pages in a new browser window
  - :heavy_check_mark:

#### Home Page

- On page load, the hero image and call to action buttons render clearly
  - :heavy_check_mark:
- The sale and free delivery banner above the navbar, appear and the fade in and out effect functions as expected
  - :heavy_check_mark:
- On page scroll, the banner disappears and the navbar remains fixed to the top, visible at all times
  - :heavy_check_mark:
- All links direct the user to the correct pages
  - :heavy_check_mark:

#### Products

- Confrim each option from the Sort By selector works and lists products in the corresponding order
  - :heavy_check_mark:
- Confirm that all categories display relevant products
  - :heavy_check_mark:
- Check product details against the database to ensure the correct info is shown for each product
  - :heavy_check_mark:
- Confirm that edit/delete product buttons only appear for admin users
  - :heavy_check_mark:


#### Product Details 

- Confirm correct product info is displayed
    - :heavy_check_mark:
- Confirm heart icon only displays when logged in as Registered user
    - :heavy_check_mark:
- When logged in as admin confirm clicking edit icon leads to the Edit Product page
    - :heavy_check_mark:
- Confirm clicking delete icon brings up modal asking for confirmation
    - :heavy_check_mark:
- Confirm clicking Delete removes the product from the database
    - :heavy_check_mark:
![order-form](wireframes/test-images/options-form.jpg)
- Confirm that users can update the quantity using the carets or by inputing into the text field
    - :heavy_check_mark:
- Confirm product quantity entered cannot be less than 1 or more than 99
    - :heavy_check_mark:
![number-input](wireframes/test-images/number-input.jpg)
- Confirm that clicking the Juices button takes user back to all products view
    - CHECK
- Confirm that clicking the Add to Cart button does add the item to the cart
    - CHECK
- Confirm that if a product has no reivews, a message asking user to leave a review is displayed, and that clicking it will take them down the Reviews anchor
    - CHECK
  
#### Reviews

- Confirm that products that have reviews, render correclty
  - :heavy_check_mark:
- Confirm that delete buttons on reviews only visible to admin users
  - :heavy_check_mark:
- Check that all edit review buttons work for registered customers and render the correct form
  - :heavy_check_mark:
- Check that all edit, delete and add buttons for products and reviews render the correct pages and forms for admin users
  - :heavy_check_mark:

#### Registration and Log In Pages

  1. Anybody can register for free. Passwords are hashed for using [Werkzeug Security](https://werkzeug.palletsprojects.com/en/2.0.x/utils/). If a user accidentally navigates to the register page, from there they can click on a log in link and vice versa.

  2. The username and password validators are in place and check that users are meeting the requirements for both registration and log in processes.

  3. Upon successful registration, a personalised welcome message is displayed to the new user. If unsuccessful, the user will be notified by a different alert letting them know that their username/password is incorrect.

  4. When a user successfully logs in, they are directed to their profile page and greeted by a personalised welcome message.

- #### Search Sets Page

  1. The Search Sets page displays all available sets added by all users.

  2. The Search Bar allows users to filter the available sets by entering some text (it is suggested they search by category or stroke). When they hit 'search', relevant sets will be displayed. Below the search bar, a message is displayed that informs the user of their search results. At this stage, if no results are returned, nothing gets displayed. A message to direct the user to try something else or direct them elsewhere would be desirable.

  3. At this stage, pagination is not an included feature, but it is also a desirable one.

- #### Add Set Page

  1. Users can add a new swim set by clicking on the 'new swim' link. There they will be directed to fill in a form that includes fields relevant to a swim programme.

  2. The input fields were developed from the Sets collection initially stored in MongoDB during the initial stages of development.

  3. The 'Select Category' field which is viewed as a dropdown menu, is connected to the Category collection stored in MongoDB. If an admin user makes adjustments to a category, this field gets updated accurately.

  4. The Pre Set and Main Set fields are stored as arrays in the database. This allows these fields to include additional entry fields that get added dynamically via some JQuery script. These are accurately rendered when a user submits the form.

  5. Upon submission, the set is added to collection on the site and in the database itself.The user is then redirected to the Search Sets page and an alert message is displayed notifying them of a successful submission.

- #### Edit Set Page

  1. For general registered users, each set stored on their profile will display an edit button, that redirects them to a form for editing.

  2. Admin users are able to edit any set from the Search Sets page. For admin, an edit button will be visible on all sets.

  3. The form is prefilled based on the selected sets existing values/field entries.

  4. The edit button updates the set in the database and on the site. The user gets an alert message notifying them that their set was succesfully updated. They remain on the Edit Set page.

  5. The cancel button will redirect the user to the Search Sets page.

- #### Profile Favourites and Print Pages

  1. A user's profile page displays their name and provides them with additional options to add a new set or to navigate to their Favourites page. All of the users stored sets are displayed as cards similar to those on the Search Set page, with the addition of three buttons: favourite, edit and print.

  2. The Favourite page includes a user's selected favourites displayed alphabetically by set name in small cards. Each card contains a 'view' button which redirects the user to that set located on the Search Sets page. They can also choose to navigate back to their profile by clicking on a 'back to profile' button at the top of the page.

  3. When a user 'favourites' a set from the collection, a new favourite is added to the database stored in a Favourites collection. Each favourite gets populated with the associated values for the set (id and name) as well as the user id.

  4. When a user clicks on a print button, they are redirected to a page that renders their selected set in a print friendly manner. The name of the set gets displayed at the top of the page. They can choose to navigate back to their profile by clicking on a 'back to profile' button at the top of the page. The print function is initialised by some JQuery script, utilising the window.print() method.

- #### Manage Content Page

  1. The Manage Content page can only be accessed by admin users in session. It gives admin users the options to add, edit and delete categories. They can also add new sets from the Manage Content page.

  2. The Add Category button will direct users to a form that requires the input of a new category name. If they hit cancel, they will be redirected back to the Manage Content page. If they hit submit, they will receive an alert message notifying of a successful add. Categories are stored and added alphabetically.

  3. The delete button will trigger a modal asking the user for confirmation before going ahead and deleting the category permanently. If they confirm deletion, an alert message will be displayed confirming that the category has been deleted.

- #### Deleting Content (Admin and Users)

  1. The deletion process of sets is similar to that of category deletion mentioned above. If a user chooses to delete a set, a modal will be triggered that asks, "Do you really want to delet your set {{ set.set_name }}? This cannot be undone!" If they choose to delete, the set is removed from the collection. If they select not to delete, they remain on their profile page.

- #### Error Handler Pages

  1. In the event of 404 and 500 errors, pages with appropriate messages will be displayed. Both pages include buttons to invite the user to return to the Home page.

---

<span id="testing-auto"></span>

> # **AUTOMATED TESTING**

- ## [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

  - Throughout the development process, DevTools was used for testing responsive behaviour on small, medium and large screen sizes.
  - It was also consistently used to debug and prototype CSS.

  ### [Lighthouse](https://developers.google.com/web/tools/lighthouse)

- Used to check performance, accessibility and SEO potential on all pages of the website.
  _Across all pages:_

  - Performance: 81%
  - Accessibility: 80%
  - Best Practices: 100%
  - SEO: 90%

- ## [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

No errors or warnings to show.

- ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

No errors found, 15 warnings

<img src="static/images/test_images/css-test.png" width="300">

- ## [Python Validator](http://pep8online.com/)

Initial Pep8 tests showed some refactoring was required, mainly removing whitespace and fixing some indenting issues. Everything was cleared apart from what is shown in the image below:

<img src="static/images/test_images/pep8-result1.png" width="300">

- ## [JavaScript Validator](https://jshint.com/)

1 undefined variable, 2 warnings

<img src="static/images/test_images/jshint-test.png" width="300">

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

## <span id="testing-responsive"></span>

> # **RESPONSIVENESS**

## CROSS BROWSER COMPATIBILITY

Browsers tested:

- Chrome _v.90_
- Microsoft Edge _v.90_
- Firefox _v.88_
- Safari _v.14_

## VARIED SCREEN SIZES

Chrome DevTools used to test:

- Moto G4
- iPhone 4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro
- Surface Duo
- Galaxy Fold

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<span id="testing-resolved"></span>

> # **RESOLVED ISSUES**

- UnboundLocalError : local variable 'product' referenced before assignment
- In contexts.py in the cart_contents model, I had referenced 'product' but not defined it yet. This was fixed by defining product = get_object_or_404(Product, pk=item_id) again, but within local scope.
<!-- - Initially tried to use Materialize *Parallax* effect on the Home Page, but image wouldn't appear. Resorted to more of a custom approach, combining *Tachyons* and *Materialize* classes for responsiveness.
<img src="static/images/test_images/test5.png" width="400">


- The following screenshots were captured to address and debug a variety of issues relating to repsonsiveness, general layout issues, ensuring consistency throughout the site (mainly navigation) and general styling/design concerns.

<img src="static/images/test_images/test6.png" width="400">

<img src="static/images/test_images/test7.png" width="400">

<img src="static/images/test_images/test8.png" width="400">

<img src="static/images/test_images/test9.png" width="400">

<img src="static/images/test_images/test10.png" width="400">

<img src="static/images/test_images/test11.png" width="400">

<img src="static/images/test_images/test12.png" width="400">

<img src="static/images/test_images/test13.png" width="400">

> # **UNRESOLVED ISSUES**

- Unable to implement **Remove Favourites** function.
- Was not able to fix sizing of buttons in form that get added dynamically through JQuery script when a user adds a new input field to the _pre_set_ and _main_set_ fields of the 'add set' form.
- Warnings reported by CSS validator
- Warnings reported by JSHint -->
