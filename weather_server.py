import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get real-time weather information for a city.
    Args:
        location: The name of the city (e.g., 'Delhi', 'London').
    """
    try:
        # 1. First, get coordinates (Latitude/Longitude) for the city name
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        
        async with httpx.AsyncClient() as client:
            geo_res = await client.get(geo_url)
            geo_data = geo_res.json()

            if not geo_data.get("results"):
                return f"Could not find coordinates for {location}."

            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
            city_name = geo_data["results"][0]["name"]

            # 2. Get the actual weather for those coordinates
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_res = await client.get(weather_url)
            weather_data = weather_res.json()

            current = weather_data["current_weather"]
            temp = current["temperature"]
            wind = current["windspeed"]

            return f"The current weather in {city_name} is {temp}°C with a wind speed of {wind} km/h."

    except Exception as e:
        return f"Error fetching weather: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")