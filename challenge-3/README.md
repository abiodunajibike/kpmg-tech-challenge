## Overview

This python script looks up a key from a nested object and returns its value. If the key doesn't exist, it returns `None`.

- `python3` required

### Usage
- To get nested object value:

    ```
    python3 get_nested_object_value.py --nested_object '{"a":{"b":{"c":"d"}}}' --object_key "a/b/c"
    ```

    Response: `d`

### Unit tests
#### Requirements
Install requirements for running unit tests.
```
pipenv shell
pipenv install --ignore-pipfile
```

#### Run unit tests
```
python3 -m pytest --cov-report term-missing --cov=. test_get_nested_object_value.py
```

```
---------- coverage: platform darwin, python 3.7.9-final-0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
get_nested_object_value.py           32      0   100%
test_get_nested_object_value.py      20      0   100%
---------------------------------------------------------------
TOTAL                                52      0   100%
````