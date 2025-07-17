from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv
# Initialize FastMCP server
mcp = FastMCP("weather")


@mcp.tool()
def sum(a: int, b: int) -> int:
    """
    This function sums the parameters `a` and `b`

    Parameters:
        a: first number to add.
        b: second number to add.
    """
    return a+b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    This function sums the parameters `a` and `b`

    Parameters:
        a: first number to subtract from.
        b: second number to be subtracted.
    """
    return a-b


@mcp.resource(uri="resource://system/users", name="get_my_system_users", mime_type="application/json")
def get_users():
    return [
        {
            "username": "luna.wolf",
            "password": "X9br!fP2eL",
            "email": "luna.wolf@example.com",
            "bod": "1991-07-12"
        },
        {
            "username": "marko_r89",
            "password": "Tj2@4qLmNp",
            "email": "marko.r89@example.net",
            "bod": "1989-03-29"
        },
        {
            "username": "sakura.kimura",
            "password": "Mi4#rLe2Zq",
            "email": "sakura.kimura@example.org",
            "bod": "1995-11-06"
        },
        {
            "username": "james_cole23",
            "password": "Ws!8xDf3Ky",
            "email": "james.cole23@example.com",
            "bod": "1990-05-20"
        },
        {
            "username": "amanda.bee",
            "password": "Zy5@cMw7Ln",
            "email": "amanda.bee@example.io",
            "bod": "1993-12-03"
        },
        {
            "username": "ronny_dev",
            "password": "Gp2#nKy9Qw",
            "email": "ronny.dev@example.dev",
            "bod": "1987-02-14"
        },
        {
            "username": "tara_skye",
            "password": "Kq7!dBx5Ru",
            "email": "tara.skye@example.com",
            "bod": "1999-08-25"
        },
        {
            "username": "liam.ocean",
            "password": "Ue6@hLm2Vi",
            "email": "liam.ocean@example.org",
            "bod": "1992-01-09"
        },
        {
            "username": "zoe_kane",
            "password": "Fr1#pGy8Oz",
            "email": "zoe.kane@example.com",
            "bod": "1996-04-18"
        },
        {
            "username": "ben_foster44",
            "password": "Yx9!vRu3Hp",
            "email": "ben.foster44@example.net",
            "bod": "1988-10-30"
        }
    ]


@mcp.tool()
def get_current_weather(location: str):
    """
    Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.

    Current object contains current or realtime weather information for a given city.
    Parameters:
        location: (str) Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name.
    """
    load_dotenv()
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?q={location}&key={WEATHER_API_KEY}")
    data = response.json()
    return data


@mcp.tool()
def get_weather_forecast(location: str, days: int = 3, aqi: str = "no", alerts: str = "no"):
    """
    Forecast weather API method returns, depending upon your price plan level, upto next 14 day weather forecast and weather alert as json or xml. The data is returned as a Forecast Object.

    Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city.
    Parameters:
        location: (str) Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name.
        days: (int) Number of days of weather forecast. Value ranges from 1 to 14
        aqi: (str) Air Quality Index. Default is "no". Set to "yes" to include Air Quality data in forecast.
        alerts: (str) Weather alerts. Default is "no". Set to "yes" to include alerts in forecast.
    """
    load_dotenv()
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    response = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?q={location}&days={days}&alerts={alerts}&aqi={aqi}&tp=24&key={WEATHER_API_KEY}")
    data = response.json()
    return data


if __name__ == "__main__":
    mcp.run(transport='stdio')
