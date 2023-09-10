![PyPI - Python Version](https://img.shields.io/pypi/pyversions/privat_exchange_rates?style=for-the-badge)

## bored-api-wrapper
#### What that project can do?

It is a API wrapper for bored API, This wrapper returns a random activity and accept parameters to filter the activities by type, number of participants, price range, and accessibility range.
Also it provides a method of returning last 5 activities.

API is implemented in Flask, database ORM - SQLAlchemy, documentation - Swagger.

---
## How to install it?

#### - Python 3.9
#### - PIP dependencies
```bash
pip install -r requirements.txt
```
---
## How to start it?

#### Database setup
Fill the data in .env file

#### API with Swagger
```bash
python3 run.py
```

To connect:
- API with Swagger: 0.0.0.0:5000
- Swagger: 0.0.0.0:5000/swagger

Also this wrapper can be used via CLI program
```bash
    python3 CLI_program.py new --type education --participants 1 --minprice 0.1
```
```bash
    python3 CLI_program.py list
```
