# Web Search Application

This is a Flask-based web application designed to perform searches on various search engines and parse the results. It's compatible with both Windows and Linux operating systems.
- Might need curl on windows but that's about it.
## Features

- Flask web server
- Search functionality for multiple search engines
- Parsing of search results
- Display of search results in a web interface

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.x
- Flask
- An internet connection

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.

## Setting Up a Virtual Environment

It's recommended to set up a virtual environment for Python projects. Here's how you can do it:

### Windows

```bash
py -3 -m venv venv
venv\Scripts\activate
```

### Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
### Installing Dependencies

```
pip install -r requirements.txt
```

### Running the Application

To start the application, run:

```bash
python app.py
```

The application will be accessible at http://127.0.0.1:5000/.

### Usage:

Open your web browser and navigate to http://127.0.0.1:5000/.
Enter your search keywords and select a search engine.
Submit the search to view the results.


### Credits
https://github.com/hoodietramp/capNcook/
