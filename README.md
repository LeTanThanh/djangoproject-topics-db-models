# djangoproject-topics-db-models

- Reference: https://docs.djangoproject.com/en/5.0/topics/db/models/

- Set up venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install packages

```bash
python3 -m pip install -r requirements.txt
```

- Make migrations

```bash
python3 manage.py makemigrations
```

- Run migrations

```bash
python3 manage.py migrate
```

- Run server

```bash
python3 manage.py runserver
```

- Open web

```bash
127.0.0.1:8000
```

- flake8

```bash
python3 -m flake8
```

- isort

```bash
python3 -m isort .
python3 -m isort . --check
```

- pytest

```bash
python3 -m pytest
```
