# Bullet Rain [PENDING NAME CHANGE]
- Top-Down 2D Bullet Hell-styled arcade shooter game

- **Development started at:** 23rd November
- **Challenge:** https://itch.io/jam/game-off-2024



## Requirements Gathering Board
- https://trello.com/b/943NztMc/game-off-2024-bullet-hell-and-spotify


## About
- The aim of the game is to create a 2-D top-down arcade shooter where the difficulty of the game is dependent on the BPM or pace of music playing in the background. The faster the music's tempo, the more difficult and challenging a game will be. 

- A player will start with three lives and aim to get the highest score whilst dodging the bullets

- Different enemies will have different shooting styles (we can represent these as polygon hitboxes to represent shooting options as well as strength of an enemy)

- A user will connect a Spotify profile to a game and load a playlist from that profile.

- The user can choose whether or not the playlist goes in order or randomly [TBC]

- The difficulty should vary depending on how big and small the BPM is. The values can be static initially for an MVP but this can be scaled out with API interaction. 

    > If this turns out to be computationally heavy, we can introduce a GO Microservice to stream TCP packets onSongChange to determine difficulty metadata. 

- There is also the challenge of integrating the challenge's theme SECRETS into the game. Here are some ideas:

  - Allow the player to collect letters that spell **SECRETS** and upon completion, launches a special attack on screen or provides some bonus. 
    


## Architecture
- Python3
    > Set virtual environment prior to starting development on a consistent python version with dependencies included on a consistent pip version with a `requirements.txt` file
- Pyxel (Game Engine library): https://github.com/kitao/pyxel 
- Spotify API: https://spotipy.readthedocs.io/en/2.24.0/#getting-started 
- unittest: Unit Testing in Python
- TCP/IP Networks for communication between microservices
- Deployment protocol for distributing executable and code-signing