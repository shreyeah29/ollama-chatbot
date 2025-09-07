const chatContainer = document.getElementById('chat-container');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const themeToggle = document.getElementById('theme-toggle');
const resetBtn = document.getElementById('reset-btn');
const voiceBtn = document.getElementById('voice-btn');

let currentTheme = 'light';
let messages = [];  // Keep track of conversation history

function addMessage(text, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);

  const img = document.createElement('img');
  img.src = sender === 'user' ? '/static/img/user.png' : '/static/img/ai.png';
  img.alt = sender === 'user' ? 'User' : 'AI';

  const contentDiv = document.createElement('div');
  contentDiv.classList.add('content');
  contentDiv.innerHTML = text.replace(/\n/g, '<br>');

  messageDiv.appendChild(img);
  messageDiv.appendChild(contentDiv);

  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

if ('webkitSpeechRecognition' in window) {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  voiceBtn.addEventListener('click', () => {
    recognition.start();
    voiceBtn.textContent = '🎙️ Listening...';
  });

  recognition.addEventListener('result', (event) => {
    const voiceText = event.results[0][0].transcript;
    userInput.value = voiceText;
    voiceBtn.textContent = '🎤';
  });

  recognition.addEventListener('end', () => {
    voiceBtn.textContent = '🎤';
  });
} else {
  voiceBtn.disabled = true;
  voiceBtn.title = "Speech Recognition Not Supported";
}

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = userInput.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  messages.push({ role: 'user', content: text });
  userInput.value = '';

  // Typing indicator
  const typingMsg = document.createElement('div');
  typingMsg.classList.add('message', 'ai');
  typingMsg.innerHTML = `
    <img src="/static/img/ai.png" alt="AI">
    <div class="content">Typing...</div>`;
  chatContainer.appendChild(typingMsg);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages }),
    });

    const data = await response.json();
    typingMsg.remove();

    const aiText = data.response || 'Sorry, I couldn’t understand that.';
    addMessage(aiText, 'ai');
    messages.push({ role: 'assistant', content: aiText });

  } catch (err) {
    typingMsg.remove();
    addMessage('Error getting response. Please try again.', 'ai');
  }

  userInput.focus();
});

themeToggle.addEventListener('click', () => {
  if (currentTheme === 'light') {
    currentTheme = 'dark';
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    themeToggle.textContent = '☀️';
  } else {
    currentTheme = 'light';
    document.body.classList.remove('dark-theme');
    document.body.classList.add('light-theme');
    themeToggle.textContent = '🌙';
  }
});

resetBtn.addEventListener('click', async () => {
  chatContainer.innerHTML = '';
  messages = [];
  try {
    await fetch('/reset', { method: 'POST' });
  } catch (err) {
    console.error('Reset failed');
  }
});

const openWebUiBtn = document.getElementById('open-web-ui');
openWebUiBtn.addEventListener('click', () => {
  window.open('http://localhost:3000', '_blank');
});

document.body.classList.add('light-theme');
themeToggle.textContent = '🌙';
