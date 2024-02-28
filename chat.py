from gpt4all import GPT4All

def chat(texto_reconocido):

    # model = GPT4All(model_name='orca-2-13b.Q4_0.gguf') #Este necesita 16GB ram
    # model = GPT4All(model_name='orca-2-7b.Q4_0.gguf') # Este necesita 8GB ram
    model = GPT4All(model_name='replit-code-v1_5-3b-newbpe-q4_0.gguf') #Este neceseita 4GB ram
    # model = GPT4All(model_name='all-MiniLM-L6-v2-f16.gguf') #Este neceseita 1GB ram
    
    with model.chat_session() as session:
        response = session.generate(prompt=texto_reconocido, temp=0.7, max_tokens=150)
        
        if isinstance(response, str):  # Si la respuesta es una cadena simple
            print(f"Mino: {response}")
        else:  # Si la respuesta es un objeto con atributos como choices
            response_text = response.choices[0].text.strip()
            print(f"Mino: {response_text}")

