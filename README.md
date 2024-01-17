# Job Portal Web Application

Welcome to the Job Portal Web Application! This web application is built using Django, providing a platform for job seekers and employers to connect. It facilitates the process of job posting, job searching, and application submission.

##### landing page

![Landing image](https://github.com/Noahwekesa/Job-django/blob/master/screenshot/landingpage.png)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

### For Job Seekers:

- **User Registration and Authentication:** Users can create accounts, log in, and manage their profiles.
- **Job Search:** Browse and search for job listings based on various criteria.
- **Application Submission:** Apply for jobs through the platform.
- **Resume Upload:** Job seekers can upload their resumes to enhance their profiles.

### For Employers:

- **Company Profile Management:** Employers can create and manage their company profiles.
- **Job Posting:** Post job listings with detailed information.
- **Application Management:** Employers can view and manage job applications received.

### General Features:

- **Responsive Design:** The application is designed to work seamlessly on various devices.
- **Admin Panel:** An admin panel is available for managing users, job listings, and other aspects of the application.
- **Email Notifications:** Users receive notifications for account creation, application submissions, etc.

## Installation

### Prerequisites:

- Python 3.x
- Django

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/noahwekesa/Job-django.git
   ```
2. Navigate into the repository

```bash
cd Job-django
```

3. Install virtualenv

```bash
pip install virtualenv venv
```

4. Activate virtualenv

```bash
source venv/bin/Activate
```

5. Install dependencies

```bash

pip install -r requirements.txt
```

6. Apply migrations

```bash
cd src

python manage.py migrate
```

7. Create superuser

```sh
python manage.py createsuperuser
```

8.  Run the development server:

```bash

python manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/ to access the application.
