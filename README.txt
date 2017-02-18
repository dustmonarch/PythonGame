############################################################################################
Battle Royale
by Thomas Rochman

Character design  and running animation credits: Hope Radel (hvr4gh)

All assets, with the exception of pygame, pycharm, and gamebox were created the creator of 
this game and the character designer (listed above) and, hence, cannot be found anywhere else.
############################################################################################
———————————————————————————————————————————————————
Required equipment:
-A computer with pycharm installed
-Pygame installed in python
-Two keyboards
-A mouse

In order to start the game, move this file to pycharm and run “game.py” file.

Table of Contents
1. Screens
	a. Title
	b. Settings
	c. Game
	d. Ending
2. How to Play
3. Features
———————————————————————————————————————————————————

1. Screens
a. Title
	The title screen includes the basic controls of the game:
		WASD for player 2 movement and Period for player 2 attack
		Arrow keys for player 1 movement and Z for player 1 attack
	On the title screen, by clicking the on or off buttons, the user can decide to play the game with
	only one player or two. If the user decides to play with only one player, the opponent will be a
	simply coded computer AI for practice.
	For the full effect of the game, the user is recommended to play with two players.
b. Settings
	On the settings screen, the user may decide whether to play until a player dies a certain amount of times 	(lives)
	or until the time runs out. These settings can be adjusted by clicking on the either of the two blue boxes 	next to the
	displayed setting.
	In the case of “timed” mode, the winner will be decided by whomever killed the opponent the most times.
	Press the enter key to continue onto the game
c. Game
	On the game screen, two players will be displayed, player 1 controls the character initially on the right 	(red) and player
	2 controls that on the left (blue). Simultaneously, two boxes with the statistics of the characters are 	displayed on the bottom in boxes.
	In these boxes are the rate at which the character will fly once hit by the opponent (displayed as a number 	and a health bar).
	With the exception of the main ground platform, all floating platforms can jumped through and can be fell 	through by pressing the respective
	down buttons.
d. Ending
	The ending screen simply displays who won and by how many kills.

———————————————————————————————————————————————————

2. How to play
	The keys to play are listed in the Title section.

	In order to gain a point and kill the enemy, the player must push the enemy off the stage by hitting them with 	their hit button.
	If the player is on the ground, they can momentarily stun the enemy when hitting them and continue into a 	three-hit combo by pressing
	the punch button multiple times.
	These punches can be directed by pushing directional keys while pushing the punch button.
	If in the air, the first hit will send the enemy flying in the opposite direction according to their hit rate 	displayed at the bottom of the screen.
	Once killed, a player will be revived at the top of the screen and will be invulnerable until they push a key 	to start moving.
	The game ends when the settings criterion has been met.
	There is also an intentional delay in combo hits and after the third hit.

———————————————————————————————————————————————————

3. Features
	User input: of course
	Graphics: of course
	Game start and end: title and end screens
	
	Optional:
		-Animation: Running animations of the characters and the change in images for the character according 			to situtation.
		-Enemies: Optional choice of a simple AI enemy depending on setting choice at beginning of game.
		-Scrolling level: The camera moves along with the positions of the characters and, therefore, the game 			has a dynamic
			level movement.
		-Timer: A timer is displayed in the “Time” mode if chosen.
		-Health meter: The health meter is substituted with a health bar indicating the fly rate of a 				character in their corresponding
			statistics box.
		-Sound effects: Jumping, hitting, and clicking sound effects were made and incorporated in the game.
		-Two players simultaneously: The main aspect of the game is for two players to play against each 			other.