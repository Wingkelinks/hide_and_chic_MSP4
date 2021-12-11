:point_left:
 Back to [README.md](README.md)

> # **TESTING**

## INDEX

- <a href="#user-stories">User Stories - how are they satisfied?</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved Issues</a>
- <a href="#testing-unresolved">Unresolved Issues</a>

---

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

**Choose from a range of sizes for certain products**

16. If a product has sizes to choose from, the user can select their preference from the product details page before adding it to their cart. If not specified, the default selection is size medium. 

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

11. Upon successfully checking out, users see a pop-up toast informing them their order was successful and that a confirmation email has been sent to their nominated email address. 

**Easily see what products are on sale**

12. Users can easily identify sale items by selecting the sale category from the shop all dropdown menu.
13. Every product that is on sale, also includes a sale alert badge in the corner of the product image. 
14. And if a product is on sale, the original price is crossed out, and the sale price (in red) can be seen below it.

**Receive free delivery above an order threshold**

15. If an order is $150 (AUD) the customer's order becomes eligible for free delivery.


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

Manual testing was performed throughout the building process. The following is a breakdown of the different areas/components that have successfully passed manual testing.

#### Navigation

- All links in navigation tested and direct users to the correct pages :heavy_check_mark:
- Correct navigation options are visible to users in session:

  - Logged in user: My Profile & Log Out
  - Admin Logged in: Product Management (includes edit, delete buttons on produts and add new in dropdown), My Profile & Log Out
  - User not logged in: Register & Log In :heavy_check_mark:
- The offcanvas mobile menu displays links as above for different users :heavy_check_mark:

#### Footer

- The footer displays essential navigation links for different users:

  - Logged in user: Log Out & My Profile
  - User not logged in: Register & Log In :heavy_check_mark:

- Social media links all in working order and direct user to external pages in a new browser window :heavy_check_mark:

#### Home Page

- On page load, the hero image and call to action buttons render clearly :heavy_check_mark:
- The sale and free delivery banner above the navbar, appear and the fade in and out effect functions as expected :heavy_check_mark:
- On page scroll, the banner disappears and the navbar remains fixed to the top, visible at all times :heavy_check_mark:
- All links direct the user to the correct pages :heavy_check_mark:

#### Products

- Confrim each option from the Sort By selector works and lists products in the corresponding order :heavy_check_mark:
- Confirm that all categories display relevant products :heavy_check_mark:
- Check product details against the database to ensure the correct info is shown for each product :heavy_check_mark:
- Confirm that edit/delete product buttons only appear for admin users :heavy_check_mark:


#### Product Details 

- Confirm correct product info is displayed :heavy_check_mark:
- Confirm heart icon only displays when logged in as Registered user :heavy_check_mark:
- When logged in as admin confirm clicking edit icon leads to the Edit Product page :heavy_check_mark:
- Confirm clicking delete icon brings up modal asking for confirmation :heavy_check_mark:
- Confirm clicking Delete removes the product from the database :heavy_check_mark:
- Confirm that users can update the quantity using the plus/minus buttons or by inputing into the text field :heavy_check_mark:
- Confirm product quantity entered cannot be less than 1 or more than 99 :heavy_check_mark:
  
  <img src="/testing/images/quantity_input.png" width="400">

- Confirm that checkout and continue shopping buttons work correctly  :heavy_check_mark:
- Confirm that Add to Cart button adds the item to the cart :heavy_check_mark:
  
#### Reviews

- Confirm that products that have reviews, render correclty :heavy_check_mark:
- Confirm that delete buttons on reviews only visible to admin users :heavy_check_mark:
- Check that all edit review buttons work for registered customers and render the correct form :heavy_check_mark:
- Check that all edit, delete and add buttons for products and reviews render the correct pages and forms for admin users :heavy_check_mark:
- Confirm that products with reviews, display the correct numnber of reviews as well as the rating :heavy_check_mark:
 
  <img src="/testing/images/reviews.png" width="400">

#### Checkout
- Confirm correct items and amounts carried over from cart, including if a discount code has been applied
  -  :heavy_check_mark:
- Confirm if user has logged in and saved their details previously, the form is pre-populated with these details
    - :heavy_check_mark:
- Confirm Stripe webhooks successfully processed and Order saved
    - :heavy_check_mark:
  
  <img src="/testing/images/stripe_trigger.png" width="400">

#### Footer 

- Check each page to confirm footer remains fixed to the bottom of the especially when there is minimal content (Sign Up)
  - This was actually a problem for some time. The original footer was much larger in height, and because its position needed to be set to fixed, it covered content on certain pages. In the end, the solution was to re-design a more minimal looking footer.  :heavy_check_mark:
- Check all footer icon to confirm hover effects :heavy_check_mark:
- Click each social icon to check pages open in a new browser window :heavy_check_mark:


#### Search Functionality 
- Hover over magnifying glass icon to confirm colour changes to blue :heavy_check_mark:
- Click on magnifying glass to confirm search modal appears :heavy_check_mark:
- Search for a specific product or keyword, eg. 'wallett to check that relevant products are displayed :heavy_check_mark:
- Confirm that returned list of wallets, displays number of filtered items, and can be sorted by price (low to high) for example :heavy_check_mark:
  
  <img src="/testing/images/search.png" width="400">

