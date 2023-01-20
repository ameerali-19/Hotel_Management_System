import mysql.connector

#Substitute your credentials here
username = "root"
password = "password"

# MySQL connection code
init_conn = mysql.connector.connect(
  host="localhost",
  user=username,
  passwd=password
)
init_curs = init_conn.cursor()
init_curs.execute('CREATE DATABASE IF NOT EXISTS hms')
init_conn.commit()
init_conn.close()

my_db = mysql.connector.connect(
  host="localhost",
  user=username,
  passwd=password,
  database="hms"
)
my_conn = my_db.cursor()

sql="create table IF NOT EXISTS room (rno int primary key auto_increment,type varchar(25),price int,vacancy varchar(15))"
my_conn.execute(sql)
sql="alter table room auto_increment=100"
my_conn.execute(sql)
my_db.commit()

sql="create table IF NOT EXISTS  customer (cid  int primary key auto_increment,name varchar(25),proof varchar(25),checkin date,checkout date,room int,cost int,status varchar(25),foreign key(room) references room(rno))"
my_conn.execute(sql)
sql="alter table customer auto_increment=1000"
my_conn.execute(sql)
my_db.commit()

print("Prerequisites completed successfully")
