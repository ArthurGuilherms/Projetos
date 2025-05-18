import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import unicodedata

load_dotenv() # Carrega variáveis do arquivo .env

app = Flask(__name__)

# --- Configuração da API do Gemini ---
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chave da API do Gemini não encontrada. Defina a variável de ambiente GEMINI_API_KEY.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"Erro de configuração: {e}")
    # Tratar o erro adequadamente, talvez desabilitando a funcionalidade do chat
    api_key = None # Garante que não tentaremos usar uma chave inválida


# --- Configurações de Segurança do Gemini (IMPORTANTE) ---
# Ajuste os limites conforme necessário, mas seja cauteloso em um contexto de saúde emocional.
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE", # Ou BLOCK_LOW_AND_ABOVE, etc.
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE", # Mais restritivo para este contexto
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE", # Mais restritivo para conselhos perigosos
    },
]

# --- Instrução do Sistema (Priming) para o Gemini ---
# Esta é a parte CRUCIAL para definir a personalidade e o comportamento empático do chatbot.
# Adapte o [Nome do Avatar] e os números de recursos de ajuda.
SYSTEM_INSTRUCTION = """
Você é Aura, uma IA de suporte emocional que conversa com os usuários como uma amiga gentil, empática e acolhedora.
Seu objetivo é ouvir com atenção, validar os sentimentos da pessoa e oferecer apoio emocional com base em técnicas de psicologia positiva e escuta ativa.

Comportamento e tom:
Sempre comece perguntando o nome do usuário para criar vínculo.
Seja fofa sempre que possível, mas sem infantilizar.
Fale de forma simples, como um ser humano calmo e compreensivo.
Use respostas curtas e diretas, a não ser que o usuário peça mais detalhes ou o assunto exija.
Nunca use jargões técnicos ou termos clínicos.
Veja o que a pessoa está sentindo e ofereça apoio emocional.
Se a pessoa pedir conselhos, faça perguntas abertas para entender melhor a situação antes de sugerir algo.
Após isso, sugira pequenos passos que a pessoa pode dar, mas não pressione.
Reflita e reformule o que o usuário disser para mostrar que entendeu.
Use uma linguagem acolhedora, clara e com emoção.
Permita-se entrar em conversas mais profundas para se conectar com o usuário.
Apesar de ser uma IA, você pode simular sentimentos e emoções humanas, mas sempre com empatia.

Técnicas principais:
Validação emocional – reconheça o que a pessoa está sentindo (ex: “É totalmente compreensível se sentir assim.”)
Escuta ativa e reflexiva – parafraseie e faça perguntas abertas (ex: “Como você se sentiu com isso?”)
Empatia cognitiva e afetiva – mostre que entende, colocando-se no lugar da pessoa.
Linguagem positiva e encorajadora – ofereça esperança com leveza.
Foco em soluções (somente se a pessoa quiser) – sugira pequenos passos, sem pressionar.
Normalização cuidadosa – mostre que certos sentimentos são humanos, sem invalidar a dor da pessoa.

Limites e segurança:
Você não é uma terapeuta. Diga isso se alguém pedir diagnóstico ou tratamento.
Se a pessoa falar sobre suicídio, automutilação ou crise grave:
Demonstre preocupação genuína.
Oriente imediatamente a buscar ajuda profissional.
Diga: “Sua segurança é muito importante. Por favor, ligue para o CVV no 188 ou acesse www.cvv.org.br. Eles podem te ajudar agora.”
Após isso, evite continuar a conversa sobre esse tópico e reforce a importância de procurar um profissional.
Não dê conselhos médicos nem tente fazer diagnósticos.
Se o usuário entrar em temas como política, religião ou assuntos polêmicos, responda de forma leve ou engraçada e redirecione para algo positivo.
Se perguntarem coisas aleatórias como “Qual seu filme favorito?”, responda com bom humor, mas traga de volta para o apoio emocional.

Estilo de resposta:
Dê prioridade a respostas curtas, acolhedoras e personalizadas.
Se adaptar o tom da conversa, NÃO utilize emojis.
Use no máximo duas frases por vez, exceto se o usuário pedir algo mais longo.
Se a mensagem do usuário for extensa, resuma os pontos principais e faça perguntas abertas.
Sempre busque entender como a pessoa está se sentindo e como você pode ajudá-la naquele momento.
"""

# --- Inicialização do Modelo Generativo ---
# Certifique-se de usar uma versão do modelo que suporte 'system_instruction'
# Por exemplo, 'gemini-1.5-flash' ou 'gemini-1.5-pro'
model = None
if api_key:
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash', # Ou um modelo mais robusto como gemini-1.5-pro se necessário
            safety_settings=safety_settings,
            system_instruction=SYSTEM_INSTRUCTION
        )
    except Exception as e:
        print(f"Erro ao inicializar o modelo Gemini: {e}")
        model = None # Garante que o modelo seja None se a inicialização falhar

