# Sked-Evento

![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)


# Sked Evento

Sked Evento is an Event Management System which is a full-stack Django web application that offers a clean, descriptive, and interactive user interface for viewing and registering events. It has responsive pages and tabs for viewing, handling, and enrolling in various events.

Event management system is used to manage all the activity related to an event. In any event many institutions work hard to manage these programs. It is also important for event organizerthat he has all the contacts details of these service providers so that he cancontact them any time to plan an event at given time. To manage all theseactivity we have developed this software

This Event Management System Project in Django created using Python Django Framework on the backend with HTML, and JavaScript on the frontend. It has user authentication features for login and registration, as well as a user dashboard for displaying and registering for events.Here students can create a unique account and register for events.This project is easy to understand. This is a design for an event management website for educational institutions called Event Portal, which showcases a variety of events and facilitates registration and its promotion.

You must be wondering what SKED EVENTO means! 'Sked' is the short , informal North American slang word for 'schedule' and 'Evento' is the spanish transalation for the word 'event'.


## Team members

1. Sradha P Naick [https://github.com/SPN-a11y]
2. Majesty Raj [https://github.com/majesty594]
3. Swalih M P[https://github.com/swalihmp]


## Team Id

BFH/rec6UmPeWEqgdV8mX/2021

## Link to product walkthrough

[link to video]


## How it Works ?

1. This is an Online event management system software project that serves the functionality of an event manager. The system allows only registered users to login and new users are allowed to resister on the application. This is a web application developed in Django framework. The project provides most of the basic functionality required for an event. 
    -> It allows the user to select from a list of event types.
    -> Once the user enters an event type , the system then allows the user to register for the event .
    -> All this data is logged in the database and the user is given a conformation message on the screen.
    -> This data is then sent to the administrator (website owner) and they may interact with the client as per his requirements and his contact data stored in the database.

2. Embed video of project demo


## Libraries used

Library Name - Version


## How to configure

1. Clone This Project
2. Go to Project Directory cd django-event-management
3. Create a Virtual Environment python3 -m venv env
4. Activate Virtual Environment source env/bin/activate
5. Install Requirements Package pip install -r requirements.txt
6. Migrate Database python manage.py migrate
7. Create Super User python manage.py createsuperuser


## How to Run

1. After the above configuration , run the webserver:
                python manage.py runserver
2. Finally, open the browser and go to http://127.0.0.1:8000/

For admin panel:
    Username: admin
    Password: admin@123
