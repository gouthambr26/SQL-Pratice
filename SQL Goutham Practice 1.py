# Databricks notebook source
# MAGIC %sql
# MAGIC use sql_catalog.sql_schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists sql_schema;
# MAGIC use sql_schema;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS emp (
# MAGIC     empno INT,
# MAGIC     ename STRING,
# MAGIC     job STRING,
# MAGIC     mgr INT,
# MAGIC     hiredate DATE,
# MAGIC     sal INT,
# MAGIC     comm INT,
# MAGIC     deptno INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO emp VALUES
# MAGIC (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20),
# MAGIC (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30),
# MAGIC (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30),
# MAGIC (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20),
# MAGIC (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
# MAGIC (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, NULL, 30),
# MAGIC (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10),
# MAGIC (7788, 'SCOTT', 'ANALYST', 7566, '1982-12-09', 3000, NULL, 20),
# MAGIC (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17', 5000, NULL, 10),
# MAGIC (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30),
# MAGIC (7876, 'ADAMS', 'CLERK', 7788, '1983-01-12', 1100, NULL, 20),
# MAGIC (7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, NULL, 30),
# MAGIC (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, NULL, 20),
# MAGIC (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS dept (
# MAGIC     deptno INT,
# MAGIC     dname STRING,
# MAGIC     loc STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO dept VALUES
# MAGIC (10, 'ACCOUNTING', 'BANGALORE'),
# MAGIC (20, 'RESEARCH', 'DALLAS'),
# MAGIC (30, 'SALES', 'CHICAGO'),
# MAGIC (40, 'OPERATIONS', 'BOSTON');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from dept

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE dept

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from dept

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS dept (
# MAGIC     deptno INT,
# MAGIC     dname STRING,
# MAGIC     loc STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO dept VALUES
# MAGIC (10, 'ACCOUNTING', 'BANGALORE'),
# MAGIC (20, 'RESEARCH', 'DALLAS'),
# MAGIC (30, 'SALES', 'CHICAGO'),
# MAGIC (40, 'OPERATIONS', 'BOSTON');

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from dept

# COMMAND ----------

# MAGIC %md
# MAGIC Q 2.2. Display unique Jobs from EMP table?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT distinct job from emp

# COMMAND ----------

# MAGIC %md
# MAGIC 2.3. List the emps in the asc order of their Salaries?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp order by sal asc

# COMMAND ----------

# MAGIC %md
# MAGIC 2.5. Display all the unique job groups in the descending order?

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct job from emp order by job desc 

# COMMAND ----------

# MAGIC %md
# MAGIC 2.6. Display all the details of all ‘Mgrs’

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *from emp where empno in(select mgr from emp )

# COMMAND ----------

# MAGIC %md
# MAGIC 2.7. List the emps who joined before 1981.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where hiredate < '1981-01-01'

# COMMAND ----------

# MAGIC %md
# MAGIC List the Empno, Ename, Sal, Daily sal of all emps in the asc order of

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT empno,ename,sal,sal/30 as DailySal,sal*12 as AnnualSal from emp order by AnnualSal asc

# COMMAND ----------

# MAGIC %md
# MAGIC 2.9. Display the Empno, Ename, job, Hiredate, Exp of all Mgrs

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT empno,ename,job,hiredate,months_between(current_date(),hiredate) as Experience from emp where empno in (select mgr from emp)

# COMMAND ----------

# MAGIC %md
# MAGIC List the Empno, Ename, Sal, Exp of all emps working for Mgr 7369

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT empno,ename,sal,hiredate, mgr, round(months_between(current_date,hiredate)/12,1) as Experience from emp where mgr = 7839;

# COMMAND ----------

# MAGIC %md
# MAGIC 2.11. Display all the details of the emps whose Comm Is more than their Sal

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where comm > sal

# COMMAND ----------

# MAGIC %md
# MAGIC 2.12. List the emps in the asc order of Designations of those joined after the second half of 1981.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where hiredate > '1981-06-30'order by job asc

# COMMAND ----------

# MAGIC %md
# MAGIC 2.13. List the emps along with their Exp and Daily Sal is more than Rs.100.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  empno,ename, job, hiredate,sal, ROUND((sal / 30), 2) AS daily_sal, ROUND(MONTHS_BETWEEN(current_date, hiredate) / 12, 2) AS exp_years
# MAGIC FROM Emp
# MAGIC WHERE (sal/30) > 100;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  empno,ename, job, hiredate,sal, ROUND((sal / 30), 2) AS daily_sal, ROUND(MONTHS_BETWEEN(current_date, hiredate) / 12, 2) AS exp_years
# MAGIC FROM Emp
# MAGIC WHERE (daily_sal) > 100;

# COMMAND ----------

# MAGIC %md
# MAGIC 2.14. List the emps who are either ‘CLERK’ or ‘ANALYST’ in the Desc order

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp WHERE job = 'CLERK' or job = 'ANALYST' ORDER BY job DESC

# COMMAND ----------

# MAGIC %md
# MAGIC 2.15. List the emps who joined on 1-MAY-81,3-DEC-81,17-DEC-81,19-JAN80 in asc order of seniority.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where hiredate IN ('1981-05-01', '1981-12-03', '1981-12-17', '1980-01-19') order by hiredate asc;

# COMMAND ----------

# MAGIC %md
# MAGIC 2.16. List the emp who are working for the Deptno 10 or20.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where deptno = 10 or deptno = 20

# COMMAND ----------

# MAGIC %md
# MAGIC 2.17. List the emps who are joined in the year 81.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where hiredate = '1981'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where year(hiredate) = '1981'

# COMMAND ----------

# MAGIC %md
# MAGIC 2.18. List the emps who are joined in the month of Aug 1980.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where month(hiredate) = '9' and year(hiredate) = '1981'

# COMMAND ----------

# MAGIC %md
# MAGIC 2.19. List the emps Who Annual sal ranging from 22000 and 45000.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where (sal*12) between 22000 and 45000

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT empno, ename, job, hiredate, sal, (sal * 12) AS annual_sal
# MAGIC FROM emp
# MAGIC WHERE (sal * 12) BETWEEN 22000 AND 45000;

# COMMAND ----------

# MAGIC %md
# MAGIC 2.20. List the Enames those are having five characters in their Names.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ename from emp where length(ename) = 5;

# COMMAND ----------

# MAGIC %md
# MAGIC List the Enames those are starting with ‘S’ and with five characters.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ename from emp where ename like 'S%' and length(ename) = 5;

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps those are having four chars and third character must be ‘r’.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where length(ename) = 4 and ename like '__R%';

# COMMAND ----------

# MAGIC %md
# MAGIC List the Five character names starting with ‘S’ and ending with ‘H’.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where length(ename) =	5 and ename	like 'S%' and ename	like '%H'

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps who joined in January.

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where month(hiredate) = 1

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps who joined in the month of which second character is ‘a’.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where SUBSTRING(date_format(hiredate, 'MMMM'), 2, 1) = 'a'

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps whose Sal is four digit number ending with Zero.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where length(sal) = 4 and sal like '%0';

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps whose names having a character set ‘ll’ together.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where ename like '%LL%'

# COMMAND ----------

# MAGIC %md
# MAGIC List the emps those who joined in 80’s.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where year(hiredate) = '1981'

# COMMAND ----------

# MAGIC %md
# MAGIC 2.29.	List	the	emps	who	does	not	belong	to	Deptno	20.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from emp where deptno != 20

# COMMAND ----------

# MAGIC %md
# MAGIC  List all the emps except ‘PRESIDENT’ & ‘MGR” in asc order of Salaries.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp where job not in ('PRESIDENT', 'MANAGER') order by sal asc