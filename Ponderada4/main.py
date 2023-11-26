import openai
import gradio as gr

openai.api_key = ""  # Substitua com sua chave

def predict(message, history):
    # Prompt inicial sobre segurança industrial
    initial_prompt = "Olá, sou um especialista em segurança industrial. Como posso ajudar você hoje?"

    # Formatação do histórico incluindo o prompt inicial
    history_openai_format = [
        {"role": "assistant", "content": initial_prompt}
    ]

    # Adiciona mensagens anteriores ao histórico formatado
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content": assistant})
    
    # Adiciona a mensagem atual ao histórico formatado
    history_openai_format.append({"role": "user", "content": message})

    # Chama a API OpenAI para previsão
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    # Gera e retorna a resposta parcial
    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(predict).queue().launch(share=True)


