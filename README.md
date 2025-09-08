# Flask HTMX Login Application

A simple Flask web application demonstrating HTMX functionality for user authentication and dynamic content loading.

## Features

- **User Authentication**: Login system with session management
- **HTMX Integration**: Dynamic form submission without page reloads
- **Interactive UI**: Real-time status updates and error/success messages
- **Demo Users**: Pre-configured test accounts for demonstration
- **Responsive Design**: Clean, modern interface with custom CSS

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd webapp_dev
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Demo Users

The application includes pre-configured demo users for testing:

- **admin** / password123
- **user** / userpass  
- **demo** / demo

## HTMX Features Demonstrated

1. **Dynamic Form Submission**: Login form submits without page reload
2. **Real-time Status Updates**: Navigation bar shows login status
3. **Interactive Messages**: Success/error messages appear dynamically
4. **Content Loading**: Buttons load content without page refresh

## Application Structure

```
webapp_dev/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with HTMX integration
│   ├── login.html        # Login form
│   └── dashboard.html    # Protected dashboard
└── static/               # Static files (if needed)
```

## Security Notes

- This is a demonstration application
- In production, use proper password hashing
- Store secret keys in environment variables
- Use HTTPS for authentication
- Implement proper user management with a database

## Technologies Used

- **Flask**: Python web framework
- **HTMX**: High power tools for HTML (via custom JavaScript implementation)
- **HTML/CSS**: Frontend styling and structure
- **Vanilla JavaScript**: Custom HTMX-like functionality
