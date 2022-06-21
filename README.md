# Keywordio

1. This Project is helpful for management of an online library for students and Administrators. 
2. Students and readers can get a list of books with necessary details and the administrators can add those details, signup or edit/delete previously filled data.
3. Only Administrators can signup in this project.

#### This project uses Django as the backend in the project along with basic HTML and CSS for its frontend. 
#### Frontend is made by help of Bookstrap, cloudflare templates.
#### Note: The assests directory if the static directory of the application.

# Base Directory: Keywordio
1. settings.py has all the settings needed in this project along with the database configurations and static, media paths.
2. urls.py has all the templates of urls of apps i.e. library in our case.

# App: Library

1. Consists of the view functions of the pages in views.py
2. The file authorization.py has everything needed for sussesful authorization, logouts and password changing functions.
3. Models.py consists of all the book model along with the abstract user model.
4. Forms.py has the bookForm.
5. The templates directory has all the HTML files whereas the static directory has the css file.
6. The urls.py has all THIS APP urls while the urls.py in base directory has the application's urls.
7. admin.py has the book models and abstract user model registered.

# Ways to use:
~~~
 $ git clone https://github.com/VINAAAYYY/Keywordio.git
~~~
Clone this repository.

Open the terminal in the cloned directory and run the following commands in the terminal:
~~~
 python manage.py makemigrations
 python manage.py migrate
~~~
~~~
 python manage.py createsuperuser
~~~ 
Enter your details so that you have the admin controls.
~~~
python manage.py runserver
~~~
This starts the server in 8000 port.
You can visit `/admin` extention for the Django admin panel of this project.
### The sqlite database is pushed to the branch. 
