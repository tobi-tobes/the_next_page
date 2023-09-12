# *The Next Page* - A Free Book Recommendations Website

![The Next Page Homepage](https://i.imgur.com/KBAviT9.png)

## Table of Contents
- [Introduction](#introduction)
    * [The Project](#the-project)
    * [The Team](#the-team)
    * [Blog Posts](#blog-posts)
    * [Visit *The Next Page*](#visit-the-next-page)
- [Getting Technical](#getting-technical)
    * [Overview and Story](#overview-and-story)
    * [Features](#features)
    * [The Console](#the-console)
    * [The Database Schema](#the-database-schema)
    * [RESTful API](#restful-api)
    * [Server/Deployment](#serverdeployment)
    * [Future Plans](#future-plans)
- [Getting Started](#getting-started)
    * [Installation](#installation)
    * [Usage](#usage)
- [Tools Used](#tools-used)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [License](#license)

## Introduction
### The Project
*The Next Page* is the ALX Foundations Portfolio Project of Oluwaseyi Salami and Oluwatobi Tijani. The aim of the project is to foster a love of reading and make it easier for people to discover new books based on what they already love to read or because they're in the mood to try something new.

### The Team
- Oluwatobi Tijani (Front end): [Github](https://github.com/tobi-tobes), [LinkedIn](https://www.linkedin.com/in/oluwatobi-tijani/)
- Oluwaseyi Salami (Back end): [Github](https://github.com/Pinerealm), [LinkedIn](https://www.linkedin.com/in/osalami/)

### Blog Posts
After the development stage of the project, we wrote a blog post to reflect on our journey building *The Next Page*. Check out the article here:
- Oluwatobi's article: [Introducing The Next Page: A Book Recommendations Website](https://medium.com/@tobioreetijani/introducing-the-next-page-a-book-recommendations-website-912aa262cc85)
<!-- - Oluwaseyi's article: -->

### Visit *The Next Page*
*The Next Page* is free and easy to use; no login required! Visit it here: [*The Next Page*](http://project.web-osalami.tech/the_next_page/)

## Getting Technical
### Overview and Story
Our web application is a Single-Page App, coded with Python on the back end and JavaScript (primarily the jQuery library) on the front end. Since this was a portfolio project for the Foundations section of the ALX Software Engineering program, we wanted to put what we had learned throughout the course into practice.

As such, we focused on utilizing the Python object model, using SQLAlchemy to map our classes into a MySQL database and facilitate CRUD operations, working with Flask to develop a RESTful API for our front-end to interact with our database, and creating an interactive and dynamic front end with HTML, CSS, and jQuery.

The project took about three weeks to complete - two weeks for the main development stage, and the remaining week for clean up.

For the front end, we used HTML, CSS, and JavaScript (with the jQuery library) without any frameworks. We had initially wanted to use the Vue.JS front-end framework, but since the time we had for development was so short, we didn't want to spend the majority of that time battling with learning new syntax and essentially experimenting. We wanted this project to be a reflection of what we'd learned so far while also challenging me in subtle ways and dedicate our time to solidifying our understanding of JavaScript and jQuery.

For the back end, we used plain Python as well as the Flask web framework for the API and the SQLAlchemy library for mapping our Python objects to the MySQL database. These are all technologies we used during the course of the program, and again we wanted to really solidify our understanding of the concepts we had touched on while also challenging ourselves with our unique project requirements.

### Features
The website has a filters section where the user can choose amongst various options to narrow down their recommendations. If no filters are selected, all the books in the database will be retrieved, which allows the user to view all the books on the system. Users can view their recommendations and also click on the book cover to view the book description. We had originally wanted the "bookshelf" portion of the site, which is basically a collection of recommendations that the user has saved, to only be accessible to users who have an account and are logged in. However, for this SPA version of the site, we opted instead for a download feature where a user can download a PDF version of their saved recommendations for future reference. There's also a "random book" feature, where a user can get a random book recommendation from the system, in case they don't have any particular thing they're looking for, so it's much like a fun surprise what they're going to get!

### The Console
The console is a command interpreter that manages *The Next Page* objects. It is written in Python using the `cmd` module. The console allows you to:
- Create a new object
- Retrieve an object from a file, a database etc
- Do operations on objects
- Update attributes of an object
- Destroy an object

The console can be run interactively or non-interactively and can utilize either File Storage or Database Storage. To run the console in interactive mode, run `./console.py`. To run the console in non-interactive mode, `echo "<command>" | ./console.py`. Valid commands for the console include `create <class>`, `show <class> <object_id>`, `update <class> <object_id>`and `destroy <class> <object_id>`.

Within the console, run `help <command>` for more information on each command.

### The Database Schema

![The Next Page Database Schema](https://i.imgur.com/ibNOUES.png)

For the database, we used SQLAlchemy as the ORM to map our objects to the database based on the above schema. This provided a seamless transition between our Python objects and the database tables.

### RESTful API
The API can be found in the `api` directory (once you've cloned the repository) and runs on port 5001. To use the API, curl (terminal) or type in your browser `http://54.82.111.149:5001/api/v1/...` with the following defined routes:

- `/books/random` (GET): retrieves a random book from the database
- `/books` (POST): fetches books based on given book_ids
- `/recommended_books` (POST): retrieves Book objects depending of the JSON in the body of the request
- `/genres/<parent_genre>` (GET): retrieves all Genres with the given parent genre

Full API route definitions can be found in `api/v1/views/genres.py` and `api/v1/views/books.py`. As the full extent of the database schema is realized in the project, more routes will be added.

### Server/Deployment

![The Next Page Infrastructure](https://i.imgur.com/v3Iheq4.png)

*The Next Page* is hosted on a server using Nginx and Gunicorn.

### Future Plans
Future improvements to our project include:
- Integrating Google Books API (or some other book-related API) for populating our database and keeping it constantly updated
- User authentication for extra functionality - rather than a download button, we want logged-in users to be able to access a fancy bookshelf view

## Getting Started
### Installation
Run *The Next Page* from your own system, no internet service required! First of all, you need clone the repository and ensure you have the following dependencies installed:
- Latest version of Python: `apt install python3`
- Flask (supports Python 3.8 and newer): `pip3 install Flask`
- MySQLdb (you need to have MySQL installed `apt install mysql-server`): 
    1. `apt-get install python3-dev`
    2. `apt-get install libmysqlclient-dev`
    3. `apt-get install zlib1g-dev`
    4. `pip3 install mysqlclient`
- SQLAlchemy: `pip3 install SQLAlchemy`

Once all the necessary dependencies have been installed, navigate to `the_next_page` directory (`cd the_next_page`).

The next set is to set up your MySQL database. This tutorial assumes you are able to set up a MySQL server and have already configured your `root` user with a password. Run the following script from within `the_next_page` directory to create the database, user, and password for the project: 

`cat setup_files/setup_mysql_dev.sql | mysql -hlocalhost -uroot -p`

Once that is done, you can import some objects into the database using the Python script (`data_for_tnp_database.py`) in the `setup_files` directory. *The Next Page* is supposed to be run by retrieving data using the Google Books API but we are still working on making that feature seamless. Until then, you can upload books to the database manually with the given script.

First make sure that all tables are created when you run the following script:

```echo "quit" | TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db ./console.py```

Then run the Python script using the following command: 

```TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db setup_files/data_for_tnp_database.py```

The script already has book and genre objects defined within; feel free to add as many more books as you'd like!

Now the database is ready for action! You can now run the API and the main application; both are served by Flask. The API runs on port 5001 while the main application runs on port 5000. To run the the API use the following command:

```TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db TNP_API_HOST=0.0.0.0 TNP_API_PORT=5001 python3 -m api.v1.app```

To run the main application, use the following command:

```TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db TNP_API_HOST=0.0.0.0 TNP_API_PORT=5000 python3 -m web_flask.tnp```

You can run both concurrently on multiple terminals using `tmux`; install with the following command: `apt-get install tmux`, then simply call `tmux` in your terminal. Use `Ctrl + B + "` to split the pane horizontally or `Ctrl + B + %` to split the pane vertically. Use `Ctrl + B + arrow keys` to navigate between panes and run the commands for the API and the application.

Whew! We're almost done here. The last thing to do is navigate to your browser and open `localhost:5000/the_next_page`, and this will allow you to try out *The Next Page*! Have fun!

### Usage
You can also access *The Next Page* directly from the web using the link in the Introduction Section. Here's a breakdown of how to navigate the website:
- First, click on the filters to narrow down your recommendations.


![The Next Page Filters section](https://i.imgur.com/GjYeGHN.png)
- Next, click on the "Get your recommendations" button to view your recommendations. You can also click on "Pick a random book" to select a random book. Click on the book cover to get the book description.


![The Next Page Recommendations section](https://i.imgur.com/MOMQoo6.png)
- View your recommendations in the final section. Here, you can choose to download your recommendations or start from the beginning to get new recommendations.


![The Next Page Bookshelf section](https://i.imgur.com/Bux5SnI.png)

## Tools Used
- **Front-end**: 
    * HTML/CSS
    * JavaScript/jQuery (front-end language)
- **Back-end**:
    * Python (back-end language)
    * MySQL (database management system)
    * Flask (web development framework)
    * SQLAlchemy (ORM)

## Contributing
Your contributions are always welcome! Since we use GitHub Flow, all code changes happen through pull requests:
1. Fork the repo and create your branch from `master`
2. If you've added code that should be tested, make sure to add tests to the `tests` directory (create an appropriate sub-directory)
3. If you've made changes to the API, be sure to update the README documentation
4. Make sure that all tests pass!
5. Make sure that your code is `pycodestyle` (Python) and `semistandard` (JavaScript) approved!
6. Issue your pull request!

Some further guidelines:
- We use GitHub Issues to track bugs. Feel free to report a bug by opening up a new issue. Bug reports should be detailed, including background and sample code.

Thank you again for thinking of contributing to this project! And many thanks to GitHub user @briandk for the [contributing template](https://gist.github.com/briandk/3d2e8b3ec8daf5a27a62)!

## Related Projects
- The AirBnB Clone - [HBNB](http://54.160.124.170/)

## License
MIT License
