import aisuite as ai
from aisuite.mcp import MCPClient
import os

filename = "pokemon_math_game.html"

prompt = f"""Create a web-based math game for kids featuring Pokémon characters.

**EXECUTION RULES:**
- Please execute ALL tools silently (no intermediate text responses)
- Write the HTML file FIRST, then provide a brief summary 

**GAME REQUIREMENTS:**
Rules:
- The game should present simple math problems (addition and subtraction)
- You start with the Bulbasaur character fighting Team Rocket
- The math problems for Bulbasaur are easy, single-digit problems (e.g., 2 + 3, 5 - 1)
- Correct answers deal damage to Team Rocket
- Incorrect answers cause Bulbasaur to take damage
- Bulbasaur and Team Rocket both have 3 health points, displayed on screen
- If Bulbasaur's health reaches 0, the game is over and you lose
- If Team Rocket's health reaches 0, you win and Bulbasaur evolves into Ivysaur and the game ends

Display:
- At the top of the page, show the title "Pokémon Math Battle!"
- Below that, show the Pokemon characters that are battling, along with remaining health
- Below that, show the Pokemon animation (e.g., fighting, evolving)
- Below that, show the current Math problem
- Below that, show a calculator-like screen for inputting answers
- Below that, show buttons for digits 0-9 and a "Submit" button
- The user can either click a number button or type the number using the keyboard
- To submit the answer, they can click the "Submit" button or press Enter

Styling:
- Fun, colorful kid-friendly look
    - The Pokemon animation should look pixelated like a Gameboy Color game
    - The calculator buttons should be large and easy to click
    - The calculator screen should have a digital font
    - The calculator and buttons should have a slight 3D effect and be colorful
    - Instructions shown on screen

**Save the file:**
    - Filename: {filename}
    - After saving, respond with confirmation that the game was created
"""

model = os.environ['AISUITE_MODEL']
print(f"Using model: {model}")

client = ai.Client()

try:
    filesystem = MCPClient(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", os.getcwd()],
    )

    response = client.chat.completions.create(
        model = model,
        messages=[{"role": "user", "content": prompt}],
        tools=filesystem.get_callable_tools(),
        max_turns=25,
    )

    if filename:
        print(f"Game created and saved as: {filename}")
    else:
        print("Failed to create the game file.")

    for choice in response.choices:
        print(choice.message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print(prompt)
    raise e

finally:
    if filesystem:
        filesystem.close() 