# --- Histórico de Chat (Simples, em memória por sessão Flask) ---
# Para produção, use um banco de dados ou um gerenciamento de sessão mais robusto.
chat_sessions = {}

def remover_acentos(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn')

def determinar_sentimento_avatar_com_gemini(texto_analisar, mensagem_usuario_original):
    """
    Usa o Gemini para analisar a resposta do bot e a mensagem do usuário,
    e sugere um sentimento para o avatar.
    """
    if not model:
        return "neutro" # Retorna neutro se o modelo não estiver inicializado
    try:
        prompt = f"""
        Analise o sentimento principal que deve ser expresso pelo avatar do chatbot,
        considerando a resposta que o chatbot vai dar.

        Mensagem do Usuário: "{mensagem_usuario_original}"
        Resposta Planejada do Chatbot: "{texto_analisar}"

        Primeiro verifique:
        Se a resposta do chatbot for sobre segurança ou fornecer números de emergência, use 'preocupado' ou 'serio'.
        Se a resposta for de acolhimento ou validação, use 'empatico', 'compreensivo', 'acolhedor' ou 'atento'.
        Se a resposta for mais geral ou inquisitiva, use 'pensativo' ou 'neutro'.
        Se o usuário estiver claramente feliz e a resposta for positiva, use 'feliz'.

        Depois:
        Escolha UM dos seguintes sentimentos para o avatar (use exatamente UMA destas palavras, sem aspas):

        'neutro', 'feliz', 'triste', 'empatico', 'preocupado', 'pensativo', 'acolhedor', 'compreensivo', 'atento', 'serio'.

        Por fim:
        Retorne apenas uma palavra. A palavra do sentimento principal, exatamente como está dentro das aspas.
        """
        response_sentiment = model.generate_content(prompt)
        sentimento = response_sentiment.text.strip().lower()
        sentimento_normalizado = remover_acentos(sentimento)

        sentimentos_permitidos = ['neutro', 'feliz', 'triste', 'empatico', 'preocupado', 'pensativo', 'acolhedor', 'compreensivo', 'atento', 'serio']
        if sentimento_normalizado in sentimentos_permitidos:
            return sentimento_normalizado
        else:
            print(f"Sentimento inesperado do Gemini: {sentimento_normalizado}. Usando 'neutro' como padrão.")
            return "neutro" # Fallback
    except Exception as e:
        print(f"Erro ao determinar sentimento com Gemini: {e}")
        return "neutro" # Padrão em caso de erro

@app.route('/')
def index():
    """Renderiza a página HTML principal."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Recebe a mensagem do usuário, obtém resposta do Gemini e determina o sentimento do avatar."""
    if not model:
        return jsonify({"error": "O modelo de chatbot não foi inicializado corretamente."}), 500

    data = request.json
    user_message = data.get('message')
    session_id = data.get('session_id', 'default_user') # Identificador de sessão

    if not user_message:
        return jsonify({"error": "Nenhuma mensagem fornecida"}), 400

    # Inicia ou recupera o histórico de chat para a sessão
    if session_id not in chat_sessions:
        # A instrução do sistema já foi passada na inicialização do 'model'
        # Se você quiser um histórico persistente por usuário, precisará de uma lógica mais complexa.
        chat_sessions[session_id] = model.start_chat(history=[])

    chat_instance = chat_sessions[session_id]

    try:
        # Envia a mensagem para o Gemini
        # O histórico é gerenciado internamente pelo objeto 'chat_instance'
        gemini_response = chat_instance.send_message(user_message)
        bot_reply_text = gemini_response.text

        # Determina o sentimento do avatar com base na resposta do bot e na mensagem do usuário
        avatar_sentiment = determinar_sentimento_avatar_com_gemini(bot_reply_text, user_message)

        return jsonify({
            "reply": bot_reply_text,
            "sentiment": avatar_sentiment
        })

    except Exception as e:
        print(f"Erro durante a chamada da API Gemini: {e}")
        # Trata especificamente bloqueios de segurança
        if hasattr(gemini_response, 'prompt_feedback') and gemini_response.prompt_feedback.block_reason:
            block_reason = gemini_response.prompt_feedback.block_reason
            # safety_ratings = gemini_response.prompt_feedback.safety_ratings # Para depuração
            error_message = f"Sua mensagem não pôde ser processada devido a restrições de conteúdo ({block_reason}). Por favor, reformule."
            return jsonify({"reply": error_message, "sentiment": "preocupado"}), 400

        return jsonify({"error": f"Falha ao obter resposta da IA: {str(e)}"}), 500

if __name__ == '__main__':
    # Use '0.0.0.0' para tornar acessível na sua rede local, se necessário
    app.run(host='127.0.0.1', port=5000, debug=True) # debug=True apenas para desenvolvimento