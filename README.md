# Blog
A blog web app where users could post and view content
Features include:
1. User Registration
2. Login System
3. User Profile
4. Create, Update and Delete Posts

## Directions for Setting up Environment-

To install the source, pre-requisites include-

- Python 3.6 or above
- Django
- Crispy forms

First, clone this repository onto your system. Then, create a virtual environment (I use anaconda):


Lastly, build the database by making migrations:
```
python manage.py makemigrations
python manage.py migrate
```

## Directions to execute-

Inside the main project directory (the directory with the 'manage.py' file), run the following command to start the server-
```
python manage.py runserver
```

Now open the link shown in the terminal in any browser of your choice.
