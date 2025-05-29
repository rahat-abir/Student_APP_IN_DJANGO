# 🎓 Student_APP_IN_DJANGO

A simple Django web application for managing student profiles with Create, Read, Update, and Delete (CRUD) functionalities.

---

## 🚀 Features

- Create new student profiles
- Edit existing student information
- Delete student records
- View all student entries
- Clean and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- Django
- HTML & CSS
- SQLite (default Django DB)

---

## 📁 Project Structure

Student_APP_IN_DJANGO/

├── student_management/ # Main Django app

│ ├── migrations/ # Database migrations

│ ├── templates/ # HTML templates

│ ├── static/ # Static files (CSS, JS, images)

│ ├── models.py # Student model

│ ├── views.py # View functions

│ ├── urls.py # App-specific URLs

│ └── admin.py # Admin panel registration

├── db.sqlite3 # SQLite database

├── manage.py # Django management script

└── README.md # Project documentation



---

## 📸 Screenshots


- **🏠 Home Page**
  
  ![Home Page](https://github.com/user-attachments/assets/06a44967-d6d9-48f7-b390-ac7abf614535)


- **➕ Create Student Profile**

  ![Create Profile](path/to/create_profile_screenshot.png)

- **✏️ Edit Student Profile**

  ![Edit Profile](path/to/edit_profile_screenshot.png)

---

## ⚙️ Setup Instructions

### 🔧 Step-by-step

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahat-abir/Student_APP_IN_DJANGO.git
   cd Student_APP_IN_DJANGO
2. **(Optional) Create and activate a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install django
4. **Apply database migrations**
   ```bash
   python manage.py migrate
5. **Run the development server**
   ```bash
   python manage.py runserver
6. **Visit in browser**
   ```bash
   http://127.0.0.1:8000/home

## 🧑‍💻 Usage

-Go to the home page to view student profiles.

-Click "Add Student" to create a new profile.

-Use the "Edit" button to modify student data.

-Use the "Delete" button to remove a student.


---



