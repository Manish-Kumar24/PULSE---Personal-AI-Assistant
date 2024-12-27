# 🤖 PULSE - Personal AI Assistant

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

PULSE is a sophisticated AI-powered virtual assistant built with Python that combines natural language processing, speech recognition, and machine learning to provide a seamless interaction experience. It can help you manage your schedule, control system functions, browse the web, and much more.

## ✨ Features

- 🎙️ Voice Recognition & Speech Synthesis
- 🧠 Natural Language Understanding using Deep Learning
- 📅 Schedule Management & Daily Planning
- 🌐 Web Browsing & Social Media Access
- 💻 System Control (Volume, Apps, etc.)
- 🔋 System Monitoring (Battery, CPU)
- 😄 Casual Conversation Capabilities

## 🛠️ Technology Stack

- Python 3.7+
- TensorFlow/Keras for NLP
- Speech Recognition
- pyttsx3 for Text-to-Speech
- PyAutoGUI for System Control
- Various Python libraries (psutil, webbrowser, etc.)

## 📋 Prerequisites

```bash
# Required Python packages
python>=3.7
tensorflow>=2.0
speech_recognition
pyttsx3
pyautogui
psutil
numpy
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Manish-Kumar24/PULSE---Personal-AI-Assistant.git
cd PULSE---Personal-AI-Assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Train the model (optional - pre-trained model included):
```bash
python model_train.py
```

4. Run the assistant:
```bash
python main.py
```

## 💡 Usage

After launching PULSE, you can interact with it using voice commands. Here are some example commands:

- **Schedule Management**: "What's my schedule today?"
- **System Control**: 
  - "Open calculator"
  - "Increase volume"
  - "Check system condition"
- **Web Browsing**:
  - "Open Google"
  - "Open Facebook"
  - "Search YouTube for..."
- **Casual Interaction**:
  - "Tell me a joke"
  - "How are you?"
  - "What's the time?"

## 📁 Project Structure

```
PULSE---Personal-AI-Assistant/
├── main.py           # Main application file
├── model_train.py    # Model training script
├── intents.json      # Training data and responses
├── chat_model.h5     # Trained model
├── tokenizer.pkl     # Tokenizer for text processing
├── label_encoder.pkl # Label encoder for intents
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape PULSE
- Special thanks to the open-source community for the amazing libraries used in this project
- Inspired by various virtual assistant projects in the Python community

## 📞 Contact

Manish Kumar - [manishkumar202209@gmail.com]

Project Link: [https://github.com/Manish-Kumar24/PULSE---Personal-AI-Assistant](https://github.com/Manish-Kumar24/PULSE---Personal-AI-Assistant)