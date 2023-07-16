# Little Lemon Bistro

The Little Lemon bistro website is a Django-based project that allows users to view the menu and make reservations online. It utilizes the Django Rest Framework (DRF) for API endpoints.

## Features

- View Menu: Users can view the bistro's current menu by going to `/api/menu`.
- Make Reservations: Users can create new reservations at `/api/booking`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.8 or later installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/WinTush/littlelemon.git
   cd littlelemon/
   ```

2. Create a virtual environment:

   - On macOS and Linux:

     ```bash
     python3 -m venv env
     ```

   - On Windows:

     ```bash
     py -m venv env
     ```

3. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source env/bin/activate
     ```

   - On Windows cmd shell:

     ```cmd
     .\env\Scripts\activate
     ```

4. Install requirements from `requirements.txt` file using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations as follows:

   ```bash
   python manage.py migrate
   ```

6. Run the server locally using the command below, then navigate to [http://localhost:8000/api/menu](http://localhost:8000/api/menu) or [http://localhost:8000/api/booking](http://localhost:8000/api/booking) in any web browser:

   ```bash
   python manage.py runserver
   ```

## Testing

We use pytest for our tests.

To run tests, execute:

```bash
pytest
```

Enjoy exploring Little Lemon Bistro!
