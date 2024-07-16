# AI Diagnosis App

This project is an AI-powered diagnosis application built using the Django framework. It includes a Jupyter Notebook (`.ipynb` file) for training the model, and the trained model is stored in the `models` folder.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Overview

The AI Diagnosis App leverages machine learning to provide diagnostic insights. The application is developed using Django, with the model training process documented in a Jupyter Notebook. The trained model is saved in the `models` directory and is utilized by the Django application to perform predictions.

## Features

- **Django-based Web Application**: A robust web framework for developing the application.
- **Machine Learning Model**: Includes a Jupyter Notebook for training the AI model.
- **Model Storage**: Trained models are stored in the `models` folder for easy access and deployment.
- **User-friendly Interface**: Simple and intuitive UI for users to interact with the diagnosis tool.

## Installation

To install and run this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ai-diagnosis-app.git
    cd ai-diagnosis-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the Application**:
    Open your web browser and navigate to `http://127.0.0.1:8000`.

2. **Model Training**:
    Open the Jupyter Notebook (`.ipynb` file)  along with the datasets in the `datasets` folder and follow the instructions to train the model. Save the trained model to the `models` folder.
   The model is trained and the trained model is stored in the models folder as a .pkl file

4. **Diagnostics**:
    Use the web interface to input data and receive diagnostic predictions based on the trained model.


- `codeinjectors/`: Django project directory containing settings and configurations.
- `models/`: Directory for storing the trained models.
- `datasets/`: Contains the Jupyter Notebook for model training and corresponding datasets.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JavaScript, images, etc.).
- `manage.py`: Django management script.
- `requirements.txt`: List of dependencies.

## Model Training

1. Open the Jupyter Notebook (`notebooks/model_training.ipynb`).
2. Follow the instructions to load data, preprocess it, train the model, and evaluate its performance.
3. Save the trained model to the `models` directory.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


