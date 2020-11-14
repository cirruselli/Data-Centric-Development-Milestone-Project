# HorseNet

This is a website for stallion owners to follow their offsprings and for the offspring owners to follow their horses siblings.

 
## User Experience (UX)



- ### User stories

    - **First Time Visitor Goals**   
        1. As a First Time Visitor, I want to 
        2. As a First Time Visitor, 
        3. As a First Time Visitor, 
        4. As a First Time Visitor, 

    - **Returning Visitor Goals**   
        1. As a Returning Visitor,   
        2. As a Returning Visitor, 

    - **Frequent Visitor Goals**    
        1. As a Frequent Visitor,  
        2. As a Frequent Visitor, 

- ### Design 
    - **Color Scheme**   
    ([see colour affects here](http://www.colour-affects.co.uk/psychological-properties-of-colours))
    The rose-red color scheme is for the love between horses and their owners and for the bloodbands that this site is for. 

    - **Typography**    
    The Ranchers font is the main font used with the Roboto font as the fallback if the font isn't being imported into the 
    site correctly. I thought the Ranchers font suits the horse-theme since a rancher is a person who owns or operates a ranch. Also 
    the font looks kinda playful to me, which the game should be.

    - **Imagery**   
    This is a memory game with 20 horse images (10 breeds).
    
    - **Interactivity**   
    A sound of horse neigh is played when each card is flipped, a sound of applause is played when two cards match,
    and a sound of fanfare is played when the game is completed.

- ### Wireframe
    The wireframe is included as pdf files in the project itself (in a separate directory called wireframes).

## Features

- ### Existing Features
    - Game-board: consists of 20 cards with 10 different horse breeds

    - Score-counter: The player gain 10 points when two cards match but loses 5 points if it's a wrong match.

    - "New game" button: Creates a new game

- ### Features Left to Implement
    - Add breed names on each card to learn the breeds
    - Add different pack of cards to choose from for variation

## Technologies Used

- HTML
- CSS
- JavaScript - The project uses JavaScript for interactivity and for the gameboard to flip the cards
- [Jasmine](https://jasmine.github.io/) - For testing the score counter of the Javascript code
- [Google fonts](https://fonts.google.com/) - to use the Ranchers font 
- [Figma](https://www.figma.com/) - to create the wireframe
- [Bootstrap](https://getbootstrap.com/) - only to reset default properties of elements.
- [Git](https://git-scm.com/) - was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) - is used to store the projects code after being pushed from Git.

## Testing

### Testing User Stories from User Experience (UX) Section
**First Time Gamer Goals**    
1. As a First Time Gamer, I want to be able to play the game so that my abstinence will be gone    
    i. The cards do flip when clicked    
    ii. when two cards match the cards stay flipped and the gamer gain scores (+10).    
    iii. When two cards don't match the cards flips back and the gamer loses scores (-5).

2. As a First Time Gamer, I want to get some feedback while I play the game   
    i. When the a card is flipped a sound of horse neigh is played.    
    ii. When two cards match a sound of applause is played.    
    iii. When the game is completed a sound of fanfare is played.    
    iiii. The gamer will gain 10 scores or lose 5 scores depending on a match or no match of the cards.

3. As a First Time Gamer, I want to be able to start a new game if i perform terribly bad or have memory enough to win the game    
    i. Sure, the "New Game" button, when clicked, reload the webpage and creates a new game (no cards flipped) whenever the gamer wants to. 

4. As a First Time Gamer, I want to play the game on my mobile while on the go   
    i. The memory game can be played on mobile phone since the webpage is resizable. 

The Returning Gamer Goals and Frequent Gamer Goals are unfortunately not happening. This is something I would like to work on
 if I had more time.

**(Returning Gamer Goals**   
1. As a Returning Gamer, I want to see new pictures once in a while   
2. As a Returning Gamer, I want to learn the name of the horses

**Frequent Gamer Goals**    
1. As a Frequent Gamer, I want to have different pack of cards to choose from.   
2. As a Frequent Gamer, I want to be able to change color scheme)

### Further testing
* Most testing was done throughout development, most of which was manual tests. Jasmine was used to automatically test the score counter. 

* Different web-browsers (Opera, Firefox, Microsoft Edge, Chrome) and Samsung galaxy 9 have been used to check the website's layout and that 
    the site works well on different devices and screensizes. Where needed I used media query to fix any responsiveness issues.
* My friends have played the game on mobile phones with Android (Huawei p smart pro and LG g7 thinQ). 

### Validation 

* The code have been validated in a [HTML validator](https://validator.w3.org/#validate_by_input), [CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    and [JavaScript validator](https://jshint.com/) respectively.
    
### Known bugs
* The cards flip a little bit to fast sometimes on mobile. The neight-sound doesn't
    sound sometimes on the second card depending on how fast you click. 

## Deployment

### <ins>The project was deployed to GitHub Pages using the following steps:</ins>

1. Log in to GitHub and locate your [GitHub Repository](https://github.com/cirruselli/Interactive-Frontend-Development).

2. At the top of the repository, locate the "Settings" button on the menu.

3. Scroll down the Settings page until you locate the "GitHub Pages" section.

4. Under "Source", click the dropdown called "None" or "Branch" and select "Master Branch".

5. Press save. 

## Configuring a publishing source for GitHub Pages

### <ins>Default source settings for repositories without the username naming scheme</ins>

The default settings for publishing your site's source files depend on your site type and the branches you have in your site repository. 
If your site repository doesn't have a master or gh-pages branch, your GitHub Pages publishing source is set to None and your site is not published. 
After you've created either a master or gh-pages branch, you can set one as your publishing source so that your site will be published. 
If you fork or upload your site repository with only a master or gh-pages branch, your site's source setting will automatically be enabled for that branch.

### <ins>Enabling GitHub Pages to publish your site from master or gh-pages</ins>

To select master or gh-pages as your publishing source, you must have the branch present in your repository. If you don't have a master or gh-pages branch, you can create them and then return to source settings to change your publishing source.

1. On GitHub Enterprise, navigate to your GitHub Pages site's repository.

2. Under your repository name, click "Settings". 

3. Use the Select source drop-down menu to select master or gh-pages as your GitHub Pages publishing source.

4. Click "Save".

### <ins>Publishing your GitHub Pages site from a /docs folder on your master branch</ins>

To publish your site's source files from a /docs folder on your master branch, you must have a master branch and your repository must:

- have a /docs folder in the root of the repository

- not follow the repository naming scheme \<username>\.[hostname] or \<orgname>\.[hostname]

1. On GitHub Enterprise, navigate to your GitHub Pages site's repository.

2. Create a folder in the root of your repository on the master branch called /docs.

3. Under your repository name, click "Settings".

4. Use the Select source drop-down menu to select master branch /docs folder as your GitHub Pages publishing source.

5. Click "Save". 

## Cloning a repository

### <ins>Cloning the Repository using the command line:</ins>

1. Log in to GitHub and navigate to the main page of the repository.

2. Above the list of files, click the button "Code".

3. To clone the repository using HTTPS, under "Clone with HTTPS", click the symbol after the link address. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the symbol after the link address.

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned directory.

6. Type "git clone", and then paste the URL you copied earlier.

7. Press "Enter" to create your local clone. 

### <ins>Cloning the Repository to GitHub Desktop:</ins>

1. Log in to GitHub and naviate to the main page of the repository.

2. Above the list of files, click the button "Code".

3. Click "Open with GitHub Desktop" to clone the repository with GitHub Desktop.

4. Follow the prompts in GitHub Desktop to complete the clone.

### <ins>Cloning an empty Repository:</ins>

1. On GitHub, navigate to the main page of the repository.

2. To clone your repository using the command line using HTTPS, under "Quick setup", click the symbol after the link address. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click the symbol after the link address.

    Alternatively, to clone your repository in Desktop, click the dowload symbol. Set up in Desktop and follow the prompts to complete the clone.

3. Open Git Bash.

4. Change the current working directory to the location where you want the cloned directory.

5. Type "git clone", and then paste the URL you copied earlier. 

6. Press "Enter" to create your local clone. 

## Expanding on my project

Is not allowed until I've finished the course at Code Institute. I'll let you know when.

## Credits

### Content
- The sound for interactivity was copied from:   
    [Horse neigh when turning the cards](https://freesound.org/people/GoodListener/sounds/322450/)

    [Applause when 2 cards match](https://freesound.org/people/xtrgamr/sounds/241132/)

    [Fanfare when completing the game](https://freesound.org/people/joepayne/sounds/413203/)

- I found inspiration from/to:

    [Javascript code for soundeffects](https://javascript-tutor.net/index.php/playing-music-using-javascript/)

    [Javascript tutorial for gamelogic](https://www.youtube.com/watch?v=ZniVgo8U7ek)

    [How to create a "new game" button that reset the gameboard](https://www.youtube.com/watch?v=Azl6WzYuvgM)

### Media
The photos used in this site were obtained from:
- First picture of [Balegro](https://www.naturepl.com/cache/pcache2/01524326.jpg), second picture of [Balegro](https://previews.agefotostock.com/previewimage/medibigoff/8c3efac1b7ca508c53cb1b168839eb48/ssj-h-81062098.jpg), third picture of [Balegro](https://media.istockphoto.com/photos/beautiful-american-quarter-horse-stallion-picture-id106413072)

- First picture of [Dimma](https://image.freepik.com/free-photo/american-quarter-horse-buckskin-stallion_74692-145.jpg), second picture of [Dimma](https://thumbs.dreamstime.com/z/wild-stallion-nature-running-gallop-147893469.jpg), third picture of [Dimma](https://media.istockphoto.com/photos/black-stallion-rearing-up-picture-id1034305800)

- First picture of [Offset](https://image.shutterstock.com/image-photo/portrait-running-stallion-black-friesian-260nw-1246577917.jpg), second picture of [Offset](https://c8.alamy.com/comp/XA6CEX/pure-spanish-horse-andalusian-gray-stallion-looking-over-a-hedge-germany-XA6CEX.jpg), third picture of [Offset](https://image.shutterstock.com/image-photo/portrait-brown-stallion-percheron-beautiful-260nw-1214364226.jpg)

- First picture of [Sunrise](https://kppusa.com/wp-content/uploads/2016/11/stallion-supplements.jpg), second picture of [Sunrise](https://images.robertharding.com/zoom/RF/RH_RF/HORIZONTAL/832-387597.jpg),third picture of [Sunrise](https://www.naturepl.com/cache/pcache2/01539794.jpg)

- First picture of [foal](https://media.gettyimages.com/photos/playful-foal-picture-id828105844?s=612x612), second picture of [foal](https://media.gettyimages.com/photos/closeup-image-of-a-new-forest-young-pony-foal-in-the-new-forest-park-picture-id1153450394?s=612x612), third picture of [foal](https://image.shutterstock.com/image-photo/young-bay-foal-galloping-on-260nw-1246728751.jpg)

- First picutre of [foal2](https://image.shutterstock.com/image-photo/newborn-brown-foal-4-days-260nw-1449952289.jpg), second picture of [foal2](https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/14/2019/01/foals-alamy-ATYR5E.jpg), third picture of [foal2](https://image.shutterstock.com/image-photo/beautiful-red-foal-run-fun-260nw-1494066905.jpg)

- First picture of [foal3](https://c8.alamy.com/comp/2BC752B/beautiful-mare-and-foal-running-with-their-herd-on-pasturage-2BC752B.jpg), second picture of [foal3](https://media.istockphoto.com/photos/horses-mare-and-foal-on-meadow-trotting-in-pasture-arabian-horse-picture-id1177258293), third picture of [foal3](https://media.gettyimages.com/photos/icelandic-foal-picture-id828105870?s=612x612)

### Acknowledgements

- Tutors at Code Institute for their support.

- My mentor for his support and ideas. 

- My long-distance boyfriend and my friend for their support.

- I received inspiration for this project from my mentor and my own interest horses.
