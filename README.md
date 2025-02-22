# Flask Project

# flask-application-factory
#[Tutorial](https://hackersandslackers.com/flask-application-factory/)
Declare app in method create_app in __init__.py


### Create Virtual
```sh
virtualenv -p python3 env
source env/bin/activate
```

### Install requirements
```sh
sudo apt install python3-pip
pip3 install -r requirements.txt 
```

### Run application (DEV)
```sh
export FLASK_APP=application
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run --host=0.0.0.0 --port=5001
```

### Run consumer on another process(DEV)
```sh
python run_consumer.py
```

### Migration
```sh
flask migratedb
```