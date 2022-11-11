# Ejercicio 01

## 1. Create virtual environment

* We create the virtual environment for our project.

  ``` 
  python -m venv venv
  ````
  
* We activate our virtual environment.

  ```bash
  source venv/bin/activate
  ````

## 2. Install requirements

* We install requirements using requirements.txt file.

  ```bash
  pip install -r requirements.txt
  ````

## 3. Run

* To run the application.

  ```bash
  python main.py
  ````
* To run _mypy_.

  ```bash
  mypy main.py --check-untyped-defs --ignore-missing-imports
  ````

