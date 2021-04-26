# Master of Science in Data Analytics
## Database & Analytics Programming (MSCDAD_JAN21A_I)
* Dr. Athanasios Staikopoulos
* Athanasios.Staikopoulos@ncirl.ie

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.ncirl.ie">
    <img src="Resources/images/NCIRL-logo.png" alt="NCIRL Logo"  width="200">
  </a>

  <h3 align="center">DAP Final Project 2021 - Group #25</h3>
  <h2>[10:31 PM] Tejveer Singh Goraya
    
Assessing the natural causes of mortality based on Healthcare Expenditure of nations in 2019

</h2>
  <p align="center">
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
        <li><a href="#Folder-Content">Folder Content</a></li>
      </ul>
    </li>
    <li>
      <a href="#Folder Content">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
      <a href="#Infraestructure">Infraestructure</a>
      <ul>
        <li><a href="#Database-1">Database 1 - MongoDB</a></li>
        <li><a href="#Database-2">Database 2 - PostgreSQL</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p>
A country's healthcare expenditure plays a major role in the physical and mental well-being of its society and the future generation.As the impact of covid-19(since it mainstream coverage from 2020) has been extensively researched upon throughout the world. This report aims to analyze the major causes of <b>mortality before covid-19</b> impacted the world and how healthcare expenditure influence the mortality of a nation.
</p>
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
    │   ├── DS01-Mexico                     # Mexico Mortality 2019
    │   ├── DS02-US                         # US Mortality 2019
    │   └── DC03-World                      # World Mortality
    ├── Resources                           # PDF and images
    ├── Report                              
    │   └── DAP-Project-Report.pdf          # Final PDF Report
    ├── prerequisites.py                    # Script to install all libraries used in Notebooks 
    ├── LICENSE
    └── README.md


### Prerequisites
* Internet connection
* Pyton > 3.7
* Run `prerequisites.py` to install all the necesary libraries used in notebooks.
* Python Libraries (run `prerequisites.py`)
  ```sh
    import pandas                   #data analysis and manipulation tool
    import psycopg2                 #Library for connection to PostgreSQL
    import pymongo                  #MongoDB Driver
    import pymongo.errors           #mongo errors and exceptions
    import urllib                   #Library to url encode the password
    import os                       #os library to interact with host OS
    import math                     #perforn math operations
    import termcolor                #Function to print console message with colors
    import datetime                 #Library for getting tim
    import requests                 #Library allows to send send HTTP requests
    import urllib                   #Library to make URL request to Wikipedia API
    import matplotlib               #data visualization library 
    import seaborn                  #data visualization library 
    import nltk                     #ligrary for naturale language processing
    import bs4                      #Beautiful Soup web scrapping
    import json                     #JSON formmat manipulation
    import string                   # Common string operations¶
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
