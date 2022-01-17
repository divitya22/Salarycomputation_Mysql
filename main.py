import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Salary_Computation"
)


mycursor=mydb.cursor()
'''
mycursor.execute("SHOW TABLES")

for db in mycursor:
    print(db)


mycursor.execute("Select * from Salary_data order by id")

mycursor.execute("Select max(Salary) from Salary_data")
myresult=mycursor.fetchall()

for r in myresult:
    print(r)

# 2nd highest salary

mycursor.execute("Select max(Salary) from Salary_data where Salary Not In(select max(Salary) from Salary_data) ")
myresult=mycursor.fetchall()

for r in myresult:
    print(r)

# nth salary :Using Correlated subquery

mycursor.execute("SELECT  Salary FROM Salary_data e1 WHERE 3-1 = (SELECT COUNT(DISTINCT Salary) FROM Salary_data e2 WHERE e2.salary > e1.salary)")

myresult=mycursor.fetchall()

for r in myresult:
    print(r)

'''

# 2nd max salary using :LIMIT
mycursor.execute("SELECT Salary FROM (SELECT Salary FROM Salary_data ORDER BY salary DESC LIMIT 3) AS Emp ORDER BY salary LIMIT 1")


myresult=mycursor.fetchall()

for r in myresult:
    print(r)
