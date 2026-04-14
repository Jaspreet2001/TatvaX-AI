# <ins>TatvaX AI [PROTOTYPE] - ReadMe</ins>
TatvaX is a groundbreaking educational AI platform that democratises learning by breaking language barriers. Built with cutting-edge AI technology, TatvaX delivers personalized educational content across 8 Indian languages (Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, and English), making quality education accessible to millions.

<div align="center">

![TatvaX Banner](https://img.shields.io/badge/TatvaX-Prototype%20v1.0-blue?style=for-the-badge&logo=python)
![Languages](https://img.shields.io/badge/Languages-8%20Supported-green?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype-yellow?style=for-the-badge)

**Breaking language barriers in education with AI**

[🚀 Features](#-features) • [📥 Installation](#-installation) • [🎯 Usage](#-usage) • [🔧 Tech Stack](#-tech-stack) • [🤝 Contributing](#-contributing)

</div>

---

## 🎥 **Watch TatvaX in Action**

[![Video Title](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://youtu.be/hqo_TAZh0ls)

---

## ⚠️ **IMPORTANT NOTICE - PROTOTYPE VERSION**

> **This repository contains a PROTOTYPE implementation of TatvaX.**
> 
> This is a **proof-of-concept** demonstrating the core functionality and vision of the TatvaX platform. The final product will include enhanced features, scalability improvements, production-grade security, cloud infrastructure, and significantly expanded educational content.
>
> **This prototype serves as:**
> - 🎯 Demonstration of core concept and functionality
> - 🧪 Testing ground for multilingual AI education
> - 📊 Foundation for gathering feedback and insights
> - 🚀 Starting point for the full-scale production version

---


---

## 🎓 **About TatvaX**

**TatvaX** is a revolutionary AI-powered educational platform that breaks language barriers to make quality education accessible to everyone. Built with a vision to democratize learning, TatvaX delivers personalized educational content in **8 Indian languages**, ensuring that language is never a barrier to knowledge.

### **Our Vision** 🌍

To create an inclusive learning ecosystem where every student can access quality education in their native language, powered by advanced AI technology.

### **Our Mission** 🎯

- Make quality education accessible to all linguistic communities
- Leverage AI to provide personalized, context-aware learning experiences
- Bridge the digital divide with voice-first learning capabilities
- Empower students to learn in the language they're most comfortable with

---

## ✨ **Features**

### 🎓 **Dual Learning Modes**

#### **1. Subject Learning Mode**
Interactive learning across 4 core subjects with AI-powered responses:
- 📐 **Mathematics**: Concepts, problem-solving, formulas
- 🔬 **Science**: Physics, Chemistry, Biology explanations
- 📚 **English**: Grammar, literature, writing skills
- 🌍 **Social Studies**: History, geography, civics

#### **2. Institutional FAQ Mode**
Comprehensive school information system covering:
- 🏫 Admission procedures and requirements
- 💰 Fee structure and payment information
- 📅 Academic calendar and exam schedules
- 📋 School policies and guidelines
- 🎓 Scholarship and financial aid information

### 🌐 **Multilingual AI Engine**

**8 Supported Languages:**
- 🇮🇳 **Hindi** (हिंदी)
- 🇮🇳 **Bengali** (বাংলা)
- 🇮🇳 **Marathi** (मराठी)
- 🇮🇳 **Telugu** (తెలుగు)
- 🇮🇳 **Tamil** (தமிழ்)
- 🇮🇳 **Gujarati** (ગુજરાતી)
- 🇮🇳 **Kannada** (ಕನ್ನಡ)
- 🇺🇸 **English**

**Smart Translation System:**
- Multiple translation API fallback (Google Free, MyMemory, LibreTranslate)
- Auto-detection of input language
- Context-aware translations
- Real-time processing

### 🎙️ **Voice-First Learning**

- **Voice Input**: Speak your questions in any supported language
- **Voice Output**: Listen to responses with text-to-speech
- **Hands-Free Learning**: Perfect for accessibility
- **Natural Language Processing**: Understands conversational queries

### 🎨 **Modern User Experience**

- **Beautiful Interface**: Clean, modern design with smooth animations
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Code Block Display**: Formatted output with copy functionality
- **Intuitive Navigation**: Easy-to-use for all age groups
- **Dark Mode Ready**: Easy on the eyes

### 🔧 **Advanced Technical Features**

- **Content Management System**: Extensive educational content library
- **AI Response Generation**: Context-aware, intelligent responses
- **Audio Processing**: High-quality TTS and speech recognition
- **Fallback Systems**: Multiple API fallback for reliability
- **Feedback System**: Built-in user feedback collection
- **Translation Mode**: Quick translate between any languages

---

## 🚀 **Why TatvaX is Revolutionary**

### **1. True Linguistic Inclusion** 🌍
Unlike platforms that simply translate content, TatvaX understands cultural context and learning patterns specific to each language, making education truly accessible.

### **2. Voice-First Approach** 🎙️
TatvaX enables hands-free learning through comprehensive voice input/output, making education accessible for students with diverse learning styles and abilities.

### **3. Dual-Mode Intelligence** 🧠
Seamlessly switches between subject learning and institutional FAQs, providing a complete educational ecosystem in one platform.

### **4. Robust Architecture** 🏗️
Multi-API fallback system ensures the platform works even when primary services are down, guaranteeing consistent access to education.

### **5. AI-Powered Personalisation** 🤖
Advanced NLP algorithms provide context-aware responses tailored to each student's language and learning level.

### **6. Accessibility First** ♿
Voice input/output, clean interface, and multilingual support make TatvaX accessible to students with various needs and backgrounds.

---

## 📥 **Installation**

### **Prerequisites**

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for translation APIs)
- Microphone (optional, for voice input)
- Speakers/Headphones (optional, for audio output)

### **Quick Start** ⚡

1. **Clone the Repository**
```
git clone https://github.com/your-username/tatvax-ai-prototype.git
cd tatvax-ai-prototype
```

2. **Create Virtual Environment**

#### Windows
```
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Download NLTK Data**
```
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

5. **Run TatvaX**
```
python app.py
```

6. **Access the Platform**
```
Open browser → http://localhost:5000
```

That's it! TatvaX is now running locally. 🎉

---

## 🎯 **Usage**

### **Getting Started** 🚦

#### **Step 1: Choose Your Mode**
After launching TatvaX, you'll see two learning modes:

- **📚 Subject Learning**: Get AI-powered help with Mathematics, Science, English, and Social Studies
- **🏫 Institutional Assistant**: Ask questions about school policies, fees, schedules, and more

#### **Step 2: Select Your Language**
Choose from 8 supported languages in the dropdown menu. The entire interface adapts to your selection.

#### **Step 3: Start Learning**
- **Type** your question in the text box, OR
- **Click the microphone** 🎙️ and speak your question
- Get instant AI-powered responses in your chosen language
- **Click audio button** 🔊 to hear the response

### **Example Queries** 💬

#### **Mathematics** 📐
```

"Explain Pythagoras theorem"
"How to solve quadratic equations?"
"What is the formula for area of circle?"
"Teach me trigonometry basics"

```

#### **Science** 🔬
```

"Explain photosynthesis process"
"What are Newton's laws of motion?"
"How does the digestive system work?"
"Tell me about solar system"

```

#### **English** 📖
```

"What are parts of speech?"
"How to write a good essay?"
"Explain active and passive voice"
"Give me grammar tips"

```

#### **Social Studies** 🌍
```

"Tell me about Indian independence"
"What is democracy?"
"Explain fundamental rights"
"History of Mughal empire"

```

#### **Institutional FAQs** 🏫
```

"What are admission requirements?"
"When are exam dates?"
"How much is school fee?"
"What is school timing?"
"How to apply for scholarship?"

```


---

## 🔧 **Tech Stack**

### **Frontend** 💻
| Technology | Purpose |
|------------|---------|
| **HTML5** | Semantic structure |
| **CSS3** | Modern styling with animations |
| **JavaScript ES6+** | Interactive functionality |
| **Responsive Design** | Mobile-first approach |

### **Backend** ⚙️
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Core language |
| **Flask** | 2.3+ | Web framework |
| **NLTK** | 3.8+ | NLP processing |
| **Sumy** | 0.11+ | Text summarization |

### **AI & Translation** 🤖
- **Google Translate API** (Primary)
- **MyMemory API** (Fallback)
- **LibreTranslate** (Secondary fallback)
- **Custom NLP Engine** (Context awareness)

### **Audio Processing** 🎙️
- **gTTS**: Text-to-speech generation
- **SpeechRecognition**: Voice input
- **pygame**: Audio playback
- **PyAudio**: Audio capture

### **Key Dependencies** 📦
```
Flask==2.3.0
nltk==3.8.1
sumy==0.11.0
gtts==2.3.2
pygame==2.5.2
SpeechRecognition==3.10.0
PyAudio==0.2.13
requests==2.31.0
```

---

## 🏗️ **Architecture**

### **System Overview**

```
┌────────────────────────────────────────────────┐
│         User Interface (HTML/CSS/JS)           │
│   -  Responsive Design  -  Voice Controls      │
│   -  8 Language Support -  Real-time Updates   │
└───────────────────────┬────────────────────────┘
                        │
┌───────────────────────▼────────────────────────┐
│           Flask Application Layer              │
│   -  Routing               -  API Endpoints    │
│   -  Session Management                        │
└───────────────────────┬────────────────────────┘
                        │
           ┌────────────┼────────────┐
           |            │            │
     ┌─────▼─────┐ ┌────▼────┐ ┌─────▼─────┐
     │Translation│ │Content  │ │  Chatbot  │
     │  Service  │ │ Manager │ │  Helpers  │
     │ Multi-API │ │ Library │ │  AI/NLP   │
     └───────────┘ └─────────┘ └───────────┘
           │            │            │
           └────────────┼────────────┘
                        │
┌───────────────────────▼─────────────────────────┐
│        External Services \& Resources           │
│   -  Translation APIs    -  Audio Processing    │
│   -  Content Database    -  Temporary Storage   │
└─────────────────────────────────────────────────┘
```

### **Request Flow**

```

User Input
    ↓
Language Detection
    ↓
Translation (if needed)
    ↓
Content Retrieval
    ↓
AI Processing
    ↓
Response Generation
    ↓
Translation to Target Language
    ↓
Audio Generation (optional)
    ↓
Response Delivery to Frontend

```

### **Key Components**

#### **1. Translation Service** 🌍
- Multi-API architecture with automatic fallback
- Supports 8 languages with high accuracy
- Caching for improved performance

#### **2. Content Manager** 📚
- Organized subject-wise content library
- Keyword-based content retrieval
- Institutional FAQ database

#### **3. Chatbot Helpers** 🤖
- NLP-powered query understanding
- Context-aware response generation
- Multi-language support

#### **4. Audio Processor** 🎙️
- Real-time speech recognition
- High-quality text-to-speech
- Temporary file management

---


