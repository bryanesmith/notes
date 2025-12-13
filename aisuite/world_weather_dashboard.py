import aisuite as ai
from aisuite.mcp import MCPClient
import os

capitals = [
    "Washington DC", "Seoul", "New York", "Bangkok", "London", "São Paulo"
]

output_file = 'weather_dashboard.html'

prompt = f"""Create a world weather dashboard for these capitals: {', '.join(capitals)}.

**EXECUTION RULES:**
- Execute ALL tools silently (no intermediate text responses)
- Write the HTML file FIRST, then provide a brief summary

**TASK:**
1. **Fetch Weather Data**
   - Use wttr.in for each city: `https://wttr.in/CityName?format=j1`
   - This returns JSON with current conditions
   - Extract: temperature (°C), weather description, humidity, wind speed
   - Note: wttr.in explicitly allows automated access

2. **Create Single page HTML Dashboard with Tailwind CSS**   
   Each weather card should have:
   - City name (bold, large)
   - Weather emoji (☀️ sunny, 🌧️ rain, ☁️ cloudy, etc.)
   - Temperature in large font
   - Weather description
   - Humidity and wind as smaller details
   - Background color based on temperature:
     * Cold (<10°C): blue tones
     * Mild (10-25°C): green/teal tones  
     * Warm (25-35°C): orange/yellow tones
     * Hot (>35°C): red tones

3. **Styling Requirements**
   - Use Tailwind CSS classes
   - Rounded cards with shadows
   - Responsive grid (2 cols mobile, 3 tablet, 5 desktop)
   - Clean, modern design
   - White text on colored backgrounds
   - Smooth gradients

4. **Save File**
   - Use write_file to save as '{output_file}'

5. **Respond with summary**
   - ONLY after file is written
   - List hottest and coldest cities
   - Any interesting weather patterns
"""

model = os.environ['AISUITE_MODEL']
print(f"Using model: {model}")

client = ai.Client()
tools = []

try:
    # MCP client for filesystem
    tools.append(
        MCPClient(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", os.getcwd()],
        )
    )

    # MCP client for searching web
    tools.append(
        MCPClient(command="uvx", args=["mcp-server-fetch"])
    )

    print(f"Initialized {len(tools)} tool(s).")

    print(f"Fetching weather for {len(capitals)} cities...")

    response = client.chat.completions.create(
        model = model,
        messages=[{"role": "user", "content": prompt}],
        tools=tools[0].get_callable_tools() + tools[1].get_callable_tools(),
        max_turns=20,
    )

    if os.path.exists(output_file):
        print(f"Dashboard created: {output_file}")
    else:
        print("Failed to create dashboard.")

    for choice in response.choices:
        print(choice.message.content)

finally:
    for tool in tools:
        tool.close()
