
The Restaurant booking system

Technologies
1. HTML
2. CSS
3. JavaScript
4. Python+Django

The purpose of this application is for users to view meals and make reservations at the KinKhao Restaurant.
The Template
The front end of the application is designed with bootstrap driven html. These files are stored in the folder named template.
Within this folder is a file named base.html. This file contains the navigation menu and the footer of the entire application. To avoid re-coding the navigation and footer all page, all other pages created will pick the navigation and footer from base.html thanks to the power of Python and Django.
All other needed that are needed in the website will always be added to the template folder.
The Static Folder
The static folder contains the assets of the website. These include the CSS, JavaScript and image files that will be standard across the entire application.
The manage.py runs the server to view the website.
The migration folder is used to migrate the database everytime there is a change


NB:So many issues were encountered while deployng the app to heroku. 
Procfile seamed not to work.
The env.py had to be created to protect some information which affected the functionallity of the app even with the helpof tutors?
