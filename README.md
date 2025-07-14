# 🐢 Turtle-Crossing-Game
<h2>Help the turtle cross the road without getting hit by cars. Each successful crossing increases the game level and speeds up the cars. The game ends when the turtle collides with a car.</h2>
<h3>🧱 Project Structure</h3>
<ul>
  <li><b>The project is modular and organized into several classes:</b>
  <ul>
    <li><b>main.py :</b>	Game loop, key bindings, and game logic</li>
    <li><b>player.py :</b>	Defines the player turtle</li>
    <li><b>car_manager.py :</b>	Generates and moves cars</li>
    <li><b>scoreboard.py :</b>	Displays and updates game level and messages</li>
  </ul>
  </li>
</ul>
<h4>📜 main.py – Game Controller</h4>
  <ul>
    <li><b>Key Responsibilities:</b>
    <ul>
      <li>Sets up the game screen using turtle.Screen().</li>
      <li>Creates the player, car manager, and scoreboard.</li>
      <li>Listens for keypresses to move the turtle (Up arrow).</li>
    </ul>
    </li>
  </ul>
<h4>🐢 player.py – Player Class</h4>
<ul>
  <li><b>Features</b>:
  <ul>
    <li>Starts at a fixed STARTING_POSITION and points upward.</li>
    <li>Moves upward on keypress (go_up()).</li>
    <li>is_at_finish_line() detects when the player reaches the goal (top of the screen).</li>
    <li>go_to_start() resets the player after successful crossing.</li>
  </ul>
  </li> 
</ul>
<h4>🚗 car_manager.py – CarManager Class</h4>
<ul>
  <li><b>Key Roles:</b>
  <ul>
    <li>Randomly creates colored cars of fixed size.</li>
    <li>Ensures cars are generated only every 6 frames (1 in 6 chance).</li>
    <li>Spawns cars randomly along the y-axis, avoiding top and bottom 50px.</li>
    <li>move_cars() shifts all cars to the left.</li>
    <li>level_up() increases the car movement speed after each level.</li>
  </li>
</ul>
<h4>🧮 scoreboard.py – Scoreboard Class</h4>
<ul>
  <li><b>Features:</b>
    <ul>
      <li>Displays the current level on the top-left.</li>
      <li>Displays the current level on the top-left.</li>
    </ul>
  </li>
</ul>
<h4>📦 Modules Used</h4>
<ul>
  <li><b>random :</b>	Randomizes car colors and spawn positions along the y-axis</li>
  <li><b>time :</b>	Adds a small delay (time.sleep(0.1)) to control game frame rate</li>
</ul>
<ul>
  <li>🐢 turtle – Python's Graphics Module
  <ul>
    <li><b>Turtle() –</b> Used to create game elements (player, cars, scoreboard).</li>
    <li><b>Screen() –</b> Sets up the game window.</li>
    <li><b>.penup() –</b> Prevents lines from drawing when moving.</li>
    <li><b>.setheading(90) –</b> Sets direction for turtle.</li>
    <li><b>.listen() + .onkey() –</b> Listens for keypresses.</li>
  </li>
</ul>
