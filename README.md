# Battlesnake

## Overview
The RBC T&amp;O Battlesnake tournament consists of building an algorithm for a Battlesnake.
The rules are as follows:
- If the Battlesnake moves beyond the boundary of the game board, it will be eliminated
- If a Battlesnake collides with another Battlesnake (including itself), it will be eliminated
- A Battlesnake loses 1 health every turn, and it is eliminated if it reaches zero
-    Food across the board restores health and increases the snake's length by one
- In head-to-head collisions, the longer Battlesnake will survive
-    If both snakes are the same length, then both are eliminated

The last Battlesnake remaining is the winner

## Game Spec
- Game board size : 10x10
- Battlesnakes must respond with HTTP 200 OK
- Must take less than 700 ms to respond
- Any error will move the Battlesnake forward
- The game engine runs in GCP US-WEST1

## Battlesnake HTTP API
- GET /
-    Testing latency and defining how the Battlesnake looks
- POST /move
-    Analyze the game board and return the next move
- POST /start , POST /end
-    Allocate and deallocate any game specific resources (optional)

More info : [Battlesnake](https://docs.battlesnake.com/)


## How to run using Replit
- On replit, import this repo
- Run main.py on replit and copy the URL in the webview page
- Create an account on https://play.battlesnake.com
- Import this battlesnake by clicking on "Create a battlesnake" and pasting the URL
- Create a new game to test the snake!
