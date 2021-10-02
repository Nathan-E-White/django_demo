# Generic App Component Description

For anyone looking at the repo that isn't familiar with Django

# Introduction
When you create a new project in the Django framework it will have a substantial amount of functionality baked into the application that needs to be unlocked.
You create your application/site, whatever, by decomposing the larger project at hand into 'Django apps', which are like subprojects, ideally, each with a
single job to do.

# Creating a new Django App
1. Open your favorite terminal in whatever OS you're using
2. cd into the project root directory
3. Run the following command:
```shell
python manange.py startapp "${NEW_APP_NAME}";
```   
4. Open the file "PROJECT_NAME/settings.py"
5. Add the name of your new app to the "INSTALLED_APPS" variable.

# Contents of a new Django App
1. "__init__.py" defines a Python package
2. "admin.py" settings for web app administrators
3. "apps.py" settings for the app 
4. "models.py" classes that will be converted to database tables by ORM
5. "tests.py" test classes
6. "views.py" classes to define how things are presented

