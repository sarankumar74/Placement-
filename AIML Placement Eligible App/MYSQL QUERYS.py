import mysql.connector
from faker import Faker
import random


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8148",
    database="placement"
)
cursor = db.cursor()
fake = Faker("en_IN")

# student query start
student_query = """
INSERT INTO Student_table 
(name, age, gender, email, phone_number, enrollment_year, course_batch, city, graduation_year)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _ in range(500):
    student_data = (
        fake.name(),
        random.randint(18, 50),
        random.choice(['Male', 'Female']),
        fake.email(),
        str(fake.random_number(digits=10, fix_len=True)),
        random.randint(2024, 2025),
        f"ENR{fake.random_number(digits=5, fix_len=True)}",
        fake.city(),
        random.randint(2026, 2030)
    )
    cursor.execute(student_query, student_data)

db.commit()
# student query ens

# Programming query start
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8148",
    database="placement"
)
cursor = db.cursor()

languages = ["Python", "SQL", "Pandas", "ML", "Java"]

programming_query = """
INSERT INTO Programming_table 
(programming_id, student_id, language, problems_solved, assessment_completion, mini_project, certificate_earned, latest_project)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for programming in range(1, 501):
    programming_data = (
        programming_data,
        programming_data,
        random.choice(languages),
        fake.random_int(min=10, max=400),
        fake.random_int(min=20, max=100),
        fake.random_int(min=1, max=6),
        fake.random_int(min=1, max=8),
        fake.random_int(min=1, max=10)
    )
    cursor.execute(programming_query, programming_data)

db.commit()
# Programming query end

# Soft skill query Start

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8148",
    database="placement"
)
cursor = db.cursor()

soft_skill_query = """
INSERT INTO Soft_skill 
(soft_skill_id, student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for soft_skill in range(1, 501):
    soft_skill_data = (
        soft_skill,
        soft_skill,
        fake.random_int(min=1, max=100),
        fake.random_int(min=1, max=90),
        fake.random_int(min=1, max=80),
        fake.random_int(min=1, max=90),
        fake.random_int(min=1, max=90),
        fake.random_int(min=1, max=90)
    )
    cursor.execute(soft_skill_query, soft_skill_data)

db.commit()
# Soft skill query end

# Placement query start

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8148",
    database="placement"
)
cursor = db.cursor()

placement_query = """
INSERT INTO Placement_table 
(placement_id, student_id, mock_interview_score, internship_completed, placement_status, company_name)
VALUES (%s, %s, %s, %s, %s, %s)
"""

placement_options = ["Placed", "Not Placed", "Ready"]

for placement in range(1, 501):
    placement_data = (
        placement,
        placement,
        fake.random_int(min=1, max=80),
        fake.random_int(min=1, max=5),
        random.choice(placement_options),
        fake.company()
    )
    cursor.execute(placement_query, placement_data)

db.commit()
# placement query end
