![images](https://github.com/VIS172/CODSOFT/assets/109724129/40d79b99-f7bd-4924-9232-52bbf011f79c)


# Rule-Based Chatbot Project

This repository contains the code for a Rule-Based Chatbot implemented in Python. Rule-based chatbots respond to user inputs based on predefined patterns and rules, making them ideal for applications such as FAQs or basic customer service interactions.

## Features

- Predefined rules and patterns for responses
- Pattern matching using regular expressions
- Easy customization of rules and responses
- Support for basic conversation flow

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed via `requirements.txt`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/rule-based-chatbot.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd rule-based-chatbot
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script**:
    ```bash
    python chatbot.py
    ```

## Code Overview

### 1. Rule Definition

- **Patterns and Responses**: Define patterns using regular expressions and map them to appropriate responses.
- **Customization**: Easily add or modify rules in the `rules.json` file.

### 2. Pattern Matching

- **Regular Expressions**: Utilize regular expressions to match user inputs with predefined patterns.
- **Response Selection**: Select and return the corresponding response based on the matched pattern.

### 3. Chatbot Interaction

- **User Input Handling**: Continuously accept user inputs and process them using the defined rules.
- **Response Generation**: Generate and return appropriate responses based on the matched patterns.

## Usage

### Define Rules and Patterns
![Untitled-53](https://github.com/VIS172/CODSOFT/assets/109724129/bd11da27-e68d-4cfd-984e-66ac34fd1d1d)

Rules and patterns are defined in the `rules.json` file. Each rule consists of a pattern and a corresponding response:
```json
{
    "patterns": [
        {"pattern": "hello|hi|hey", "response": "Hello! How can I help you today?"},
        {"pattern": "bye|exit|quit", "response": "Goodbye! Have a nice day!"}
    ]
}

