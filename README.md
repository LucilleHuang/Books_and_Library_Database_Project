# Books_and_Library_Database_Project
This project contains: <br />
A command-line client application <br />
An entity-relationship design to model the data <br />
A relational schema based on the ER design <br />
A data-mining investigation of the dataset <br />

Data Source: Kaggle <br />
https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m <br />
https://www.kaggle.com/seattle-public-library/seattle-library-checkout-records <br />

The requirements for the project are as follows: <br />

	1. A command-line client application appropriate to the domain <br />
		Requirements: <br />
			1. Querying the data in a way that a customer in the domain would do <br />
			2. Modifying the data in a way that a customer in the domain would do <br />
		Decide: <br />
			1. What you think an ideal client should be able to do <br />
			2. What you plan to actually implement for your client given the time constraints <br />
			3. (At the end of the project, when you write your report) What you actually implemented from your plan, and what you left <br />
			4. An explanation justifying each of the above choices <br />

	2. An entity-relationship design to model the data <br />
		1) All entity sets, specifying the entity set name and attributes, showing any compound attributes, multivalued attributes, and optional attributes per the methods described in the course <br />
		2) All relationship sets, specifying the relationship set name and any attributes it might have <br />
		3) All primary keys, cardinality constraints, and attribute domains <br />
		4) Any weak, specialized, or aggregations <br />
		5) Any other aspects relevant to an ER design <br />

	3. A relational schema based on the ER design <br />
		write the necessary SQL code to: <br />
			1) create the required tables, views, etc. for the relational schema <br />
			2) create the required primary keys, foreign keys, and integrity constraints <br />
			3) create indexes as necessary for the query operations you will do both in the client and in the data-mining exercise <br />
			4) load the data from your dataset CSVs into the tables <br />

		Handle error and errors and inconsistencies relative to your design in the data: <br />
			1) fixing obvious data errors <br />
			2) removing any duplicate data <br />
			3) modifying your design in certain cases <br />
			Note: document what you did to handle the issues <br />

	4. A data-mining investigation of the dataset <br />
		1. Select a domain-appropriate question that you want data mining to answer <br />
		2. Select a technique or technique that will be appropriate to the question you are investigating <br />
		3. Implement said technique efficiently to build a data model <br />
		4. Determine the validity of your model <br />
		5. Report the results of your investigation <br />

Deliverables: <br />
	1. Final Written Report: this should describe the client application, the ER design, the relational schema, and your data-mining investigation, detailing the specific issues required above. In addition, you should include a test case plan that describes how you test the various code aspects of your project. <br />
	2. Code: you are not expected to submit your code but rather store it in a GitHub repository, or equivalent, to which we can have access. The code in the repository should include the following: <br />
		1) All client code <br />
		2) The SQL code necessary to implement the relational schema and load the data from the CSV files <br />
		3) The code, SQL and otherwise, needed to implement your data-mining investigation <br />
		4) Test cases for the above <br />
	3. Video Demo: a 20-minute walk-through/presentation of your project. It should describe all of the aspects of your design, implementation, and results. <br />
