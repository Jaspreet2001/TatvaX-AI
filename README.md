# <ins>TatvaX AI [PROTOTYPE] - ReadMe</ins>
TatvaX is a groundbreaking educational AI platform that democratises learning by breaking language barriers. Built with cutting-edge AI technology, TatvaX delivers personalized educational content across 8 Indian languages (Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, and English), making quality education accessible to millions.


---


---

## 🎓 **About TatvaX**

**TatvaX** is a revolutionary AI-powered educational platform that breaks language barriers to make quality education accessible to everyone. Built with a vision to democratize learning, TatvaX delivers personalized educational content in **8 Indian languages**, ensuring that language is never a barrier to knowledge.

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


