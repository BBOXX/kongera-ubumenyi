# Kongera Ubumenyi
*A tool to help team members develop their skills and knowledge*

## Overview
This tools will allow people to better understand the current level of their skills in the areas important to success at BBOXX. It will allow you to agree where you want to focus your personal development and communicate these with you manager and track your process on these over time.

## Architecture
The main application is a simple webapp made using the flask framework.
- The flask app uses multiple blueprints to split the functionality into separate modules.
- Flask-admin is used to create and edit objects that only admins are able to access. This admin panel is accessed on /admin
- Flask-login is used to manage users but the authentication is handled by an external active directory server.
- Data is stored in a postgresql database and are accessed through a SQLalchemy ORM.

## Development
This app uses docker and docker-compose to configure a suitable environment. To start a dev environment run ```docker-compose up```. This will create the following services:
- app - the main application code with the flask development server which will reload if source code files are changed in the host environment.
- nginx - a reverse proxy for the app and hosting of the static files
- db - a postgresql database for data persistence, in the dev environment this will be populated with sample data on launch of the application.

To access the webapp just point your browser at <http://127.0.0.1/>

## FAQ
What does Kongera Ubumenyi mean?
It's a translation of Skills Growth or Personal Development in Kinyarwanda.

