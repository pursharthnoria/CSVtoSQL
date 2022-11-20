# CSVtoSQL

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#Setup">Setup</a></li>
    <li><a href="#roadmap">Routes</a></li>
    <li><a href="#contributing">Directory structure</a></li>
    <li><a href="#license">Modules used</a></li>
  </ol>
</details>

#about-the-project

# Setup

The project can be set up by simply running the shell script "setupScript.sh" within the project.
The script will create the virtual environment, install all the libraries and run the application on the localhost at port 5000.
http://localhost:5000/

## Routes for JSON

The following routes are based on the get request that will show the data in both the tables.
1. http://localhost:5000/getMerticTable:  The following link will return the json of all the rows in the Metric Table.
2. http://localhost:5000/getValueDefTable:  The following link will return the json of all the rows in the Value Definition Table.
3. http://localhost:5000/:  Front-end for the qpplication.

## Directory structure:

1. conf directory: Contains the file config.ini which can be edited as per requirements. The requirements are then imported into the code and the code complies based on the imported values.
2. db directory:  Contains the database file. 
3. Resources:  Contains the CSV file to be read.
4. templates:  Contains the template for the front-end.
5. backend.py:  The driver structure of the code. It contains the functions for reading the CSV and uploading data to SQL database.
6. main.py:  The code is responsible for building the bridge between front-end and the backend. 

## Modules used:

1. Pandas:  For reading the CSV and storing data as a dataframe.
2. Flask:  For defining the routes and functionalities.
3. sqlite3:  For interacting with the sqlite database.
4. configparser:  For reading the config.ini file.
