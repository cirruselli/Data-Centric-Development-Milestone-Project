# HorseNet

My Milestone Project 3 presents a website for stallion owners to follow their offsprings progressions and for the offspring owners to 
follow their horses siblings and also the progression in both breeding and achievements of the stallions.

Here's a link to the live app: https://data-centric-horsenet.herokuapp.com/

This site is for breeders and I had an idea of a family tree when I created this site. Although there is not a family tree there is at 
least some information on every offspring about their mother and father.  The idea of following the males (and also the females) 
progression in breeding is interesting to know for both the stallion owner and the owners of the offsprings. This site acts a bit 
like a community for the offspring owners to come together. The typical user is a owner of an offspring to one of the four stallions. 
The primary goal of the website is to lead users to add offsprings to the website. This type of site could also be useful for breeding 
catteries and kennels.

The business goals of this website are:    
* Showcase the stallions available for breeding    
* Showcase the offsprings from each stallion    

The user goals of this website are:    
* Searching the offsprings     
* Add your own offspring     
* View the stallions available for breeding and follow their progressions in breeding  

## User Experience (UX)

### User stories

**First Time Visitor Goals**   
    1. As a First Time Visitor, I want to easily understand the main purpose of the site    
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.     

**Returning Visitor Goals**   
    1. As a Returning Visitor, I want to be able to search the site    
    2. As a Returning Visitor, I want to be able to follow the stallions     
        
**Frequent Visitor Goals**    
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
    The wireframes was created using Figma and the wireframes are included as pdf files in the project itself (in a separate directory 
    called wireframes). In the pdf to the wireframe for stallion on mobile device, the picture is gone and also for the offsprings 
    on mobile device.

## Features
Each page features a responsive navigation bar with a logo in the top left corner. Each page has a footer with copyright information.

**Home page**    
The homepage features a carousel in which each of the four stallions are presented on their own slide.    
After the carousel there is four percentbars which presents the statistics of the four stallions' breeding progress. When a user adds an 
offspring this will be reflected in the percentbar for the stallion that is the father of the offspring. 

**Stallions page**    
There are a page for each of the four stallions available for breeding. On each page there is a picture and information about the stallion: 
name, birth year, gender, breed, country, owner, number of offsprings and achievements. When a user adds an offspring this will 
be reflected on the number of offsprings.

**Offsprings page**   
The offspring page features a carousel with pictures on some of the offsprings. After the carousel there is a search-bar 
for searching the offsprings. You can search on everything that exists on the offspring page, for example search for one of the stallions 
and view all the offprings he has. The offsprings' names is sorted in alphabetically order for easier overview.     
The owner of an offspring can edit and delete the added offspring whenever they want to, and also read about other offsprings 
(the CRUD functionality). Admin can delete and edit all offsprings. 

**Add offspring page**    
The "add offspring" page is only visible for a registered and logged in user. To add an offspring the page has a form to fill out with the 
following fields: name, birth year, gender, father, mother, breed, country, owner and achievements.
There is a dropdown list for the field "father" to eliminate misspelling or adding of another stallion. 

- ### Existing Features
    - Homepage - allows users to follow statistics for the stallions
    - Stallion pages (Balegro, Sunrise, Offset, Dimma) - information about each of the four stallions
    - Offsprings page - presents all offsprings. Has a search-function. Edit and delete button for each offspring the user has added. 
    - Add offspring page - users can add offsprings by filling out the form. Option "Father" has a dropdown list to eliminate misspelling or adding of another stallion.
    - Register - click here to register to the page.
    - Log in - click here when you have a registered account and want to log in to the site.
    - Log out - click here when you want to log out from the site.
    - Footer - on each side with copyright information

- ### Features Left to Implement
    - Offsprings should be listed alpfabetically on pages "offsprings A-I", "offspring J-R" and "offspring S-Z" for easier navigation, 
    even though you can now search the offsprings.
    - Contact page
    - Pricelist for semin

I decided to not have a profile page for the user, instead the "add offspring" page serves this purpose since adding offsprings is the main 
function for the user. Perhaps I could have left the media query for the carousel to make the images the same height. I decided to delete 
the media queries.

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
- [Bootstrap](https://getbootstrap.com/) - Bootstrap 4 to create carousel, navbar, forms
- [Git](https://git-scm.com/) - was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) - is used to store the projects code after being pushed from Git.
- [Gitpod](https://gitpod.io/) - IDE used
- [MongoDB](https://cloud.mongodb.com) - database used
- [Heroku](https://dashboard.heroku.com/) - for deployment of the project
- [Figma](https://www.figma.com/) - to create the wireframes during the design process

## Testing
Testing information can be found in separate [TESTING.md file](https://github.com/cirruselli/Data-Centric-Development-Milestone-Project/blob/master/TESTING.md)

## Deployment

### GitHub Pages Deployment
To deploy this project to GitHub Pages, the following steps is taken:
1. Log in to GitHub and locate this GitHub Repository [(Data-Centric-Development-Milestone-Project)](https://github.com/cirruselli/Data-Centric-Development-Milestone-Project).
2. At the top of this repository, locate the "Settings" button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" section.
4. Under "Source", click the dropdown menu called "None" or "Branch" and select "Master Branch".
5. Press save
6. The website is now deployed to GitHub Pages. Scroll down to the GitHub pages section to retrieve the link to the deployed website.

### Heroku Deployment
To deploy this project to Heroku, the following steps were taken:
1. Create a `requirements.txt` file using the terminal command `pip3 freeze --local > requiremenets.txt`.
2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.
3. Use `git add` and `git commit` for the `requirements.txt` and `Procfile` and then `git push` the project to GitHub.
4. Log in and create a new app on the [Heroku website](https://dashboard.heroku.com) by clicking the "New" button and "Create New App" in your dashboard. Give the app a unique name, set the region to Europe and click "Create app".
5. Go to the IDE, in the terminal write `npm install -g Heroku` to install Heroku.
6. To connect Git remote to Heroku, copy the Heroku git URL under "Settings" on the Heroku website. In the terminal write the command `git remote add` + a name for the remote + the link you've just copied.
7. On the Heroku website for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

    KEY | VALUE
    ----|---------
    IP | 0.0.0.0
    MONGO_DBNAME | <your_mongo_db_name>
    MONGO_URI | mongodb+srv://\<username>:\<password>@<cluster_name>.t81d9.mongodb.net/<database_name>?retryWrites=true&w=majority
    PORT | 5000
    SECRET_KEY | <your_secret_key>

9. In your app.py, set "debug" to "False".
10. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
11. Confirm the linking of the Heroku app to the correct GitHub repository.
12. In the Heroku dashboard, click "Connect"
13. In the "Automatic deploys" section choose "master" branch and click "Enable Automatic Deploys"
14. In the "Manual Deployment" section, make sure the master branch is selected and then click "Deploy Branch".
15. The project is now deployed. 

### How to run this project locally
To clone this project into Gitpod, use the following steps:
1. Log in to your Github account.
2. Use the Chrome browser.
3. Install the Gitpod Browser Extensions for Chrome
4. After installation, restart the browser
5. Log into Gitpod with your gitpod account 
6. Navigate to the [project GitHub repository](https://github.com/cirruselli/Data-Centric-Development-Milestone-Project)
7. Click the green "Gitpod" button in the top right corner of the repository.
8. A new gitpod workspace will be created where you can work locally.


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
