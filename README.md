# The Next Page
## A Free Book Recommendations Website

### Introduction
#### The Project
The Next Page is the ALX Foundations Portfolio Project of Oluwaseyi Salami and Oluwatobi Tijani. The aim of the project is to foster a love of reading and make it easier for people to discover new books based on what they already love to read or because they're in the mood to try something new.
<img src="https://i.imgur.com/KBAviT9.png" alt="Home Page" style="height: 100px; width:200px;"/>
The website has a filters section where the user can choose amongst various options to narrow down their recommendations. If no filters are selected, all the books in the database will be retrieved, which allows the user to view all the books on the system. Users can view their recommendations and also click on the book cover to view the book description. Users can download a PDF version of their saved recommendations for future reference. There's also a "random book" feature, where a user can get a random book recommendation from the system, in case they don't have any particular thing they're looking for, so it's much like a fun surprise what they're going to get!

#### Getting Technical
##### Overview
Our web application is a Single-Page App, coded with Python on the back end and JavaScript (primarily the jQuery library) on the front end. Since this was a portfolio project for the Foundations section of the ALX Software Engineering program, we wanted to put what we had learned throughout the course into practice. As such, we focused on utilizing the Python object model, using SQLAlchemy to map our classes into a MySQL database and facilitate CRUD operations, working with Flask to develop a RESTful API for our front-end to interact with our database, and creating an interactive and dynamic front end with HTML, CSS, and jQuery.
![The Next Page Infrastructure](https://i.imgur.com/v3Iheq4.png)
##### The Database Schema:
<img src="https://i.imgur.com/ibNOUES.png" alt="Home Page" style="height: 100px; width:200px;"/>

##### API
The API can be found in the `api` directory (once you've cloned the repository) and runs on port 5001. To use the API, curl (terminal) or type in your browser `http://54.82.111.149:5001/api/v1/...` with the following defined routes:
- `/books/random` (GET): retrieves a random book from the database
- `/books` (POST): fetches books based on given book_ids
- `/recommended_books` (POST): retrieves Book objects depending of the JSON in the body of the request
- `/genres/<parent_genre>` (GET): retrieves all Genres with the given parent genre
Full API route definitions can be found in `api/v1/views/genres.py` and `api/v1/views/books.py`. As the full extent of the database schema is realized in the project, more routes will be added.

#### The Team
- Oluwatobi Tijani: [Github](https://github.com/tobi-tobes), [LinkedIn](https://www.linkedin.com/in/oluwatobi-tijani/)
- Oluwaseyi Salami: [Github](https://github.com/Pinerealm), [LinkedIn](https://www.linkedin.com/in/osalami/)

#### Blog Posts
After the development stage of the project, we wrote a blog post to reflect on our journey building The Next Page. Check out the article here:
- Oluwatobi's article: 
- Oluwaseyi's article:

#### Visit The Next Page
The Next Page is free and easy to use; no login required! Visit it here: [The Next Page](http://project.web-osalami.tech/the_next_page/)

### Getting Started
#### Installation
Run The Next Page from your own system, no internet service required! First of all, you need clone the repository and ensure you have the following dependencies installed:
- Latest version of Python: `apt install python3`
- Flask (supports Python 3.8 and newer): `pip3 install Flask`
- MySQLdb (you need to have MySQL installed `apt install mysql-server`): 
    1. `apt-get install python3-dev`
    2. `apt-get install libmysqlclient-dev`
    3. `apt-get install zlib1g-dev`
    4. `pip3 install mysqlclient`
- SQLAlchemy: `pip3 install SQLAlchemy`

Once all the necessary dependencies have been installed, navigate to `the_next_page` directory (`cd the_next_page`).

The next set is to set up your MySQL database. This tutorial assumes you are able to set up a MySQL server and have already configured your `root` user with a password. Run the following script from within `the_next_page` directory to create the database, user, and password for the project: `cat setup_files/setup_mysql_dev.sql | mysql -hlocalhost -uroot -p`.

Once that is done, you can import some objects into the database using the Python script (`data_for_tnp_database.py`) in the `setup_files` directory. The Next Page is supposed to be run by retrieving data using the Google Books API but we are still working on making that feature seamless. Until then, you can upload books to the database manually with the given script using the following command: 
`TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db setup_files/data_for_tnp_database.py`

The script already has book and genre objects defined within; feel free to add as many more books as you'd like!

Now the database is ready for action! You can now run the API and the main application; both are served by Flask. The API runs on port 5001 while the main application runs on port 5000. To run the the API use the following command:
`TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db TNP_API_HOST=0.0.0.0 TNP_API_PORT=5001 python3 -m api.v1.app`

To run the main applicationm, use the following command:
`TNP_MYSQL_USER=tnp_dev TNP_MYSQL_PWD=tnp_dev_pwd TNP_MYSQL_HOST=localhost TNP_MYSQL_DB=tnp_dev_db TNP_STORAGE_TYPE=db TNP_API_HOST=0.0.0.0 TNP_API_PORT=5000 python3 -m web_flask.tnp`

You can run both concurrently on multiple terminals using `tmux`; install with the following command: `apt-get install tmux`, then simply call `tmux` in your terminal. Use `Ctrl + B + "` to split the pane horizontally or `Ctrl + B + %` to split the pane vertically. Use `Ctrl + B + arrow keys` to navigate between panes and run the commands for the API and the application.

Whew! We're almost done here. The last thing to do is navigate to your browser and open `localhost:5000/the_next_page`, and this will allow you to try out The Next Page! Have fun!

#### Usage
You can also access The Next Page directly from the web using the link in the Introduction Section. Here's a breakdown of how to navigate the website:
- First, click on the filters to narrow down your recommendations. <img src="https://i.imgur.com/GjYeGHN.png" alt="Filters Section" style="height: 100px; width:200px;"/>
- Next, click on the "Get your recommendations" button to view your recommendations. You can also click on "Pick a random book" to select a random book. Click on the book cover to get the book description. <img src="https://i.imgur.com/MOMQoo6.png" alt="Recommendations Section" style="height: 100px; width:200px;"/>
- View your recommendations in the final section. Here, you can choose to download your recommendations (coming soon!) or start from the beginning to get new recommendations. <img src="https://i.imgur.com/Bux5SnI.png" alt="Bookshelf Section" style="height: 100px; width:200px;"/>

### Tools Used:
- Front-end: HTML/CSS, jQuery
- Back-end: Python, MySQL, Flask
