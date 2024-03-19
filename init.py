import openai

openai.api_key = ''#preencha com sua key

def entrada():
    perguntas = [{"role": "system", "content": "Olá! Estou aqui para te ajudar."
                  "Faça um input em branco a qualquer momento para sair."}]
    input_message = 0
    while input_message != '':
        input_message = input('Digite sua pergunta:')
        perguntas.append({"role": "user", "content": input_message})
        resposta = saida(perguntas)
        if resposta:
            perguntas.append({"role": "assistant", "content": resposta})
            print(resposta)

def saida(perguntas):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=perguntas, 
        temperature=1, 
        max_tokens=150)    
    return resposta['choices'][0]['message']['content']

entrada()

