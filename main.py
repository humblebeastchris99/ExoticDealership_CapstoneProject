import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name

        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")


#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"

#create coupe table
create_coupe_table = """  
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
year integer NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
DOA VARCHAR(75) NOT NULL,
DOL VARCHAR(75) NOT NULL);
"""

#create suv table
create_suv_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
year integer NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
DOA VARCHAR(75) NOT NULL,
DOL VARCHAR(75) NOT NULL);
"""


#create sedan table
create_sedan_table = """
create table SEDAN_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
year integer NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
DOA VARCHAR(75) NOT NULL,
DOL VARCHAR(75) NOT NULL);
"""

#create truck table
create_truck_table = """
create table TRUCK_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
year integer NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL,
engine VARCHAR(50) NOT NULL,
DOA VARCHAR(75) NOT NULL,
DOL VARCHAR(75) NOT NULL);
"""

#populate coupe table
populate_coupe_table = """ 
insert into COUPE_MODELS values
('001122333','Aston Martin','Vanquish',2010,200, 115000,'V12','11/28/23','13'),
('0121314121', 'Audi','R8',2011, 8888, 112500, 'V12', '11/19/23','22'),
('1234567777', 'BMW', 'M4', 2022,300 ,46999,'V8', '09/19/23', '45'),
('3456488888', 'Camaro', 'SS',2022, 8000, 39000, 'V8', '10/12/23', '30'),
('4566647885', 'Ford', 'Mustang', 2022, 8030, 38000, 'V8', '10/23/23','45'),
('8797559475','GTR', 'Nissan', 2022, 9000, 74000, 'V12', '12/09/23', '12'),
('9884456955', 'Infiniti','Q60',2023, 8500, 50000, 'V8', '02/14/23', '2'),
('7852525266', 'Corvette', 'Z06',2019, 5000,52000, 'V12', '03/10/23', '10');
"""

#populate suv table
populate_suv_table = """
insert into SUV_MODELS values
('123ABC321','Lamborghini','URU',2021, 787, 135000,'V12','03/13/23','2'),
('ASD748541', 'BMW', 'X5',2019, 1200, 12500,'V12', '03/10/23','4'),
('ASD183949', 'Toyota', 'Pathfinder',2004, 9000, 9220, 'V6','01/12/23','36'),
('878825112', 'Toyota', 'Rav4',2005, 8008, 5000, 'V6', '11/23/22','120'),
('B85855996', 'Jeep', 'Grand Cherokee',2020, 5000,9000, 'V6', '10/22/22', '80'),
('C63987783', 'Jeep', 'Track-hawk',2021, 5000,11000, 'V12', '03/10/23', '5'),
('D63773337', 'Jeep', 'Trail-hawk',2023, 4000, 1200,'V6', '01/05/23', '45'),
('E09897666', 'Mercedes', 'GLE',2023, 5500,8000, 'V6', '03,14,23', '2');
"""

#populate sedan table
populate_sedan_table = """
insert into SEDAN_MODELS values
('C67899799', 'Mazda', 'Q3S',2018,31600, 2000, 'V6', '10/17/22','90'),
('A65595844', 'Ford','Fusion', 2017,42000,2200, 'V6', '10/15/22','80'),
('P56554565', 'Toyota','Camry',2015, 22000, 3100, 'V6', '09/08/23','17'),
('P64544554', 'Audi', 'A3',2017, 5000, 40000, 'V6', '11/21/23', '20'),
('A456464882', 'Kia', 'Stinger', 2023,100,3250, 'V6', '02/28/23', '15'),
('P878985599', 'Kia', 'K-5', 2023, 3000, 3100, 'V6', '05/30/22', '100'),
('QT62662780', 'Honda', 'Accord',2016,30000, 1500, 'V6','02/15/23', '15'),
('WP98388339', 'Honda', 'Civic',2005, 50000, 1200, 'V6', '01/10/23', '39');
"""


#populate truck table
populate_truck_table = """
insert into TRUCK_MODELS values
('A44144414','Ford','F150',2016,40000,60000,'V6','09/08/22','122'),
('A72866382', 'Ford','Raptor',2017, 45000, 55000, 'V8','02/02/23','20'),
('PP6556789', 'GMC', 'Sierra', 2004, 11900, 6500, 'V6','01/19/22','97'),
('T76543456', 'Chevy', 'Silverado', 2017, 10000, 29000, 'V6', '02/22/23','15'), 
('A44175433','Ford','F250',2017,40000,60546,'V6','09/08/22','120'),
('A72878445', 'Ford','Raptor',2020, 45000, 75000,' V8','03/22/23','6'),
('QP6558755', 'GMC', 'Sierra', 2016, 8000, 46500, 'V8','01/19/22', '5'),
('T76548855', 'Chevy', 'Silverado', 2000, 10000, 2900, 'V6', '02/22/22', '155'); 
"""



#read values from coupe table
display_coupe_models_table = """
SELECT * FROM COUPE_MODELS;
"""

#read values from suv table
display_suv_models_table = """
SELECT * FROM SUV_MODELS;
"""


#read values from sedan table
display_sedan_models_table = """
SELECT * FROM SEDAN_MODELS;
"""

#read values from truck table
display_truck_models_table = """
SELECT * FROM TRUCK_MODELS;
"""

#read values from employee table
display_employee_directory_table = """
SELECT * FROM employee_directory_table;
"""

#READ values from Customer information
display_customer_information_table = """
SELECT * FROM CUSTOMER_INFORMATION;
"""


#create Employee directory table
create_employee_directory = """
create table employee_directory_table(
emp_ID integer PRIMARY KEY,
First_Name VARCHAR(75) NOT NULL,
Last_Name VARCHAR(75) NOT NULL,
employee_position VARCHAR(75) NOT NULL,
salary integer NOT NULL,
phone_number VARCHAR(75) NOT NULL,
Years_experience VARCHAR(75) NOT NULL);
"""

#populate employee directory table
populate_employee_directory = """
insert into  employee_directory_table values 
(001, 'Tod', 'Smith', 'sales-rep', 3500,'7108955555', '1+'),
(002, 'Nya', 'Burke', 'branch-manager',44,'8158295899', '2+'),
(003,'Lilly', 'Bianca','regional-manager',72,'3039108988', '5+'),
(004, 'Nolan', 'Blake','store-manager',52, '8705178441',' 5+'),
(005, 'Jake', 'Alexander', 'regional-manager',72, '3058889845',' 5+'),
(006, 'Josh', 'Brown','store-manager', 52, '7867418978',' 4+'),
(007, 'Chris', 'Black', 'regional-manager',75, '7868798755', '7+'),
(008, 'Mike', 'Miller', 'corporate-manager', 80, '5059878887', '9+'),
(009, 'Carter', 'Banks', 'sales-rep',36, '3057894555', '2+'),
(010, 'India','Love', 'sales-rep', 40,'7863058157', '3+'),
(011, 'Floyd', 'Green', 'mechanic', 42, '9107057189', '4+'),
(012, 'Linda', 'Hamilton','mechanic', 38,'9104807548', '2+'),
(013, 'Clark', 'Kent', 'sales-rep', 39, '3109872214', '3+'),
(014, 'Lloyd', 'Banks', 'mechanic', 44, '7862897887', '4+'),
(015,'Jerry', 'Rice', 'mechanic', 42, '9108777558', '4+'),
(016,'Rico','Lewis', 'mechanic',40, '3052128755', '3+');
"""

#create customer information table
create_customer_information_table = """
create table customer_information(
Full_name VARCHAR(75) NOT NULL,
Address VARCHAR (80) NOT NULL,
phone_number VARCHAR (80) NOT NULL,
Email VARCHAR (80) NOT NULL,
DOB  VARCHAR (80) NOT NULL,
SSN VARCHAR (80) NOT NULL,
employee_position VARCHAR(75) NOT NULL,
Monthly_income integer NOT NULL);"""

#populate customer information table
populate_customer_information_table = """
insert into customer_information values
('Jack Black', '1312 Peachtree St', '9108459899','jblack@aol.com', '01/22/84', 589787454,'teacher','3200'),
('Bianca Henry', '1301 Nw 207St', '8157912233', 'flowerb@yahoo.com', '11/21/92', 82223055, 'librarian', '4000'),
('Jake Green', '4040 Nw Dogwood Ave', '3058157922', 'cweh@aol.com', '05/31/99', 792879877, 'fire-fighter', '5200'),
('Louis Blake', '851 Nw 206Terr', '9548617899', 'loveispower@gmail.com', '02/24/04', 875658712, 'Army-guard', '3100'),
(')Dianna Hall', '1201 NE 125ST', '8049877203', 'diannah@rocketmail.com', '03/20/02', 512658789,'Bank-teller', '2800'),
('Lenny Brooks', '888 Peachtree St', '7042458600', 'lennybrooks@aol.com', '04/27/97', 872256894,'chef', '3200'),
('Matt Hardy', '1212 Scooby Lane', '8757893112', 'mHardy91@gmail.com', '11/27/97', 598587112, 'policeman', '4500'),
('Jeff Hardy', '1897 Core Valley', '7869722309', 'hardyjeffg@icloud.com', '09/14/96', 2897885112,'wrestler', '4200'),
('Paul Anthony', '2404 NE Dogwood Ave', '3058887922', 'cwecch@aol.com', '05/31/98', 777879877, 'fire-fighter', '5200'),
('Blake Carter', '8851 Nw 204BLVd', '9548617459', 'blakecarter@gmail.com', '02/24/02', 845658712, 'navy-guard', '3200')
"""

#update the second vehicle in your coupe table to have 8888 miles
update_coupe_models = """
update COUPE_MODELS
set mileage = 8888
where vin_number = '0121314121'
"""

#update the forth vehicle in your SUV table to have 4444 miles
update_suv_models = """
update_suv_models
set mileage = 4444
where vin_number = '878825112'
"""



#update the second regional manager salary to $116,599
update_employee_directory_ = """
update employee_directory_table
set salary = 116599
where emp_ID = 005;
"""


#update your third mechanic to have a salary of $76,444
update_employee_directory= """
update employee_directory_table
set salary = 76444
where emp_ID = 014;
"""


#remove the second to last person from your directory table
#delete value from table
remove_employee_directory = """
delete from  employee_directory_table 
where emp_ID =015;
"""



#remove the eight vehicle from your sedan table
#delete value from table
remove_LastSedan_vehicle = """
DELETE FROM SEDAN_MODELS
WHERE vin_number = 'WP98388339';"""



#calling statement
connection = create_server_connection("localhost","root","student","exotic_dealership")
execute_query(connection,populate_suv_table)

#call work horse function to create database
#call read query function to fetch information from MySQL
results=read_query(connection,display_suv_models_table)
#iterate through the table to display all information
for result in results:
    print(result)

