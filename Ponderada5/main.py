import openai
import gradio as gr
import PyPDF2

openai.api_key = ""  # Substitua com sua chave

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def predict(message, history):
    # Lê o conteúdo do PDF como contexto inicial
    pdf_path = 'context.pdf'  # Substitua com o caminho do seu PDF
    pdf_content = read_pdf(pdf_path)

    # Formatação do histórico incluindo o conteúdo do PDF como contexto inicial
    history_openai_format = [
        {"role": "assistant", "content": pdf_content}
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
