# Example project #
![GGitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/rdurica/example?style=flat-square)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/rdurica/example/django?style=flat-square)
![GitHub](https://img.shields.io/github/license/rdurica/example?style=flat-square)


Django skeleton for new applications


# Installation #
1. Clone or download repository
2. Update database connection inside <code>./config/settings.py</code>
3. Install python dependencies <code>pipenv install --dev</code>
4. Activate virtual environment <code>pipenv shell</code>
5. Apply migrations <code>python ./manage.py migrate</code>
6. Create superuser <code>python ./manage.py createsuperuser</code>
7. Run development server <code>python ./manage.py runserver</code>

> **_NOTE:_**  Do not forget to change SECRET_KEY before deploy

# Coding standards #
When installing dependencies for --dev there are automatically installed tools to format & check code. To run this checks manually use command <code>pre-commit run --all-files</code>

![Screenshot from 2021-09-19 20-45-04](https://user-images.githubusercontent.com/16089770/134048563-fcfbbbc5-ceb5-4710-981f-15db5111cec7.png)


For automatic check before commit initialize hook for your repository using <code>pre-commit install</code>

# Folder structure #
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
## Useful links ##
- [django documentation](https://docs.djangoproject.com/)
- [black](https://github.com/psf/black)
- [pre-commit](https://pre-commit.com/)
- [flake8](https://github.com/PyCQA/flake8)
- [isort](https://github.com/PyCQA/isort)