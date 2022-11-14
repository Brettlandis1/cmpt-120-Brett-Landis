# Assignment 4 - Input

Open up your local project folder and create a new folder in your `assignments` folder called `userinput`. Create a file called `guessing_game.py` within that folder. Within that file, copy the following code into it.

```py
def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    # Create a string variable that contains the answer.

    return None # replace this line with your game loop logic.

start()
```

Here are the steps needed to complete the function.

1. First, create a string variable that contains your answer; call it `answer` and make it any animal you can think of. Also print a message at the start of the game explaining the rules.
2. Next, you are to use a `while` loop so that your game will run indefinitely. A `while(condition)` loop has one argument and it takes a boolean value and as long as that condition is `True` the loop will continue.
3. Inside the body of the `while` loop, ask the user to guess the animal; if the guess is correct - `print` a congratulatory message and exit the loop with the `break` keyword. Otherwise, `print` a message to the user their answer is wrong and to guess again.

Test this thoroughly; once you have finished the first three steps and everything works, now you can make some enhancements to the game.

4. Allow the user to exit the game. You can do this breaking out of the loop if the guess is ever `quit`.
5. Convert both the answer and the guess to lower or upper case text such no matter what case their guess is in it will always be the same case as the answer.
6. Give the user a maximum number of 3 guesses.

> Be sure to update the rules at the beginning of the game.

## Finishing the Assignment

Once your game is complete, please submit the assignment by copying the output of `pytest` and pasting into the assignment on iLearn.

Once you have done this, please push your code to your GitHub by running the following:

```bash
# This adds all your code to you your stage.
git add -A

# This commits the added code to your next push with a message.
git commit -m "adding all of my completed labs"

# This actually pushes the code to your remote repository.
git push origin main
```
