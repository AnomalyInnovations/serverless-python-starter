## Steps

1. Install Python
```
$ brew install python3
```

1. Install virtualenv
```
$ pip install virtualenv
```

1. Create a virtual environment for your project
```
$ cd my_project_folder
$ virtualenv -p /usr/bin/python3.6 venv
```

1. Activate virtual environment
```
$ source venv/bin/activate
```

1. Install Serverless plugin: serverless-python-requirements
```
$ npm install
```

1. Install Python dependencies
```
$ pip install -r requirements.txt
```

1. Run tests
```
$ python -m unittest discover -s tests
```

1. Invoke locally
```
$ serverless invoke local -f hello
```

1. Deploy locally
To deploy locally, you need to install docker and enable **dockerizePip** in **serverless.yml**. This requires docker installed on your machine.
```
$ vi serverless.yml

# enable dockerize Pip
custom:
  pythonRequirements:
    dockerizePip: true

$ serverless deploy
```

1. Deploy via Seed  
Do not enable **dockerizePip** as the Seed build environment mimics the Lambda runtime.

1. Deactivate virtual environment
```
$ deactivate
```
