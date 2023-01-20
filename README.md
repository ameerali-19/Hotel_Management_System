# Hotel_Management_System

This project is a simple user interface built using Python's Tkinter library and styled using TTKBootstrap. The backend is implemented using MySQL and the connection between the frontend and backend is established using the mysql-connector library.

## Features

- Check-in and check-out customers
- Edit and delete customer details
- Display a list of current customers in the main window
- Automatically calculate and display the cost and current status of the customer
- Add, edit and delete room details

## Requirements

- Python 3
- Tkinter
- TTKBootstrap
- mysql-connector
- MySQL

## Installation

1. Clone the repository to your local machine
```
git clone https://github.com/ameerali-19/Hotel_Management_System.git
```
2. Install the required libraries by running the following command in the project directory
```
pip install -r requirements.txt
```
3. Update the `main.py` and `setup.py` file with your MySQL database credentials, including your username and password for the MySQL connection
4. To create a new database and corresponding tables in MySQL , execute the file `setup.py` **just once**.
```
python setup.py
```
5. Give the absolute path of your logo.ico file in the logo_path variable in the `main.py` file.
6. Run the following command to start the application
```
python main.py
```

## Usage

The application should start as you execute the `main.py` and you should see the main window with an empty list of customers. You can navigate through the different options using the buttons. Start by adding a few rooms before you checkin any customers because the customers can only be checked into existing rooms.
