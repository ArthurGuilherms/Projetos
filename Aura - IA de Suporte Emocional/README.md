# Aura – IA de Suporte Emocional

**Desenvolvido durante a Imersão IA 2025 da Alura**, o **Aura** é um chatbot de apoio emocional construído em Python com Flask e integrado à Google Gemini API. Seu propósito é ir além de respostas frias: oferecer uma experiência calorosa e humanizada, capaz de transmitir sentimentos e emoções reais a quem busca conforto ou simplesmente queira ser ouvido.  

Os elementos visuais — incluindo as expressões do avatar em 3D — foram gerados com inteligência artificial.

---

## 📋 Funcionalidades

- 💬 **Chat em tempo real** com respostas empáticas  
- 🔍 **Detecção de sentimento** na resposta da IA, alternando o avatar  
- 🌗 **Modo claro/escuro** com botão de alternância  
- 🔊 **Sons de envio/recebimento** de mensagem, com controle on/off  
- 🔄 **Textarea expansível** (cresce conforme o texto)  
- ↵ **Suporte a múltiplos parágrafos** (Shift + Enter para nova linha)  
- ⚠️ **Avisos de segurança** para contextos sensíveis  
- 📱 **Interface responsiva** para desktop e mobile

---
## 🛠 Tecnologias

- **Back‑end**: Python 3.8+, Flask  
- **IA**: Google Gemini API  
- **Front‑end**: HTML5, CSS3, JavaScript  
- **Ícones**: Phosphor Icons  

---

## 🚀 Pré‑requisitos

1. **Python 3.8+** instalado  
2. **Conta Google Cloud** com acesso à Gemini API  
3. **Chave de API** da Google Gemini  
4. (Opcional) Ambiente virtual Python

---

## ⚙️ Instalação

```bash
# 1. Clone este repositório
git clone https://github.com/SEU_USUARIO/aura-chatbot.git
cd aura-chatbot

# 2. (Opcional) Crie e ative ambiente virtual
python3 -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure a chave da API
echo "GOOGLE_API_KEY=SEU_TOKEN_AQUI" > .env

# 5. Execute o servidor Flask
flask run

Abra no navegador: http://127.0.0.1:5000

📂 Estrutura do Projeto
├── app.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── avatars/
│   │   ├── neutro.png
│   │   └── feliz.png
│   └── sounds/
│       ├── send.mp3
│       └── receive.mp3
└── docs/
    ├── ARQUITETURA.md
    └── USO_API.md

🎨 Personalização
Avatares: em static/avatars/, substitua ou adicione imagens nomeadas pelos sentimentos (neutro.png, triste.png, etc.).

Sons: em static/sounds/, coloque seus arquivos .mp3 (envio/recepção).

Cores & temas: edite static/css/style.css para ajustar paleta, fontes e espaçamentos.

⚠️ Observações Importantes
Não substitui suporte profissional. Para crises graves ou pensamentos suicidas, procure ajuda especializada imediatamente.

Uso educacional e demonstrativo: este projeto é uma prova de conceito para a Imersão IA 2025.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias!
