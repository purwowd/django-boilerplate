# django-boilerplate
Boilerplate for new django project


### Setup:
```bash
$ mkdir <new_folder_project>
$ cd <new_folder_project>
$ git clone https://github.com/purwowd/django-boilerplate.git .
$ cd src/django_project/
$ mv config/settings/devs.example.py config/settings/devs.py
$ ./manage.py runserver --settings=config.settings.devs
```

### Command:
  - Generate new `SECRET_KEY` (Important!)
    ```bash
    $ ./manage.py seckeygen --settings=config.settings.devs
 
    ```
    
  - Change project name (optional)
    ```bash
    $ ./manage.py renameproj <new_name> --settings=config.settings.devs
    ```