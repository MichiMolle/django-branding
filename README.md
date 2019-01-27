# django-branding
Dynamically change logos and color-schemes of your project in django-admin.

If you want to distribute the awesome Django-Project you just built,
you may want to offer your users the possibility to brand their instance
easily from within the backend.

django-branding provides you with an easy way to add such functionality
to your project.

## Installation
django-branding can not yet be found in PyPI, to install just clone 
the repository, cd into it and use pip to install.

```bash
git clone https://github.com/MichiMolle/django-branding
cd django-branding
pip install .
```

## Configuration

After Installation, the `branding`-Module is available to your project.
First of all add django-branding to your installed apps in settings.py

```python
# yourproject/yourproject/settings.py
"""
...
All the rest of settings.py
...
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # All your other apps go here.
    'branding',
]
```

After that add a `BRANDING`-Variable to your settings.py. This variable
is supposed to be a dict in which you define the default location of your
project-Logo and your default color theme of your project.

```python
# yourproject/yourproject/settings.py
# Branding Variables
BRANDING = {
    'LOGO': 'img/logo.png',
    'COLOR_SCHEME': {
        'Main Color Accents': {
            'class': '.main-accent',
            'background-color': '#61CCC3',
            'color': '#FFCC00',
        },
        'Minor Color Accents': {
            'class': '.minor-accent',
            'background-color': '#F46050',
            'color': '#EBE9DD',
        },
        'Content':{
            'class': '.content',
            'background-color': '#EBE9DD',
            'color': '#000000',
        }
    },
}
```

In order to have the branding configuration affect your project's look,
you have to add the css-classes we just defined, `.main-accent`, 
`.minor-accent` and `.content` to your project's base template. 
Additionally load branding, add the `{% branding 'styles' %}`-templatetag 
to the template's head and `{% branding 'logo' %} wherever you want the 
logo to be displayed.

```html
<!-- yourproject/templates/base.html -->
{% load static %}
{% load branding %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="{% static 'yourapp/css/styles.css %}">
        {% branding 'styles' %}
        <title>Title</title>
    </head>
    <body>
        <header class="main-accent">
            {% branding 'logo' %}
            <button class="minor-accent">
                Log In
            </button>
        </header>
        <content class="content">
            Lorem Ipsum dolor...
        </content>
    </body>
</html>
```

After that our sample Page looks something like this:

IMAGE

Now anybody who installs your project is able to easily customize the
look and feel of their instance by changing the logo and color scheme
from within django-admin.

IMAGE