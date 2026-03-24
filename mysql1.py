

import mysql.connector

# Connect to MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pratyushnanda7@",
    database="pydb",
    port=3306
)

cursor = cnx.cursor()

# 🔥 Helper function to execute and print results
def run_query(title, query):
    print("\n" + "="*50)
    print(f"👉 {title}")
    print("="*50)
    
    try:
        cursor.execute(query)
        
        # If SELECT query → fetch results
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print(f"\nTotal rows: {len(rows)}")
        else:
            cnx.commit()
            print("✅ Query executed successfully")
    
    except Exception as e:
        print("❌ Error:", e)



cursor.execute("CREATE TABLE IF NOT EXISTS giet (name VARCHAR(255), roll VARCHAR(255) PRIMARY KEY, address VARCHAR(255), salary VARCHAR(255), gender VARCHAR(255), designation VARCHAR(255))")
cursor.execute("INSERT INTO giet (name, roll, address, salary, gender, designation) VALUES ('Pratyush', '23CSE183', 'Jamala', '5000000', 'Male', 'Student'), ('Shivam', '23CSE148', 'Jaleswar', '500000', 'Male', 'Student'), ('Pabitra', '23CSE165', 'Baliapal', '5000000', 'Male', 'Student'), ('Avaneesh', '23LECSE002', 'Bargarh', '50000', 'Male', 'Student'), ('Lipun', '23CSE235', 'Balangir', '500000', 'Male', 'Student'),('Aman','23CSE199','Bhubaneswar','5000000','Male','Student'),('Satyarth','23CSE200','Delhi','5000000','Male','Student'),('Satyarth','23CSE201','Bhubaneswar','5000000','Male','Doctor')")
print("Data inserted successfully")
print("Data in the table:")

# ==============================
# 🔹 T-1 Queries
# ==============================

queries = [
    ("Salary = 15000", "SELECT * FROM giet WHERE salary = 15000"),
    ("Salary > 20000", "SELECT * FROM giet WHERE salary > 20000"),
    ("Salary < 30000", "SELECT * FROM giet WHERE salary < 30000"),
    ("Male and salary > 20000", "SELECT * FROM giet WHERE gender='Male' AND salary > 20000"),
    ("Female OR Raipur", "SELECT * FROM giet WHERE gender='Female' OR address='raipur'"),
    ("Name starts with a", "SELECT * FROM giet WHERE name LIKE 'a%'"),
    ("Name ends with h", "SELECT * FROM giet WHERE name LIKE '%h'"),
    ("Address contains pur", "SELECT * FROM giet WHERE address LIKE '%pur%'"),
    ("Sort by name ASC", "SELECT * FROM giet ORDER BY name ASC"),
    ("Sort by salary DESC", "SELECT * FROM giet ORDER BY salary DESC"),
    ("Total employees", "SELECT COUNT(*) FROM giet"),
    ("Count Male", "SELECT COUNT(*) FROM giet WHERE gender='Male'"),
]

# ==============================
# 🔹 T-2 Queries
# ==============================

queries += [
    ("Salary between 15000-30000", "SELECT * FROM giet WHERE salary BETWEEN 15000 AND 30000"),
    ("Not from Delhi", "SELECT * FROM giet WHERE address != 'delhi'"),
    ("Not teacher", "SELECT * FROM giet WHERE designation != 'teacher'"),
    ("Name aman or naman", "SELECT * FROM giet WHERE name IN ('aman','naman')"),
    ("At least 2 'a'", "SELECT * FROM giet WHERE name LIKE '%a%a%'"),
    ("Name length 5", "SELECT * FROM giet WHERE name LIKE '_____'"),
    ("Address starts with r", "SELECT * FROM giet WHERE address LIKE 'r%'"),
    ("Top 3 salary", "SELECT * FROM giet ORDER BY salary DESC LIMIT 3"),
    ("Lowest salary", "SELECT * FROM giet ORDER BY salary ASC LIMIT 1"),
    ("Total salary Male", "SELECT SUM(salary) FROM giet WHERE gender='Male'"),
    ("Avg salary Female", "SELECT AVG(salary) FROM giet WHERE gender='Female'"),
    ("Count salary >20000", "SELECT COUNT(*) FROM giet WHERE salary > 20000"),
    ("Count per designation", "SELECT designation, COUNT(*) FROM giet GROUP BY designation"),
    ("Avg per gender", "SELECT gender, AVG(salary) FROM giet GROUP BY gender"),
    ("Total salary per city", "SELECT address, SUM(salary) FROM giet GROUP BY address"),
    ("Designation avg >20000", "SELECT designation FROM giet GROUP BY designation HAVING AVG(salary) > 20000"),
    ("Cities >1 employee", "SELECT address FROM giet GROUP BY address HAVING COUNT(*) > 1"),
    ("Above avg salary", "SELECT * FROM giet WHERE salary > (SELECT AVG(salary) FROM giet)"),
    ("Max salary employees", "SELECT * FROM giet WHERE salary = (SELECT MAX(salary) FROM giet)"),
    ("Min salary employees", "SELECT * FROM giet WHERE salary = (SELECT MIN(salary) FROM giet)")
]

# ==============================
# 🔹 T-3 Queries
# ==============================

queries += [
    ("Second highest salary", "SELECT MAX(salary) FROM giet WHERE salary < (SELECT MAX(salary) FROM giet)"),
    ("Third highest salary", """SELECT MAX(salary) FROM giet WHERE salary < (
        SELECT MAX(salary) FROM giet WHERE salary < (SELECT MAX(salary) FROM giet)
    )"""),
    ("Employees 2nd highest", "SELECT * FROM giet WHERE salary = (SELECT MAX(salary) FROM giet WHERE salary < (SELECT MAX(salary) FROM giet))"),
    ("Salary > city avg", """SELECT * FROM giet g1 WHERE salary > (
        SELECT AVG(salary) FROM giet g2 WHERE g1.address = g2.address
    )"""),
    ("Duplicate salaries", "SELECT * FROM giet WHERE salary IN (SELECT salary FROM giet GROUP BY salary HAVING COUNT(*) > 1)"),
    ("Unique salaries", "SELECT * FROM giet WHERE salary IN (SELECT salary FROM giet GROUP BY salary HAVING COUNT(*) = 1)"),
    ("Highest per designation", "SELECT designation, MAX(salary) FROM giet GROUP BY designation"),
    ("Salary > designation avg", """SELECT * FROM giet g1 WHERE salary > (
        SELECT AVG(salary) FROM giet g2 WHERE g1.designation = g2.designation
    )"""),
    ("Top 3 total salary", "SELECT SUM(salary) FROM (SELECT salary FROM giet ORDER BY salary DESC LIMIT 3) as t"),
    ("Unique city employees", "SELECT * FROM giet WHERE address IN (SELECT address FROM giet GROUP BY address HAVING COUNT(*) = 1)"),
    ("Most common designation", "SELECT designation FROM giet GROUP BY designation ORDER BY COUNT(*) DESC LIMIT 1"),
    ("City highest salary", "SELECT address FROM giet GROUP BY address ORDER BY SUM(salary) DESC LIMIT 1"),
    ("Same designation+salary", "SELECT * FROM giet WHERE (designation, salary) IN (SELECT designation, salary FROM giet GROUP BY designation, salary HAVING COUNT(*) > 1)"),
    ("Salary > Delhi", "SELECT * FROM giet WHERE salary > ALL (SELECT salary FROM giet WHERE address='delhi')"),
]

# ==============================
# 🚀 EXECUTE ALL
# ==============================

for title, query in queries:
    run_query(title, query)

# Close connection
cursor.close()
cnx.close()