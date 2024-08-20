# Service Management System

A Django-based application to manage and monitor various services and their configurations, including environment variables, network configurations, dependencies, and more.

## Features

- Manage multiple service systems
- Track environment variables, configuration files, and dependencies
- Configure network settings, logging, and monitoring tools
- Set up and manage applications, ports, and scaling configurations
- Disaster recovery, backup, and runbook management

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**: Make sure Python is installed on your system.
- **Django 3.2+**: This project uses Django as the web framework.
- **PostgreSQL** (Optional): If you plan to use PostgreSQL as your database.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/zaelgohary/service-management-system.git
    cd your-repo-name

    `````

2. **Create a virtual environment (recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set up the database**

    Update the DATABASES setting in settings.py if you are using a different database (e.g., PostgreSQL).
    Then, run the following commands to apply migrations:

      ```bash
      python manage.py migrate
      ```

4. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**

    ```bash
    python manage.py runserver
    ```

## Usage

Once the development server is running, you can access the application in your web browser at:

```bash
http://127.0.0.1:8000/admin/
```

1. Log in to the admin panel using the superuser account you created.
2. Manage your service systems: Add, edit, and manage your service systems and related configurations like environment variables, network settings, applications, and more.
3. Search and filter: Use the search fields provided in the admin panel to quickly find and manage specific entries.
