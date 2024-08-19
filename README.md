# Build a Chat Bot with Python & Flask

## Setup Local Environment
### Environment Varibles
A Evironment variable named OPENAI_API_KEY and containing your OpenAI API key. 

## Verify Local Environment

### Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project. 

#### Windows
```
py -m venv .\.venv
```
Or
```
python -m venv .\.venv
```

#### macOS & Linux
```
python -m venv ./.venv
```

Once that completes, also run this command from the same folder.

#### Windows
```
.\.venv\Scripts\activate
```

#### macOS & Linux
```
source .venv/bin/activate
```
### Install Dependencies
Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```
### Create database
The following command creates a new, empty database:
```
./.venv/bin/python tests/create_database.py
```
After creating the database you need to create a new user. Run the application (seeing Running Flask section for instructions), then navigate to "/signup" to create a new user.

### Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you any failing tests. 
```
pytest
```
Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

### Direct Python Execution
#### MacOS
```
./.venv/bin/python openai-streaming-handler.py
```
#### Windows
```
py openai-streaming-handler.py
```
### Running in Flask

You can preview your work by running `flask run` in the root of your fork and then visit`http://localhost:5000` in your browser.
