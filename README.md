# HorseNet

My Milestone Project 3 presents a website for stallion owners to follow their offsprings progressions and for the offspring owners to 
follow their horses siblings and also the progression in both breeding and achievements of the stallions.

## User Experience (UX)

The owner of an offspring can register an account and login to add the offspring to the database. (At the moment offsprings is only added 
to the "offsprings A-I" page, since I have not done the functionality for the "offsprings J-R" nor the "offsprings S-Z". These two 
last pages is empty for now. I decided to leave them up if I want to work on this project in the future.) The same person can also edit 
and delete the offspring whenever they want to, and also read about other offsprings (the CRUD functionality). This site is for breeders 
and I had an idea of a family tree when I created this site. Although there is not a family tree there is at least some information on every 
offspring about their mother and father. The stallions have information about how many offsprings each stallion has. There is a search-bar 
for searching the offsprings on the "offsprings A-I" page. You can search on everything, for example search for one of the stallions and view 
all the offprings he has. The offsprings' names is sorted in alphabetically order for easier overview. The "add offspring" page has a dropdown 
list for the option "father" to eliminate misspelling or adding of another stallion. 

This type of site could also be useful for breeding catteries and kennels. The idea of following the males (and also the females) 
progression in breeding is interesting to know for both the stallion owner and the owners of the offsprings. And this site acts a bit like a 
community for the offspring owners to come together. 

I decided to not have a profile page for the user, instead the "add offspring" page serves this purpose since adding offsprings is the main 
function for the user. 


- ### User stories

    - **First Time Visitor Goals**   
        1. As a First Time Visitor, I want to easily understand the main purpose of the site
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.

    - **Returning Visitor Goals**   
        1. As a Returning Visitor, I want to be able to search the site
        2. As a Returning Visitor, I want to be able to follow the stallions 
        
    - **Frequent Visitor Goals**    
        1. As a Frequent Visitor, I want to be able to register an account and login 
        2. As a Frequent Visitor, I want to interact with the site and add content
        3. As a Frequent Visitor, I want to view other offsprings related to my own offspring

