# Extractive Text Summarization

A demo project on extractive text summarization.

## Prerequisites

* Python >= 3.7.4
* pip >= 21.0.1
* git >= 2.23.0
* Docker >= 20.10.2

## Usage

### Without Docker:

```bash
git clone https://github.com/Illumaria/extractive-text-summarization.git
cd extractive-text-summarization/
```

The next two commands are only needed if you want to use a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
```

### With Docker:

```bash
git clone https://github.com/Illumaria/extractive-text-summarization.git
cd extractive-text-summarization/
docker build -t ext_sum .
docker run --rm -p <SOME_UNUSED_PORT>:5000 ext_sum
```

## Work Log

The problem statement and commentaries can be found in a separate [work log](https://github.com/Illumaria/extractive-text-summarization/blob/master/WORKLOG.md) file.
