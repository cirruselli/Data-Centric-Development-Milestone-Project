### Testing User Stories from User Experience (UX) Section
**First Time Visitor Goals**    
1. As a First Time Visitor, I want to easily understand the main purpose of the site    
    i. Upon entering the site, users can easily navigate the site through the navigation bar.     
    ii. On the start/home page there is statistics about how many percent of the offsprings each stallion has.

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
    iii. Cancel a filled in form to verify the page refreshes and all text disappears. 

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

* The code have been validated in a [HTML validator](https://validator.w3.org/#validate_by_input), [CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input), 
    [JavaScript validator](https://jshint.com/) and [Python validator](http://pep8online.com/) respectively.

* Lighthouse is an open-source, automated tool for improving the quality of web pages and was used to check the site for performance.
    
    Homepage:
    ![2020-12-11 (1)](https://user-images.githubusercontent.com/60824715/101905247-6d13cc00-3bb7-11eb-813c-b7d06752c4d8.png)

    Balegro page:
    ![2020-12-11 (2)](https://user-images.githubusercontent.com/60824715/101905445-c4b23780-3bb7-11eb-8d12-7d875b037797.png)

    Offsprings A-I page:
    ![2020-12-11 (3)](https://user-images.githubusercontent.com/60824715/101905915-73567800-3bb8-11eb-83a6-23395eeaff36.png)

    Add offspring page:
    ![2020-12-11 (4)](https://user-images.githubusercontent.com/60824715/101906019-9b45db80-3bb8-11eb-9e44-67c61cb80deb.png)
    
### Known bugs