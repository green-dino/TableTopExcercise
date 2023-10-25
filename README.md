# Tabletop Tool 

The Tabletop Tool is a Flask-based web application designed for tabletop excercises. It allows users to manage player data, select scenarios, perform in-depth game analysis, and build custom playbooks.

## Features

- User Management: Register, log in, and manage user profiles.
- Scenario Selection: Choose from a list of available tabletop scenarios.
- Game Analysis: Perform analysis based on user inputs and view the results.
- Playbook Building: Generate playbooks tailored to your game analysis.

## Prerequisites

- Python 3.6 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- A modern web browser

## Installation
 
1. Clone the repository:

   ```bash
   git clone git@github.com:green-dino/TableTopExcercise.git
   cd tabletop-tool
   ```

2. Initialize the virtual environment and install dependencies:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Start the Flask application:

   ```bash
   python run.py
   ```

The application will be accessible at `http://localhost:5000` in your web browser.

## Usage

- Visit `http://localhost:5000` to access the Tabletop Tool.
- Register a new user or log in with an existing account.
- Select a tabletop scenario and perform analysis.
- Build custom playbooks based on the analysis results.

## Linting

This project uses Flake8 for linting. To check your code for compliance, run:

```bash
poetry run lint
```

## Configuration

- Database configurations and other application settings can be found in the `config.py` file.
- You can customize the Flask application in `app/` and its subdirectories.

## Contributing

Contributions are welcome! If you'd like to improve this project, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- Poetry: [Poetry Documentation](https://python-poetry.org/)
- Flake8: [Flake8 Documentation](https://flake8.pycqa.org/)
