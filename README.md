# Serverless Stack Python Starter

A simple starter Python project for [Serverless Framework](https://serverless.com/framework/) that uses [virtualenv](https://pypi.python.org/pypi/virtualenv), [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements), and [unittest](https://docs.python.org/2/library/unittest.html#module-unittest).

### Requirements

- [Install Python](https://www.python.org/downloads/release/python-363/)
- [Install Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

### Installation

Create a new project

```sh
$ serverless install --url https://github.com/AnomalyInnovations/serverless-stack-python-starter --name my-project
```

Create a virtual environment for your project

```sh
$ cd my-project
$ virtualenv -p /usr/bin/python3.6 venv
```

Activate the virtual environment

```sh
$ source venv/bin/activate
```

Install Serverless plugin: serverless-python-requirements

```sh
$ npm install
```

### Usage

Install a Python dependency (for ex, [Requests](http://docs.python-requests.org/en/master/))

```sh
$ pip install requests
```

Store a reference to your dependencies

```sh
$ pip freeze > requirements.txt
```

Re-install your dependencies from your requirements

```sh
$ pip install -r requirements.txt
```

Run your tests
```
$ python -m unittest discover -s tests
```

Invoke a function locally

```
$ serverless invoke local -f hello
```

Deactivate your virtual environment

```sh
$ deactivate
```

### Deploying

Deploy your project

```sh
$ serverless deploy
```

Deploy a single function

```sh
$ serverless deploy function --function hello
```

To compile non-pure Python modules, install [Docker](https://docs.docker.com/engine/installation/) and the [Lambda Docker Image](https://github.com/lambci/docker-lambda). And enable enable **dockerizePip** in **serverless.yml**.

```yml
# enable dockerize Pip
custom:
  pythonRequirements:
    dockerizePip: true
```

If you are deploying using [SEED](https://seed.run], you don't need to enable **dockerizePip** or install Docker. [SEED](https://seed.run) does it automatically.

### Support

- Send us an [email](mailto:contact@anoma.ly) if you have any questions
- Open a [new issue](https://github.com/AnomalyInnovations/serverless-es7/issues/new) if you've found a bug or have some suggestions.
- Or submit a pull request!

### Maintainers

Serverless ES7 Service is maintained by Frank Wang ([@fanjiewang](https://twitter.com/fanjiewang)) & Jay V ([@jayair](https://twitter.com/jayair)). [**Subscribe to our newsletter**](http://eepurl.com/cEaBlf) for updates. Send us an [email](mailto:contact@anoma.ly) if you have any questions.
