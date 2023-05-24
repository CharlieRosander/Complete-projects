# Flask Weather and Chat Application README

## Introduction

This is a web application built using the Flask web framework. It features a weather service that utilizes the OpenWeatherMap API to fetch current weather details for a specific city. In addition to this, the application also uses OpenAI's GPT-4 to create a chatbot interface. The application is built with user authentication and provides the ability to sign up, log in, and interact with the chatbot interface and weather service.

## Setup and Installation

This application requires Python 3 and the following libraries:

- Flask
- Flask-SQLAlchemy
- openai
- requests
- python-dotenv
- Werkzeug

You can install these using pip:

```bash
pip install Flask Flask-SQLAlchemy openai requests python-dotenv Werkzeug
```

## Usage

To use this application, start by cloning this repository and navigating to the application directory.

Create a `.env` file in the root directory of the application. This file will contain your OpenAI and OpenWeatherMap API keys:

```bash
OPENAI_API_KEY=<your-openai-api-key>
OPENWEATHERMAP_API_KEY=<your-openweathermap-api-key>
```

Next, set up the database by running the application with Python:

```bash
python app.py
```

The SQLite database will be automatically created in the root directory of the application (`database.db`).

Access the application by navigating to `http://localhost:5000` in your web browser.

### Features

1. **User Authentication**: Users can sign up and log in. This functionality is handled using Flask's session feature and password hashing is done using Werkzeug.

2. **Weather Service**: On the home page, users can search for a city to get its current weather details, including temperature, weather description, and a related weather icon.

3. **Chatbot**: The chatbot page contains an interactive chat interface that utilizes OpenAI's GPT-4 to generate responses to user messages.

## Contributing

Please feel free to fork this repository and submit pull requests for any improvements or features you'd like to add.

## License

This project is open-source and available under the MIT License.
