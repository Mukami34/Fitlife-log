# Fitlife-log

FitLife Log is a command-line fitness tracking application that allows users to record and monitor their workouts, exercises, and fitness statistics.

## Installation and Setup

1. Clone the repository:
       ```bash
   git clone <https://github.com/Mukami34/Fitlife-log.git>

   Navigate to the project directory:
   cd fitlife-log

   Create a virtual environment and install dependencies:
   pipenv install

    Activate the virtual environment:
    pipenv shell

    Run the CLI application:
    python fitlife_log.py


## Usage

FitLife Log provides the following commands:

- `init_db`: Initialize the database.
- `run_migrations`: Apply database migrations.
- `add_user`: Add a new user profile.
- ...

Example usage:
    ```bash 
# Initialize the database

fitlife_log.py init_db

# Add a new user

fitlife_log.py add_user --username johndoe --email <john@example.com>

## Database Schema

FitLife Log uses the following database schema:

- `users`: Stores user profiles with information like username, email, and registration date.
- `workouts`: Records workout sessions with user references and date.
- `exercises`: Contains exercise details, such as name, description, sets, reps, and weight, associated with workouts.

## Fitness Statistics

FitLife Log offers the following fitness statistics:

- `calculate_bmi`: Calculate Body Mass Index (BMI).
- `calculate_bmr`: Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation.
- `calculate_tdee`: Calculate Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

## Contact

For questions or support, you can reach out to [Mary Mukami]
(<https://github.com/Mukami34>)
