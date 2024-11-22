# SOCIAL MEDIA APP

---

### PREREQUISITES
1. Python (3.8 or higher)
   - For installation procedure, use the following link (for both MacOS and Windows) - https://youtu.be/YYXdXT2l-Gg
2. MySQL LTS version (8.3 or higher version)
   - For installation procedure, use the following link (for Windows) - https://youtu.be/a3HJnbYhXUc
   - For installation procedure, use the following link (for MacOS) - https://youtu.be/ODA3rWfmzg8
5. Postman API application
   - For installation procedure, use the following link (for Windows) - https://youtu.be/Hmn5XeZv-GE
   - For installation procedure, use the following link (for MacOS) - https://youtu.be/PkJwV1cB0BQ

---

### CREATING THE DATABASE
1. For MacOS -
   - Step I - `mysql -u root -p`
   - Step II - `<enter-your-password>`
   - Step III - `create database social_media_app;`
2. For Windows -
   - Locate the MySQL `bin` Directory :
     - Open File Explorer.
     - Navigate to MySQL installation folder, typically found at: `C:\Program Files\MySQL\MySQL Server X.X\bin`
     - Copy the full path.
   - Open the System Environment Variables :
     - Press `Windows + S` and search for Environment Variables.
     - Click on Edit the system environment variables.
   - Edit the PATH Variable :
     - In the System Properties window, click on the Advanced tab.
     - Click on Environment Variables.
   - Add the MySQL Path to PATH :
     - Under System Variables, find and select the `Path` variable.
     - Click Edit.
   - Add a New Entry :
     - Click New.
     - Paste the copied MySQL `bin` path.
     - Click OK to close all dialog boxes.
   - Verify the Change :
     - Open a new Command Prompt window.
     - Type - `mysql --version`
   - If `mysql --version` works, then run, `mysql -u root -p`.
   - `<enter-your-password`
   - `create database social_media_app;`

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

###
