# Student Management System (Django)

Includes student login functionality. See instructions.

## Setup (quick)

python -m venv venv
# activate venv: Windows: venv\Scripts\activate ; macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
python manage.py create_student_users
# run server
python manage.py runserver

Student accounts created will be student1, student2... with password 'studentpass'.
Login: http://127.0.0.1:8000/student/login/

