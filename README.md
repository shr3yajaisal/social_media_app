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
4. pip installation should be done.
   - Click for - [How to install pip on command prompt](https://youtu.be/TqE4jBH4Me4?si=0WU8bYP9m9lbqcD3)
   - Click for - [How to install pip on terminal](https://youtu.be/ioZoC8_Hk7o?si=UFm1aVi0EP6HuXgc)

---

### CREATING THE DATABASE IN MacOS
1. Step I - Open terminal
2. Step II - `mysql -u root -p`
3. Step III - `<enter-your-password>`
4. Step IV - `create database social_media_app;`

### CREATING A DATABASE IN WINDOWS -
1. Locate the MySQL `bin` Directory :
   - Open File Explorer.
   - Navigate to MySQL installation folder, typically found at: `C:\Program Files\MySQL\MySQL Server X.X\bin`
   - Copy the full path.
2. Open the System Environment Variables :
   - Press `Windows + S` and search for Environment Variables.
   - Click on Edit the system environment variables.
3. Edit the PATH Variable :
   - In the System Properties window, click on the Advanced tab.
   - Click on Environment Variables.
4. Add the MySQL Path to PATH :
   - Under System Variables, find and select the `Path` variable.
   - Click Edit.
5. Add a New Entry :
   - Click New.
   - Paste the copied MySQL `bin` path.
   - Click OK to close all dialog boxes.
6. Verify the Change :
   - Open a new Command Prompt window.
   - Type - `mysql --version`
5. If `mysql --version` works, then run, `mysql -u root -p`.
7. `<enter-your-password`
8. `create database social_media_app;`

---

### CLONING THE REPOSITORY
1. Ensure GitHub Desktop is installed on your system from [desktop.github.com](https://github.com/apps/desktop)
2. Open GitHub Desktop and sign in with your GitHub account.
3. GitHub Desktop provides a CLI tool github for operations. Ensure it is installed:
   - On **Windows**, it is automatically included.
   - On **MacOS**, you may need to install it using Homebrew : `brew install github/gh/gh`
4. Verify the GitHub installation by using : `github --version` *(syntax is same for both MacOS and Windows)*.
5. In case, `github --version` doesn't work, then use : `gh --version`.
6. - For **Windows**, run : `cd path\to\your\directory`
   - For **MacOS**, run : `cd path/to/your/directory`
7. To clone the repository, run : `git clone <repository-URL>`
   
---

### CREATING THE VIRTUAL ENVIRONMENT -
1. 
