# Master of Science in Data Analytics
## Database & Analytics Programming (MSCDAD_JAN21A_I)
* Dr. Athanasios Staikopoulos
* Athanasios.Staikopoulos@ncirl.ie

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.ncirl.ie">
    <img src="Resources/images/NCIRL-logo.png" alt="NCIRL Logo"  width="120">
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
        <li><a href="#Folder Content">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#Folder Content">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
      <a href="#Infraestructure">Infraestructure</a>
      <ul>
        <li><a href="#Database 1">Database 1 - MongoDB</a></li>
        <li><a href="#Database 2">Database 2 - PostgreSQL</a></li>
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



<!-- FOLDER CONTENT-->
## Folder Content

    .
    ├── Notebooks                           # Project Notebooks
    │   ├── DS01-Pre-Processing.ipynb       # Notebook - Raul Sainz (19158696)
    │   ├── DS02-Pre-Processing.ipynb       # Notebook - Sadhvi Rajkumar (19199350)
    │   ├── DS03-Pre-Processing.ipynb       # Notebook - Tejveer Singh (19202687)
    │   └── Final-Merged.ipynb              # Final Notebook with Merged Data and visualizations
    ├── Datasets                            # Documentation files (alternatively `doc`)
    │   ├── DS01-Mex                        # Mexico Mortality 2019
    │   └── DC02-Us                         # US Mortality 2019
    ├── Resources                           # PDF and images
    ├── Report                              # Final PDF Report
    ├── LICENSE
    └── README.md


### Prerequisites

Python Libraries
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
## Infraestructure
### Database 1
MongoDB Atlas (24/7 availability)
* DB Engine: Mongo DB Atlas
* Region: AZURE Ireland (northeurope)
* Version 4.4.4
* Cluster name: ClusterDAP
* Tier: M0 Sandbox (General)
* vCPU: Shared
* RAM: Shared
* Storage: 512 MB
### Database 2
Running on Azure VM (restricted availability, please contact Team before running the notebooks to start VM)
* DB Engine: PostgreSQL
* DB Version: 11.11
* Infraestructure: Microsoft AZURE
* Location: West Europe
* VM Size: Standard 
* OS: Linux (debian 10.9)
* vCPU: 1 vcpus
* Memory: 1 GiB
* Storage: 30 GB

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
* Raul Sainz - x19158696@student.ncirl.ie
* Sadhvi Rajkumar - x19199350@student.ncirl.ie
* Tejveer Singh - x19202687@student.ncirl.ie
