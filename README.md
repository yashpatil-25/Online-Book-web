# Online Book Web

**Online Book Web** is a Django-powered web application that allows users to browse books by category, view detailed information, and access external purchase links. It also features a secure admin panel for managing book listings and categories.

---

# Technologies Used

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite  
- **Version Control**: Git

---

# Key Features

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

#  How to Run the Project

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

## Sequence diagram : https://sequencediagram.org/index.html#initialData=%40startuml%0Aactor%20User%0Aparticipant%20%22Browser%22%20as%20B%0Aparticipant%20%22Django%20URL%20Dispatcher%22%20as%20URL%0Aparticipant%20%22UserApp.views%22%20as%20View%0Aparticipant%20%22models.py%22%20as%20Model%0Aparticipant%20%22templates%22%20as%20Template%0Adatabase%20%22Database%22%20as%20DB%0A%0A%3D%3D%20Homepage%20Request%20%3D%3D%0AUser%20-%3E%20B%20%3A%20Visit%20Homepage%20(%22%2F%22)%0AB%20-%3E%20URL%20%3A%20Send%20GET%20request%0AURL%20-%3E%20View%20%3A%20Call%20homepage()%0AView%20-%3E%20Model%20%3A%20Category.objects.all()%5CnBook.objects.all()%0AModel%20-%3E%20DB%20%3A%20Fetch%20categories%20and%20books%0ADB%20--%3E%20Model%20%3A%20Return%20queryset%0AModel%20--%3E%20View%20%3A%20List%20of%20categories%20and%20books%0AView%20-%3E%20Template%20%3A%20Render%20homepage.html%0ATemplate%20-%3E%20B%20%3A%20Display%20homepage%20(with%20books%20and%20categories)%0A%0A%3D%3D%20View%20Books%20by%20Category%20%3D%3D%0AUser%20-%3E%20B%20%3A%20Click%20on%20category%0AB%20-%3E%20URL%20%3A%20GET%20%2FViewBooks%2F%3Ccid%3E%0AURL%20-%3E%20View%20%3A%20Call%20ViewBooks(cid)%0AView%20-%3E%20Model%20%3A%20Book.objects.filter(category_id%3Dcid)%0AModel%20-%3E%20DB%20%3A%20Query%20books%20for%20given%20category%0ADB%20--%3E%20Model%20%3A%20Return%20books%0AModel%20--%3E%20View%20%3A%20List%20of%20books%0AView%20-%3E%20Template%20%3A%20Render%20category_books.html%0ATemplate%20-%3E%20B%20%3A%20Display%20category%20books%0A%0A%3D%3D%20View%20Book%20Details%20%3D%3D%0AUser%20-%3E%20B%20%3A%20Click%20on%20a%20book%0AB%20-%3E%20URL%20%3A%20GET%20%2FViewBookDetail%2F%3Cbook_id%3E%0AURL%20-%3E%20View%20%3A%20Call%20viewBookDetail(book_id)%0AView%20-%3E%20Model%20%3A%20Book.objects.get(id%3Dbook_id)%0AModel%20-%3E%20DB%20%3A%20Get%20book%20detail%0ADB%20--%3E%20Model%20%3A%20Return%20book%20info%0AModel%20--%3E%20View%20%3A%20Book%20object%0AView%20-%3E%20Template%20%3A%20Render%20book_detail.html%0ATemplate%20-%3E%20B%20%3A%20Show%20book%20description%20and%20buy%20link%0A%0A%40enduml%0A
# Sequence diagram
<img width="569" height="734" alt="book" src="https://github.com/user-attachments/assets/a2fdbff8-38c2-40b8-a57b-71a625dd9bea" />



