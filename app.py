import sqlite3
# Add these imports at the top
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Create a static folder for CSS if it doesn't exist
if not os.path.exists('static/css'):
    os.makedirs('static/css')

# Create CSS file
with open('static/css/styles.css', 'w') as f:
    f.write("""/* SmartHisaab - Modern Order Management System Stylesheet */
:root {
  /* Color Palette */
  --primary: #4361ee;
  --primary-dark: #3a56d4;
  --secondary: #3f37c9;
  --accent: #f72585;
  --success: #4cc9f0;
  --warning: #f9c74f;
  --danger: #ef476f;
  --light: #f8f9fa;
  --dark: #212529;
  --gray: #6c757d;
  --light-gray: #e9ecef;
  
  /* Typography */
  --font-main: 'Poppins', sans-serif;
  --font-secondary: 'Open Sans', sans-serif;
  
  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2.5rem;
  
  /* Borders */
  --border-radius: 8px;
  --border-radius-lg: 12px;
  --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --box-shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}

/* Global Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-main);
  line-height: 1.6;
  color: var(--dark);
  background-color: #f5f7ff;
  padding: 0;
  margin: 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: var(--spacing-md);
}

/* Header & Navigation */
.navbar {
  background: linear-gradient(to right, var(--primary), var(--secondary));
  color: white;
  padding: var(--spacing-md) var(--spacing-lg);
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: var(--box-shadow);
}

.navbar-brand {
  display: flex;
  align-items: center;
  font-size: 1.8rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
}

.navbar-brand i {
  margin-right: var(--spacing-sm);
}

.navbar-nav {
  display: flex;
  list-style: none;
  gap: var(--spacing-lg);
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--border-radius);
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

/* Cards */
.card {
  background-color: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  padding: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
}

.card-header {
  border-bottom: 1px solid var(--light-gray);
  padding-bottom: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  font-weight: 600;
  font-size: 1.25rem;
  color: var(--primary);
}

/* Forms */
.form-container {
  max-width: 600px;
  margin: 0 auto;
  background-color: white;
  padding: var(--spacing-xl);
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
}

.form-title {
  color: var(--primary);
  margin-bottom: var(--spacing-lg);
  text-align: center;
  font-weight: 600;
}

.form-group {
  margin-bottom: var(--spacing-md);
}

label {
  display: block;
  margin-bottom: var(--spacing-xs);
  font-weight: 500;
  color: var(--dark);
}

input[type="text"],
input[type="password"],
input[type="number"],
input[type="email"],
select,
textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--light-gray);
  border-radius: var(--border-radius);
  font-family: var(--font-main);
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.25);
}

/* Buttons */
.btn {
  display: inline-block;
  font-weight: 500;
  text-align: center;
  padding: 0.75rem 1.5rem;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-size: 1rem;
  text-decoration: none;
}

.btn-primary {
  background-color: var(--primary);
  color: white;
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-secondary {
  background-color: var(--secondary);
  color: white;
}

.btn-secondary:hover {
  background-color: #332fb5;
}

.btn-success {
  background-color: var(--success);
  color: white;
}

.btn-success:hover {
  background-color: #3db3d9;
}

.btn-danger {
  background-color: var(--danger);
  color: white;
}

.btn-danger:hover {
  background-color: #d93e64;
}

.btn-sm {
  padding: 0.4rem 0.8rem;
  font-size: 0.875rem;
}

.btn-outline {
  background-color: transparent;
  border: 1px solid var(--primary);
  color: var(--primary);
}

.btn-outline:hover {
  background-color: var(--primary);
  color: white;
}

.btn-icon {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Tables */
.table-container {
  overflow-x: auto;
  margin-bottom: var(--spacing-lg);
}

.table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
}

.table th {
  background-color: var(--primary);
  color: white;
  text-align: left;
  padding: var(--spacing-md);
  font-weight: 600;
}

.table tr:nth-child(even) {
  background-color: rgba(67, 97, 238, 0.05);
}

.table td {
  padding: var(--spacing-md);
  border-bottom: 1px solid var(--light-gray);
}

.table tr:last-child td {
  border-bottom: none;
}

.table .actions {
  display: flex;
  gap: var(--spacing-sm);
}

/* Status Badges */
.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 500;
}

.badge-pending {
  background-color: var(--warning);
  color: var(--dark);
}

.badge-processing {
  background-color: var(--primary);
  color: white;
}

.badge-delivered {
  background-color: var(--success);
  color: white;
}

.badge-cancelled {
  background-color: var(--danger);
  color: white;
}

/* Alerts & Messages */
.alert {
  padding: var(--spacing-md);
  border-radius: var(--border-radius);
  margin-bottom: var(--spacing-lg);
  font-weight: 500;
}

.alert-success {
  background-color: rgba(76, 201, 240, 0.2);
  color: var(--success);
  border-left: 4px solid var(--success);
}

.alert-danger {
  background-color: rgba(239, 71, 111, 0.2);
  color: var(--danger);
  border-left: 4px solid var(--danger);
}

/* Dashboard Stats */
.stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
}

.stat-card {
  background-color: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  padding: var(--spacing-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: var(--spacing-md);
  color: var(--primary);
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: var(--spacing-xs);
  color: var(--dark);
}

.stat-label {
  color: var(--gray);
  font-size: 1rem;
}

/* Footer */
.footer {
  background-color: var(--secondary);
  color: white;
  text-align: center;
  padding: var(--spacing-lg);
  margin-top: var(--spacing-xl);
}

/* Login Page Specific */
.login-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #4361ee, #3a0ca3);
}

.login-container {
  width: 100%;
  max-width: 400px;
  background-color: white;
  border-radius: var(--border-radius-lg);
  padding: var(--spacing-xl);
  box-shadow: var(--box-shadow-lg);
}

.login-logo {
  text-align: center;
  margin-bottom: var(--spacing-lg);
  font-size: 2rem;
  font-weight: 600;
  color: var(--primary);
}

/* Utilities */
.text-center {
  text-align: center;
}

.mb-1 { margin-bottom: var(--spacing-sm); }
.mb-2 { margin-bottom: var(--spacing-md); }
.mb-3 { margin-bottom: var(--spacing-lg); }
.mb-4 { margin-bottom: var(--spacing-xl); }

.mt-1 { margin-top: var(--spacing-sm); }
.mt-2 { margin-top: var(--spacing-md); }
.mt-3 { margin-top: var(--spacing-lg); }
.mt-4 { margin-top: var(--spacing-xl); }

.d-flex {
  display: flex;
}

.justify-between {
  justify-content: space-between;
}

.align-center {
  align-items: center;
}

.flex-wrap {
  flex-wrap: wrap;
}

.gap-2 {
  gap: var(--spacing-md);
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    padding: var(--spacing-md);
  }
  
  .navbar-brand {
    margin-bottom: var(--spacing-md);
  }
  
  .navbar-nav {
    flex-wrap: wrap;
    justify-content: center;
    gap: var(--spacing-sm);
  }
  
  .stat-card {
    margin-bottom: var(--spacing-md);
  }
  
  .table th, 
  .table td {
    padding: var(--spacing-sm);
  }
  
  .form-container {
    padding: var(--spacing-lg);
  }
}
""")