- ### Design 
    - **Color Scheme**   
    The rose-red color scheme is for the love between horses and their owners and for the bloodbands that this site is representing,
    ([see colour affects here](http://www.colour-affects.co.uk/psychological-properties-of-colours))

    - **Typography**    
    The Montserrat font is the main font used.

    - **Imagery**   
    The images in the carousels represents the stallions and some of the offsprings. 
    
    - **Interactivity**   
    Users can register and login to add offsprings. This is later reflected on the percent-bar on the homepage where statistics over how many
    offsprings each stallion has i represented.

- ### Wireframe
    The wireframes is included as pdf files in the project itself (in a separate directory called wireframes).

## Features

- ### Existing Features
    - Homepage - allows users to follow statistics for the stallions
    - Stallion pages (Balegro, Sunrise, Offset, Dimma) - information about each of the four stallions
    - Offspring A-I page - presents all offsprings. Has a search-function. Edit and delete button for each offspring the user has added. 
    - Add offspring page - users can add offsprings by filling out the form. Option "Father" has a dropdown list to eliminate misspelling or adding of another stallion.
    - Register - click here to register to the page.
    - Log in - click here when you have a registered account.
    - Log out - click here when you want to log out from the page.

- ### Features Left to Implement
    - Offsprings should be listed alpfabetically on pages "offsprings A-I", "offspring J-R" and "offspring S-Z" for easier navigation, 
    even though you can now search the offsprings.
    - Admin page perhaps...

## Technologies Used
### Languages Used
- HTML
- CSS
- JavaScript
- Python3 

### Frameworks, Libraries & Programs Used
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - for functionality
- [Google fonts](https://fonts.google.com/) - Montserrat font
- [Font Awesome](https://fontawesome.com/) - to use icons 
- [Bootstrap](https://getbootstrap.com/) - to create carousel, navbar, forms
- [Git](https://git-scm.com/) - was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) - is used to store the projects code after being pushed from Git.
- [MongoDB](https://cloud.mongodb.com) - database used
- [Heroku](https://dashboard.heroku.com/) - for deployment of the project
- [Figma](https://www.figma.com/) - to create the wireframes during the design process

## Testing

### Testing User Stories from User Experience (UX) Section
**First Time Visitor Goals**    
1. As a First Time Visitor, I want to easily understand the main purpose of the site    
    i. Upon entering the site, users can easily navigate the site through the navigation bar.     
    ii. On the start/home page there is statistics about how many procent of the offsprings each stallion has.

2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.   
    i. At the top of each page there is a navigation bar, each link describes what page they will end up at.    
    ii. On both the register and login page, the page refreshes and the user is brought to the top of the homepage 
    where the navigation bar is.
 
**Returning Visitor Goals**   
1. As a Returning Visitor, I want to be able to search the site       
    i. At the moment there is a search-bar on the "offspring A-I" page where you can search the information about the offsprings. 

2. As a Returning Visitor, I want to be able to follow the stallions    
    i. This is possbile on the homepage where statistics over how many offsprings each stallion has is represented with percentage.    
    ii. Each stallion has its own page with information such as how many offsprings and achievements. 

**Frequent Visitor Goals**    
1. As a Frequent Visitor, I want to be able to register an account and login     
    i. Via the navbar the user can register and also login to the site.        
    ii. When registered or logged in the page redirect to homepage.

2. As a Frequent Visitor, I want to interact with the site and add content    
    i. When logged in users can add offsprings to the "offspring A-I" page via a form on the "add offspring" page.     
    ii. The number of offsprings is reflected on the homepage where each stallion has a percentbar.      
    iii. Each stallion has its own page where number of offsprings i represented. 

3. As a Frequent Visitor, I want to view other offsprings related to my own offspring      
    i. The page "offspring A-I" presents all offsprings        
    ii. The "offspring A-I" page has a search function where you can search for the stallion of the offspring and get all
    other offsprings related to that stallion. You can search for the mother as well.

### Further testing
* Most testing was done throughout development, and it was manual tests. 
1. Homepage:    
    i. Go to the "home" page      
    ii. See how many percentages the stallion to your offspring has     
    iii. Go to "add offspring" page     
    iiii. Add your offspring by filling out the form   
    iiiii. Press "Save offspring"    
    iiiiii. Go back to "home" page  
    iiiiiii. Verify that the percentage of the stallion to your offspring has changed   

2. Stallions page (Balegro, Sunrise, Offset, Dimma):   
    i. Go to one of the stallions page, eg Balegro          
    ii. See the number of offsprings Balegro has       
    iii. Go to "add offspring" page       
    iiii. Add your offspring by filling out the form - make sure to choose Balegro as the father         
    iiiii. Press "Save offspring"      
    iiiiiii. Go back to "Balegro" page          
    iiiiiiii. Verify that the number of offspring has increased with one offspring       

3. Offsprings A-I page:     
    i. Search the page with a word that you now exists in the offsprings information (baloo)    
    ii. See the number of results (1)
    ![2020-12-09 (1)](https://user-images.githubusercontent.com/60824715/101657590-5ef16e80-3a44-11eb-87f4-bf027db412a2.png)    
    iii. Search the page with a word you know not exists in the offsprings information    
    iiii. See the number of results (0)    
    iiiii. Press "reset" to see all offsprings again

4. Add offspring page:    
    i. Try to submit the empty form and verify that a message appears "Fill in this field"
    ![2020-12-09 (4)](https://user-images.githubusercontent.com/60824715/101660899-f5735f00-3a47-11eb-8229-f23941465370.png)     
    ii. Try to submit the form with all fields filled in and verify that a success message appears     
    ![2020-12-09 (5)](https://user-images.githubusercontent.com/60824715/101661627-ce695d00-3a48-11eb-9cb9-e86ffe2f823c.png)
    ![2020-12-09 (6)](https://user-images.githubusercontent.com/60824715/101661644-d1644d80-3a48-11eb-8122-be671c7db01a.png)

5. Register:    
    i. Click "register" on the navbar     
    ii. Try to register a short username/password and verify that a error message appears     
    ![2020-12-09 (7)](https://user-images.githubusercontent.com/60824715/101663137-9bc06400-3a4a-11eb-93f4-61793dcd2bb6.png)
    iii. Try to register a longer username/password and verify that registration is successful and redirect to homepage     
    ![2020-12-09 (8)](https://user-images.githubusercontent.com/60824715/101663315-d9bd8800-3a4a-11eb-8b11-2b15abaf37b2.png)
    ![2020-12-09 (9)](https://user-images.githubusercontent.com/60824715/101663347-e510b380-3a4a-11eb-96b1-c532f335c9f1.png)

6. Log in:     
    i. Click "Log in" on the navbar    
    ii. Try to log in with an invalid username and/or password and verify that a relevant error message appears    
    ![2020-12-09 (10)](https://user-images.githubusercontent.com/60824715/101664660-63ba2080-3a4c-11eb-90c9-127c2c2d19bb.png)    
    iii. Try to log in with a valid username and password and verify that a success message appears and redirects to homepage    
    ![2020-12-09 (11)](https://user-images.githubusercontent.com/60824715/101664863-9f54ea80-3a4c-11eb-8c27-9f435c0b82e5.png)

7. Log out:   
    i. Click "Log out" on the navbar     
    ii. Verify a success message appear


* Different web-browsers (Opera, Firefox, Microsoft Edge, Chrome) and Samsung galaxy 9 - Android have been used to check the website's 
    layout and that the site works well on different devices and screensizes. Where needed I used media query to fix any responsiveness issues.


### Validation 

* The code have been validated in a [HTML validator](https://validator.w3.org/#validate_by_input), [CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    and [JavaScript validator](https://jshint.com/) respectively.
    
### Known bugs
*  Perhaps I could have left the media query for the carousel to make the images the same height. I decided to delete the media queries
    and let the images have different heights.

## Deployment


## Expanding on my project

Is not allowed until I've finished the course at Code Institute. I'll let you know when.

## Credits

### Content
All content was written by the developer and exeptions with copied code is commented in the code.

### Media
The photos used in this site were obtained from:
- First picture in the carousel of [Balegro](https://www.naturepl.com/cache/pcache2/01524326.jpg), second picture of [Balegro](https://previews.agefotostock.com/previewimage/medibigoff/8c3efac1b7ca508c53cb1b168839eb48/ssj-h-81062098.jpg), third picture of [Balegro](https://media.istockphoto.com/photos/beautiful-american-quarter-horse-stallion-picture-id106413072)

- First picture in the carousel of [Dimma](https://image.freepik.com/free-photo/american-quarter-horse-buckskin-stallion_74692-145.jpg), second picture of [Dimma](https://thumbs.dreamstime.com/z/wild-stallion-nature-running-gallop-147893469.jpg), third picture of [Dimma](https://media.istockphoto.com/photos/black-stallion-rearing-up-picture-id1034305800)

- First picture in the carousel of [Offset](https://image.shutterstock.com/image-photo/portrait-running-stallion-black-friesian-260nw-1246577917.jpg), second picture of [Offset](https://c8.alamy.com/comp/XA6CEX/pure-spanish-horse-andalusian-gray-stallion-looking-over-a-hedge-germany-XA6CEX.jpg), third picture of [Offset](https://image.shutterstock.com/image-photo/portrait-brown-stallion-percheron-beautiful-260nw-1214364226.jpg)

- First picture in the carousel of [Sunrise](https://kppusa.com/wp-content/uploads/2016/11/stallion-supplements.jpg), second picture of [Sunrise](https://images.robertharding.com/zoom/RF/RH_RF/HORIZONTAL/832-387597.jpg),third picture of [Sunrise](https://www.naturepl.com/cache/pcache2/01539794.jpg)

- First picture in the carosusel of [foal](https://media.gettyimages.com/photos/playful-foal-picture-id828105844?s=612x612), second picture of [foal](https://media.gettyimages.com/photos/closeup-image-of-a-new-forest-young-pony-foal-in-the-new-forest-park-picture-id1153450394?s=612x612), third picture of [foal](https://image.shutterstock.com/image-photo/young-bay-foal-galloping-on-260nw-1246728751.jpg)

- First picutre in the carousel of [foal2](https://image.shutterstock.com/image-photo/newborn-brown-foal-4-days-260nw-1449952289.jpg), second picture of [foal2](https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/14/2019/01/foals-alamy-ATYR5E.jpg), third picture of [foal2](https://image.shutterstock.com/image-photo/beautiful-red-foal-run-fun-260nw-1494066905.jpg)

- First picture in the carousel of [foal3](https://c8.alamy.com/comp/2BC752B/beautiful-mare-and-foal-running-with-their-herd-on-pasturage-2BC752B.jpg), second picture of [foal3](https://media.istockphoto.com/photos/horses-mare-and-foal-on-meadow-trotting-in-pasture-arabian-horse-picture-id1177258293), third picture of [foal3](https://media.gettyimages.com/photos/icelandic-foal-picture-id828105870?s=612x612)

### Acknowledgements

- Tutors at Code Institute for their support.

- My mentor for his support. 

- My long-distance boyfriend for his support.

- I received inspiration for this project from Code Insitute's Project Example Idea 1: Create an online cookbook, and my own interest horses.
