# Neighbourhood

>[Brian Odhiambo](https://github.com/Brian23-eng)  
  
# Description  
This project allows users to post their hood, hospitals, police stations and businesses around their neighbourhood
##  Live Link  
 Click [View Site](https://hoodart.herokuapp.com/)  to visit the site
  

## User Story  
  
* A user can view different neighbourhoods  
* A user can post their neighbourhood 
* A user can join or leave a different neighbourhood  
* Search for businesses  
* A user can write a post for other users to see
* A user can view their profile page. 
* A user can add a business name that is near the neigbourhood 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash
https://github.com/Brian23-eng/Neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash
 cd Neighbourhood pip install -r requirements.txt 
 ```
##### Install and activate Virtual  
```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies  
```bash
 pip install -r requirements.txt 
``` 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations watch
 ``` 
 Now Migrate

```bash
python manage.py migrate 
```
##### Run the application  
```bash
python manage.py runserver 
```
##### Testing the application  
```bash
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [b.odhiambo.bo@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/brian23-eng/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **BranTech**