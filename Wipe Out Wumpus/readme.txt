
ReadMe File

Jessica Oh Hui Yu

Table of Contents:
Introduction	
Functionalities	
Game Setup	
Options	
Help	
Map	
Move	
Shoot	
Details	
Extra Functionalities
Changes



Introduction

	This ReadMe file illustrates the functionalities of the game called Wipe Out Wumpus. It is a game whereby player has to find and kill a troll named Wumpus, and at the same time avoid the hazards around the map. The functionalities of the game include the game setup, options, help, map, move, shoot and details. Additional functionality and changes made will also be discussed.

	



Functionalities

Game Setup

	When the game begins, introFunction()  is called. introFunction() reads from a file called “intro.txt”. It displays the introduction of the game, illustrating the background context and the aim of the game. 

	The player will be asked to enter his/her name. This name will be stored and loaded so that the name will be used to address the player throughout the game. 

      The player can choose which version of the game does he/she wants to play. The standard version of the game allows the player to start with 5 lantern oils and 5 oil counts. On the other hands, the customised version of the game allows the player to key in as many lantern oil and arrows he/she wants. This would be explained further under the extra functionality below.
      
      The number of lantern oil determines the number of moves the player can take. After each move, the number of lantern oil will decrease by 1. The number of arrows is determined by the number of times the player shoots the arrow. After each shot, the number of arrows will decrease by 1. When the lantern oils or arrows deplete to 0, the player loses the game. 
      
      The functions such as optionsFunction(), introFunction(), helpFunction(), mapFunction() and locationDetailsFunction(); are stored in the functions.hpp and functions.cpp.

Options
	
	Every round, the optionsFunction() will be called. Options reads from a file called “options.txt” and displays it.

      Player gets to choose one of the options from the option list. The player’s option will be stored, and different response will be given, as explained below.
	
Help

	When the player chooses Help, the helpFunction() is called. It reads from the file called “help.txt” and explains how to play the game. Actions taken when meeting the different hazards will also be explained.

	After the help screen is displayed the optionsFunction() will be called again and the player gets to choose his/her next action. 

Map

	When the player chooses Map, the mapFunction() is called. It reads from the file called “map.txt” and displays a map of the 25 areas the player can go to. 

	After the map screen is displayed, the optionsFunction() will be called again and the player gets to choose his/her action.


Move

	Firstly, the hazards location and name of hazards will be created using the Location Class and Hazard Class.

      In the “location.hpp” file, it shows the different variables stored in private so that it cannot be easily assessed by others. Different functions such as the constructor, getting and setting variables are stored in the public. 
      
      In the “location.cpp” file, the constructor reads from a file called “locationsList.txt” and puts the name of the locations into an array. It constructs a new location by taking in the numbers for row and column. 
      
      In the “hazard.hpp” file, it shows the different variables stored in private and different functions are stored in the public.
      
      In the “hazard.cpp” file, the constructor is similar to the one used in location.cpp file. However, now, it takes in an additional variable which is the hazard’s name. Another file called “IncludeEnum.cpp” file is also created to declare the different hazard types such as Wumpus, pit1, pit2, bat1, and bat2.
      
      The rows and columns for the 5 different hazards are generated randomly. At the start of the game, srand(time(NULL)) has to be included to ensure that the number generated on every variable is not the same. The hazard locations are generated as well as the hazard’s name.
      
      The player will be asked whether he/she wants to move up, down, left or right. The function to display the different choices based on the different locations of the player is stored in “location.cpp” and called using oldLocation.updateExit(). The exit choice is stored and used to process the new row and column. The new row and column is processed by increasing and decreasing the row and column by 1, which is called using the functions in “location.cpp” file, oldLocation.getExitRow() and oldLocation.getExitCol().
      
      If the player has lantern oil left and the player’s location changed, the number of lantern oil will decrease by 1 and display the new location. However, if the number of lantern oil decrease to 0, the game will be over, and the player loses. 
      
      In the hazard.cpp file, the player’s location is compared to the hazard’s location. It will determine if the player is one move away from the hazard or in the same area as the hazard checkHazard.getCheckHazard(). If the player is at the same location as the hazard, it will call for the .getHazard() which will display different actions taken based on the different hazards. If the player enters the same location as Wumpus or pits, the player loses and the game is over. If the player enters the same location as the bats, the row and column will be randomly generated, bringing the player to a random location. If the player is a move away from the hazard, different clues will be given to the player using  .clueBats() or .cluePits() or .clueWumpus().
      
      At the end of the move, the optionsFunction() will be called again and player can choose his/her next action.

Shoot

	To shoot, it uses similar functions as move. When the player chooses which exit to shoot at, a new location for the arrow is constructed. When there are arrows left and the player manages to shoot at an exit the number of arrows will decrease by 1. 

	If the player managed to shoot Wumpus, the player wins the game. Otherwise, if the player did not manage to shoot Wumpus and he/she does not have any arrows left, he/she loses the game and the game is over. If he/she still has arrows left, there is a 75% chance that Wumpus wakes up and shift to another location while the other 25% chance that Wumpus goes back to sleep and stays at the same location. 

      Wumpus will shift to one of the adjacent exits which is generated by random, and then increasing and decreasing the row and columns. The random adjacent location Wumpus has to go to will have to be valid. For example, if Wumpus is at the right side of the map, he cannot possibly move to the right. Hence, different movements have to be restricted based on the Wumpus’s location. 

      If Wumpus enters the same area as the player, the player will lose, and the game is over. This is done by comparing the player’s location and Wumpus’s location.	

Details

	When the player chooses Details, the locationDetailsFunction() will be called. It reads from the file called “details.txt” and displays a short description on each of the 25 areas. 

	It will also display the current number of lantern oils and arrows the player has. By displaying newLocation.getLocation(), the current location the player is at will also be showed. 
	



Extra Functionality

	In addition to these functions, extra functionality is added to the game to enhance the player’s experience when playing the game. 

	There will be 2 versions to this game. One of the versions is the standard version whereby the player will start off with 5 arrows and 5 lantern oils. The other version of the game is the customised version. Player will be able to input their desired number of lantern oils and arrows to start with.

	This way, the game will be more suited to more people. Player can train up their skills in this game. If the standard version is too difficult for them, they can start off with a lot more lantern oils and arrows. For example, they could start with 20 lantern oils and 20 arrows. When they got used to the game and their skills improved, they can go on to decrease the number of lantern oils and arrows.

	If the player thinks the game is too easy for them, they can go on to challenge themselves with lesser number of lantern oils and arrows compared to the standard version of the game.

	This additional functionality will be able to provide more flexibility to this game and the player will not lose interest in the game as easily. 



Changes

	Initially, there were 2 additional functionalities planned out for this game. The first additional functionality was to create more useful items such as increasing the number of lantern oils and arrows. The second functionality was to have 2 difficulty levels in the game. The easy level will have 1 Wumpus while the difficult level has 2 trolls which the player has to find and kill. 

      However, after further analysis, the second version of the game is not as feasible as the map is too small and the map will be too congested with different hazards. Hence, the second additional functionality was taken away.










1


