# App-Component-Description-Generic.txt

<p>For anyone looking at the repo that isn't familiar with Django   </p>

<h1> Introduction </h1>
When you create a new project in the Django framework it will have a substantial amount of functionality baked into the application that needs to be unlocked.
You create your application/site, whatever, by decomposing the larger project at hand into 'Django apps', which are like subprojects, ideally, each with a
single job to do.

<h1> Creating a new Django App </h1>
1. Open your favorite terminal in whatever OS you're using
2. cd into the project root directory
3. Run the following command:
   python manange.py startapp "${NEW_APP_NAME}";

# Contents of a new Django App

The Python file manage.py will create a new folder with the appropriate name. Within the 