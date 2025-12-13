import aisuite as ai
from aisuite.mcp import MCPClient
import os

prompt = """Create a complete, playable Snake game.

**EXECUTION RULES:**
- Please execute ALL tools silently (no intermediate text responses)
- Write the HTML file FIRST, then provide a brief summary 

**GAME REQUIREMENTS:**
Styling:
- Clean, modern look 
    - Centered on page
    - Nice colors (dark background, gright snack, contrasting food)
    - Clear score display
    - Arrow keys to change direction
    - Instructions shown on screen

**Save the file:**
    - Filename: snake_game.html
    - After saving, respond with confirmation that the game was created
"""

filesystem = MCPClient(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-filesystem", os.getcwd()],
)

model = os.environ['AISUITE_MODEL']
print(f"Using model: {model}")

client = ai.Client()
response = client.chat.completions.create(
    model = model,
    messages=[{"role": "user", "content": prompt}],
    tools=filesystem.get_callable_tools(),
    max_turns=5,
)

for choice in response.choices:
    print(choice.message.content)

filesystem.close()