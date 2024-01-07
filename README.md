# LASER CATS!
A 2D platformer where you're a cat shooting lasers at your mortal enemies!

Made by Anishka Chauhan for CS50 Python's final project 

Last updated: 1/5/2024

[Demo link (in progress)]()
## Description:
The object of the game is to shoot lasers at as many enemy characters as possible. You have 9 lives, and once you lose them, the game is over.

This game is built using the pygames library, and requires an installation in order to be run. 

     pip3 install pygames
### Controls 
* A: Left
* D: Right
* Space: Jump
* left arrow key: shoot lasers left
* right arrow key: shoot lasers right
* q: quit

## Project Strucutre 

The project design is meant to be similar to how standard 2D platformer projects are structured. 

There are the *states* of each game: <span style="color:rgb(255, 179, 90)">playstate, scorestate, titlescreenstate </span>.

Because of circular importing issues, <span style="color:rgb(66, 184, 252)">settings.py</span>. was created in order to initialize any variables across states, such as the display dimensions and state machine dictionary. 

The <span style="color:rgb(56, 224, 185)"> project.py </span> file handles the switching of the states and leaderboard, and a dictionary in <span style="color:rgb(66, 184, 252)">settings.py</span> terminates the game loops in the current game states.

 All sprites are derived from the <span style="color:rgb(255, 88, 120)"> Sprite </span> class in <span style="color:rgb(255, 88, 120)">sprite.py</span>,
 which allows all sprites to have image loading and collision detection capabilities

 #### Player (the cat)
 <span style="color:rgb(152, 80, 226)">player.py</span> and the Player class represent the cat in the game. It also handles lasers being fired, which are stored in a list and iteratively rendered
 #### Enemy
 <span style="color:rgb(79, 150, 225)">enemy.py</span> contains the rendering capabilities for enemies in the game. In the playstate, these enemies are added to a list and iteratively rendered. 

### Play State
<span style="color:rgb(255, 179, 90)">playstate.py </span> handles the gameplay aspect. It creates a new instance of the <span style="color:rgb(255, 85, 141)">Player </span> class and spawns new enemies in intervals between 2 and 4 seconds. There can only be a maximum of 5 enemies spawned, and they move either left or right until they reach the player's most recent x position. If the enemy and player collide, the player loses a life.

A cooldown ensures that a player has ample time to get away from the enemy, and avoid losing multiple lives in one instance.

### Title State
<span style = "color:rgb(97, 179, 122)"> titlescreenstate.py </span> shows the title of the game when the user first starts the game up. Pressing space switches to the game state. 

### Score State 
<span style = "color:rgb(241, 0, 184)"> scorestate.py </span> is used when the game is over. It shows the user's score and directs them to press space in order to move states. Before score state is switched, the console prompts the user to enter their name for the leaderboard, which is then displayed. 

### Spritesheet
In most 2D games, spritesheets are used as a way to save space and easily store different graphical states of characters. I created my own spritesheet using procreate, in which each of my sprites were put in 256px by 256px boxes. Using pygames' image processing tools, I created an image loading utility in the Sprite base class which helped me load specific 256px by 256px tiles. 

Unfortunately, not all the sprites were in perfectly aligned 256px by 256px boxes, so there was some tinkering involved on which part of the spritesheet needed to be converted into an image. 

### Some miscellaneous easter eggs

- The idea of making Laser Cats was based off the [SNL digital short](https://www.youtube.com/watch?v=e5fiBFhf9OQ), also titled Laser Cats. 
- Pressing B when you're on the title screen plays an audio snippet from the first installment of Laser Cats
  
- The music and sounds for the main game were made by me using Bfxr and BeepBox
  
- The "red flag" enemy was added as an inside joke with friends
  
- The number of lives is 9 because cats have 9 lives
  
- The game physics is loosely based off the bird50 project in CS50G
- The cat is orange because let's be real, this game is peak orange cat behavior
  
- Also, all cat behavior exhibited in the game is realistic
</p>
/ᐠ - ˕ -マ₊˚⊹♡₊ ⊹