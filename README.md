# 📦 Inventory Management System
![Homepage](images/responsive.png)

Welcome to the **Inventory Management System**! This application helps businesses efficiently manage their product inventory, including adding, updating, deleting, and uploading product data via CSV/Excel files.

---
## 📖 Table of Contents
1. [🔍 Project Overview](#-project-overview)
2. [👤 User Stories](#-user-stories)
3. [🎨 UX/UI Design](#-uxui-design)
4. [🛠️ Technologies Used](#-technologies-used)
5. [✨ Features](#-features)
6. [🧪 Testing](#-testing)
7. [🗄️ Database](#-database)
8. [📁 File Overview](#-file-overview)
9. [🚀 Deployment](#-deployment)
10. [🙏 Credit & Acknowledgments](#-credit--acknowledgments)

---
## 🔍 Project Overview

This project is a **Full-Stack Web Application** that allows businesses to manage their inventory through a web interface. It enables users to **add, update, delete, upload, and download** product data with ease.

### ✅ Key Features:
- User authentication (Login/Logout)
- CRUD operations for products
- Upload and download inventory via CSV/Excel
- Responsive design for mobile and desktop
- Secure and efficient database management

The application is built using **Django (Python), Bootstrap, JavaScript, and SQLite3**.

---
## 👤 User Stories

### 🧑‍💻 As a Business Owner, I want to:
1. **Easily add and manage inventory** to keep track of available products.
2. **Bulk upload inventory from CSV/Excel** to save time in data entry.
3. **Download inventory data as a CSV** for reporting and analysis.
4. **Quickly update product details** without navigating complex menus.
5. **Ensure security with user authentication**, restricting access to authorized personnel only.

### 👥 As a Store Employee, I want to:
1. **View all products in an organized manner** with categories and pricing.
2. **Search for products easily** using a search or filter feature.
3. **Edit product details quickly** when stock levels or prices change.
4. **Prevent accidental deletions** by adding confirmation steps.

---
## 🎨 UX/UI Design

### 💡 Design Principles:
- **Simplicity:** Minimalist and intuitive user interface.
- **Responsiveness:** Works on desktop and mobile devices.
- **Consistency:** Uses a uniform design across all pages.
- **Error Handling:** Provides clear feedback messages for user actions.

### 🖥️ Screenshots:
#### ✅ Home Page
- Displays all products with an option to add, edit, delete, or upload new products.

#### ✅ Edit Product Page (Improved Layout)
- User-friendly product editing interface with clear labels and spacing.

#### ✅ Upload CSV/Excel Page (Now Functional)
- Enhanced file upload validation with clear messages and confirmation prompts.

#### ✅ User Authentication
- Secure login/logout system with session management.

---
## 🛠️ Technologies Used

### 💻 Frontend:
- **HTML, CSS, Bootstrap** – For responsive and stylish UI.
- **JavaScript (ES6+)** – For interactive elements and form validation.

### 🖥️ Backend:
- **Django (Python)** – Robust framework for handling business logic.
- **SQLite3** – Lightweight database for efficient data storage.
- **Pandas (Python Library)** – Used for handling CSV/Excel file uploads.

### 🛠️ Tools & Deployment:
- **Git & GitHub** – Version control and repository management.
- **DB Browser for SQLite** – Database inspection and management.
- **Django Admin Panel** – For managing inventory easily from the backend.

---
## ✨ Features

### 🏗️ Core Features:
✅ User authentication (Login/Logout)  
✅ Product Management (Add, Update, Delete)  
✅ Upload CSV/Excel file to add bulk products  
✅ Download inventory as CSV for reports  
✅ Secure access with Django's built-in authentication  
✅ Search and filter products  
✅ Mobile-responsive design  

### 🔜 Future Enhancements:
🚀 Implement product categories and search filters  
🚀 Add barcode scanning for faster data entry  
🚀 Introduce a reporting dashboard with insights  

---
## 🧪 Testing :
Ensuring the **Inventory Management System** functions correctly across different environments is a key part of the development process. The following tests have been conducted to validate the system's **functionality, responsiveness, and error handling**.

### **📝 Testing Matrix**

#### **✅ Validation Results**

| **Validation Type** | **Status**                             | **Notes**                            |
|---------------------|----------------------------------------|--------------------------------------|
| **HTML**            | ✅ Passed (No errors or warnings)       | Code validated using W3C Validator   |
| **CSS**             | ✅ Passed (No errors found)             | Code validated using W3C CSS Validator |
| **JavaScript**      | ✅ Passed (No errors or warnings)       | Checked using ESLint and JSHint      |

#### **📱 Responsiveness Test Results**

| **Device Type/Width**                          | **Pixel 5** | **Galaxy S8+** | **iPhone 11** | **iPad Mini** | **iPad Air** | **Surface Pro** | **Desktop 1024px+** | **Desktop 1280px+** | **iMac 1900px+** |
|------------------------------------------------|-------------|----------------|---------------|---------------|--------------|-----------------|---------------------|---------------------|-------------------|
| **Devices with width of 375px or more**        | Good        | Good           | Good          | n/a           | Good         | n/a             | Good                | Good                | Good              |
| **Devices with width of 768px or more**        | n/a         | Good           | Good          | Good          | Good         | Good            | Good                | Good                | Good              |
| **Devices with width of 1024px or more**       | n/a         | n/a            | Good          | n/a           | Good         | Good            | Good                | Good                | Good              |
| **Internal Links**                             | Good        | Good           | Good          | Good          | Good         | Good            | Good                | Good                | Good              |

#### **🌐 Browser Compatibility**

| **Browser**               | **Chrome** | **Safari** | **Firefox** | **Edge** |
|---------------------------|------------|------------|-------------|----------|
| **Appearance**            | Good       | Good       | Good        | Good     |
| **Responsiveness**        | Good       | Good       | Good        | Good     |

---
Here is the updated **Testing** section of your **README.md**, now including subheadings for **Testing User Stories, Manual Testing, Bugs & Error Checking, Solved Bugs, Known Bugs, and Python Validation**.

---
### **📌 Testing User Stories**
Each user story has been tested to confirm the system meets its intended purpose.

#### **🧑‍💻 As a Business Owner, I want to:**
✅ **Easily add and manage inventory** – Successfully tested via manual form entries and database verification.  
✅ **Bulk upload inventory from CSV/Excel** – Multiple CSV/Excel files were uploaded with different structures to test compatibility.  
✅ **Download inventory data as a CSV** – Confirmed that the file downloads successfully and contains correct product data.  
✅ **Quickly update product details** – Checked that all product details can be modified seamlessly.  
✅ **Ensure security with user authentication** – Verified login/logout system, including session expiration and invalid login attempts.

#### **👥 As a Store Employee, I want to:**
✅ **View all products in an organized manner** – Products are correctly displayed on the dashboard.  
✅ **Search for products easily** – Implemented a search/filter option to locate products efficiently.  
✅ **Edit product details quickly** – Users can update product details via an easy-to-use form.  
✅ **Prevent accidental deletions** – Implemented confirmation prompts before deletion.

---

### **📝 Manual Testing**
**Manual tests** were conducted on different devices, browsers, and screen sizes. Below is an overview of the **core test scenarios**:

| **Test Case** | **Expected Outcome** | **Actual Outcome** | **Status** |
|--------------|---------------------|--------------------|------------|
| User Login with Valid Credentials | Redirects to dashboard | Works as expected | ✅ Passed |
| User Login with Incorrect Credentials | Shows error message | Works as expected | ✅ Passed |
| Product Addition via Form | Saves product to database and displays it | Works as expected | ✅ Passed |
| Product Update | Updates the existing product details | Works as expected | ✅ Passed |
| Product Deletion | Removes product from database after confirmation | Works as expected | ✅ Passed |
| CSV Upload (Valid File) | Imports products successfully | Works as expected | ✅ Passed |
| CSV Upload (Invalid File) | Displays an error message | Works as expected | ✅ Passed |
| Download Inventory Data | Downloads CSV with correct data | Works as expected | ✅ Passed |
| Logout Functionality | Logs user out and redirects to login page | Works as expected | ✅ Passed |

---

### **🐛 Bugs & Error Checking**
**During development, several bugs and issues were identified and resolved. Below is a breakdown:**

#### **🔍 Solved Bugs**
1. **CSV Upload Not Working:**  
   - **Issue:** The system did not correctly parse CSV headers, causing upload failures.  
   - **Fix:** Implemented dynamic column mapping and validation for uploaded files.

2. **Broken Logout Redirect:**  
   - **Issue:** Users remained logged in even after clicking "Logout."  
   - **Fix:** Ensured Django’s `logout()` function properly cleared sessions.

3. **Delete Button Instantly Deleting Without Confirmation:**  
   - **Issue:** Clicking "Delete" immediately removed products without warning.  
   - **Fix:** Added a **JavaScript confirmation popup** before deletion.

4. **CSS Styling Issues in Mobile View:**  
   - **Issue:** Some elements were overlapping on smaller screens.  
   - **Fix:** Adjusted CSS for better mobile responsiveness.

---

### **⚠ Known Bugs**
Despite rigorous testing, the following **minor issues** are present:

1. **Pagination for Product List Needs Improvement**  
   - Current implementation loads all products on a single page.
   - Solution planned: Implement **Django’s built-in pagination feature**.

2. **Error Handling for Large File Uploads Needs Refinement**  
   - System currently rejects oversized files, but lacks detailed feedback.
   - Solution planned: Display a **file size warning** before upload.

---

### **🐍 Python Validation**
To ensure **code quality and compliance**, **Python validation tools** were used:

| **Validation Type** | **Tool Used** | **Status** |
|--------------------|--------------|------------|
| **PEP8 Compliance (Python Code Style Guide)** | `flake8` | ✅ Passed |
| **HTML Validation** | W3C Validator | ✅ Passed |
| **CSS Validation** | W3C CSS Validator | ✅ Passed |
| **JavaScript Validation** | ESLint & JSHint | ✅ Passed |
| **Django Security Checks** | `python manage.py check --deploy` | ✅ Passed |

All **Python scripts follow PEP8 standards**, and Django’s security checks confirm no major vulnerabilities.

---

## **✅ Conclusion**
Testing has ensured that the **Inventory Management System** is **fully functional, secure, and responsive**. Future improvements will focus on **enhancing pagination, improving error handling, and adding more automated tests**. 

---
## 🗄️ Database

- **Database Used:** SQLite3
- **Tables Managed:**
  - `Product` – Stores all product-related data including name, price, stock, and category.
  - `Users` – Manages authentication and access control.
- **Database Management:**
  - DB Browser for SQLite is used for managing and inspecting data.
  - Data is validated before insertion to prevent inconsistencies.

### **Entity Relationship Diagram (ERD)**:

| **Products**  | **Users**  | **Categories** | **Orders**  | **Order_Items**  |
|--------------|------------|---------------|-------------|------------------|
| `id` (PK)   | `id` (PK)   | `id` (PK)     | `id` (PK)   | `id` (PK)        |
| `name`      | `username`  | `name`        | `user_id` (FK) | `order_id` (FK) |
| `description` | `email`   | `description` | `order_date` | `product_id` (FK) |
| `price`     | `password`  |               | `total_price` | `quantity`      |
| `stock`     |            |               | `status`     | `subtotal_price` |
| `category_id` (FK) |    |               |             |                  |

### **Relationships**:
1. **One-to-Many:** A **Category** can have multiple **Products**, but each product belongs to only one category.
2. **One-to-Many:** A **User** can place multiple **Orders**, but an order belongs to one user.
3. **Many-to-Many:** **Orders** contain multiple **Products**, and a product can belong to multiple orders (handled through the **Order_Items** table).
4. **Foreign Keys:**
   - `category_id` in **Products** references `id` in **Categories**.
   - `user_id` in **Orders** references `id` in **Users**.
   - `order_id` and `product_id` in **Order_Items** reference `id` in **Orders** and **Products**, respectively.

This structure provides a **normalized relational database** that ensures **data consistency** and **efficient inventory tracking**.

---
## 🙏 Credit & Acknowledgments
- **Bootstrap** for UI styling.
- **Django Documentation** for backend support.
- **Pandas** for handling CSV/Excel uploads.
- **GitHub & Open-Source Community** for valuable resources.

---
## 🎉 Conclusion
This **Inventory Management System** simplifies inventory tracking and product management for businesses. Future improvements will enhance automation, analytics, and reporting features.

💡 **Feel free to fork, improve, and contribute to the project!** 🚀

