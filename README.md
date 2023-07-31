# PROMPT-INV

## Description

The PromptGPT Client Service is a multilingual web application that allows users to interact with OpenAI's GPT-3 language model through a user-friendly interface. The application is designed to automatically detect the user's language and generate responses in the detected language.

Key Features:
- Seamless Interaction: Users can input prompts in their preferred language, and the system will automatically detect the language to generate appropriate responses.
- Multilingual Support: The application supports multiple languages, providing a truly global experience for users.
- Human-like Responses: Utilizing the power of GPT-3, the generated responses are natural and human-like, creating a realistic conversation experience.

The project is developed with Python 3.10 for the backend, and the frontend utilizes HTML, CSS, and JavaScript to create an intuitive and responsive user interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/darkropo/prompt-inv.git

2. Navigate to the project directory:

   ```bash
   cd prompt-inv

3. Create a virtual environment (venv) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate

4. Install Pipenv if you don't have it:

   ```bash
   pip install pipenv

5. Install the required dependencies from the Pipfile:

   ```bash
   pipenv install

## Usage

1. Start the Flask development server by running the bootstrap.sh script:

   ```bash
   ./bootstrap.sh

The application will be accessible at http://localhost:5000.

2. Open your web browser and visit the above URL to access the application.

3. Use the application as per its functionality.

## Contributing

If you want to contribute to this project and make it better, follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message here"

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name

5. Create a pull request with a detailed description of your changes.

## License

[Apache License 2.0]
