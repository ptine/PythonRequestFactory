# Python request factory
Simple python class using fake user agent and rotating ip to avoid websites server ban or honeypot during scraping tasks

## Installation and usage

1. Create virtual environment:

- on Windows:
```
python -m venv env

.\env\Scripts\activate
```

- on Gnu/Linux:
```
virtualenv env #or python3 -m venv env

source env/bin/activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run from command line
```
python -m request_factory.py
```

4. To use class as library you need to add ```__init__.py``` file to folder

Full article [here](https://www.paolotine.it/webscraping-in-python-rotazione-di-proxy-e-fake-user-agent/)
