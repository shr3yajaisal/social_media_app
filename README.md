# SOCIAL MEDIA APP

---

## Table of Contents
- [About Social Media App](#about-social-media-app)
- [Key Features](#key-features)
  - [User Account Management](#user-account-management)
  - [Posts](#posts)
  - [Direct Messaging (DMs)](#direct-messaging-dms)
  - [Database Integration](#database-integration)
  - [API-Driven Design](#api-driven-design)
  - [Scalable Architecture](#scalable-architecture)
  - [Real-Time Communication](#real-time-communication)
- [Tech Stack](#tech-stack)
- [Instructions to Run Social Media App](#instructions-to-run-social-media-app)
  - [Prerequisites](#prerequisites)
  - [Creating the Database](#creating-the-database)
    - [Creating a Database in MacOS](#creating-a-database-in-macos)
    - [Creating a Database in Windows](#creating-a-database-in-windows)
  - [Cloning the Repository](#cloning-the-repository)
  - [Activating the Virtual Environment and Installing Requirements' Packages](#activating-the-virtual-environment-and-installing-requirements-packages)
  - [Configuring the Code](#configuring-the-code)
  - [Connecting the Social Media App to Database](#connecting-the-social-media-app-to-database)
  - [Running the Application](#running-the-application)
  - [Using the Postman Application](#using-the-postman-application)
    - [Creating a Collection on Postman](#creating-a-collection-on-postman)
    - [Creating a Request on Postman](#creating-a-request-on-postman)
- [Contact](#contact)

---

## ABOUT SOCIAL MEDIA APP
This **Social Media App** is a Flask-based application designed to provide users with an engaging platform for seamless communication, content sharing, and interaction. It features essential functionalities such as user account management, direct messaging (DMs), and post creation. Built using Python, Flask, and MySQL, this app serves as a demonstration of modular application design and API integration for modern social media platforms.

---

### KEY FEATURES

1. **User Account Management**
   - Users can create accounts, update their profiles, and manage their information.
   - Passwords are securely stored using encryption mechanisms.
     
2. **Posts**
   - Users can create, read, update, and delete (CRUD) posts.
   - The app supports multimedia content integration for posts.
   - 
3. **Direct Messaging (DMs)**
   - Users can send and receive direct messages.
   - Users can also delete and edit a message that has already been sent.
     
4. **Database Integration**
   - ata is stored in a MySQL database with tables for users, posts, and messages.
   - SQLAlchemy is used for ORM (Object-Relational Mapping), making database operations efficient and secure.
     
5. **API-Driven Design**
   - The app's endpoints are structured for easy integration with client-side applications or third-party systems.
   - Postman is recommended for API testing and debugging.
     
6. **Scalable Architecture**
   - The application is divided into modules: user_app, post_app, and message_app, making it easy to maintain and extend.
   - Shared resources and configurations are managed centrally in the shared folder.
     
7. **Real-Time Communication**
   - Implements WebSocket or polling-based communication (future improvement).
     
---

### TECH STACK
1. Backend Framework: Flask (Python)
2. Database: MySQL
3. Frontend/API Testing: Postman
4. Additional Libraries:
   - SQLAlchemy for database management.
   - Flask-Migrate for handling database migrations.
   - Cryptography for secure password handling.

---

## INSTRUCTIONS TO RUN SOCIAL MEDIA APP

---

### PREREQUISITES
1. Python (3.8 or higher)
   - Click for - [How to install Python on Windows and MacOS both](https://youtu.be/YYXdXT2l-Gg)
     
2. MySQL LTS version (8.3 or higher version)
   - Click for - [how to install MySQL LTS version on windows](https://youtu.be/a3HJnbYhXUc)
   - Click for - [how to install MySQL LTS version on MacOS](https://youtu.be/ODA3rWfmzg8)
   - **NOTE : use simple passwords that only has characters and numbers while setting up the password for the MySQL to avoid descrepencies (DO NOT USE SPECIAL CHARACTERS)**
     
3. Postman API application
   - Click for - [How to install Postman applciation on windows](https://youtu.be/Hmn5XeZv-GE)
   - Click for - [How to install Postman application on MacOS](https://youtu.be/PkJwV1cB0BQ)
     
4. pip installation
   - Click for - [How to install pip on command prompt](https://youtu.be/TqE4jBH4Me4?si=0WU8bYP9m9lbqcD3)
   - Click for - [How to install pip on terminal](https://youtu.be/ioZoC8_Hk7o?si=UFm1aVi0EP6HuXgc)
     
5. GitHub Desktop
   - Click for - [How to install github desktop on Windows](https://youtu.be/G4SIIp14Xx4?si=dc30HD8PTP50X8NC)
   - Click for - [How to install github desktop on MacOS](https://youtu.be/F1Jx-3QR-NQ?si=wqdh8V-bMPqRwlhN)

---

### CREATING THE DATABASE 

#### Creating a database in MacOS -
1. Open terminal
2. Run:
   ```bash
   mysql -u root -p
3. Enter your MySQL password.
4. Create the database:
   ```bash
   create database social_media_app;

#### Creating a database in Windows 
1. Locate the MySQL `bin` directory :
   - Navigate to `C:\Program Files\MySQL\MySQL Server X.X\bin`.
   - Copy the path.
     
2. Add MySQL to path :
   - Open System Environment Variables:
     - Press `Windows + S` and search for **Environment Variables**.
   - Under **System Variables**, edit the `Path` variable and add the copied MySQL `bin` path.
     
3. Verify Installation :
   - Open a new Command Prompt window and run :
     ```bash
     mysql --version
   - If successful, create the database :
     ```bash
     mysql -u root -p
     create database social_media_app;

---

### CLONING THE REPOSITORY
1. Ensure GitHub CLI is installed -
   - **Windows:** Pre-installed.
   - **macOS:** Install using -
     - ```bash
       brew install github/gh/gh
       
2. Verify installation -
   - ```bash
     github --version
   - if it doesn't work, use -
     ```bash
     gh --version
     
3. Clone the repository:
   ```bash
   git clone https://github.com/shr3yajaisal/social_media_app
   
---

### ACTIVATING THE VIRTUAL ENVIRONMENT AND INSTALLING REQUIREMENTS' PACKAGES 
- Open terminal.
- Navigate to your project folder - 
  - For Windows -
    ```bash
    cd path\to\your\project  
  - For MacOS
    ```bash
    cd path/to/your/project
    
- Create the virtual environment -
  ```bash
  # For both MacOS and Windows
  python -m venv venv
  OR
  python3 -m venv venv   # In case you are using python3
  
- Activate the virtual environment -
  - For Windows
    ```bash
    venv\Scripts\activate

  - For MacOS
    ```bash
    source venv/bin/activate
  
- Installing the packages of the requirements.txt file -
  ```bash
  # For both MacOS and Windows
  pip install -r requirements.txt
  OR
  pip3 install -r requirements.txt   # In case you are using pip3
  
- Installing the package "cryptography" -
  ```bash
  # For both MacOS and Windows
  pip install cryptography
  OR
  pip3 install cryptography

---

### CONFIGURING THE CODE 
1. Update the python path -
   - Open `social_media_app/app_runner.py`.
   - Copy the `path` of the `venv/bin/python`.
   - replace `<version/of/Python/used/within/the/venv>` in line numbers 5, 9 and 13 with the `path`.
     
2. Update MySQL password -
   - In `user_app/app.py`, `shared/app.py`, `post_app/app.py` and `message_app/app.py` -
   - Go to the line number 11.
   - replace `<enter-your-password>` with your actual MySQL password.

---

### CONNECTING THE SOCIAL_MEDIA_APP TO DATABASE 
1. Set the Flask application -
   - For Windows -
     ```bash 
     set FLASK_APP=shared/app.py
   - For MacOS -
     ```bash
     export FLASK_APP=shared/app.py
     
2. Initializing migrations -
   ```bash
   # For both Windows and MacOS
   flask db init
   
3. Generating a migration script -
   ```bash
   # For both Windows and MacOS
   flask db migrate -m "Added new table for user profiles"
   
4. Applying the migrations -
   ```bash
   # For both Windows and MacOS
   flask db upgrade

---

### RUNNING THE APPLICATION 
- Start the application
  ```bash
  # For both MacOS and Windows
  python app_runner.py
  OR
  python3 app_runner.py
  
- The servers will be available at -
  - User App: http://127.0.0.1:5001
  - Post App: http://127.0.0.1:5002
  - Message App: http://127.0.0.1:5003
    
---

### USING THE POSTMAN APPLICATION 
1. Now, for sending message or to create post, first of all you need to create a user.
2. When you go to `social_media_app/shared/post_model.py`, you can see, you have the structure of the user table.

3. **CREATING A COLLECTION ON POSTMAN APPLICATION -**
   - Open the Postman application 
   - open `collections`.
   - select the `+` sign i.e., `create new collection`.
   - select `blank collection`.
   - Give name to your collection.

4. **CREATING A REQUEST ON POSTMAN APPLICATION -**
   - Now, select the **option bar** of your created collection.
   - select the option `Add request`.
   - Give name to your request. For example, here you are going to create a users request, so name it `users`.
   - Place where, `enter URL or paste text` is written, enter the address of the server. Here, we are making the request for users, so we will be adding the address of the user_app. i.e., `http://127.0.0.1:5001`
   - Now go to the `social_media_app/user_app/routes/user_routes.py`.
   - There, you can see that the endpoint of `create_user()` function is `/api/users` and the method is `POST`.
   - Now enter the URL as - `http://127.0.0.1:5001/api/users` and select the method as `POST`.
   - Now, go to the `Headers` column, enter the **key** as `Content-Type` and enter the **value** as `application/json`
   - Now, go to the `Body` column, select `raw` and then, `json`.
   - In the blank space provided, enter the values of the users in the json format.
   - Example -
     ```bash
     {
        "username" : "Shreya",
        "email" : "shreya@example.com",
        "password" : "shreya@123",
        "full_name" : "Shreya Jaisal",
        "bio" : "backend developer"
     }
   - Now click the `send` button.
   - On success, you will see,
     ```bash
     { "message": "User created successfully", "user_id": 1 }
   - And hence, a user is successfully created in your database.
  
5. Explore Additional Routes:
   - check `routes` in -
     - `user_app/routes/user_routes.py`
     - `post_app/routes/post_routes.py`
     - `message_app/routes/message_routes.py`

6. And this is how you can run your social_media_app.

---

For further setup and usage instructions, refer to the "INSTRUCTIONS TO RUN SOCIAL MEDIA APP" section above. If you have suggestions or questions, feel free to email me at shreyajaisal90@gmail.com.
