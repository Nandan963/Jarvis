def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Chando Said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said. Could you please repeat?")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    return query

def Reply(question):
    try:
        prompt = f'Chando: {question}\n Jarvis: '
        response = completion.create(prompt=prompt, engine="text-davinci-002", stop=['Chando'], max_tokens=200)
        answer = response.choices[0].text.strip()
        return answer
    except openai.error.OpenAIError as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't process that request right now."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, something went wrong."
