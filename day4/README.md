# Day 4

## Topics

  - Decorators
  - Magic Methods
  - Typing
  - REST
  - FastAPI

## Refer

  - https://realpython.com/primer-on-python-decorators/ Decorators
  - https://book.pythontips.com/en/latest/decorators.html More Decorators
  - https://www.tutorialsteacher.com/python/magic-methods-in-python Magic Methods
  - https://www.restapitutorial.com/ REST API Tutorial
  - https://docs.python.org/3/library/typing.html Typing

## Practice

  - Write a decorator that prints the start and end time of the function execution
  - Write a class that overwrites `__str__`, `__add__` magic methods
  - Add typehints to your existing programs above
  - Revisit your existing REST APIs and see if they follow the REST best practices
    - If you're new to rest, just try writing endpoints that are REST compliant for your use case
  - Use pipenv to install FastAPI and try the basic example in the docs.
  - Play with the below code and make sure you undertand decorators.

```python
def print_before_after(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper

def print_done(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('done')
    return wrapper

@print_before_after
@print_done
def hey():
    print("hey")

hey()
```

## Bonus Challenge (Optional)

  - Create a FastAPI app and develop the below endpoints
    - /developers - returns a list of devs
    - /developers/2 - returns dev belongs to the ID 2
    - /developers/512 - returns 404 as we don't have a dev with ID 512
    - /developers/3/skills - returns the list of skills for developer belongs to the ID 3
    - /developers/3/skills/2 - returns the skill belongs to ID 2 for the dev that belongs to ID 3