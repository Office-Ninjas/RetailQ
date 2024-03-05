import speech_recognition as sr
import pyaudio
import pyttsx3
import openai

init_rec = sr.Recognizer()
engine = pyttsx3.init() 
def get_completion(prompt, model="gpt-3.5-turbo"):
    client = openai.OpenAI(api_key="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")
    
    response = client.chat.completions.create(
        model=model,
      messages = [{"role": "system", "content": "You are a helpful assistan that provides information only  related to e-commerce products. Generate a response -'No product found, I can answer only e-commerce queries' when the prompt is not related to e-commerce products"},{"role": "user", "content": prompt}],
        
    )
    return response.choices[0].message.content
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    print(text)
    res = get_completion(text)
    print(res)
    engine.say(res) 
    engine.runAndWait() 
    

def live:
    
    aai.settings.api_key = "811dc671c6c64822986ea84e2d2c1332"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    print(transcript.text)



