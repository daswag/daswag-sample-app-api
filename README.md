# DaswagSampleAppApi

This is a sample daSWAG template for your API - Below is a brief explanation of what we have generated for you:

```bash
.
├── README.md                               <-- This instructions file
├── docs                                    <-- Source code for your auto-generated documentation
│   ├── config                              <-- ASCIIDOC Documentation configuration
│   ├── files                               <-- Generated documentation files will be saved here
│   ├── images                              <-- Folder to store your documentation images
│   ├── index.adoc                          <-- First page of your documentation
├── specs                                   <-- Source code for your Api specifications (based on OpenAPI 3 standard)
├── src                                     <-- Source code for a lambda functions
│   ├── __init__.py
│   ├── main.py                             <-- project main function code
│   ├── core                                <-- Project Core utils
│   │   ├── decorator
│   │   │   ├── __init__.py
│   │   │   ├── api_endpoint.py
│   │   │   └── api_required.py
│   │   ├── request
│   │   │   ├── __init__.py
│   │   │   └── api_request.py
│   │   ├── validator
│   │   │   ├── __init__.py
│   │   │   └── uuid_validator.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── response.py
│   ├── handlers                            <-- Project Handlers folder
│   │   └── __init__.py
│   ├── models                              <-- Project Models folder
│   │   ├── __init__.py
│   │   └── model.py
│   ├── schemas                             <-- Project Schemas (from model to JSON) folder
│   │   └── __init__.py
│   ├── services                            <-- Project Services folder
│   │   └── __init__.py
├── dev-requirements.txt                    <-- Python Dev dependencies
├── Makefile                                <-- Command file used to simplify your build / package / deploy / ... process
├── requirements.txt                        <-- Python dependencies
├── setup.py                                <-- Python package setup
├── setup.cfg                               <-- Python package configuration
├── sonar-project.properties                <-- Sonar configuration
├── template.yaml                           <-- SAM Template
├── template-init.yaml                      <-- CloudFormation template used to initialize your workspace
├── test-requirements.txt                   <-- Python Test dependencies
├── tox.ini                                 <-- Tox configuration file
├── VERSION                                 <-- Python package version
└── tests                                   <-- Unit tests
    ├── unit
    │   ├── __init__.py
    │   ├── core
    │   │   ├── __init__.py
    │   │   ├── test_logger.py
    │   │   ├── test_response.py
    │   │   ├── decorator
    │   │   │   ├── __init__.py
    │   │   │   ├── test_api_endpoint.py
    │   │   │   └── test_api_required.py
    │   │   ├── request
    │   │   │   ├── __init__.py
    │   │   │   └── test_api_request.py
    │   │   └── validator
    │   │       ├── __init__.py
    │   │       └── test_validator.py
    ├── __init__.py
    ├── conftest.py                         <-- Test fixtures
```

## Requirements

- AWS CLI already configured with at least PowerUser permission
- [Python 3 installed](https://www.python.org/downloads/)
- [Docker installed](https://www.docker.com/community-edition)
- [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Setup process

### Building the project

[AWS Lambda requires a flat folder](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) with the application as well as its dependencies. When you make changes to your source code or dependency manifest,
run the following command to build your project local testing and deployment:

```bash
make build
```

If your dependencies contain native modules that need to be compiled specifically for the operating system running on AWS Lambda, use this command to build inside a Lambda-like Docker container instead:

```bash
make build-container
```

By default, this command writes built artifacts to `.aws-sam/build` folder.

### Local development

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```

If the previous command ran successfully you should now be able to hit the following local endpoint to invoke your function `http://localhost:3000/hello`

**SAM CLI** is used to emulate both Lambda and API Gateway locally and uses our `template.yaml` to understand how to bootstrap this environment (runtime, where the source code is, etc.) - The following excerpt is what the CLI will read in order to initialize an API and its routes:

```yaml

---
Events:
  HelloWorld:
    Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
    Properties:
      Path: /hello
      Method: get
```

## Packaging and deployment

AWS Lambda Python runtime requires a flat folder with all dependencies including the application. SAM will use `CodeUri` property to know where to look up for both application and dependencies:

```yaml
...
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
            CodeUri: src/
            ...
```

Firstly, we need a `S3 bucket` where we can upload our Lambda functions packaged as ZIP and a technical user following the `Least Privilege principle` before we deploy anything - If you don't have a technical user or a S3 bucket to store code artifacts then this is a good time to create one:

```bash
make deploy-init
```

Next, run the following command to package our Lambda function to S3:

```bash
make package
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
make deploy
```

You can also use directly this command to build / package / deploy your project

```bash
make release
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) for more details in how to get started with AWS SAM. Or see [daSWAG HOWTO Guide] for more details on daSWAG Api component integration.**

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
make output
```

## Production

By default all your resources are going to be built for a development environment. If you need to deploy to other stage, you simply need to add a `STAGE_NAME=your-env` parameters on each previous command.

For example to deploy into production you will have:

```bash
make package STAGE_NAME=prod

make deploy STAGE_NAME=prod

make release STAGE_NAME=prod
```

## Testing

We use **Pytest** and **pytest-mock** for testing our code and you can install it using pip: `pip install pytest pytest-mock`

Next, we run `pytest` against our `tests` folder to run our initial unit tests:

```bash
make test
```

with code coverage report generation

```bash
make test-with-cov
```

**NOTE**: It is recommended to use a Python Virtual environment to separate your application development from your system Python installation.

# Appendix

### Python Virtual environment

**In case you're new to this**, python3 comes with `virtualenv` library by default so you can simply run the following:

1. Create a new virtual environment
2. Install dependencies in the new virtual environment

```bash
make bootstrap
```

**NOTE:** You can find more information about Virtual Environment at [Python Official Docs here](https://docs.python.org/3/tutorial/venv.html). Alternatively, you may want to look at [Pipenv](https://github.com/pypa/pipenv) as the new way of setting up development workflows

## daSWAG CLI commands

daSWAG CLI commands to build, package, deploy and describe outputs defined within the cloudformation stack:

```bash
make build

make package

make deploy

make output

```
