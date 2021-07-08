# Version \#1

## For this action you need to have as secrets in your repository:

- WAKATIME_API_KEY : Your WakaTime API Key, so the request can be made to the API to get the desired data about your programming activity
- OPEN_WEATHER_MAP_KEY: Your Open Weather map key, so the request can be made to the API to get the desired data about your location's weather
- LOCATION: Your Location's name in a format that Open Weather map can understand.

Please use:
```yaml
env:
    WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
    OPEN_WEATHER_MAP_KEY: ${{ secrets.OPEN_WEATHER_MAP_KEY }}
    LOCATION: ${{ secrets.LOCATION }}
```
when calling the action