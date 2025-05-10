import speech_recognition as sr
def user_audio() :
    init_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
            print("Say something (you have 5 seconds to start)...")
            init_recognizer.adjust_for_ambient_noise(source,duration=1)
            audio = init_recognizer.listen(source, timeout=5)
            try:
                text = init_recognizer.recognize_google(audio, language="vi-VN")
                return text
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except KeyboardInterrupt:
                print("\nListening interrupted by user.")

    
