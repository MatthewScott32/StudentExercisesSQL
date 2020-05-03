import sqlite3
from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

class StudentExerciseReports():
    """Methods for reports on the Student Exercise database"""
    
    def __init__(self):
        self.db_path = "/home/blagg32/workspace/sql/StudentExercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])
            
    def all_students(self):
        """retrieve all students with the cohort name"""
        
        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT s.Id,
                   s.FirstName,
                   s.LastName,
                   s.SlackHandle,
                   s.CohortId,
                   c.Name
            FROM Student s
            JOIN Cohort c on s.CohortId = c.Id
            ORDER BY s.CohortId
            """)
            
            all_students = db_cursor.fetchall()
            
            # print(all_students)
            
            for student in all_students:    
                # print(f'{student.first_name} {student.last_name} is in {student.cohort}')
                print(student)
                # [print(s) for s in all_students]
                
    def all_cohorts(self):
    
        """Retrieve all cohorts with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Id,
                   c.Name
            FROM Cohort c
            """)

            all_cohorts = db_cursor.fetchall()
            
            for cohort in all_cohorts:
                print(cohort) 
                
    def all_instructors(self):
        
        """Retrieve all instructors with the instructors name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.Id,
                   i.FirstName,
                   i.LastName,
                   i.SlackHandle,
                   i.CohortId,
                   i.Specialty,
                   c.Name
            FROM Instructor i
            JOIN Cohort c on i.CohortId = c.Id
            ORDER BY i.CohortId;
            """)

            all_instructors = db_cursor.fetchall()
            
            for instructors in all_instructors:
                print(instructors)
                
    def all_exercises(self):
        
        """Retrieve all exercises with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                   e.Name,
                   e.ExLanguage
            FROM Exercise e
            """)

            all_exercises = db_cursor.fetchall()
            
            for exercise in all_exercises:
                print(exercise)
                
    def all_javascript(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.Id,
                   e.Name,
                   e.ExLanguage
            FROM Exercise e                  
            """)
            all_javascript = db_cursor.fetchall()
            for exercise in all_javascript:
                if exercise.language == 'JavaScript':
                    print(f'Java exercise {exercise}')
                    
    def all_python(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.Id,
                   e.Name,
                   e.ExLanguage
            FROM Exercise e                  
            """)
            all_python = db_cursor.fetchall()
            for exercise in all_python:
                if exercise.language == 'Python':
                    print(f'Python exercise {exercise}') 
                    
    def all_sql(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.Id,
                   e.Name,
                   e.ExLanguage
            FROM Exercise e                  
            """)
            all_sql = db_cursor.fetchall()
            for exercise in all_sql:
                if exercise.language == 'SQL':
                    print(f'SQL exercise {exercise}')   
                    
    def all_html(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT e.Id,
                   e.Name,
                   e.ExLanguage
            FROM Exercise e                  
            """)
            all_html = db_cursor.fetchall()
            for exercise in all_html:
                if exercise.language == 'HTML':
                    print(f'HTML exercise {exercise}')               
                 
    def exercises_and_students(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
            exercises = dict()
            db_cursor.execute("""
                SELECT
                    e.Id ExerciseId,
                    e.Name,
                    s.Id StudentId,
                    s.FirstName,
                    s.LastName
                FROM Exercise e
                JOIN StudentExercise se on se.ExerciseId = e.Id
                JOIN Student s on s.Id = se.StudentId              
            """)
            
            dataset = db_cursor.fetchall()
            
            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                    
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
                    
    def student_exercise(self):
        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""      
            SELECT
                s.Id,
	            s.FirstName,
	            s.LastName,
	            e.Id,
	            e.Name
            FROM Exercise e
            JOIN StudentExercise se on se.ExerciseId = e.Id
            JOIN Student s on s.Id = se.StudentId""")

            data = db_cursor.fetchall()

            for row in data:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')
     
        
reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_instructors()
reports.all_exercises()
reports.all_javascript()
reports.all_python()
reports.all_sql()
reports.all_html()
reports.exercises_and_students()
reports.student_exercise()

                