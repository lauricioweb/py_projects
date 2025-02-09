import speech_recognition as sr

def ouvir_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Fale algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para ruído ambiente
        try:
            audio = recognizer.listen(source)  # Escuta o áudio
            texto = recognizer.recognize_google_cloud(audio, language="pt-BR")  # Converte em texto
            print("🗣 Você disse:", texto)
        except sr.UnknownValueError:
            print("❌ Não entendi o que você disse.")
        except sr.RequestError:
            print("❌ Erro ao conectar-se ao serviço de reconhecimento.")

if __name__ == "__main__":
    while True:
        ouvir_microfone()

