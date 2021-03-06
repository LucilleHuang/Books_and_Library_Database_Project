# Books_and_Library_Database_Project
Project in progress, will be completed by Dec. 23, 2021

This project contains: <br />
1. A command-line client application <br />
2. An entity-relationship design to model the data <br />
3. A relational schema based on the ER design <br />
4. A data-mining investigation of the dataset <br />

Data Source: Kaggle <br />
https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m <br />
https://www.kaggle.com/seattle-public-library/seattle-library-checkout-records <br />

The requirements for the project are as follows: <br />

	1. A command-line client application appropriate to the domain (in 1_Client folder)
		Requirements：
			1. Querying the data in a way that a customer in the domain would do
			2. Modifying the data in a way that a customer in the domain would do
		Decide:
			1. What you think an ideal client should be able to do
			2. What you plan to actually implement for your client given the time constraints
			3. Document what you actually implemented from your plan, and what you left (At the end of the project, when you write your report)
			4. An explanation justifying each of the above choices
	
	2. An entity-relationship design to model the data (in 2_Server folder)
		1) All entity sets, specifying the entity set name and attributes, showing any compound attributes, multivalued attributes, and optional attributes per the methods described in the course
		2) All relationship sets, specifying the relationship set name and any attributes it might have
		3) All primary keys, cardinality constraints, and attribute domains
		4) Any weak, specialized, or aggregations
		5) Any other aspects relevant to an ER design
	
	3. A relational schema based on the ER design (in 2_Server folder)
		write the necessary SQL code to:
			1) create the required tables, views, etc. for the relational schema
			2) create the required primary keys, foreign keys, and integrity constraints
			3) create indexes as necessary for the query operations you will do both in the client and in the data-mining exercise
			4) load the data from your dataset CSVs into the tables
		Handle error and errors and inconsistencies relative to your design in the data:
			1) fixing obvious data errors
			2) removing any duplicate data
			3) modifying your design in certain cases
			Note: document what you did to handle the issues
	
	4. A data-mining investigation of the dataset (in 3_Data_Mining folder)
		1. Select a domain-appropriate question that you want data mining to answer
		2. Select a technique or technique that will be appropriate to the question you are investigating
		3. Implement said technique efficiently to build a data model
		4. Determine the validity of your model
		5. Report the results of your investigation
