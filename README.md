# Master of Science in Data Analytics
## Database & Analytics Programming (MSCDAD_JAN21A_I)
* Dr. Athanasios Staikopoulos
* Athanasios.Staikopoulos@ncirl.ie

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.ncirl.ie">
    <img src="Resources/images/NCIRL-logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">DAP Final Project 2021</h3>

  <p align="center">
    <br />
    <a href="https://github.com/raulsainz/MSCDA-JAN01A-DAP"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/raulsainz">Raul Sainz (19158696)</a>
    ·
    <a href="https://github.com/sadhvidubey22">Sadhvi Rajkumar (19199350)</a>
    ·
    <a href="https://github.com/tejveersinghgoraya">Tejveer Singh (19202687)</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#Running VM Instances">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Your project must incorporate the following elements/tasks:
1. Three or four semi-structured datasets must be used, depending on whether there are 3 or 4
members in each group.
2. Datasets must be programmatically stored in appropriate database(s) prior to processing.
3. Programmatic pre-processing, transformation, analysis and visualisation of the data.
4. Programmatically storing the processed output data in appropriate databases.
5. Programmatically create a dataset that joins together the initial datasets (or data resulting
from processing the initial datasets) for a further analysis of the resultant dataset.
6. Report writing.

### Built With

Major frameworks used to built the project
* [Python 3.7](https://www.python.org)
* [Jupyter Notebook](https://jupyter.org)
* [Anaconda](https://www.anaconda.com)
* [Visual Studio Code](https://code.visualstudio.com)



<!-- GETTING STARTED -->
## Getting Started

The project contains 4 Notebooks

### Prerequisites

Libraries dependencies
* npm
  ```sh
    import pandas
    import psycopg2                   #Library for setting up the connection to PostgreSQL
    import psycopg2.extras as extras 
    import pymongo                  #MongoDB Driver
    import pymongo.errors 
    import urllib                   #Library to url encode the password
    import os                       #os library to interact with host OS
    import math
    import termcolor                #Function to print console message with colors
    import datetime                 #Library for getting tim
    import requests                 #Library allows to send send HTTP requests
    import urllib                   #Library to make URL request to Wikipedia API
    import matplotlib
    import seaborn
    import nltk                     #ligrary for naturale language processing
    import string
  ```
### Data Base Infraestructure
* DB1 - MongoDB Atlas (24/ availability)
* DB2 - PostgreSQL, Running on Azure VM (restricted availability)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
* Raul Sainz - x19158696@student.ncirl.ie
* Sadhvi Rajkumar - x19199350@student.ncirl.ie
* Tejveer Singh - x19202687@student.ncirl.ie
