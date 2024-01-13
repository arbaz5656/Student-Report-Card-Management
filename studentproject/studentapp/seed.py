from faker import Faker
fake=Faker()
import random
from .models import *

def seed_db(n=10)-> None:
    for i in range(0,n):
        try:
            # department
            # [1,2,3,4] index like
            deparment_objs=Department.objects.all()
            rendom_index=random.randint(0,len(deparment_objs)-1)
            department=deparment_objs[rendom_index]

            # student id
            student_id =f'STU-0{random.randint(100,999)}'
            student_id_obj=StudentId.objects.create(student_id=student_id)

            student_name = fake.name()
            student_email =fake.email()
            student_age = random.randint(20,30)
            student_address=fake.address()


            # create Quesey
            student_obj=Student.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name =student_name,
            student_email =student_email,
            student_age =student_age,
            student_address=student_address
            )
        except Exception as e:
            print(e)


def create_subject_marks(n):
    try:
        studentobj=Student.objects.all()
        for student in studentobj:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)