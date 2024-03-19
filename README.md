# PageObjectFinal

## Requirements
- Python 3.10.10
- pytest==8.1.1
- selenium==4.18.1

A browser driver is required in the PATH directory. Chrome, Edge, or Firefox browsers are supported.

## Command for running tests
To run the tests, execute the following command:

```bash
pytest -v -s --tb=line --language=en -m need_review test_product_page.py
