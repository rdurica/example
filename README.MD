# Example project #
![GGitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/rdurica/example?style=flat-square)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/rdurica/example/django?style=flat-square)
![GitHub](https://img.shields.io/github/license/rdurica/django-skeleton?style=flat-square)


Base django skeleton for new applications


## Installation ##
1. Clone or download repository
2. Update database connection inside <code>./config/settings.py</code>
3. Install python dependencies <code>pipenv install --dev</code>
4. Activate virtual environment <code>pipenv shell</code>
5. Apply migrations <code>python ./manage.py migrate</code>
6. Create superuser <code>python ./manage.py createsuperuser</code>
7. Run development server <code>python ./manage.py runserver</code>

> **_NOTE:_**  Do not forget to change SECRET_KEY before deploy

## Folder structure ##
New applications always put into <code>./app</code> folder

```
📦root
 ┣ 📂app
 ┃ ┣ 📂core
 ┣ 📂config
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂media
 ┣ 📂static
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜README.MD
 ┗ 📜manage.py
```