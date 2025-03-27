# Gas Utility Project 🚀

A Django-based web application to provide consumer services for gas utilities. This platform allows customers to:
1. Submit service requests online.
2. Track the status of their requests.

## Features ✨

- **Create Service Request**: Users can fill out a form to create service requests, upload attachments, and specify request types.
- **Track Request Status**: View the status of your submitted service requests at any time.

## Tech Stack 🛠️

**Backend**: Django (Python Framework)
**Frontend**: HTML, CSS
**Database**: SQLite (default Django database)

 Demo Video 📹:  https://www.youtube.com/watch?v=2xUiarIj14E 
## Installation Instructions 📝

Follow these steps to set up the project on your local system:

1. Clone the repository:
   git clone <repository-url>
   cd gas_utility_project
   
2.Install dependencies:
pip install -r requirements.txt

3.Apply migrations:
python manage.py makemigrations
python manage.py migrate

4.Run the server:
python manage.py runserver :
Open your browser and navigate to http://127.0.0.1:8000/service/create/ to create a service request.



