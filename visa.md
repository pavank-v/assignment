1. Optimize a database table for efficient retrieval

Indexes: Create indexes on columns frequently used in WHERE, JOIN, and ORDER BY clauses. This helps the database locate rows faster.

Covering Indexes: Include all columns needed by a query in the index so the database doesn’t need to read the table itself.

Partitioning: Split large tables into smaller partitions (by range, hash, or list) to reduce the data scanned per query.

Normalization vs Denormalization: Use normalization to reduce redundancy, but consider denormalization for frequently joined tables to reduce join overhead.

Query optimization: Analyze queries using EXPLAIN/EXPLAIN ANALYZE and adjust indexes or rewrite queries for efficiency.

Caching: Use query result caching or materialized views for frequently accessed, expensive queries.

2. What happens when a query is executed
Steps of query execution:

Parsing: SQL query is parsed for syntax correctness.

Query Optimization: The optimizer chooses the most efficient execution plan based on indexes, statistics, and joins.

Execution: The database engine executes the plan, reading data from disk or cache.

Fetching & Returning Results: Rows are retrieved and returned to the client.

Optional note: Explain transaction management and locking if relevant for concurrency.

3. Query to select the second highest mark

-- Using LIMIT and ORDER BY (MySQL/PostgreSQL)
SELECT mark
FROM student_marks
ORDER BY mark DESC
LIMIT 1 OFFSET 1;

-- Using a subquery (Standard SQL)
SELECT MAX(mark) AS second_highest
FROM student_marks
WHERE mark < (SELECT MAX(mark) FROM student_marks);


Explain both approaches and trade-offs: LIMIT/OFFSET is simple; subquery works even if duplicates exist and is standard SQL.

4. Design a weather app

Frontend: Mobile app (iOS/Android) or web app, showing current weather, hourly forecast, weekly forecast, and alerts.

Backend: API server fetching data from a weather provider (like OpenWeatherMap).

Database: Store user preferences, favorite locations, and cached weather data.

Features:

Search for locations

Weather notifications/alerts

Offline mode with cached data

Improvements: Optimize API calls using caching, provide personalized suggestions (e.g., “carry umbrella today”), use efficient data structures for fast lookup.

5. How blockchains work and why they are used

Concept: A blockchain is a decentralized, append-only ledger of transactions. Each block contains data, a timestamp, a hash of the previous block, and its own hash.

Why used:

Immutability: Once recorded, data cannot be changed without altering all subsequent blocks.

Decentralization: Eliminates need for a trusted central authority.

Transparency and Auditability: All participants can verify transactions.

Technical improvements you could mention:

Implementing more efficient consensus mechanisms (e.g., Proof-of-Stake instead of Proof-of-Work)

Reducing storage requirements via pruning

Improving transaction throughput using off-chain solutions or layer 2 protocols




1. What is Normalization and why is it used?

Definition: Normalization is the process of organizing a database to reduce redundancy and improve data integrity. It typically involves dividing a large table into smaller tables and defining relationships between them.

Goals / Benefits:

Eliminate redundancy: Avoid storing duplicate data.

Ensure data integrity: Prevent anomalies during insert, update, or delete operations.

Improve query efficiency: Although normalized tables may require joins, they make updates and maintenance easier and less error-prone.

Common Normal Forms: 1NF (no repeating groups), 2NF (no partial dependency), 3NF (no transitive dependency), BCNF (more strict version of 3NF).


1. What is Inheritance?

Definition: Inheritance is an OOP concept where a class (child/subclass) acquires properties and behaviors (methods) of another class (parent/superclass).

Purpose: Promotes code reuse, extensibility, and hierarchical modeling of real-world entities.

2. What is a Dequeue (Deque)?

Definition: A Deque (Double-Ended Queue) is a data structure where elements can be inserted or removed from both the front and rear ends.

3. Real-world Application of Deque:

Implementing browser history (forward/back navigation).

Task scheduling in operating systems.

Sliding window algorithms in competitive programming.

4. Intersection and Union in DBMS:

Union: Combines results of two queries, removing duplicates.

SELECT column_name FROM table1
UNION
SELECT column_name FROM table2;


Intersection: Returns only the common records between two queries (supported in some DBMS like Oracle or using INNER JOIN in MySQL).

SELECT column_name FROM table1
INTERSECT
SELECT column_name FROM table2;


5. Difference Between Primary Key and Foreign Key:

Feature	Primary Key	Foreign Key
Purpose	Uniquely identifies a record	References primary key in another table
Uniqueness	Must be unique	Can have duplicates
Null Allowed	No	Yes (unless specified)
Relationship	Defines entity uniqueness	Defines relationship between tables

