<h1>nclsbayona-readme-action</h1>

<h2>Contents</h2>

<ol>
  <li>
    <details name="info">
      <summary>
        <h3>What this action does?</h3>
      </summary>
      This action builds a file (I usee it for my profile README but it's not limited to that) for you using some APIs and also some information about you.
      <details name="built">
        <summary>
          <h4>What information does this action support?</h4>
        </summary>
        This action supports:
        <ul>
          <li>GitHub username --> github-username</li>
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
    </td></tr>
</table>
<!-- readme: contributors -end -->

<h2>Collaborators</h2>
<!-- readme: collaborators -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/nclsbayona">
            <img src="https://avatars.githubusercontent.com/u/59931437?v=4" width="100;" alt="nclsbayona"/>
            <br />
            <sub><b>nclsbayona</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: collaborators -end -->

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
