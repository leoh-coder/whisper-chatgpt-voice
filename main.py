import os
import tempfile
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from openai import OpenAI
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SAMPLE_RATE = 44100
CHANNELS = 1
DURATION = 5

SYSTEM_PROMPT = """
Você é um assistente inteligente e amigável que responde em português brasileiro.
Seja direto e conciso nas suas respostas, pois elas serão convertidas em áudio.
"""

historico = [{"role": "system", "content": SYSTEM_PROMPT}]

# 1. Gravação de áudio
def gravar_audio(duracao: int = DURATION) -> str:
    """Grava áudio do microfone e salva como WAV temporário."""
    print(f"\n🎙️  Gravando por {duracao} segundos... Fale agora!")
    audio = sd.rec(
        int(duracao * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )
    sd.wait()
    print("✅ Gravação concluída.")

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(tmp.name, SAMPLE_RATE, audio)
    return tmp.name



# 2. Transcrição com Whisper
def transcrever_audio(caminho_audio: str) -> str:
    """Envia o áudio para o Whisper e retorna o texto transcrito."""
    print("🔍 Transcrevendo com Whisper...")
    with open(caminho_audio, "rb") as f:
        transcricao = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="pt"
        )
    texto = transcricao.text.strip()
    print(f"📝 Você disse: {texto}")
    return texto

# 3. Resposta do ChatGPT
def perguntar_chatgpt(pergunta: str) -> str:
    """Envia a pergunta ao ChatGPT mantendo o histórico da conversa."""
    historico.append({"role": "user", "content": pergunta})

    print("🤖 Consultando o ChatGPT...")
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico
    )
    texto_resposta = resposta.choices[0].message.content
    historico.append({"role": "assistant", "content": texto_resposta})

    print(f"💬 ChatGPT: {texto_resposta}")
    return texto_resposta


# 4. Síntese de voz com gTTS
def falar(texto: str) -> None:
    """Converte texto em áudio e reproduz."""
    print("🔊 Sintetizando voz...")
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts = gTTS(text=texto, lang="pt", slow=False)
    tts.save(tmp.name)
    playsound(tmp.name)
    os.unlink(tmp.name)

# Loop principal
def main():
    print("=" * 50)
    print("  🎤 Assistente de Voz com ChatGPT + Whisper")
    print("  Pressione ENTER para falar | 'sair' para encerrar")
    print("=" * 50)

    while True:
        comando = input("\n[ENTER para gravar | 'sair' para encerrar] → ").strip().lower()

        if comando == "sair":
            print("👋 Encerrando. Até logo!")
            break

        # Pipeline completo: voz → texto → ChatGPT → voz
        caminho_audio = gravar_audio()

        try:
            pergunta = transcrever_audio(caminho_audio)

            if not pergunta:
                print("⚠️  Nenhuma fala detectada. Tente novamente.")
                continue

            resposta = perguntar_chatgpt(pergunta)
            falar(resposta)

        finally:
            os.unlink(caminho_audio)


if __name__ == "__main__":
    main()
