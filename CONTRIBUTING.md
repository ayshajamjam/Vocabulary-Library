## How to Contribute

### Git

We use Git as our version control system.

### Setting up a Development Environment

To set up your local development environment for contributing to the main repository [Vocabulary-Extension](https://github.com/ayshajamjam/Vocabulary-Extension):

- Fork the [Vocabulary-Extension](https://github.com/ayshajamjam/Vocabulary-Extension) repository on GitHub to your account
- Clone your forked repository locally: git clone https://github.com/<your-github-username>/Vocabulary-Extension.git
- Install Python version 3.7.3
- Install virtual environment: python -m venv env
- Activate virtual env: source env/bin/activate
- Install the dependencies: pip install .[develop]
- python setup.py build
- Create a remote link from your local repository to the upstream ayshajamjam/Vocabulary-Extension on GitHub (git remote add upstream https://github.com/ayshajamjam/Vocabulary-Extension) -- you will need to use this upstream link when updating your local repository with all the latest contributions.

### GitHub Pull Requests

- Go to the main branch (git checkout develop);
- Get all the latest work from the upstream repository (git pull upstream main);
- Create a new branch off of main with a descriptive name. You can do it by switching to the develop branch (git checkout <new-branch-name>) and then creating a new branch (git checkout -b <new-branch-name>);
- Do many small commits on that branch locally (git add files-changed, git commit -m "Add some change"). Make these commits descriptive. No need to squash commits.
- Add tests for any new features
- Run the linter and tests to make sure nothing breaks (make lint, make test);
- Push to your fork on GitHub (with the name as your local branch: git push origin branch-name);
- Create a pull request using the GitHub Web interface (asking us to pull the changes from your new branch and add to them our develop branch);
- Wait for comments.

# Tips

- Never use git add .: it can add unwanted files. Add files individually

# Testing

You should write tests for every feature you add or bug you solve in the code. Having automated tests for every line of our code lets us make big changes without worries: there will always be tests to verify if the changes introduced bugs or lack of features. If we don't have tests we will be blind and every change will come with some fear of possibly breaking something.

- Add unit tests to file test_unit.py
- Add integration tests to file test_integration.py

Run "make test" to ensure all tests fail. We use pytest to run tests.

#### Resources Used For This Contributing Page

- [NLTK](https://github.com/nltk/nltk/blob/develop/CONTRIBUTING.md)
