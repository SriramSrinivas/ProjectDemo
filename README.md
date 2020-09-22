# ProjectDemo
This project is developed by Sriram Srinivasan, it is a simple web application built using Django (Python).

##Website Functionality
This website will allow users to access list of departments in the university, if you are an admin user you should be able to create new departments, edit and delete existing one.
The website has User interface which allows users to see and do the CRUD functionality, also website has REST end points, which can be accessed using Postman or any Java Script framework such as Angular. In order to use the API's user must be enrolled in the system.

### Steps to Run this project Locally
There are two ways you can run this project, first is simply install Python (version 3 or above), and pip, after installation run the following commands:
1.  pip install Django
2. pip djangorestframeworkork==3.6.3
3. pip install markdown
4. pip install django-filter==1.1
5. pip install psycopg2-binary
6. pip install requests
7. pip install gunicorn==19.6.0
8. pip install django-crispy-forms
9. pip install django-cors-headers


Alternatively, you can add all the dependencies in requirements.txt in parent project project where manage.py is located and run pip install -r requirements.txt.
 I avoided the first approach because of my familiarity with Docker.
Next after installing all of them, lets create migrations to create tables in database using the following command:
1. Navigate to cd uneplan directory  
2. run the command python manage.py makemigrations
3. next run python manage.py migrate to migrate all the files
4. To create super user run python manage.py create superuser, it will ask username and password in command prompt, please enter and once it passes, the user entered will be a admin user.  
5. If you want to add more user not as admin, please do step 4 and later in admin interface add more user as non-admin ( step 4 is only for amdin user )
6.Now all set with database, to run the application type python manage.py runserver

The author assumes that user has some basic knowledge about Unix and how to run the above commands.

## Alternate Way:- 
To try the second apporach, you will need Docker and familiarity with containers and how they work, if you have not used Docker before, please refer to Docker tutorial at web and then try the alternative approach.
The benefit of Docker it will  take care of the dependencies, all you need is to run following commands:

1. sudo docker-compose build
2. sudo docker-compose up  // To bring up the application
3. sudo docker-compose down  // To bring up the application


There is a lot of things which are inside the docker-compose file such as the nginx (webserver), Docker version is mostly used for production deployment also can be used locally, but the way it is set up such that any one who wants to deploy this to production in 
AWS EC2, he can run the Docker commands and make necessary security groups to bring the application Live with in few minutes.



Which ever approach you have used once the server starts running, you should be able to connect via browser to the application 
by typing localhost:8000 or 127.0.0.1:800/, if you are using alternate approach you need to use the nginx port in my case I am using it 100.

Here is what you will see after application is loaded:

![Home](Screenshot%20from%202020-09-22%2007-04-46.png)


Next you can login, by selecting the user you have opted as admin user

 
![Home](Screenshot%20from%202020-09-22%2007-09-30.png)

After the Login screen, if login is successful, you should see the home page as shown below:
 
![Home](Screenshot%20from%202020-09-22%2007-16-50.png)

You should be able to see list of departments, you should be able to edit/Delete/Create since you are an admin user. 

On top of the banner you can see the link to add new Department, once you click (you should see the following page):

![Home](Screenshot%20from%202020-09-22%2007-18-33.png)


In order to add new user (non-admin user), please navigate to localhost:8000/admin/ and you can select add user in the home page, and add user details as shown below:

![Home](Screenshot%20from%202020-09-22%2007-22-02.png)

In order to keep new user as non-admin, please uncheck staff status and supervisor status, as shown in the screen below:


![Home](Screenshot%20from%202020-09-22%2007-23-22.png)

Now you can navigate  home page by typing (localhost:8000/department/) in browser and you can log out and login with new (non-admin user). The non-admin user only has Read access.

If the user is non-admin, when he tries to click edit/delete/create the user sees the following note:

![Home](Screenshot%20from%202020-09-22%2007-27-03.png)


The application API can be consumed with following end points (for testing and demo using Postman)


Enpoints are:-  PUT :localhost:8000/department/4/update/
                GET : localhost:8000/department/read
                POST: localhost:8000/department/update ( Add body while sending request)
                
                
 Example of GET is shown to get an undestanding of how to use API.
 
 ![Home](Screenshot%20from%202020-09-22%2007-31-25.png)
 
 

If you have questions/issues regarding the API/ website, please reach out to me via GitHub. Thank you for your time and checking out my Github webpage.
 






