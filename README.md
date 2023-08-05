# FinanceChatbot with GPT-3 using ADA-002 Embeddings

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Collection](#data-collection)
- [Prompt Engineering](#prompt-engineering)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to FinanceChatbot, an AI-powered chatbot built using OpenAI's GPT-3 model with ADA-002 embeddings. The chatbot is designed to provide insightful financial advice and answers to user queries based on the wisdom from the interviews of renowned investors Warren Buffet and Charlie Munger, extracted from YouTube audio files.

## Features

- Natural Language Understanding: FinanceChatbot is trained on GPT-3, which enables it to understand natural language inputs and generate human-like responses.

- ADA-002 Embeddings: The chatbot leverages the powerful ADA-002 embeddings, enhancing the quality of responses and financial insights.

- Financial Wisdom: The chatbot is trained on transcriptions of interviews with Warren Buffet and Charlie Munger, ensuring that it offers advice based on their extensive experience and knowledge.

## Technologies Used

The FinanceChatbot utilizes the following technologies:

- [OpenAI GPT-3](https://openai.com): The chatbot's underlying model, GPT-3, powers the AI's language understanding and response generation.

- ADA-002 Embeddings: By utilizing ADA-002, the chatbot provides more contextually accurate and coherent responses.

- [YouTube-DL](https://github.com/ytdl-org/youtube-dl): The tool used to download audio files from YouTube interviews of Warren Buffet and Charlie Munger.

## Data Collection

The data for training the chatbot was sourced from interviews of Warren Buffet and Charlie Munger available on YouTube. We used YouTube-DL to download the audio files and then transcribed them to create the training dataset.

## Prompt Engineering

To optimize the chatbot's responses and make them more relevant to finance-related queries, we performed prompt engineering. By designing appropriate prompts, we ensured that the chatbot generates meaningful and contextually accurate answers.

## Installation

To run the FinanceChatbot locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/finance-chatbot.git
cd finance-chatbot
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Obtain API keys for GPT-3 and ADA-002 embeddings. Add them to the configuration files.

4. Run the chatbot:

```python
python app.py
```

## Usage

Once the chatbot is running, you can interact with it by entering your financial queries or seeking investment advice. The chatbot will provide insightful responses based on its training data.

## Contributing

We welcome contributions to enhance the chatbot's knowledge base, improve responses, and expand its financial expertise. Please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md) if you wish to contribute.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using FinanceChatbot. We hope it provides valuable financial insights and guidance. For any questions or feedback, feel free to contact us. Happy investing!
