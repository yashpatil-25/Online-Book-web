# Online Book Web

**Online Book Web** is a Django-powered web application that allows users to browse books by category, view detailed information, and access external purchase links. It also features a secure admin panel for managing book listings and categories.

---

##  Technologies Used

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite  
- **Version Control**: Git

---

##  Key Features

- **Homepage**  
  Displays all book categories and featured books.

- **Category-wise Browsing**  
  Users can filter and view books based on selected categories.

- **Book Detail Page**  
  View detailed book information: name, author, description, image, and a “Buy Now” link.

- **Admin Panel**  
  Admins can add, edit, and delete categories and books through Django’s built-in admin interface.

- **Dynamic Content**  
  Books and categories are dynamically loaded from the SQLite database using Django ORM.

- **Media Support**  
  Supports uploading and displaying book cover images.

- **Responsive UI**  
  Clean and modern interface built with HTML, CSS, and Bootstrap, optimized for all devices.

- **Custom URL Routing**  
  User-friendly URL patterns:  
  `/` – Homepage  
  `/ViewBooks/<cid>` – Books by Category  
  `/ViewBookDetail/<book_id>` – Book Details

---

## How to Run the Project

1. **Clone the Repository**
   ```bash
   "git clone https://github.com/yashpatil-25/Online-Book-web.git"
   "cd Online-Book-web"
    "cd Onlinebookweb"
    "python -m venv env"
    "source env/bin/activate"  
    "On Windows: env\Scripts\activate"
    "pip install -r requirements.txt"
    "python manage.py makemigrations"
    "python manage.py migrate"
    "python manage.py createsuperuser"
    "python manage.py runserver"


# Sequence diagram
<img width="569" height="734" alt="book" src="https://github.com/user-attachments/assets/7957ae22-72ae-4204-8ebc-b5f9e7bcfa0c" />

