# SOCIAL MEDIA APP

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

### CREATING THE DATABASE IN MacOS
- Step I - Open terminal
- Step II - `mysql -u root -p`
- Step III - `<enter-your-password>`
- Step IV - `create database social_media_app;`

### CREATING A DATABASE IN WINDOWS 
- Step I - Locate the MySQL `bin` Directory :
   - Open File Explorer.
   - Navigate to MySQL installation folder, typically found at: `C:\Program Files\MySQL\MySQL Server X.X\bin`
   - Copy the full path.
- Step II - Open the System Environment Variables :
   - Press `Windows + S` and search for Environment Variables.
   - Click on Edit the system environment variables.
- Step III - Edit the PATH Variable :
   - In the System Properties window, click on the Advanced tab.
   - Click on Environment Variables.
- Step IV - Add the MySQL Path to PATH :
   - Under System Variables, find and select the `Path` variable.
   - Click Edit.
- Step V - Add a New Entry :
   - Click New.
   - Paste the copied MySQL `bin` path.
   - Click OK to close all dialog boxes.
- Step VI - Verify the Change :
   - Open a new Command Prompt window.
   - Type - `mysql --version`
- Step VII - If `mysql --version` works, then run, `mysql -u root -p`.
- Step VIII - `<enter-your-password>`
- Step IX - `create database social_media_app;`

---

### CLONING THE REPOSITORY
1. GitHub Desktop provides a CLI tool github for operations. Ensure it is installed:
   - On **Windows**, it is automatically included.
   - On **MacOS**, you may need to install it using Homebrew : `brew install github/gh/gh`
2. Verify the GitHub installation by using : `github --version` *(syntax is same for both MacOS and Windows)*.
3. In case, `github --version` doesn't work, then use : `gh --version`.
4. - For **Windows**, run : `cd path\to\your\directory`
   - For **MacOS**, run : `cd path/to/your/directory`
5. To clone the repository, run : `git clone https://github.com/shr3yajaisal/social_media_app`
   
---

### ACTIVATING THE VIRTUAL ENVIRONMENT AND INSTALLING REQUIREMENTS' PACKAGES 
- Open terminal.
- Navigate to your project folder - 
  ```bash
  # For Windows
  cd path\to\your\project
  
  # For MacOS
  cd path/to/your/project
- Create the virtual environment -
  ```bash
  # For both MacOS and Windows
  python -m venv venv
  OR
  python3 -m venv venv   # In case you are using python3
- Activate the virtual environment -
  ```bash
  # For Windows
  venv\Scripts\activate

  # For MacOS
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

### CHANGES TO MAKE IN THE CODE FILES
1. social_media_app/app_runner.py -
   - Copy the `path` of the `venv/bin/python`.
   - replace `<version/of/Python/used/within/the/venv>` in line numbers 5, 9 and 13 with the `path`.
2. In user_app/app.py and shared/app.py and post_app/app.py and message_app/app.py -
   - Go to the line number 11.
   - replace `<enter-your-password>` with your actual MySQL password.

---

### CONNECTING THE SOCIAL_MEDIA_APP TO DATABASE 
1. Running the Flask application -
   ```bash
   # For Windows -
   set FLASK_APP=shared/app.py
   # For MacOS -
   export FLASK_APP=shared/app.py
2. Initializing the database migration system -
   ```bash
   # For both Windows and MacOS
   flask db init
3. Generating database migration script -
   ```bash
   # For both Windows and MacOS
   flask db migrate -m "Added new table for user profiles"
4. To apply the latest database migration scripts -
   ```bash
   # For both Windows and MacOS
   flask db upgrade

---

### RUNNING THE app_runner.py 
- Run on the terminal / command prompt -
  ```bash
  # For both MacOS and Windows
  python app_runner.py
  OR
  python3 app_runner.py 

---

### USING THE POSTMAN APPLICATION 
1. After running the app_runner.py, you can see, you will be getting three addresses of the server -
   - Address of the server for user_app - http://127.0.0.1:5001
   - Address of the server for post_app - http://127.0.0.1:5002
   - Address of the server for message_app - http://127.0.0.1:5003
2. Now, for sending message or to create post, first of all you need to create a user.
3. When you go to `social_media_app/shared/post_model.py`, you can see, you have the structure of the user table.

4. **CREATING A COLLECTION ON POSTMAN APPLICATION -**
   - Open the Postman application 
   - open `collections`.
   - select the `+` sign i.e., `create new collection`.
   - select `blank collection`.
   - Give name to your collection.

5. **CREATING A REQUEST ON POSTMAN APPLICATION -**
   - Now, select the **option bar** of your created collection.
   - select the option `Add request`.
   - Give name to your request. For example, here you are going to create a users request, so name it `users`.
   - Place where, `enter URL or paste text` is written, enter the address of the server. Here, we are making the request for users, so we will be adding the address of the user_app. i.e., `http://127.0.0.1:5001`
   - Now go to the `social_media_app/routes/user_routes.py`.
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
   - You will recieve a message like this `{ "message": "User created successfully", "user_id": 1 }`
   - And hence, a user is successfully creted in your database.
  
6. 
