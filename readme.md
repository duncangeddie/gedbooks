 gedbooks/
├── controllers/                     # Python controllers for handling logic
│   ├── page_controller.py           # Controller for rendering pages (welcome, dashboard, customers, suppliers)
│   ├── customer_controller.py       # CRUD logic for customers
│   └── supplier_controller.py       # CRUD logic for suppliers
│
├── css/                             # Stylesheets for views
│   ├── customers.css                # Styling for customers page
│   ├── suppliers.css                # Styling for suppliers page
│   └── dashboard.css                # Styling for dashboard page
│
├── database/                        # Database schema and SQL dump
│   └── user_data.sql                # MySQL schema with tables (customers, suppliers, etc.)
│
├── routes/                          # Flask routing layer
│   └── web.py                       # Main Flask app with routes for pages and CRUD endpoints
│
├── views/                           # HTML templates (Jinja2)
│   ├── customers.html               # Customers list view with modals
│   ├── suppliers.html               # Suppliers list view with modals
│   ├── dashboard.html               # Dashboard with navigation buttons
│   ├── add_customer.html            # Modal for adding a customer
│   ├── edit_customer.html           # Modal for editing a customer
│   ├── delete_customer.html         # Modal for deleting a customer
│   ├── add_supplier.html            # Modal for adding a supplier
│   ├── edit_supplier.html           # Modal for editing a supplier
│   ├── delete_supplier.html         # Modal for deleting a supplier
│   └── welcome.html                 # Welcome page for new users
│
├── config/                          # Configuration files
│   └── users_database.py            # Database initialization helper
│
├── views/render.py                  # Utility for rendering templates with context
│
└── venv/                            # Python virtual environment (dependencies isolated)
