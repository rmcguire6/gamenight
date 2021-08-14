# soloproject-tier3-gamenight

Chingu Solo Project - Tier 3 - Chingu Game Night

# Overview

This project is your chance to go back in time. It's a turn based RPG game. The most popular, longest running example is Final Fantasy.

For this project you're just creating a simple turn based battle. No story, levels or inventory. Just a hero and an enemy taking turns bashing each other until one wins.

# Tech Stacks and Resources

You can use any tech stack you choose. Frameworks and libraries are allowed.

Since this is a time limited project there are sprites you can use in the assets folder of this repo. You can create your own or use another resource, but the goal is to create the basic functionality and user interface.

# Flow of the Game

Turn based battle gives the player and enemy alternating turns. Play does not happen at the same time.
The player picks an attack first and then carries out that attack.After the attack the new enemy hit points and a message to the player are shown. Then the enemy attacks, and in early RPG games it was a fixed attack with varying damage. The new player hit points are shown with a message. If either player or enemy is out of hit points the battle is over.

# Functionality

Pages:

- A home page, or start screen
- A character selection page
- Battle page which shows
  - Enemy image
  - Player image
- Battle results either on the battle page or a results page
- Every page must be responsive and fit on a mobile sized screen as as well as a desktop.

# User Stories

- [ ] User clicks a button or a link to move from the homepage to the selection page
- [ ] User has at least three characters to choose from
- [ ] Along with a picture of the character there should be text explaining each character's abilities
- [ ] When the character is selected the user should be sent to the battle page
- [ ] The user's turn should be first
- [ ] The user's character should have at least two abilities it can select against the enemy -- for example fight and defend or cast spell and duck
- [ ] Once a user has chosen an action, the results should be carried out on the battle screen/page
- [ ] Hitpoints(health) of player and enemy should be shown at the end of each turn
- [ ] Battle won if the enemies hit points are at 0 or less
- [ ] Battle lost if the players hit points are at 0 or less
- [ ] User must be able to lose
- [ ] At the end of the battle a message should be shown declaring whether the player won or lost

# For Tier 3

- [ ] Add a place on the home screen for a player to input and then save their first name or select their name from a list of previous players
- [ ] Allow their chosen character to be saved also
- [ ] Save some kind of game stats--could be as simple as Number of Total wins or Percentage of Wins
- [ ] When they navigate to the selection screen show their previous character choice chosen but allow them to change it
