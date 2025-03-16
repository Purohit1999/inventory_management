# 📦 Inventory Management System

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
## 🧪 Testing

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
## 🗄️ Database

- **Database Used:** SQLite3
- **Tables Managed:**
  - `Product` – Stores all product-related data including name, price, stock, and category.
  - `Users` – Manages authentication and access control.
- **Database Management:**
  - DB Browser for SQLite is used for managing and inspecting data.
  - Data is validated before insertion to prevent inconsistencies.

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

