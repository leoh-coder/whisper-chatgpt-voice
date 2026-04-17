# 🎤 Assistente de Voz com ChatGPT e Whisper

Aplicação em Python que permite **conversar por voz com o ChatGPT**. O usuário fala, o [Whisper](https://openai.com/research/whisper) transcreve, o [ChatGPT](https://openai.com/chatgpt) responde e o [gTTS](https://gtts.readthedocs.io/) fala a resposta em voz alta — tudo em português.

Projeto desenvolvido como parte do **Bootcamp Bradesco - GenAI & Dados** na plataforma [DIO](https://www.dio.me/).

---

## 🚀 Pipeline da Aplicação

```
Microfone → [Whisper] → Texto → [ChatGPT] → Resposta → [gTTS] → Áudio
```

| Etapa | Tecnologia | Função |
|-------|-----------|--------|
| Gravação | `sounddevice` | Captura o áudio do microfone |
| Transcrição | `Whisper (OpenAI)` | Converte áudio em texto |
| Resposta | `GPT-4o Mini` | Gera a resposta em linguagem natural |
| Síntese | `gTTS` | Converte a resposta em áudio |

---

## 🛠️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/whisper-chatgpt-voice.git
cd whisper-chatgpt-voice
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **Observação:** Em alguns sistemas Linux, pode ser necessário instalar o `libportaudio2`:
> ```bash
> sudo apt-get install libportaudio2
> ```

### 4. Configure a chave da OpenAI

Copie o arquivo `.env.example` para `.env` e adicione sua chave:

```bash
cp .env.example .env
```

Edite o `.env`:
```
OPENAI_API_KEY=sk-...sua_chave_aqui...
```

> Obtenha sua chave em [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 5. Execute

```bash
python main.py
```

---

## 🎯 Como Usar

1. Ao iniciar, pressione **ENTER** para começar a gravar
2. Fale sua pergunta em voz alta (5 segundos de janela)
3. Aguarde a transcrição, resposta e síntese de voz
4. A conversa mantém **histórico de contexto** — o assistente lembra do que foi dito
5. Digite `sair` para encerrar

---

## 📁 Estrutura do Projeto

```
whisper-chatgpt-voice/
├── main.py           # Código principal da aplicação
├── requirements.txt  # Dependências do projeto
├── .env.example      # Modelo do arquivo de variáveis de ambiente
├── .env              # Sua chave de API (não commitar!)
└── README.md
```

---

## 🔧 Tecnologias Utilizadas

- **Python 3.10+**
- **OpenAI API** — Whisper (transcrição) + GPT-4o Mini (resposta)
- **sounddevice** — captura de áudio
- **gTTS** — síntese de voz em português
- **python-dotenv** — gerenciamento de variáveis de ambiente

---

## 📌 Observações

- A gravação tem duração fixa de **5 segundos** por padrão. Altere a constante `DURATION` em `main.py` conforme necessário.
- O histórico de conversa é mantido **em memória** durante a sessão. Ao encerrar, o contexto é perdido.
- O modelo utilizado é o `gpt-4o-mini` para equilibrar custo e qualidade. Pode ser substituído por `gpt-4o` para respostas mais elaboradas.

---

## 👨‍💻 Autor

**Leonardo Henrique** — [LinkedIn](https://linkedin.com/in/seu-perfil) | [GitHub](https://github.com/seu-usuario)
