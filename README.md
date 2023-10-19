# Version \#2

## For this action you need to have as secrets in your repository

- WAKATIME_API_KEY : Your WakaTime API Key, so the request can be made to the API to get the desired data about your programming activity
- GH_TOKEN: A GitHub token with repository and user access to publish new readme
- NASA_KEY: A NASA Apod API Key, so the request can be made to the API to get the desired data about a picture of the universe
- NEWS_API_KEY: A News API Key, so the request can be made to the API to get some tech-related news

Please use:
```yaml
env:
    WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
    NASA_KEY: ${{ secrets.NASA_KEY }}
    NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
```
when calling the action.
Here, you can see an example of a workflow that uses this action
```yaml
jobs:
  build:
    name: Update README
    runs-on: ubuntu-latest
    steps:
        - uses: actions/checkout@v2
        - name: Generate README file
          uses: nclsbayona/nclsbayona-readme-action@v2
          env:
            WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
            GH_TOKEN: ${{ secrets.GH_TOKEN }}
            NASA_KEY: ${{ secrets.NASA_KEY }}
            NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
```
