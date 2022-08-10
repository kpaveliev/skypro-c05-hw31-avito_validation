# SkyPro.Python course
## HW27. Avito - simple Django app

**Create fixtures and load data**

1. Move to folder "data" (csv files with data are located there)
2. Execute 'python3 csv_to_json.py' (gets data from csv files, converts into json and puts into fixtures folder)
3. Return to project folder and execute 'python3 manage.py loaddata ads.json'
4. Execute 'python3 manage.py loaddata categories.json'

**Available routes and methods**

1. /ad/ - GET, POST
2. /ad/<pk> - GET
3. /cat/ - GET, POST
4. /cat/<pk>/ - GET

Kirill Paveliev/
August 2022