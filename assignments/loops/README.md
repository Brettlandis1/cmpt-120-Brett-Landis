# Assignment 3 - Loops

Open up your local project folder and create a new folder inside `assignments` called `loops`. Copy the the files `test_loops.py` and `myloops.py` into that folder. After that, you must complete the functions in `myloops.py` and make sure that they are included in your `pytest` tests and that they pass.

## Complete the functions

Locate the following file `/assignments/loops/myloops.py` and complete the following methods:

- `calculate_sum`
- `calculate_pi`
- `fibonacci`

These methods are here for you to exercise your problem solving ability, loop creation, working with functions, working with arguments, and more.

### calculate_sum

To complete this function you must create a for loop using the `for` and `range` python keywords. Iterate through the range and add each number up to a variable in your function called `result` (or whatever you want). After the loop has finished adding the numbers, please `return` the result back to the caller.

### calculate_pi

To complete this function you must calculate `pi` using a `for` loop and the [Liebniz Formula for Pi](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80). This formula in Python looks like this:

```python
X = 1 - 4/1 + 4/3 - 4/5 + 4/7 - 4/9 + 4/11 - ...
```

**_Note:_** _this series continues infinitely but we want to get as close to Pi as possible by passing a very high number into the function._

You can compare your value for **Pi** by importing the value from the `math` package like so:

```python
from math import pi

print(pi)
```

### fibonacci

To complete this function you must complete the function that gets the `n` value in the fibonacci series. The [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) is the sum of the previous two numbers in the series. The series starts like:

```python
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]
```

So if you pass in the number 1 into your function; you should get the return value of `0`. If you pass in the number 5 you should get the return value of `3`.

_Remember you functions must return the value, not print it!_

---

## Completing your assignment

In order to complete your assignment, you must have all passing test cases when you run `pytest`. Once they are all successful (this includes labs 1, 2 and 3), you must now push all your code to your remote repository on GitHub.

To do this, you must run:

```bash
# This adds all your code to you your stage.
git add -A

# This commits the added code to your next push with a message.
git commit -m "adding all of my completed labs"

# This actually pushes the code to your remote repository.
git push origin main
```

Once you have finished all of this; please copy the output of your `pytest` command and paste into the assignment submission box on iLearn. Also please include the link to your repository!
