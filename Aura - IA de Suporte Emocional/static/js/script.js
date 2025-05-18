document.addEventListener('DOMContentLoaded', () => {
    const chatbox = document.getElementById('chatbox');
    const userInput = document.getElementById('userInput');
    const sendMessageBtn = document.getElementById('sendMessageBtn');
    const avatarImage = document.getElementById('avatarImage');
    const themeToggleButton = document.getElementById('themeToggleButton'); // Botão de tema
    const soundToggleButton = document.getElementById('soundToggleButton'); // Botão de som
    const body = document.body;
    const avatarBasePath = '/static/images/avatar/';

    const sessionId = `web_session_${Date.now()}_${Math.random().toString(36).substring(2, 15)}`;

    // --- Sons ---
    const sendSound = new Audio('/static/sounds/send.mp3');
    const receiveSound = new Audio('/static/sounds/receive.mp3');
    let soundEnabled = true; // Estado inicial do som

    // Alternar som
    soundToggleButton.addEventListener('click', () => {
        soundEnabled = !soundEnabled;
        const iconElement = soundToggleButton.querySelector('i');
        if (soundEnabled) {
            iconElement.className = 'ph ph-speaker-high';
        } else {
            iconElement.className = 'ph ph-speaker-x';
        }
    });

    // Função para reproduzir som
    function playSound(sound) {
        if (soundEnabled) {
            sound.play();
        }
    }

    // --- LÓGICA PARA ALTERNAR TEMA ---
    const iconElement = themeToggleButton.querySelector('i'); // Pega o elemento <i> dentro do botão

    // Função para aplicar o tema e salvar a preferência
    function applyTheme(theme) {
        if (theme === 'dark') {
            body.classList.add('dark-theme');
            body.classList.remove('light-theme');
            if (iconElement) iconElement.className = 'ph ph-moon'; // Ícone de lua para tema escuro
            localStorage.setItem('auraTheme', 'dark');
        } else {
            body.classList.add('light-theme');
            body.classList.remove('dark-theme');
            if (iconElement) iconElement.className = 'ph ph-sun'; // Ícone de sol para tema claro
            localStorage.setItem('auraTheme', 'light');
        }
    }

    // Verifica o tema salvo no localStorage ao carregar a página
    const savedTheme = localStorage.getItem('auraTheme');
    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        // Se não houver tema salvo, verifica a preferência do sistema operacional
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            applyTheme('dark');
        } else {
            applyTheme('light'); // Padrão para claro se nada for detectado ou salvo
        }
    }

    // Garante que o body tenha uma classe de tema inicial, se nenhuma foi aplicada acima
    if (!body.classList.contains('light-theme') && !body.classList.contains('dark-theme')) {
        applyTheme('light'); // Fallback para tema claro
    }

    themeToggleButton.addEventListener('click', () => {
        if (body.classList.contains('dark-theme')) {
            applyTheme('light');
        } else {
            applyTheme('dark');
        }
    });

    // --- LÓGICA DO CHAT ---
    function addMessageToChatbox(text, sender, isTyping = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');

        if (sender === 'user') {
            messageDiv.classList.add('user-message');
        } else {
            messageDiv.classList.add('bot-message');
            if (isTyping) {
                messageDiv.classList.add('bot-typing');
                messageDiv.style.color = 'var(--secondary-text-color)'; // Cor para "digitando"
            }
        }

        const p = document.createElement('p');
        p.innerHTML = text.replace(/\n/g, '<br>');
        messageDiv.appendChild(p);
        chatbox.appendChild(messageDiv);
        // Scroll suave para a nova mensagem
        chatbox.scrollTo({ top: chatbox.scrollHeight, behavior: 'smooth' });
        return messageDiv;
    }

    const sentimentosValidos = ['neutro', 'feliz', 'triste', 'empatico', 'preocupado', 'pensativo', 'acolhedor', 'compreensivo', 'atento', 'serio'];

    function updateAvatar(sentiment) {
        const sentimentosValidos = ['neutro', 'feliz', 'triste', 'empatico', 'preocupado', 'pensativo', 'acolhedor', 'compreensivo', 'atento', 'serio'];
        let nomeImagem = 'neutro.png'; // Imagem padrão

        // Verifica se o sentimento é válido e não nulo/undefined
        if (sentiment && sentimentosValidos.includes(sentiment.toLowerCase())) {
            nomeImagem = `${sentiment.toLowerCase()}.png`; // Padrão: sentimento.png
        } else {
            console.warn(`Sentimento desconhecido ou nulo: ${sentiment}, usando avatar neutro.`);
        }

        avatarImage.src = `${avatarBasePath}${nomeImagem}`;
        avatarImage.alt = `Avatar Aura: ${sentiment || 'neutro'}`;

        // Fallback para caso a imagem específica do sentimento não exista
        avatarImage.onerror = () => {
            console.warn(`Imagem do avatar para '${nomeImagem}' não encontrada. Usando neutro.png.`);
            avatarImage.src = `${avatarBasePath}neutro.png`; // Fallback para neutro.png
            avatarImage.alt = 'Avatar Aura: neutro';
        };
    }

    async function sendMessage() {
        const messageText = userInput.value.trim();
        if (messageText === '') return;

        addMessageToChatbox(messageText, 'user');
        playSound(sendSound); // Reproduz som ao enviar mensagem
        userInput.value = '';
        userInput.focus();

        const typingIndicator = addMessageToChatbox("Aura está digitando...", 'bot', true);

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: messageText, session_id: sessionId }),
            });

            if (typingIndicator && chatbox.contains(typingIndicator)) {
                chatbox.removeChild(typingIndicator);
            }

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ reply: "Ocorreu um erro no servidor." }));
                addMessageToChatbox(errorData.reply || `Erro: ${response.status}`, 'bot');
                updateAvatar('preocupado');
                return;
            }

            const data = await response.json();
            addMessageToChatbox(data.reply, 'bot');
            playSound(receiveSound); // Reproduz som ao receber mensagem
            if (data.sentiment) {
                updateAvatar(data.sentiment);
            } else {
                updateAvatar('neutro');
            }

        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
            if (typingIndicator && chatbox.contains(typingIndicator)) {
                chatbox.removeChild(typingIndicator);
            }
            addMessageToChatbox('Desculpe, não consegui me conectar. Verifique sua conexão e tente novamente.', 'bot');
            updateAvatar('triste');
        }
    }

    sendMessageBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    // Foca no campo de input ao carregar a página
    userInput.focus();

    if (userInput) {
        userInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    }

});