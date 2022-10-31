# Lab 6 - Error Handling

Error handling is a major part of software development. Not everything always goes according to plan when executing some piece of software. Often times we want to tailor the user output to fit the error case they encountered. We can do this using something called a `try/except` block in Python. This can be done like so:

```python
try:
    # this function can raise an Exception.
    some_function()
    print("Success!)
except Exception as e:
    '''
    if Exception is raised, the print block above will not happen
    and the print statement below will.
    '''
    print("Failed!", e)
```

## Lab steps

Please update the code in the EmailStore.py class in this package. There are various `TODO`s that must be completed in order for this code to work the way I want it to. It may require you to use `try/except` or `if/elif/else` to handle the error scenarios.

The `add` method must generate an email with the format `{first_name}.{last_name}{count}@marist.edu}`. If an email exists in the store already, increment the count. So for example, if `kevin.hayden1@marist.edu` exists, generate `kevin.hayden2@marist.edu`.

To test your code, you can run the `email_main.py` code or you can activate your environment and run the `pytest` command. All tests should pass.

## Finishing up

When all `pytest` tests pass, please copy the output and paste in the assignment on iLearn and then submit your code to GitHub.
