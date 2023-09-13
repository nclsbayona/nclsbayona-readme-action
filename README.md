# Version \#2

## For this action you need to have as secrets in your repository

- WAKATIME_API_KEY : Your WakaTime API Key, so the request can be made to the API to get the desired data about your programming activity
- GH_TOKEN: A Github token with repo and user access to publish new readme

Please use:
```yaml
env:
    WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
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
```
