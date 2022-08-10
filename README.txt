CONTENTS OF THIS FILE
-----------------------------

* Purpose
* Methodology
* Requirements
* How to run?
* Data Input guidelines
* Data Output Expectation
* How to Run Tests & QA Analysis

----------------------------
PURPOSE

The purpose of this program is to invite any customers
within a 100km of the SF Office, by reading from a database
of customers [see database - "Customer List.txt"]. The program
will also sort the output in ascending order by User ID into
a .txt file called "Output.txt"

----------------------------
METHODOLOGY

The program is split into 3 main parts

	- Data Obtain
	- Distance Calculation
	- Data Format

Data Obtain:

	In order to obtain the data, the program reads from
	"Customer List.txt", and creates a variable called
	"index" that contains the .txt's contents.

	To make the data usable by the program, it would
	"split" the contents, to create a new index named
	"new_index". So by using "new_index", I was able to
	create a new list named "customer_info", which is a 
	nested list that holds the contents of "new_index",
	at a given point - allowing for easy data retrieval.

	Relevant function(s):

		sort_index(user):
		user_id_to_int(user):

Distance Calculation:

	To obtain the coordinates, the program first retrieved 
	the list and reformated the list to convert the GPS data,
	latitude and longitude into float values.

	After converting the data, the program would then utilize
	the math library to implement trigonometry to convert the
	GPS data from degrees to radians and use the provided 
	mathematical formula to obtain the distance from the SF
	Office to the User Location. Next, the program would use
	the distance into a classifier to determine whether the 
	user would receive an invite or not based upon they
	are within 100km of the SF Office.

	Relevant function(s):

		get_coordinates(user):
		get_distance(user):

Data Format:

	This part formats the data into a more intuitive way of
	reading the data. Initially the data was formatted as

	latitude | user_id | name | longitude 

	So as a result, I opted to reformat the data by using
	user_id as the sorted field. Resulting in the format

	user_id | name | latitude | longitude | distance

	I added distance as a field to act as proof to why the
	user is in the 'INVITE' list. And in the output file,
	the data is catagorized in two lists -
	
	INVITE and NO INVITE

	Relevant function(s):

		output_format(useList,user):
		write_to_output():

----------------------------
REQUIREMENTS

All that is needed to run the program is a computer that has
Python installed and the required files:

	Customer List.txt
	main.py

----------------------------
How to Run?

First create a .txt file called "Customer Info.txt" (if it 
does not exist), and populate the .txt file following the 
"Data Input Guidelines" section. 

Next, to run the program, follow the Python run command 
under your OS of choice

OS Guide:
(https://www.cs.bu.edu/courses/cs108/guides/runpython.html)

Then use the command "python main.py"
----------------------------
Data Input Guidelines

The guideleins to inputting data is as follows:

{ latitude: "float" , user_id: "int", name: "string", longitude: "float" }

If the values for the fields that the guidesline indicates, the 
program will produce a ValueError as a result of an improper 
value type being inputted into the program.

But formatting wise, any field can be moved around, as long as
there is one of each field for each user (aka no duplicates), as
well as avoiding duplicates of users.

----------------------------
Data Output Expectation

The expected data would be two categories, in ascending order
of User_Id within their respective categories - INVITE and NO INVITE

Ex:	INVITE
	--------------------
	{user_id: 6, name: "", latitude: "", longitude: "", Distance: "" }
	{user_id: 7, name: "", latitude: "", longitude: "", Distance: "" }

	NO INVITE
	--------------------
	{user_id: 4, name: "", latitude: "", longitude: "", Distance: "" }
	{user_id: 5, name: "", latitude: "", longitude: "", Distance: "" }

----------------------------
How to run Tests & QA Analysis

To run tests on the code, all that needs to be done is to modify
the "Customer List.txt" and run the Python program.

After performing testing with several events such as:

	- Non-number in user_id, latitude, and longitude
	- Duplicates of field(s)
	- Missing field(s)
	- Missing comma(s)

The built-in Python error messaging would occur, prompting the
user to correctly (following Data Input Guidelines).


SF Office longitude and latitude:
Latitude: 37.7866
Longitude: -122.41284