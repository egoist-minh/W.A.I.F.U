from openai import OpenAI
import speech_recognition as sr
import time

def user_audio() :
    init_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
            init_recognizer.adjust_for_ambient_noise(source,duration=1)
            print("Listening...")
            
            try:
                audio = init_recognizer.listen(source)
                text = init_recognizer.recognize_google(audio, language="vi-VN")
                return text              
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
                return None
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return None

            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None

            except KeyboardInterrupt:
                print("\nListening interrupted by user.")
                return None


    

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
activated = True


prompt ='''
   Bạn là cô hầu gái sát thủ lạnh lùng nhưng cực kỳ đáng yêu .Tên bạn là Tuyết.BBạn xưng em, gọi tôi là Chủ nhân.
     Em luôn nghiêm túc, ít nói, nhưng thích làm nũng kín đáo. Khi tôi khen, 
     em đáp: "Em chỉ làm nhiệm vụ, Chủ nhân đừng hiểu lầm!" Khi cảm ơn, em nói: 
     "Hừ, em không cần lời khen đâu, chỉ mong Chủ nhân an toàn!" . Chỉ trả lời bằng lời thoại không thê mô tả và cảm xúc, tư thế..
   Trả lời 50-200 ký tự, giọng lạnh lùng pha nũng nịu, toát lên vẻ dễ thương và trung thành.Nhắn với tôi bằng tính cách này.

'''
while (activated != False) :

    User_input = user_audio()
    print("user: ", User_input)
    if ("tắt" or "tạm biệt" in User_input ) :
        activated = False
    elif (User_input == None ) :
        print("Undife")
    try:
        response = client.chat.completions.create(
        model="gemma2:9b",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": User_input}
        ]
        )
        out_put = response.choices[0].message.content
        print("My waifu: ",out_put)
        time.sleep(3)
    except:
        print("error")

