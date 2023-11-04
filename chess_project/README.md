# Backend Documentation

1. Create a file directory named chessbackend (you can name it anyhow you want - at least be polite!) and open it

    ```
    mkdir chessbackend
    cd chessbackend
    ```

2. Activate the virtual environment to develop in isolation from the rest of file directories available on your local host

    On Windows:
    ```
    python3 -m venv env
    env\Scripts\activate
    ```

    On Linux/Mac:
    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Clone the repository to your computer

    ```
    git clone https://github.com/KNyathi/OnlineChess/tree/master/chess_project
    ```

4. On typing 'ls', the following backend structure should appear:

    ```
    chess_game (directory)
    chess_project (directory)
    README.md
    db.sqlite3
    manage.py
    ```

    This means everything is working in order.

5. Project dependencies - We will be using PostgreSQL for our database, and as a result, you need to configure settings in your computer as follows:

    a) Navigate to the `chess_project` directory and open it. Inside, open a file called 'settings.py'. The following code should appear:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '******',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Fill in the corresponding details for a PostgreSQL hosted locally on your computer (change name, host, port in accordance with your local setup). If you don't have PostgreSQL on your computer, follow the steps below to install it:

    For Ubuntu:

    ```shell
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    sudo systemctl start postgresql.service
    sudo -i -u postgres
    psql
    ```

    b) The frontend will be communicating with our backend (this one) through API Endpoints. In this case, the backend is a REST API in Django. On cloning, everything is already set up, but we will lay out the code below for understanding:

    On navigation to the `chess_project` directory and to the `settings.py` file:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'chess_game',
        'rest_framework',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication'
            # Add more authentication classes if needed
        ],
    }
    ```

6. Database migration

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. Run the server

    ```
    python3 manage.py runserver 8000
    ```

<button id="copy-button">Copy to Clipboard</button>

<script>
    const copyButton = document.getElementById("copy-button");

    copyButton.addEventListener("click", function () {
        const codeSnippet = `git clone https://github.com/KNyathi/OnlineChess/tree/master/chess_project`;
        const textArea = document.createElement("textarea");
        textArea.value = codeSnippet;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("copy");
        document.body.removeChild(textArea);
        alert("Command copied to clipboard!");
    });
</script>

