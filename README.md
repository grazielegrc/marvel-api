## Introduction

This project was created in order to testing the Marvel API using Python and Behave framework. To further information on how to use this API, please visit the website: https://developer.marvel.com/documentation/getting_started 

## Requirements
- [virtualenv](https://docs.python.org/3.8/library/venv.html) 20.10.0+
- [python](https://www.python.org/downloads/release/python-3810/) 3.8.10+
- [pip](https://pypi.org/project/pip/) 21.3.1+

## Installation

Creating a virtual environment using python3 location. Remember to retrieve the current python location to ensure the correct version.

```bash
virtualenv -p /usr/bin/python3 venv
```

Activating the new virtual environment

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the generator.

```bash
pip install -r requirements.txt
```

## Usage

Run the command below to run all tests:


```bash
behave
```

To run with tags:


```bash
behave --tags=stories
```
To generate xml report:


```bash
behave --junit
```

To generate json report:


```bash
behave -f json.pretty
```

To generate Allure report. First install Allure in your computer, see here: https://docs.qameta.io/allure-report/#_installing_a_commandline
After that, run:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/my_allure
```

Starting Allure server to see the report. On project root folder, run:


```bash
allure serve reports/my_allure
```