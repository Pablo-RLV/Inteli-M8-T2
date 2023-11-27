# Usa a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

COPY context.pdf .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo main.py para o diretório de trabalho
COPY main.py .

# Expõe a porta 7860
EXPOSE 7860

# Comando para executar o arquivo main.py
CMD ["python", "-u", "main.py"]
