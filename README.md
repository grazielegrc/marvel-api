## Introduction

This project has been created in order to testing the Marvel API using Python and Behave framework. To further information on how to use this API, please visit the website: https://developer.marvel.com/documentation/getting_started 

## Requirements
- [virtualenv](https://docs.python.org/3.8/library/venv.html) 20.10.0+
- [python](https://www.python.org/downloads/release/python-3810/) 3.8.10+
- [pip](https://pypi.org/project/pip/) 21.3.1+

## Installation

Creating a virtual environment using python3 location. Remember to retrieve the current python location to ensure the correct version.

```bash
virtualenv -p /usr/bin/python3 venv
```

Activating the new virtual environment:

```bash
source venv/bin/activate
```

Use the package manager pip to install the libs:

```bash
pip install -r requirements.txt
```

## Usage

First of all, open the *params.py* file under *utils* folder and inform your API keys.

After that, run the command below to run all tests:


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

To generate Allure report. First, its necessary to install Allure in your computer, follow here: https://docs.qameta.io/allure-report/#_installing_a_commandline

After that, run:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/my_allure
```

Starting Allure server to see the report. On project root folder, run:


```bash
allure serve reports/my_allure
```