6. Relations in DBMS:

Definition: A relation is a table with rows (tuples) and columns (attributes) that represents an entity and its attributes.

Properties: Each row is unique, and the order of rows and columns does not matter.

7. Real-world use case of One-to-Many Relationship:

Example: A customer can have multiple orders, but each order belongs to only one customer.

8. What is Indexing in DBMS?

Definition: Indexing is a technique to speed up data retrieval by creating a data structure (like B-Tree or Hash) that allows fast searches on columns.

Benefit: Reduces full table scans, improves query performance.

9. What do you know about Triggers?

Definition: A trigger is a set of SQL statements automatically executed in response to certain events on a table (INSERT, UPDATE, DELETE).

Use-case: Maintain audit logs, enforce constraints, or automatically update related tables.

10. Scenario: After inserting data in one table, how to modify a row in another table?

Use a trigger:

CREATE TRIGGER update_another_table
AFTER INSERT ON table1
FOR EACH ROW
BEGIN
    UPDATE table2
    SET column_name = NEW.value
    WHERE condition;
END;


This ensures the second table updates automatically whenever a new row is inserted in the first table.


1. Out of SQL, NoSQL, and Oracle, which is best and why?

Answer: There’s no one-size-fits-all; it depends on use-case:

SQL (MySQL, PostgreSQL): Best for structured data with clear relationships; supports ACID transactions.

NoSQL (MongoDB, Cassandra): Best for unstructured or semi-structured data, horizontal scalability, and high-volume, low-latency requirements.

Oracle: Enterprise-level RDBMS with advanced features like strong security, high availability, and optimization tools; suitable for large-scale enterprise applications.

Conclusion: Choose based on project needs: relational consistency → SQL/Oracle; flexible schema or massive scale → NoSQL.

2. For RDBMS, which database would fit best?

Answer: For most standard RDBMS needs:

PostgreSQL: Open-source, feature-rich, supports ACID, complex queries, and indexing.

MySQL: Widely used, easy to manage, good for web apps.

Oracle: Best for enterprise apps requiring high reliability, security, and advanced features.

3. Explain Referential Integrity

Definition: Referential integrity ensures that a foreign key in one table always refers to a valid primary key in another table.

Purpose: Prevents orphaned records and maintains consistent relationships between tables.

Example: An Orders table has a CustomerID foreign key referencing Customers table; you cannot insert an order with a CustomerID that doesn’t exist.

4. Concept of Indexing and Advantages

Definition: Indexing is creating a data structure (like B-Tree or Hash) on a table column to speed up searches.

Advantages:

Speeds up query retrieval (WHERE, JOIN, ORDER BY).

Reduces the need for full table scans.

Can enforce uniqueness (unique indexes).

Trade-off: Slightly slower inserts/updates and additional storage.

5. Difference Between Triggers and Stored Procedures

Feature	Trigger	Stored Procedure
Execution	Auto-executed on specific table events	Manually called by application/user
Use-case	Enforce business rules, audit logs	Reusable business logic, complex operations
Parameters	Cannot accept input parameters (in most DBMS)	Can accept input and output parameters
Invocation	INSERT, UPDATE, DELETE	CALL statement


1. What is a Thread?

Definition: A thread is the smallest unit of execution within a process. Multiple threads can exist within the same process, sharing the same memory space but executing independently.

Purpose: Allows concurrent execution, efficient CPU utilization, and faster program performance.

2. Difference Between a Process and a Thread

Feature	Process	Thread
Memory Space	Has its own memory space	Shares memory space with other threads in the same process
Creation Overhead	High (requires separate resources)	Low (shares resources with parent process)
Communication	Inter-process communication (IPC) required	Can communicate directly via shared memory
Isolation	Isolated from other processes	Not isolated; can affect other threads if mismanaged
Execution	Independent	Runs as part of a process

3. What are Deadlocks?

Definition: A deadlock is a situation in concurrent programming where two or more processes or threads are waiting indefinitely for resources held by each other.

Example: Process A holds resource X and waits for resource Y; Process B holds resource Y and waits for resource X → both are stuck.

Prevention Strategies:

Avoid circular wait by acquiring resources in a fixed order.

Use timeout mechanisms.

Apply deadlock detection and recovery algorithms.

4. Difference Between Mutex and Semaphore

Feature	Mutex	Semaphore
Definition	Mutual exclusion lock for a single thread at a time	Synchronization primitive that can allow multiple threads depending on count
Ownership	Owned by the thread that locks it	No ownership; any thread can signal or wait
Usage	Protects critical sections in shared memory	Controls access to a limited number of resources
Binary vs Counting	Binary (locked/unlocked)	Can be binary or counting


