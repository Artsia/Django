{"filter":false,"title":"settings.py","tooltip":"/django_projects/locallibrary/locallibrary/settings.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":32,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":["INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","]"],"id":3},{"start":{"row":32,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    # Add our new application","    'catalog.apps.CatalogConfig', #This object was created for us in /catalog/apps.py","]",""]}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":17},"action":"remove","lines":["TIME_ZONE = 'UTC'"],"id":4},{"start":{"row":110,"column":0},"end":{"row":111,"column":0},"action":"insert","lines":["TIME_ZONE = 'Europe/London'",""]}],[{"start":{"row":110,"column":27},"end":{"row":111,"column":0},"action":"remove","lines":["",""],"id":5}]]},"ace":{"folds":[],"scrolltop":543.5,"scrollleft":0,"selection":{"start":{"row":110,"column":27},"end":{"row":110,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":37,"state":"start","mode":"ace/mode/python"}},"timestamp":1686011973716,"hash":"d81bd5a80a3c1f4808af2d3c428cc2d430e776b0"}