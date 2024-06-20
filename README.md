<h1>nclsbayona-readme-action</h1>

<h2>Contents</h2>

<ol>
  <li>
    <details name="info">
      <summary>
        <h3>What this action does?</h3>
      </summary>
      This action builds a file (I use it for my profile README but it's not limited to that) for you using some APIs and also some information about you.
      <details name="built">
        <summary>
          <h4>What information does this action support?</h4>
        </summary>
        This action supports:
        <ul>
          <li>
              python-version:
              required: false
              description: 'Python version to use to run the file'
              default: '3.10'
          </li>
          <li>
              drink-format:
              required: false
              default: 'html'
              description: 'The format to output drink instructions (string|html|json|csv)'
          </li>
          <li>
            wakatime-format:
            required: false
            default: 'html'
            description: 'The format to output wakatime information (string|html|json|csv)'
          </li>
          <li>
            wakatime-api-key:
            required: false
            default: ''
            description: 'Wakatime API Key to display information about time on PC. Not adding a value to this input disables the lookup of info on Wakatime servers'
          </li>
          <li>
            nasa-api-key:
            required: false
            default: ''
            description: 'Nasa API Key to display a photo of the universe. Not adding a value to this input disables the lookup of info on Nasa servers'
          </li>
          <li>
            file-path:
            required: false
            default: 'README.md'
            description: 'File path of the file we want to generate'
          </li>
          <li>
            template-file-path:
            required: false
            default: 'render_templates/main_template_file'
            description: 'File path of the template we use to generate the file'
          </li>
          <li>
            github-username:
            required: true
            description: 'Github username of the user running the action'
          </li>
          <li>
            telegram-username:
            required: false
            default: ''
            description: 'Telegram username of the user running the action'
          </li>
          <li>
            twitter-username:
            required: false
            default: ''
            description: 'Twitter username of the user running the action'
          </li>
          <li>
            linkedin-username:
            required: false
            default: ''
            description: 'LinkedIn username of the user running the action'
          </li>
          <li>
            webpage-url:
            required: false
            default: ''
            description: 'The url to the user webpage'
          </li>
          <li>
            webpage-qr:
            required: false
            default: ''
            description: 'A QR to the user webpage'
          </li>
          <li>
            contributions-url:
            required: true
            description: 'URL to a grid an image of user contributions'
          </li>
          <li>
            remove-old-readme:
            required: false
            description: 'Whether or not this action should delete the old README'
            default: true
          </li>
        </ul>
        <br />
      </details>
      <hr />
    </details>
  </li>
  <li>
    <details name="info">
      <summary>
        <h3>How was this action built?</h3>
      </summary>
      This action was built using python. The idea is that you can use this action in your profile README so it captures people's attention when they see it.
      <br />
      <details name="built">
        <summary>
          <h4>Why is this action a composite action?</h4>
        </summary>
        This action is a composite action because I wanted to learn more about them. I understand that It might have been easier to use containers for this since the environment is always the same but the generated file would also be in the container and I did not find how could I share that file with the runner so people could use the generated file the way they wanted (Upload it to a remote server, store it in the repository, upload as an artifact to use it somewhere else ...). So I found it useful to keep this action as a composite action. Anyways, if you want to develop this action using containers feel free to do it (I have to admit I created two other versions that use containers, you can check them at the different branches of this repo!).
        <br />
      </details>
      <details name="built">
        <summary>
          <h4>What steps does this action follow?</h4>
        </summary>
        This action does the following steps:
        <ol>
          <li>Download required files (main.py , requirements.txt and a directory containing the render templates for the file that is going to be generated) </li>
          <li>Remove the old README file</li>
          <li>Setup Python in the runner</li>
          <li>Install the required dependencies</li>
          <li>Generate the file using the main.py</li>
          <li>Delete the downloaded files</li>
        </ol>
        <br />
      </details>
      <hr />
    </details>
  </li>
  <li>
    <details name="info">
      <summary>
        <h3>How can I use this action?</h3>
      </summary>
      To use this action you can include in your workflow file a step that uses this action, defining the variables you want to.
      Here's an example
      <img src="https://github.com/nclsbayona/nclsbayona-readme-action/assets/59931437/96f1f3c8-7103-4f1a-bd38-08d6cd3c60c1" />
      <hr />
    </details>
  </li>
</ol>

<h2>Contributors</h2>
<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/nclsbayona">
            <img src="https://avatars.githubusercontent.com/u/59931437?v=4" width="100;" alt="nclsbayona"/>
            <br />
            <sub><b>nclsbayona</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/semantic-release-bot">
            <img src="https://avatars.githubusercontent.com/u/32174276?v=4" width="100;" alt="semantic-release-bot"/>
            <br />
            <sub><b>semantic-release-bot</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

<h2>Bots</h2>
<!-- readme: bots -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/dependabot[bot]">
            <img src="https://avatars.githubusercontent.com/in/29110?v=4" width="100;" alt="dependabot[bot]"/>
            <br />
            <sub><b>dependabot[bot]</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/github-actions[bot]">
            <img src="https://avatars.githubusercontent.com/in/15368?v=4" width="100;" alt="github-actions[bot]"/>
            <br />
            <sub><b>github-actions[bot]</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: bots -end -->
