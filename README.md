# Project Cost Prediction

A full-stack machine learning application that predicts project costs based on various parameters like project type, client industry, timeline, team allocation, complexity, and revision count.

## Features

- **ML-Powered Cost Prediction**: Uses trained XGBoost and scikit-learn models to predict project costs
- **RESTful API**: Flask backend with CORS support for easy integration
- **Modern Frontend**: React-based UI with Vite for fast development and builds
- **Dataset Generation**: Synthetic dataset generation for realistic training data
- **Model Training**: Jupyter notebook for model development and experimentation

## Project Structure

```
Project_Cost_Prediction/
├── backend/
│   ├── app.py                                    # Flask application & API endpoints
│   ├── dataset.py                               # Synthetic dataset generation
│   ├── requirements.txt                         # Python dependencies
│   ├── model.ipynb                              # Jupyter notebook for model training
│   ├── cost_prediction_model.pkl                # Trained ML model (binary file)
│   ├── project_cost_dataset.csv                 # Project dataset
│   ├── synthetic_project_cost_dataset.csv       # Synthetic dataset variant 1
│   └── synthetic_project_cost_dataset_realistic.csv  # Synthetic dataset variant 2
├── frontend/
│   ├── src/
│   │   ├── main.jsx                             # React entry point
│   │   ├── App.jsx                              # Main App component
│   │   ├── App.css                              # Application styles
│   │   ├── index.css                            # Global styles
│   │   └── assets/                              # Static assets
│   ├── public/                                  # Public assets
│   ├── package.json                             # JavaScript dependencies
│   ├── vite.config.js                           # Vite configuration
│   ├── eslint.config.js                         # ESLint rules
│   └── README.md                                # Frontend documentation
└── index.html                                    # Root HTML file
```

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+** - For the backend
- **Node.js 16+** - For the frontend
- **npm or yarn** - Package manager for Node.js

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Project_Cost_Prediction
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create a Python virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install
```

## Running the Project

### Starting the Backend

```bash
# From the backend directory
# Make sure the virtual environment is activated (if created)

python app.py
```

The Flask backend will start on `http://localhost:5000`

### Starting the Frontend

```bash
# From the frontend directory

# For development with hot reload:
npm run dev

# Or build for production:
npm run build

# Or preview production build:
npm run preview
```

The frontend will start on `http://localhost:5173` (Vite default port)

### Running Both Simultaneously

You can run both backend and frontend in separate terminal windows:

**Terminal 1 (Backend):**
```bash
cd backend
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

Access the application at `http://localhost:5173`

## API Endpoints

### Health Check
- **POST** `/simple` - Simple health check endpoint
  - Response: `{"message": "Hello from Flask!", "status": "Success"}`

### Cost Prediction
- **POST** `/predict` - Predict project cost
  - Request body:
    ```json
    {
      "project_type": "AI/ML Solution",
      "client_industry": "E-commerce",
      "estimated_timeline_months": 5,
      "team_allocation": 6,
      "complexity_score": 3,
      "revision_count": 3
    }
    ```
  - Response:
    ```json
    {
      "success": true,
      "predicted_cost": 150000,
      "currency": "USD"
    }
    ```

## Available Project Types

- Web Application
- Mobile Application
- AI/ML Solution
- ERP System
- CRM System
- DevOps Automation
- Cloud Migration
- Cybersecurity Implementation
- Data Engineering Pipeline
- Business Intelligence Dashboard
- IoT System
- Blockchain Solution
- E-commerce Platform
- SaaS Product
- Legacy System Modernization

## Available Client Industries

- Finance
- Healthcare
- Retail
- Education
- Startup

## Training the Model

To train or retrain the cost prediction model:

1. Open `backend/model.ipynb` in Jupyter Notebook
2. Run all cells to train the model with the dataset
3. The trained model will be saved as `cost_prediction_model.pkl`

### Generate Synthetic Data

To generate new synthetic training data:

```bash
cd backend
python dataset.py
```

This will create/update the dataset files in the backend directory.

## Technologies Used

### Backend
- **Flask** - Web framework for Python
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **scikit-learn** - Machine learning library
- **XGBoost** - Gradient boosting framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Joblib** - Model serialization
- **Matplotlib & Seaborn** - Data visualization

### Frontend
- **React 19** - UI framework
- **Vite** - Frontend build tool and development server
- **ESLint** - Code quality tool

## Development Workflow

### Backend Development
1. Make changes to `backend/app.py` or other Python files
2. The Flask development server will automatically reload
3. Test endpoints using tools like Postman or curl

### Frontend Development
1. Modify files in `frontend/src/`
2. Vite provides hot module replacement (HMR) for instant updates
3. View changes immediately in the browser

### Linting
```bash
# Lint frontend code
cd frontend
npm run lint
```

## Troubleshooting

### Model not loading
- Ensure `cost_prediction_model.pkl` exists in the backend directory
- If missing, train the model using the Jupyter notebook

### CORS errors
- The backend enables CORS by default
- Verify both backend and frontend are running

### Port already in use
- Backend: Change the port in `app.py` (default: 5000)
- Frontend: Vite will automatically use the next available port

### Module not found errors
- Backend: Ensure virtual environment is activated and dependencies are installed
- Frontend: Delete `node_modules/` and run `npm install` again

## Notes

- The application uses a synthetic dataset for training
- The trained model is saved as a pickle file for quick loading
- The frontend is configured with Vite for optimal development experience
- CORS is enabled on the backend to allow frontend requests from different origins

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please [add support information here]