#### Profile Dashboard
- Confirm details can be updated and checkout form is prefilled :heavy_check_mark:
- Order history displayed :heavy_check_mark:
- Can view individual orders via the link on order number :heavy_check_mark:
- Can view review history/links to reviews :heavy_check_mark:
  
#### Add / Edit / Delete Products
- Only admin can access pages :heavy_check_mark:
- Confirm deletion modals working correctly :heavy_check_mark:
 
  <img src="/testing/images/confirm_delete.png" width="400">

- Added or updated products reflect in database :heavy_check_mark:
  
  <img src="/testing/images/db_reflect.png" width="400">


#### Error Handler Pages

- In the event of 404 and 500 errors, pages with appropriate messages will be displayed. Both pages include buttons to invite the user to return to the Home page.

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---

<span id="testing-auto"></span>

> # **AUTOMATED TESTING**

#### [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

  - Throughout the development process, DevTools was used for testing responsive behaviour on small, medium and large screen sizes.
  - It was also consistently used to debug and prototype CSS.

#### [Lighthouse](https://developers.google.com/web/tools/lighthouse)

- Used to check performance, accessibility and SEO potential on all pages of the website.
  _Across all pages:_

  - Performance: 78%
  - Accessibility: 76%
  - Best Practices: 93%
  - SEO: 82%

- Overall performance is alright, however some issues are noted:
  - *unused CSS* - a Bootstrap related issue
  - *unused JavaScript* - caused by Stripe & JQuery

#### [W3C HTML Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

 - NO Errors
 - 253 Warnings

#### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

 - NO Errors
 - 253 Warnings

<img src="/testing/images/CSS_validation.png" width="400">

#### [Python Validator](http://pep8online.com/)

- Code refactoring done and all tests passed PEP8 requirements since initial submission.

#### [JavaScript Validator](https://jshint.com/)

  -  2 warnings
  -  NO Errors

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---

## <span id="testing-responsive"></span>

> # **RESPONSIVENESS**

### CROSS BROWSER COMPATIBILITY

Browsers tested:

- Chrome _v.90_
- Microsoft Edge _v.90_
- Firefox _v.88_
- Safari _v.14_

### VARIED SCREEN SIZES

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

### Real world testing 
- iPhone SE
- MacBook Pro
- MacBook Air
- iPad

<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

---
<span id="testing-resolved"></span>

> # **RESOLVED ISSUES**

- When a footer was initially extended from the base.html, it seemed to render correctly on most pages, apart from the checkout ones. 
- This was eventually resolved by removing the Material Icons from the buttons. 
- It is not clear why these were the cause of the issue.

  <img src="/testing/images/footer-issue.png" width="400">

<br><hr>

- Previously, the checkout success page was not working as it was meant to - the loading overlay would't render and sometimes the checkout success page didn't appear.
- A typo in the stripe_elements.js file was discovered - the card variable had been incorrectly named.

  <img src="/testing/images/stripe_issue.png" width="400">

<br><hr>

- When first implementing the cart modal (in the navbar), the CSS across the navigation and home page, wasn't rendering.
- A template looping issue was found to be the cause.

  <img src="/testing/images/looping-issue.png" width="400">

<br><hr>

- Fixed footer covering inner page content.
- Resolved by adding a CSS class of `vh=100` to certain containers across the site
- And increasing the padding on some of the elements near the bottom of the page

  <img src="/testing/images/footer-margin-issue.png" width="400">

- Static files issue - resolved 
  
   <img src="/testing/images/static_files_issue.png" width="400">

- Image URL issue - resolved 
   <img src="/testing/images/image_url_issue.png" width="400">


- Overflow issues resolved - assisted by [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)

<img src="/testing/images/overflow.png" width="400">

<span id="testing-unresolved"></span>



> # **UNRESOLVED ISSUES**

- The following screenshots address and attempt to debug issues relating to repsonsiveness, general layout issues, ensuring consistency throughout the site (mainly navigation) and general styling/design concerns.


<br><hr>

- Sale items not being filtered by category buttons or via the search bar. 
- Filtered correctly when navigating from the products menu.

  <img src="/testing/images/sale-not-filtering.png" width="400">

- Coupon Issue - discounted amount not being rendered. No time left to try and fix this now.
  
  <img src="/testing/images/coupon_issue.png" width="400">

- I am aware that the **Leather Care** dropdown menu doesn't have any functioning links - if time allowed this is where a blog app would be located.


<div align="right"><a style="text-align:right" href="#top">Back to index	:point_up_2:</a></div>

<br><hr>

- I am aware that cart and checkout images appear to be stretched when viewed on IOS devices - this is not the case when checked against breakpoints on the pc. Tried various attempts to fix it. 

  <img src="/testing/images/image_stretch.png" width="400">

<br><hr>

- I am also aware that the reviews model does not direct a user to the correct view when selecting to edit a review. I made several attempts at trying to fix this and other CRUD functionality took precendence in the end.

<br><hr>

- The issue of emails not being sent to the users email address has also not been resolved despite confirmation of payments being recorded through Stripe, Heroku Logs and in the admin panel. I have worked extensively on this with student support and not been able to debug it.

- Please see screenshots below as proof of payments being successful. 

<img src="/testing/images/payment_success1.png" width="400">

<img src="/testing/images/payment_success2.png" width="400">

<img src="/testing/images/payment_success3.png" width="400">

<img src="/testing/images/tutor_support.png" width="400">

<br><hr>