# 📦 SmartHisaab

**SmartHisaab** is a smart, customizable order tracking and management system built using **Flask**, **SQLite**, and modern HTML/CSS. It allows businesses and individuals to efficiently manage their orders, track statuses, and customize their data structures on the fly.

---

## 🚀 Features

- 🔐 User Authentication (Login & Signup)
- 📋 Dashboard to view and manage orders
- ➕ Add new orders with dynamic form fields
- 🛠️ Admin Settings to:
  - Add new columns to the orders table
  - Rename existing columns
  - Change column data types
- 📊 View order status (Pending, Delivered, etc.)
- 📁 Clean UI using Bootstrap & Tailwind-inspired styles
- ✅ Responsive and user-friendly interface

---

## 🛠️ Tech Stack

| Tech              | Description                        |
|------------------|------------------------------------|
| Flask (Python)   | Backend framework                  |
| SQLite           | Lightweight database               |
| Jinja2           | Template rendering engine          |
| HTML/CSS         | Frontend markup and styling        |
| Bootstrap Icons  | Icons and UI elements              |
| JavaScript       | Interactivity (minimal usage)      |

---

## 🔧 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smarthisaab.git
cd smarthisaab
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python app.py
```

### 5. Visit the app

Open your browser and go to `http://localhost:5000`

---

## 📁 Project Structure

```
SmartHisaab/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_order.html
│   ├── settings.html
│   └── ...more templates
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── app.py                 # Main Flask app
├── orders.db              # SQLite database
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## ✅ To-Do / Future Enhancements

- 📱 Mobile responsive enhancements
- 📤 Export data to CSV or Excel
- 🔔 Notifications for order updates
- 🔍 Search & filter functionality
- 🧑‍💼 Role-based access for admin & users

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions or improvements, please fork the repo and submit a PR.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## 🌐 Live Demo (Optional)

_Coming soon!_

---

## ✨ Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Jinja2](https://jinja.palletsprojects.com/)

---

### 🔗 Connect

Built with 💙 by [Your Name](https://github.com/yourusername)
