## VisionMarker

This verison is designed specifically for vehicle labelling.

## Install
```
git clone https://github.com/wasit7/visionmarker.git
pip install django-extensions
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Dataset Preparation
  1. create MyUser in the Django Admin, or use setup.sh
  2. copy all images into /static/raw and then start Jupyter using notebook.bat, the import script is the main project directory (load_dataset.ipynb). The resolution of the raw input images must be 960x540, otherwise some additinal configuration is requred in /app/templates/home.html.
  
``` JavaScrit
    var  rmax=540, cmax=960, svg_h=540, svg_w=960;
```

## Run Server
you may run the server locally using the command below or use setup.sh
```
python manage.py runserver
```
