# 🐢 Turtle-Crossing-Game
<h2>Help the turtle cross the road without getting hit by cars. Each successful crossing increases the game level and speeds up the cars. The game ends when the turtle collides with a car.
</h2>


Help the turtle cross the road without getting hit by cars. Each successful crossing increases the game level and speeds up the cars. The game ends when the turtle collides with a car.

🧱 Project Structure
The project is modular and organized into several classes:

File	Purpose
main.py	Game loop, key bindings, and game logic
player.py	Defines the player turtle
car_manager.py	Generates and moves cars
scoreboard.py	Displays and updates game level and messages

📜 main.py – Game Controller
Key Responsibilities:
Sets up the game screen using turtle.Screen().

Creates the player, car manager, and scoreboard.

Listens for keypresses to move the turtle (Up arrow).

Main game loop:

Updates the screen and introduces a delay using time.sleep().

Calls create_car() (approx. every 6 loops).

Moves cars with move_cars().

Checks for:

Collision with cars (game over).

Reaching the top (level up, increase speed).

🐢 player.py – Player Class
Features:
Inherits from Turtle.

Starts at a fixed STARTING_POSITION and points upward.

Moves upward on keypress (go_up()).

is_at_finish_line() detects when the player reaches the goal (top of the screen).

go_to_start() resets the player after successful crossing.

🚗 car_manager.py – CarManager Class
Features:
Randomly creates colored cars of fixed size.

Ensures cars are generated only every 6 frames (1 in 6 chance).

Spawns cars randomly along the y-axis, avoiding top and bottom 50px.

move_cars() shifts all cars to the left.

level_up() increases the car movement speed after each level.

🧮 scoreboard.py – Scoreboard Class
Features:
Displays the current level on the top-left.

Updates score using increase_level() when the player completes a level.

Shows "GAME OVER" at the center when the player is hit.

📦 Modules Used
✅ Built-in Python Modules:
Module	Purpose
random	Randomizes car colors and spawn positions along the y-axis
time	Adds a small delay (time.sleep(0.1)) to control game frame rate

🐢 turtle – Python's Graphics Module
Uses Across All Files:
Turtle() – Used to create game elements (player, cars, scoreboard).

Screen() – Sets up the game window.

.shape("turtle" / "square") – Sets shape of objects.

.penup() – Prevents lines from drawing when moving.

.goto(x, y) – Moves turtle to coordinates.

.color() – Changes color of game elements.

.shapesize() – Resizes cars (length and width).

.distance() – Calculates distance between objects (for collision).

.write() – Displays score and messages.

.setheading(90) – Sets direction for turtle.

.listen() + .onkey() – Listens for keypresses.
