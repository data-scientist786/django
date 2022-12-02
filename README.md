# django
#Django is a web framework—a set of tools designed to help you build interactive websites
#spec 
1,We’ll write a web app called Learning Log that allows users to
2,log the topics they’re interested in and to make journal entries as they learn about each topic. 
3,The Learning Log home page will describe the site and invite users to either register or log in.
4,Once logged in, a user can create new topics, add new entries, and read and edit existing entries
#Creating a Virtual Environment following commands will used:
cd desktop
mkdir foldername
cd foldername
 python -m venv webapp
 webapp\Scripts\activate 
 pip install django
 django-admin startproject learning_log .
 python manage.py migrate
 python manage.py runserver
 ctrl click url or copy paste in browser
 Note ctrl c (to quit)
 deactivate (to deactivate the virtual env)
