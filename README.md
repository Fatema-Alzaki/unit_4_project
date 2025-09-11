# FabriQueue  

FabriQueue is a Django web application that allows engineers, makers, and students to manage **3D printing job queues**.  
Users can submit print jobs, upload STL files, assign materials, and track status from **Queued → In Progress → Completed**.  

The app automatically calculates **estimated cost per print (based on weight and material)** and **estimated print time**, while keeping a history of all jobs per user.  

This project reflects **real-world fabrication lab management systems** for 3D printers, CNC machines, and maker spaces.  

---

## ✨ Features

### 1. **User Management**
- Sign up, login, and logout with Django’s authentication.
- Each user manages their own queue of jobs.
- Superusers (admins) can view all jobs across the system.

---

### 2. **Print Job CRUD**
- Create, Read, Update, Delete jobs.
- Job attributes:
  - Name of the part
  - STL file upload
  - Material (linked to Material model)
  - Status (Queued, In Progress, Completed, Failed)
  - Estimated weight (grams)
  - Estimated print time (minutes)
  - Auto-calculated cost (material × weight)

---

### 3. **Material Management**
- Add and manage materials (PLA, ABS, Resin, etc.).
- Attributes:
  - Name
  - Type (Filament, Resin, Powder)
  - Cost per gram
- Materials are linked to jobs to calculate cost.

---

### 4. **Job Workflow**
- Default status: **Queued**
- Admin or user updates status:
  - **In Progress**
  - **Completed**
  - **Failed**
- History of updates stored with timestamps.

---

### 5. **Dashboard**
- Overview of all jobs created by a user.
- Shows:
  - Print job list
  - Status filter
  - Costs and estimated times
- Admin dashboard shows **all jobs from all users**.

---

### 6. **Future Add-ons**
- STL preview (using Three.js).
- Live 3D printer monitoring via OctoPrint API.
- Notifications when jobs complete.
- Material stock management.

---

## 🛠️ Tech Stack

- **Backend:**  
  - Django 5.x (Models, Views, Templates, Authentication)  
  - Python 3.11+  

- **Database:**  
  - SQLite (development)  
  - PostgreSQL (production-ready)  

- **Frontend:**  
  - HTML5 & CSS3 (with modular CSS in `/static/css/`)  
  - Django Templates (dynamic rendering, template inheritance)  

- **File Handling:**  
  - Django FileField for STL uploads  
  - Stored in `/media/stl_files/`  

- **Version Control:**  
  - Git + GitHub  

- **Optional Enhancements:**  
  - Docker for deployment  
  - Celery + Redis for async queue handling  

---

## 📂 Project Structure

```
fabriqueue/
 ┣ fabriqueue/                # Main project settings
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ asgi.py
 ┣ jobs/                      # Print job app
 ┃ ┣ migrations/
 ┃ ┣ templates/jobs/
 ┃ ┃ ┣ job_list.html
 ┃ ┃ ┣ job_form.html
 ┃ ┃ ┣ job_detail.html
 ┃ ┃ ┗ job_confirm_delete.html
 ┃ ┣ static/jobs/css/
 ┃ ┣ models.py
 ┃ ┣ views.py
 ┃ ┣ urls.py
 ┃ ┗ forms.py
 ┣ materials/                 # Materials app
 ┃ ┣ templates/materials/
 ┃ ┣ models.py
 ┃ ┣ views.py
 ┃ ┣ urls.py
 ┃ ┗ admin.py
 ┣ manage.py
 ┣ requirements.txt
 ┣ README.md
 ┗ .gitignore
```

---

## 🗄️ Models and ERD

### Models

#### User (Django built-in)
- username, email, password
- Relationship: One-to-Many with PrintJob

#### Material
- `name`: PLA, ABS, Resin  
- `type`: filament / resin / powder  
- `cost_per_gram`: decimal  

#### PrintJob
- `name`: job name  
- `stl_file`: file upload (STL)  
- `material`: ForeignKey → Material  
- `user`: ForeignKey → User  
- `status`: Enum (Queued, In Progress, Completed, Failed)  
- `weight_grams`: integer  
- `est_time_minutes`: integer  
- `created_at`: timestamp  

---

### Relationships

- `User` → `PrintJob` : One-to-Many  
- `Material` → `PrintJob` : One-to-Many  

**ERD Diagram**
```
User 1 ────< PrintJob >───── Material
```

```
+----------------+         +------------------+
|     User       |         |     Material     |
+----------------+         +------------------+
| id (PK)        |         | id (PK)          |
| username       |         | name             |
| email          |         | type             |
| password       |         | cost_per_gram    |
+----------------+         +------------------+
        |
        | 1-to-Many
        v
+------------------+
|    PrintJob      |
+------------------+
| id (PK)          |
| name             |
| stl_file         |
| material_id (FK) |
| user_id (FK)     |
| status           |
| weight_grams     |
| est_time_minutes |
| created_at       |
+------------------+
```

---

## 🖥️ Setup Instructions

1. Clone repo:
   ```bash
   git clone https://github.com/your-username/fabriqueue.git
   cd fabriqueue
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scriptsctivate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate database:
   ```bash
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run server:
   ```bash
   python manage.py runserver
   ```

7. Open browser:  
   👉 http://127.0.0.1:8000/

---

## 🌟 Why FabriQueue?

- Engineering relevance → directly relates to **3D printing and CNC workflows**.  
- Practical → helps labs & makerspaces manage queues efficiently.  
- Expandable → ready for integration with real printers (OctoPrint, Klipper).  
- Visual → STL uploads and cost breakdown make the UI engaging.  

---

## 📜 License
Educational project for General Assembly SEI Unit 4.  
Feel free to fork and expand.

---

💡 *FabriQueue – Where every print has its place.*
