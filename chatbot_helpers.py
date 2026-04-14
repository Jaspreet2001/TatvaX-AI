import os
import re
import threading
import time
from datetime import datetime
from typing import Optional, Tuple

# Audio processing imports
try:
    import pygame
    import speech_recognition as sr
    from gtts import gTTS

    AUDIO_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Audio libraries not available: {e}")
    AUDIO_AVAILABLE = False

# NLP imports
try:
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lex_rank import LexRankSummarizer

    NLP_AVAILABLE = True

    # Download required NLTK data
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt", quiet=True)

    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords", quiet=True)

except ImportError as e:
    print(f"⚠️ NLP libraries not available: {e}")
    NLP_AVAILABLE = False


class EnhancedChatbotHelpers:
    """Enhanced chatbot with multilingual support and advanced features"""

    def __init__(self, translation_service=None, content_manager=None):
        print("🤖 Initializing Enhanced Chatbot Helpers...")

        self.translation_service = translation_service
        self.content_manager = content_manager

        # Default audio variables
        self.recognizer = None
        self.microphone = None

        # Audio system
        self.audio_playing = False
        self.current_audio_thread = None
        self.temp_audio_dir = "temp_audio"
        os.makedirs(self.temp_audio_dir, exist_ok=True)

        # Initialize pygame for audio
        try:
            import pygame
            pygame.mixer.init()
            print("✅ Audio system initialized")
        except Exception as e:
            print(f"⚠️ Audio system not available: {e}")

        # Speech recognition (SAFE VERSION)
        try:
            import speech_recognition as sr

            try:
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()

                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                print("✅ Speech recognition initialized")

            except Exception as e:
                print(f"⚠️ Audio initialization failed: {e}")
                self.recognizer = None
                self.microphone = None

        except ImportError:
            print("⚠️ speech_recognition not installed, audio disabled")
            self.recognizer = None
            self.microphone = None

        # Enhanced keywords for different subjects and institutional queries
        self.subject_keywords = {
            "mathematics": [
                "math",
                "mathematics",
                "number",
                "calculate",
                "equation",
                "algebra",
                "geometry",
                "fraction",
                "decimal",
                "percentage",
                "addition",
                "subtraction",
                "multiplication",
                "division",
                "problem",
                "solve",
                "formula",
                "graph",
                "triangle",
                "circle",
                "area",
                "volume",
                "angle",
                "coordinate",
                "गणित",
                "संख्या",
                "गुणा",
                "भाग",
                "जोड़",
                "घटाव",
                "समीकरण",
            ],
            "science": [
                "science",
                "physics",
                "chemistry",
                "biology",
                "experiment",
                "lab",
                "atom",
                "molecule",
                "energy",
                "force",
                "motion",
                "gravity",
                "light",
                "sound",
                "heat",
                "electricity",
                "plant",
                "animal",
                "cell",
                "DNA",
                "ecosystem",
                "environment",
                "climate",
                "weather",
                "earth",
                "space",
                "विज्ञान",
                "भौतिकी",
                "रसायन",
                "जीव",
                "प्रयोग",
                "ऊर्जा",
                "बल",
            ],
            "english": [
                "english",
                "grammar",
                "sentence",
                "noun",
                "verb",
                "adjective",
                "essay",
                "story",
                "poem",
                "reading",
                "writing",
                "spelling",
                "vocabulary",
                "literature",
                "comprehension",
                "paragraph",
                "punctuation",
                "tense",
                "subject",
                "predicate",
                "clause",
                "phrase",
                "metaphor",
                "simile",
                "अंग्रेजी",
                "व्याकरण",
                "वाक्य",
                "कहानी",
                "कविता",
                "लेखन",
                "पढ़ना",
            ],
            "social_studies": [
                "history",
                "geography",
                "civics",
                "politics",
                "government",
                "constitution",
                "rights",
                "duties",
                "democracy",
                "culture",
                "tradition",
                "heritage",
                "civilization",
                "ancient",
                "medieval",
                "modern",
                "independence",
                "freedom",
                "country",
                "state",
                "city",
                "village",
                "population",
                "इतिहास",
                "भूगोल",
                "नागरिकशास्त्र",
                "सरकार",
                "संविधान",
                "अधिकार",
            ],
        }

        self.institutional_keywords = [
            "admission",
            "fee",
            "exam",
            "schedule",
            "timetable",
            "syllabus",
            "holiday",
            "vacation",
            "result",
            "grade",
            "marks",
            "scholarship",
            "library",
            "book",
            "uniform",
            "bus",
            "transport",
            "canteen",
            "principal",
            "teacher",
            "staff",
            "contact",
            "phone",
            "email",
            "policy",
            "rule",
            "regulation",
            "procedure",
            "application",
            "प्रवेश",
            "फीस",
            "परीक्षा",
            "समय-सारणी",
            "पाठ्यक्रम",
            "छुट्टी",
            "परिणाम",
            "अंक",
            "छात्रवृत्ति",
            "पुस्तकालय",
            "पुस्तक",
            "वर्दी",
        ]

        # Response templates for different languages
        self.response_templates = {
            "en": {
                "greeting": "Hello! How can I help you today?",
                "clarification": "Could you please provide more details about your question?",
                "not_found": "I don't have specific information about that topic. Could you try rephrasing your question?",
                "error": "I'm sorry, I encountered an error while processing your request.",
            },
            "hi": {
                "greeting": "नमस्ते! आज मैं आपकी कैसे मदद कर सकता हूँ?",
                "clarification": "कृपया अपने प्रश्न के बारे में और विस्तार से बताएं?",
                "not_found": "मेरे पास इस विषय की विशिष्ट जानकारी नहीं है। कृपया अपना प्रश्न दूसरे तरीके से पूछने की कोशिश करें?",
                "error": "मुझे खुशी है, आपके अनुरोध को संसाधित करते समय मुझे एक त्रुटि आई।",
            },
        }

        print("✅ Enhanced Chatbot Helpers initialized")

    def identify_intent_and_subject(self, query: str) -> Tuple[str, str]:
        """Identify user intent and subject from query"""
        query_lower = query.lower()

        # Check for institutional keywords first
        institutional_score = sum(
            1 for keyword in self.institutional_keywords if keyword in query_lower
        )

        # Check for subject keywords
        subject_scores = {}
        for subject, keywords in self.subject_keywords.items():
            score = sum(1 for keyword in keywords if keyword in query_lower)
            subject_scores[subject] = score

        # Determine intent
        if institutional_score > 0:
            return "institutional", "general"

        # Find best matching subject
        best_subject = max(subject_scores, key=subject_scores.get)
        if subject_scores[best_subject] > 0:
            return "subject", best_subject

        # Default to general subject learning
        return "subject", "general"

    def handle_subject_query(self, query: str, subject: str = "general") -> str:
        """Handle subject-based learning queries"""
        try:
            print(f"📚 Processing subject query for {subject}: {query}")

            # If no specific subject provided, try to identify from query
            if subject == "general":
                _, detected_subject = self.identify_intent_and_subject(query)
                if detected_subject != "general":
                    subject = detected_subject

            # Load subject content
            if subject != "general" and self.content_manager:
                content = self.content_manager.load_subject_content(subject)
                relevant_content = self.content_manager.find_relevant_content(
                    query, content, 5
                )
            else:
                # General educational response
                relevant_content = self.generate_general_educational_response(query)

            # Process and format response
            response = self.process_educational_content(
                query, relevant_content, subject
            )

            # Make child-friendly
            response = self.make_child_friendly(response)

            print(f"✅ Generated subject response: {len(response)} characters")
            return response

        except Exception as e:
            print(f"❌ Error handling subject query: {e}")
            return "I'm sorry, I couldn't process your question right now. Please try asking in a different way."

    def handle_institutional_query(self, query: str) -> str:
        """Handle institutional FAQ queries"""
        try:
            print(f"🏫 Processing institutional query: {query}")

            # Load institutional content
            if self.content_manager:
                content = self.content_manager.load_institutional_content()
                relevant_content = self.content_manager.find_relevant_content(
                    query, content, 7
                )
            else:
                relevant_content = self.generate_general_institutional_response(query)

            # Process and format response
            response = self.process_institutional_content(query, relevant_content)

            # Make informative and helpful
            response = self.make_informative(response)

            print(f"✅ Generated institutional response: {len(response)} characters")
            return response

        except Exception as e:
            print(f"❌ Error handling institutional query: {e}")
            return "I'm sorry, I couldn't find information about that right now. Please contact the school office for specific details."

    def process_educational_content(
        self, query: str, content: str, subject: str
    ) -> str:
        """Process educational content into structured response"""
        try:
            if not content:
                return f"I don't have specific information about that {subject} topic. Could you try asking about a different concept?"

            # Use NLP summarization if available
            if NLP_AVAILABLE and len(content) > 500:
                try:
                    parser = PlaintextParser.from_string(content, Tokenizer("english"))
                    summarizer = LexRankSummarizer()
                    summary = summarizer(
                        parser.document, 3
                    )  # Get 3 most relevant sentences
                    content = " ".join([str(sentence) for sentence in summary])
                except Exception as e:
                    print(f"⚠️ Summarization failed, using original content: {e}")

            # Structure the response
            response = f"Here's what I can tell you about your {subject} question:\n\n"

            # Add main content
            response += content

            # Add helpful closing
            response += (
                f"\n\nWould you like me to explain any specific part in more detail?"
            )

            return response

        except Exception as e:
            print(f"❌ Error processing educational content: {e}")
            return content

    def process_institutional_content(self, query: str, content: str) -> str:
        """Process institutional content into helpful response"""
        try:
            if not content:
                return "I don't have specific information about that. Please contact the school office for detailed information."

            # Structure the response
            response = "Here's the information you requested:\n\n"

            # Add main content
            response += content

            # Add helpful closing
            response += "\n\nIf you need more specific details, please contact the school office or check the official website."

            return response

        except Exception as e:
            print(f"❌ Error processing institutional content: {e}")
            return content

    def make_child_friendly(self, text: str) -> str:
        """Make text more child-friendly and engaging"""
        try:
            # Simple sentence starters for engagement
            friendly_starters = [
                "Great question! ",
                "That's interesting! ",
                "Let me explain that! ",
                "Here's something cool! ",
            ]

            # Add encouraging words
            text = text.replace("You should", "You can")
            text = text.replace("You must", "It's good to")
            text = text.replace("difficult", "challenging but fun")
            text = text.replace("hard", "needs practice")
            text = text.replace("complex", "interesting")

            # Add emojis sparingly for engagement
            if "mathematics" in text.lower() or "math" in text.lower():
                text = "🔢 " + text
            elif "science" in text.lower():
                text = "🔬 " + text
            elif "english" in text.lower():
                text = "📚 " + text
            elif "history" in text.lower() or "geography" in text.lower():
                text = "🌍 " + text

            return text

        except Exception as e:
            print(f"❌ Error making child-friendly: {e}")
            return text

    def make_informative(self, text: str) -> str:
        """Make institutional information clear and organized"""
        try:
            # Organize with bullet points if multiple pieces of info
            sentences = text.split(". ")
            if len(sentences) > 3:
                # Convert to bullet points for better readability
                organized_text = sentences[0] + ".\n\n"
                for sentence in sentences[1:]:
                    if sentence.strip():
                        organized_text += f"• {sentence.strip()}\n"
                text = organized_text

            # Add helpful formatting
            text = text.replace("Important:", "\n📌 Important:")
            text = text.replace("Note:", "\n💡 Note:")
            text = text.replace("Contact:", "\n📞 Contact:")

            return text

        except Exception as e:
            print(f"❌ Error making informative: {e}")
            return text

    def generate_general_educational_response(self, query: str) -> str:
        """Generate general educational response when specific content is not available"""
        query_lower = query.lower()

        if any(word in query_lower for word in ["what", "how", "why", "when", "where"]):
            return (
                "That's a great question! While I don't have specific information about that topic right now, "
                "I encourage you to explore this further. You could ask your teacher, check your textbook, "
                "or research this topic online with a parent or guardian."
            )

        return (
            "I understand you're curious about this topic. Keep asking questions - that's how we learn! "
            "Try asking your teacher or looking in your study materials for more detailed information."
        )

    def generate_general_institutional_response(self, query: str) -> str:
        """Generate general institutional response when specific content is not available"""
        return (
            "For specific information about school policies, procedures, or schedules, "
            "I recommend contacting the school office directly. They will be able to provide "
            "you with the most accurate and up-to-date information."
        )

    # Speech and Audio Functions
    def speech_to_text(
        self, timeout: int = 5, phrase_timeout: int = 2
    ) -> Tuple[str, str]:
        """Convert speech to text with language detection"""
        if not AUDIO_AVAILABLE:
            raise Exception("Speech recognition not available")

        try:
            print("🎤 Listening for speech...")

            with self.microphone as source:
                # Listen for audio
                audio = self.recognizer.listen(
                    source, timeout=timeout, phrase_time_limit=phrase_timeout
                )

            print("🔄 Processing speech...")

            # Try to recognize speech in different languages
            languages_to_try = ["en", "hi", "bn", "mr", "te", "ta", "gu", "kn"]

            for lang in languages_to_try:
                try:
                    # Convert language code to format expected by speech_recognition
                    recognition_lang = self.get_recognition_language_code(lang)
                    text = self.recognizer.recognize_google(
                        audio, language=recognition_lang
                    )

                    if text:
                        print(f"✅ Speech recognized in {lang}: {text}")
                        return text, lang

                except sr.UnknownValueError:
                    continue
                except sr.RequestError:
                    continue

            # If no language worked, try default English
            try:
                text = self.recognizer.recognize_google(audio, language="en-US")
                return text, "en"
            except:
                raise Exception("Could not understand the audio")

        except sr.WaitTimeoutError:
            raise Exception("No speech detected within timeout period")
        except Exception as e:
            raise Exception(f"Speech recognition failed: {str(e)}")

    def get_recognition_language_code(self, lang_code: str) -> str:
        """Convert language code to speech recognition format"""
        mapping = {
            "en": "en-US",
            "hi": "hi-IN",
            "bn": "bn-IN",
            "mr": "mr-IN",
            "te": "te-IN",
            "ta": "ta-IN",
            "gu": "gu-IN",
            "kn": "kn-IN",
        }
        return mapping.get(lang_code, "en-US")

    def generate_audio(self, text: str, language: str = "en") -> Optional[str]:
        """Generate audio file from text"""
        if not AUDIO_AVAILABLE:
            print("⚠️ Audio generation not available")
            return None

        try:
            print(f"🔊 Generating audio in {language}: {text[:50]}...")

            # Clean text for TTS
            clean_text = self.clean_text_for_tts(text)
            if not clean_text:
                return None

            # Convert language code to TTS format
            tts_lang = self.get_tts_language_code(language)

            # Generate TTS
            tts = gTTS(text=clean_text, lang=tts_lang, slow=False)

            # Save to temporary file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"tts_{language}_{timestamp}.mp3"
            filepath = os.path.join(self.temp_audio_dir, filename)

            tts.save(filepath)

            print(f"✅ Audio generated: {filename}")
            return filename

        except Exception as e:
            print(f"❌ Audio generation failed: {e}")
            return None

    def get_tts_language_code(self, lang_code: str) -> str:
        """Convert language code to TTS format"""
        mapping = {
            "en": "en",
            "hi": "hi",
            "bn": "bn",
            "mr": "mr",
            "te": "te",
            "ta": "ta",
            "gu": "gu",
            "kn": "kn",
        }
        return mapping.get(lang_code, "en")

    def clean_text_for_tts(self, text: str) -> str:
        """Clean text for better TTS output"""
        try:
            # Remove markdown formatting
            clean_text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)  # Remove bold
            clean_text = re.sub(r"\*(.*?)\*", r"\1", clean_text)  # Remove italic
            clean_text = re.sub(r"`(.*?)`", r"\1", clean_text)  # Remove code

            # Remove HTML tags
            clean_text = re.sub(r"<[^>]+>", "", clean_text)

            # Remove excessive whitespace
            clean_text = re.sub(r"\s+", " ", clean_text)

            # Remove emojis and special characters that might cause issues
            clean_text = re.sub(r"[^\w\s.,!?;:\-()]", "", clean_text)

            # Limit length for TTS
            if len(clean_text) > 500:
                sentences = clean_text.split(".")
                clean_text = ". ".join(sentences[:3]) + "."

            return clean_text.strip()

        except Exception as e:
            print(f"❌ Error cleaning text for TTS: {e}")
            return text[:500]  # Fallback to truncated original

    def play_audio_file(self, filepath: str) -> bool:
        """Play audio file using pygame"""
        if not AUDIO_AVAILABLE:
            print("⚠️ Audio playback not available")
            return False

        try:
            if not os.path.exists(filepath):
                print(f"❌ Audio file not found: {filepath}")
                return False

            print(f"🔊 Playing audio: {filepath}")

            # Stop any currently playing audio
            self.stop_audio()

            # Load and play audio
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()

            self.audio_playing = True

            # Start monitoring thread
            self.current_audio_thread = threading.Thread(
                target=self._monitor_audio_playback
            )
            self.current_audio_thread.daemon = True
            self.current_audio_thread.start()

            return True

        except Exception as e:
            print(f"❌ Audio playback failed: {e}")
            self.audio_playing = False
            return False

    def _monitor_audio_playback(self):
        """Monitor audio playback in separate thread"""
        try:
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            self.audio_playing = False
            print("✅ Audio playback completed")

        except Exception as e:
            print(f"❌ Audio monitoring error: {e}")
            self.audio_playing = False

    def stop_audio(self) -> bool:
        """Stop currently playing audio"""
        if not AUDIO_AVAILABLE:
            return False

        try:
            if self.audio_playing:
                pygame.mixer.music.stop()
                self.audio_playing = False
                print("🔇 Audio stopped")

            return True

        except Exception as e:
            print(f"❌ Error stopping audio: {e}")
            return False

    def is_audio_playing(self) -> bool:
        """Check if audio is currently playing"""
        return self.audio_playing

    def cleanup_temp_audio_files(self, max_age_hours: int = 2):
        """Clean up old temporary audio files"""
        try:
            if not os.path.exists(self.temp_audio_dir):
                return

            current_time = time.time()
            max_age_seconds = max_age_hours * 3600

            cleaned_count = 0
            for filename in os.listdir(self.temp_audio_dir):
                filepath = os.path.join(self.temp_audio_dir, filename)

                try:
                    if os.path.isfile(filepath):
                        file_age = current_time - os.path.getctime(filepath)
                        if file_age > max_age_seconds:
                            os.remove(filepath)
                            cleaned_count += 1
                except Exception as e:
                    print(f"⚠️ Error removing file {filename}: {e}")

            if cleaned_count > 0:
                print(f"🧹 Cleaned up {cleaned_count} old audio files")

        except Exception as e:
            print(f"❌ Audio cleanup error: {e}")

    def get_response_template(self, template_key: str, language: str = "en") -> str:
        """Get response template in specified language"""
        templates = self.response_templates.get(language, self.response_templates["en"])
        return templates.get(template_key, templates["error"])

    def __del__(self):
        """Cleanup when object is destroyed"""
        try:
            self.stop_audio()
            # Clean up all temp files on exit
            self.cleanup_temp_audio_files(max_age_hours=0)
        except:
            pass