# Create templates folder if it doesn't exist
if not os.path.exists('templates'):
    os.makedirs('templates')

# Create base template
with open('templates/base.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}SmartHisaab - Digital Order Tracking{% endblock %}</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% if 'username' in session %}
    <!-- Navigation -->
    <nav class="navbar">
        <a href="/home" class="navbar-brand">
            <i class="fas fa-clipboard-list"></i> SmartHisaab
        </a>
        <ul class="navbar-nav">
            <li><a href="/home" class="nav-link"><i class="fas fa-home"></i> Home</a></li>
            <li><a href="/dashboard" class="nav-link"><i class="fas fa-th-list"></i> Orders</a></li>
            <li><a href="/add" class="nav-link"><i class="fas fa-plus-circle"></i> New Order</a></li>
            <li><a href="/add_column" class="nav-link"><i class="fas fa-columns"></i> Manage Columns</a></li>
            <li><a href="/" class="nav-link"><i class="fas fa-sign-out-alt"></i> Logout</a></li>
        </ul>
    </nav>
    {% endif %}

    <!-- Main Content -->
    <div class="container">
        {% block content %}{% endblock %}
    </div>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2025 SmartHisaab. All rights reserved.</p>
    </footer>

    {% block scripts %}{% endblock %}
</body>
</html>""")

# Create base_login template
with open('templates/base_login.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}SmartHisaab - Digital Order Tracking{% endblock %}</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
    
    {% block scripts %}{% endblock %}
</body>
</html>""")

# The rest of app.py remains the same

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
# Insert a default user if it doesn't already exist
cursor.execute("SELECT * FROM users WHERE username = ?", ('admin',))
if not cursor.fetchone():
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))
    print("✅ Default user created: admin / admin123")
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('❌ Invalid username or password')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/add', methods=['GET', 'POST'])

