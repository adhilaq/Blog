# Blog
A blog web app where users could post and view content.

Features include:
- User Registration
- Login System
- User Profile
- Create, Update and Delete Posts
- Filter posts based on user who created the post


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
