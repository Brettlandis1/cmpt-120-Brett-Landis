# Lab 7 - REST APIs

Before we go into building the actual application, we need to take a quick step back to understand at a very high level what a REST API is. Ironically, REST APIs are not something new. It has been around since the year 2000 but has been very popular recently with the rise of JavaScript libraries. If you are curious about all the specific details, I’ll let you go ahead and read about it on Google as I am not trying to bore you with all these crazy details.

At a very high level, REST APIs are a way for developers to pass data back and forth for an application. It uses the concept of CRUD (Create, Read, Update, Delete). CRUD operations are performed on a piece of data inside of a database but with REST APIs we use the verbs POST, GET, PUT, and DELETE instead.

## Instructions

### Step 1: Installing Flask

The first step to get this application up and running is to install Flask. Flask is a micro web framework that allows us to create endpoints inside of Python. It has other functionality, but we only care about the REST APIs here. There are other frameworks out there that allow us to achieve this same functionality, but Flask is a pretty popular framework so we will be working with it in this article.

Add the following lines to your `requirements.txt` file in your root folder of your project.

```bash
# Package is a tool for creating a RESTful interface.
flask
```

Next, ensure that your Python3 virtual enviroment is activated.

1. For Mac and Linux

   ```bash
   # From the root folder in your project.
   source venv/bin/activate
   ```

2. For Windows

   ```bash
   # From the root folder in your project.
   .\venv\Scripts\activate.bat
   ```

And once it is activated; run the following command to actually install `flask` onto your virtual environment.

```bash
# This
pip install -r requirements.txt
```

Once you installed Flask onto Python environment; run the following command to ensure it is installed properly.

```bash
flask --version
```

### Step 2: Analyzing/Running the Flask Application

## So now that we have Flask installed on our machines. We have a file in this package called `main.py` and let's go ahead and open it up and look through the code.

1. The first thing we see at the top of the file is an import of the Flask object from the flask package.

   ```python
   from flask import Flask
   ```

2. The next thing we see is the creation of an instance of the Flask object.

   ```python
   app = Flask(__name__)
   ```

3. The third thing we see is the creation of a function called `hello()`. This is a function but here we see something a little different that what we are normally seeing. This function has something above it called an **_annotation_**. Annotations are used to inform the interpreter and libraries that the following code has a specific function. In our case we are informing the Flask library that the function should be exposed to the web.

4. The last thing we see is the invocation of the Flask object's `run` method which starts our REST API application.

#### Running the Server

Now let us start our Flask application server and test our first endpoint! Run the following code:

```python
python main.py
```

Once the server has started, open up your browser to the following URL: http://127.0.0.1:5000. You should now see the following text displayed in the web page: `"Hello world!"`

### Step 3: Creating a new REST API Endpoint

Now that we have a basic index route that our users can hit, what if our users want to access an endpoint that we expose for some type of model we are creating? Well, this is where we will introduce a REST endpoint into our application.

So this part is almost as simple as the previous step. The concept behind it is the same, we are just going to need to pay attention to a few more parts.

Remember, REST APIs retrieve data from an application as well as giving data to an application. In this case, we are creating an endpoint so that our users can retrieve data from our application. We will not be going over putting data into the application as we would need a database to be set up for that. If you would like to see that, then feel free to leave a response and I will create a tutorial on that!

So let's say that our application stores information about books. Create a list object in our `main.py` file right below the `app` variable declaration.

```python
# Creating a "books" JSON / dict to emulate data coming from a database.
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]
```

Lets also import another library we need to use from the `flask` package. Update your import statement at the top of the file to now be:

```python
from flask import Flask, jsonify
```

Let us create our new endpoint function that retrieves the books we have stored. This time the annotation is going to look a bit different. The route is now accessed by accessing the site with `/books` at the end of the URL. The methods argument signifies what type of operations can be invoked against the input. In this case only `GET` requests can be issued.

```python
@app.route("/books", methods=["GET"])
def get_books():
    # Returns the books list in JSON which stands for JavaScript Object Notation.
    return jsonify({"books": books})
```

Now let's give this a run: http://127.0.0.1:5000/books. You will now see all the books we defined in the books list object in JSON. Keep in mind, typically these REST APIs are used to fetch data from a backend database.

Okay, so now ee have our very own REST API. It returns a JSON to us. So that means if you have ever worked with an API before, this is more or less the format/data that comes back from a REST API. Obviously we won’t be covering all the different endpoints that you can create since that would be too much information in one assignment. We will however create a GET with a specified ID of the model since that is a pretty common endpoint as well.

So now let's create an endpoint that is ID specific.

### Step 4: Creating a new REST API Endpoint that is ID specific

So what if want a REST API endpoint that targets a single book instead of all of them. This is important because one of the main users of REST APIs are web sites. They issue requests against a database backed REST API in order to populate their data and retrieving a single resource is less expensive than everything. Below is the code for the function that will retrieve a book by a specified ID.

```python
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    # Create a dictionary object to hold book data.
    result = {}

    # Iterate through each book in the list.
    for book in books:
        # If the book's id matches what the user passed in; set the result and break.
        if book["id"] == book_id:
            result = jsonify({"book": book})
            break

    # Returns the book in JSON form or an empty dictionary if the book could not be found. Normally would throw a 404.
    return result
```

There you have it. You are probably asking:

> How do we add a new book? How do we update a book?

We will be going over that next week. By the end of this CMPT 120 course you will have created your very own database backed REST API.

## Assignment submission

Access the following 4 endpoints while the flask server is running and take screen shots of each:

- http://127.0.0.1/5000
- http://127.0.0.1/5000/books
- http://127.0.0.1/5000/books/1
- http://127.0.0.1/5000/books/2

Run `pytest` and ensure the 4 test cases pass.

To submit this assignment, upload the four screenshots to the assignment in iLearn and include the output of `pytest` by pasting it into the assignment.

Finally, push your code to GitHub.