def add_order():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Get column information for dynamic form creation
    cursor.execute("PRAGMA table_info(orders)")
    columns_info = cursor.fetchall()  # [(cid, name, type, notnull, default_value, pk), ...]

    if request.method == 'POST':
        order_data = {}

        for col in columns_info:
            col_name = col[1]
            col_type = col[2]

            if col_name == 'id':
                continue  # Skip auto-increment primary key

            if col_name == 'status':
                order_data[col_name] = 'Pending'  # Default value
                continue

            value = request.form.get(col_name)

            # Type conversion based on column type
            if 'INT' in col_type.upper():
                value = int(value)
            elif 'REAL' in col_type.upper():
                value = float(value)

            order_data[col_name] = value
            
        # Prepare dynamic INSERT query
        column_names = ', '.join(order_data.keys())
        placeholders = ', '.join(['?'] * len(order_data))
        values = list(order_data.values())

        cursor.execute(f"INSERT INTO orders ({column_names}) VALUES ({placeholders})", values)

        order_id = cursor.lastrowid # Capture the auto-generated ID

        conn.commit()
        conn.close()

        print(f"Inserted Order ID: {order_id}")  # Optional: for debug/logging

        return redirect(url_for('dashboard'))

    conn.close()
    return render_template('add_order.html', column_names=columns_info)


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Get all column names
    cursor.execute("PRAGMA table_info(orders)")
    columns_info = cursor.fetchall()
    column_names = [info[1] for info in columns_info]  # Extract column names

    # Get all order rows
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()

    return render_template('dashboard.html', column_names=column_names, orders=orders)


@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/update/<int:order_id>', methods=['GET', 'POST'])
def update_order(order_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Fetch table column info
    cursor.execute("PRAGMA table_info(orders)")
    columns_info = cursor.fetchall()

    if request.method == 'POST':
        updates = []
        values = []

        for col in columns_info:
            col_name = col[1]
            col_type = col[2]

            if col_name == 'id':
                continue  # Never update ID

            value = request.form.get(col_name)

            if 'INT' in col_type.upper():
                value = int(value)
            elif 'REAL' in col_type.upper():
                value = float(value)

            updates.append(f"{col_name} = ?")
            values.append(value)

        values.append(order_id)  # For the WHERE clause
        update_query = f"UPDATE orders SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(update_query, values)

        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    # Fetch existing order data
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    order = cursor.fetchone()
    conn.close()

    return render_template('update.html', order=order, columns_info=columns_info)

@app.route('/add_column', methods=['GET','POST'])
def add_column():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        new_column = request.form['column_name']
        table_name = request.form['table_name']
        column_type = request.form['column_type'] 
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        try:
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {new_column} {column_type}")
            conn.commit()
            message = f"✅ Column '{new_column}' added to table '{table_name}'"
        except Exception as e:
            message = f"❌ Error: {e}"
        finally:
            conn.close()

        return render_template('add_column.html', message=message)
    return render_template('add_column.html')

@app.route('/update_column', methods=['GET','POST'])
def update_column():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn=sqlite3.connect('orders.db')
    cursor=conn.cursor()
    # Fetch table column info
    cursor.execute("PRAGMA table_info(orders)")
    columns_info = cursor.fetchall()
    if request.method == 'POST':
        table_name = request.form['table_name']
        column_name = request.form['old_column_name']
        new_column_name = request.form['new_column_name']
        column_type = request.form['new_column_type']
        try:
            cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {column_name} TO {new_column_name}")
            conn.commit()
            message = f"✅ Column '{column_name}' updated to '{new_column_name}' in table '{table_name}'"
        except Exception as e:
            message = f"❌ Error: {e}"
        conn.close()
        return render_template('update_column.html', columns_info=columns_info, message=message)

    return render_template('update_column.html', columns_info=columns_info)

@app.route('/change_column_type', methods=['GET', 'POST'])
def change_column_type():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        column_to_change = request.form['column_name']
        new_type = request.form['new_type']

        # Get existing schema
        cursor.execute(f"PRAGMA table_info(orders)")
        old_columns = cursor.fetchall()

        new_columns_def = []
        column_names = []
        for col in old_columns:
            name = col[1]
            old_type = col[2]
            if name == column_to_change:
                type_to_use = new_type
            else:
                type_to_use = old_type
            new_columns_def.append(f"{name} {type_to_use}")
            column_names.append(name)

        # Create temp table
        cursor.execute(f"CREATE TABLE orders_new ({', '.join(new_columns_def)})")

        # Copy data
        cursor.execute(f"INSERT INTO orders_new ({', '.join(column_names)}) SELECT {', '.join(column_names)} FROM orders")

        # Drop old table
        cursor.execute("DROP TABLE orders")

        # Rename new table
        cursor.execute("ALTER TABLE orders_new RENAME TO orders")

        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))

    # On GET
    cursor.execute("PRAGMA table_info(orders)")
    columns_info = cursor.fetchall()
    conn.close()
    return render_template('change_column_type.html', columns_info=columns_info)


if __name__ == '__main__':
    app.run(debug=True)