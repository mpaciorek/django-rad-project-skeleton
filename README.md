# HOW TO USE

## Requirements ##
- python >= 2.6
- pip
- virtualenv/wrapper (optional)


## Installation ##
### Creating the environment ###

```bash
mkdir example_project
cd example_project
```

```bash
virtualenv --no-site-packages env
env/bin/pip install django
env/bin/django-admin.py startproject --template https://github.com/paco1987/django-rad-project-skeleton/zipball/master --extension py,md yourprojectname
```


### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirments/local.txt
```

### Configure project ###
```bash
cp {{ project_name }}/__local_settings.py {{ project_name }}/local_settings.py
vi {{ project_name }}/local_settings.py
```

### Sync database ###
```bash
../env/bin/python manage.py syncdb
```

## Running ##
```bash
../env/bin/python manage.py runserver
```

Open browser to http://127.0.0.1:8000
