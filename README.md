# INSTRUCTIONS  
** Create a virtual env **

virtualenv -p python3 env
source env/bin/activate

** Install framworks **

pip install django
pip install djangorestframework
pip install django-cors-headers

** Start the project **

django-admin startproject MozioAPI

** Run Server **

python manage.py runserver

# the app will run in http://127.0.0.1:8000

** Create an app in Django Project **

python manage.py startapp ProviderApp

** Register the app **

# In settings.py >> INSTALLED_APPS

INSTALLED_APPS = [
...,
'rest_framework',
'rest_framework.authtoken',
'corsheaders',
'ProviderApp.apps.ProviderappConfig',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
...,
]

** Create classes **

# PROVIDER_CRUD >> models.py

class Provider(models.Model):
    ProviderId = models.AutoField(primary_key=True)
    ProviderName = models.CharField(max_length=50)
    ProviderEmail = models.EmailField(max_length=50)
    ProviderPhoneNumber = models.CharField(max_length=50)
    ProviderLanguage = models.CharField(max_length=50)
    ProviderCurrency = models.CharField(max_length=50)

*** MONGODB CONNECTION ***

pip install djongo
pip install dnspython

DATABASE

username: mozio
password: group

# In settings.py >> DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': 'mongodb+srv://mozio:group@marcelo.1l2i7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
            'name': 'moziodb',
            'authmechanism': 'SCRAM-SHA-1', # For MongoDB Atlas
        }
    }
}

** CREATE A TABLE FOR THE MODEL **

python manage.py makemigrations ProviderApp
python manage.py migrate ProviderApp

# Add serializers.py in the ProviderApp

Help to convert the complex type of models in the native python data type and make easy to conver to json
