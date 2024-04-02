# PageObjectFinal

## Requirements
- Python 3.10.10
- pytest==8.1.1
- selenium==4.18.1

A browser driver is required in the PATH directory. Chrome or Edge browsers are supported.

## Installation

```bash
pip install -r requirements.txt
```
## Run tests

```bash
pytest -v -s --tb=line --language=en -m need_review test_product_page.py
```

## Bash scripts with a virtual environment
### Installation in a virtual environment
```bash
@echo off

python -m venv venv

call venv\Scripts\activate.bat

pip install -r requirements.txt

pause

deactivate
```
### Launching from a virtual environment
```bash
call venv\Scripts\activate.bat

echo tests is running...

pytest -v -s --tb=line --language=en -m need_review test_product_page.py

pause

deactivate
```
