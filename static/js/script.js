
// const form = document.getElementById('chat-form');
// const input = document.getElementById('user-input');
// const chatContainer = document.getElementById('chat-container');
// const resetBtn = document.getElementById('reset-btn');

// const userImgSrc = '/static/img/user.png';
// const aiImgSrc = '/static/img/ai.png';

// // Helper to add message to chat
// function addMessage(text, sender) {
//     const messageElem = document.createElement('div');
//     messageElem.classList.add('message', sender);

//     const img = document.createElement('img');
//     img.src = sender === 'user' ? userImgSrc : aiImgSrc;
//     img.alt = sender === 'user' ? 'User' : 'AI';

//     const content = document.createElement('div');
//     content.classList.add('content');
//     content.textContent = text;

//     messageElem.appendChild(img);
//     messageElem.appendChild(content);

//     chatContainer.appendChild(messageElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// // Show typing indicator
// function showTyping() {
//     const typingElem = document.createElement('div');
//     typingElem.id = 'typing-indicator';
//     typingElem.classList.add('message', 'ai', 'typing');
//     typingElem.textContent = 'Ollama AI is typing...';
//     chatContainer.appendChild(typingElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// // Remove typing indicator
// function removeTyping() {
//     const typingElem = document.getElementById('typing-indicator');
//     if (typingElem) typingElem.remove();
// }

// // Load chat history from server on page load (optional)
// // Here, for simplicity, we start fresh each reload.

// // Handle form submit
// form.addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const question = input.value.trim();
//     if (!question) return;

//     addMessage(question, 'user');

//     input.value = '';
//     input.disabled = true;

//     showTyping();

//     try {
//         const response = await fetch('/ask', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ question }),
//         });
//         const data = await response.json();

//         removeTyping();

//         if (data.error) {
//             addMessage('Error: ' + data.error, 'ai');
//         } else {
//             addMessage(data.answer, 'ai');
//         }
//     } catch (err) {
//         removeTyping();
//         addMessage('Error: Unable to get response. Please try again.', 'ai');
//     } finally {
//         input.disabled = false;
//         input.focus();
//     }
// });

// // Reset chat
// resetBtn.addEventListener('click', async () => {
//     if (!confirm('Are you sure you want to reset the chat?')) return;

//     try {
//         const res = await fetch('/reset', {
//             method: 'POST',
//         });
//         const data = await res.json();
//         if (data.status === 'reset') {
//             chatContainer.innerHTML = '';
//         }
//     } catch {
//         alert('Failed to reset chat.');
//     }
// });









// const form = document.getElementById('chat-form');
// const input = document.getElementById('user-input');
// const chatContainer = document.getElementById('chat-container');
// const resetBtn = document.getElementById('reset-btn');
// const themeToggle = document.getElementById('theme-toggle');
// const voiceBtn = document.getElementById('voice-btn');
// const fileUpload = document.getElementById('file-upload');

// const userImgSrc = '/static/img/user.png';
// const aiImgSrc = '/static/img/ai.png';

// function addMessage(text, sender) {
//     const messageElem = document.createElement('div');
//     messageElem.classList.add('message', sender);

//     const img = document.createElement('img');
//     img.src = sender === 'user' ? userImgSrc : aiImgSrc;
//     img.alt = sender === 'user' ? 'User' : 'AI';

//     const content = document.createElement('div');
//     content.classList.add('content');
//     content.textContent = text;

//     messageElem.appendChild(img);
//     messageElem.appendChild(content);

//     chatContainer.appendChild(messageElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// function showTyping() {
//     const typingElem = document.createElement('div');
//     typingElem.id = 'typing-indicator';
//     typingElem.classList.add('message', 'ai', 'typing');
//     typingElem.textContent = 'Ollama AI is typing...';
//     chatContainer.appendChild(typingElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// function removeTyping() {
//     const typingElem = document.getElementById('typing-indicator');
//     if (typingElem) typingElem.remove();
// }

// form.addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const question = input.value.trim();
//     if (!question) return;

//     addMessage(question, 'user');

//     input.value = '';
//     input.disabled = true;

//     showTyping();

//     try {
//         const response = await fetch('/ask', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ question }),
//         });
//         const data = await response.json();

//         removeTyping();
//         addMessage(data.answer || 'No response received.', 'ai');
//     } catch (err) {
//         removeTyping();
//         addMessage('Error: Unable to get response. Please try again.', 'ai');
//     } finally {
//         input.disabled = false;
//         input.focus();
//     }
// });

// resetBtn.addEventListener('click', async () => {
//     if (!confirm('Are you sure you want to reset the chat?')) return;

//     try {
//         const res = await fetch('/reset', { method: 'POST' });
//         const data = await res.json();
//         if (data.status === 'reset') chatContainer.innerHTML = '';
//     } catch {
//         alert('Failed to reset chat.');
//     }
// });

// // Voice input
// voiceBtn.addEventListener('click', () => {
//     const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//     recognition.lang = 'en-US';
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;

//     recognition.onresult = (e) => {
//         const transcript = e.results[0][0].transcript;
//         input.value = transcript;
//     };

//     recognition.onerror = () => alert('Voice input error!');
//     recognition.start();
// });

// // Theme toggle
// themeToggle.addEventListener('click', () => {
//     document.body.classList.toggle('dark-theme');
//     themeToggle.textContent = document.body.classList.contains('dark-theme') ? '☀️' : '🌙';
// });

// // File upload
// fileUpload.addEventListener('change', async (e) => {
//     const file = e.target.files[0];
//     if (!file) return;

//     const formData = new FormData();
//     formData.append('file', file);

//     addMessage(`Uploaded file: ${file.name}`, 'user');

//     try {
//         const response = await fetch('/upload', {
//             method: 'POST',
//             body: formData
//         });
//         const data = await response.json();
//         addMessage(data.message || 'File received!', 'ai');
//     } catch {
//         addMessage('Error: Failed to upload file.', 'ai');
//     }
// });










// const form = document.getElementById('chat-form');
// const input = document.getElementById('user-input');
// const chatContainer = document.getElementById('chat-container');
// const resetBtn = document.getElementById('reset-btn');
// const themeToggle = document.getElementById('theme-toggle');
// const voiceBtn = document.getElementById('voice-btn');
// const fileUpload = document.getElementById('file-upload');

// const userImgSrc = '/static/img/user.png';
// const aiImgSrc = '/static/img/ai.png';

// function addMessage(text, sender) {
//     const messageElem = document.createElement('div');
//     messageElem.classList.add('message', sender);

//     const img = document.createElement('img');
//     img.src = sender === 'user' ? userImgSrc : aiImgSrc;
//     img.alt = sender === 'user' ? 'User' : 'AI';

//     const content = document.createElement('div');
//     content.classList.add('content');
//     content.textContent = text;

//     messageElem.appendChild(img);
//     messageElem.appendChild(content);

//     chatContainer.appendChild(messageElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// function showTyping() {
//     const typingElem = document.createElement('div');
//     typingElem.id = 'typing-indicator';
//     typingElem.classList.add('message', 'ai', 'typing');
//     typingElem.textContent = 'Ollama AI is typing...';
//     chatContainer.appendChild(typingElem);
//     chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// function removeTyping() {
//     const typingElem = document.getElementById('typing-indicator');
//     if (typingElem) typingElem.remove();
// }

// form.addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const question = input.value.trim();
//     if (!question) return;

//     addMessage(question, 'user');

//     input.value = '';
//     input.disabled = true;

//     showTyping();

//     try {
//         const response = await fetch('/ask', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ question }),
//         });
//         const data = await response.json();

//         removeTyping();
//         addMessage(data.answer || 'No response received.', 'ai');
//     } catch (err) {
//         removeTyping();
//         addMessage('Error: Unable to get response. Please try again.', 'ai');
//     } finally {
//         input.disabled = false;
//         input.focus();
//     }
// });

// resetBtn.addEventListener('click', async () => {
//     if (!confirm('Are you sure you want to reset the chat?')) return;

//     try {
//         const res = await fetch('/reset', { method: 'POST' });
//         const data = await res.json();
//         if (data.status === 'reset') chatContainer.innerHTML = '';
//     } catch {
//         alert('Failed to reset chat.');
//     }
// });

// // Voice input
// voiceBtn.addEventListener('click', () => {
//     const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//     recognition.lang = 'en-US';
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;

//     recognition.onresult = (e) => {
//         const transcript = e.results[0][0].transcript;
//         input.value = transcript;
//     };

//     recognition.onerror = () => alert('Voice input error!');
//     recognition.start();
// });

// // Theme toggle
// // Improved toggle to save user preference in localStorage

// function setTheme(isDark) {
//     if (isDark) {
//         document.body.classList.add('dark-theme');
//         themeToggle.textContent = '☀️';
//         localStorage.setItem('theme', 'dark');
//     } else {
//         document.body.classList.remove('dark-theme');
//         themeToggle.textContent = '🌙';
//         localStorage.setItem('theme', 'light');
//     }
// }

// // On page load, apply theme from localStorage if present
// window.addEventListener('DOMContentLoaded', () => {
//     const savedTheme = localStorage.getItem('theme');
//     if (savedTheme === 'dark') {
//         setTheme(true);
//     } else {
//         setTheme(false);
//     }
// });

// themeToggle.addEventListener('click', () => {
//   document.body.classList.toggle("dark-theme");
//   document.body.classList.toggle("light-theme");
// });

// // File upload
// fileUpload.addEventListener('change', async (e) => {
//     const file = e.target.files[0];
//     if (!file) return;

//     const formData = new FormData();
//     formData.append('file', file);

//     addMessage(`Uploaded file: ${file.name}`, 'user');

//     try {
//         const response = await fetch('/upload', {
//             method: 'POST',
//             body: formData
//         });
//         const data = await response.json();
//         addMessage(data.message || 'File received!', 'ai');
//     } catch {
//         addMessage('Error: Failed to upload file.', 'ai');
//     }
// });


















// const chatContainer = document.getElementById('chat-container');
// const chatForm = document.getElementById('chat-form');
// const userInput = document.getElementById('user-input');
// const themeToggle = document.getElementById('theme-toggle');
// const resetBtn = document.getElementById('reset-btn');
// const voiceBtn = document.getElementById('voice-btn');

// let currentTheme = 'light'; // default

// // Function to add messages
// function addMessage(text, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.classList.add('message', sender); // sender: 'user' or 'ai'

//   const img = document.createElement('img');
//   img.src = sender === 'user' ? '/static/img/user.png' : '/static/img/ai.png';  // Corrected path
//   img.alt = sender === 'user' ? 'User' : 'AI';

//   const contentDiv = document.createElement('div');
//   contentDiv.classList.add('content');
//   contentDiv.textContent = text;

//   messageDiv.appendChild(img);
//   messageDiv.appendChild(contentDiv);

//   chatContainer.appendChild(messageDiv);
//   chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// if ('webkitSpeechRecognition' in window) {
//   const recognition = new webkitSpeechRecognition();
//   recognition.lang = 'en-US';
//   recognition.interimResults = false;
//   recognition.maxAlternatives = 1;

//   voiceBtn.addEventListener('click', () => {
//     recognition.start();
//     voiceBtn.textContent = '🎙️ Listening...';
//   });

//   recognition.addEventListener('result', (event) => {
//     const voiceText = event.results[0][0].transcript;
//     userInput.value = voiceText;
//     voiceBtn.textContent = '🎤';
//   });

//   recognition.addEventListener('end', () => {
//     voiceBtn.textContent = '🎤';
//   });
// } else {
//   voiceBtn.disabled = true;
//   voiceBtn.title = "Speech Recognition Not Supported";
// }

// // Handle form submit
// chatForm.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const text = userInput.value.trim();
//   if (!text) return;

//   addMessage(text, 'user');
//   userInput.value = '';

//   // Simulate AI response after delay
//   setTimeout(() => {
//     addMessage('This is an AI response to: ' + text, 'ai');
//   }, 1000);
// });

// // Toggle theme
// themeToggle.addEventListener('click', () => {
//   if (currentTheme === 'light') {
//     currentTheme = 'dark';
//     document.body.classList.remove('light-theme');
//     document.body.classList.add('dark-theme');
//     themeToggle.textContent = '☀️';
//   } else {
//     currentTheme = 'light';
//     document.body.classList.remove('dark-theme');
//     document.body.classList.add('light-theme');
//     themeToggle.textContent = '🌙';
//   }
// });

// // Reset chat
// resetBtn.addEventListener('click', () => {
//   chatContainer.innerHTML = '';
// });


// // Initialize theme on page load
// document.body.classList.add('light-theme');
// themeToggle.textContent = '🌙';








// not workinh

// const chatContainer = document.getElementById('chat-container');
// const chatForm = document.getElementById('chat-form');
// const userInput = document.getElementById('user-input');
// const themeToggle = document.getElementById('theme-toggle');
// const resetBtn = document.getElementById('reset-btn');
// const voiceBtn = document.getElementById('voice-btn');

// let currentTheme = 'light'; // default

// // Function to add messages
// function addMessage(text, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.classList.add('message', sender);

//   const img = document.createElement('img');
//   img.src = sender === 'user' ? '/static/img/user.png' : '/static/img/ai.png';
//   img.alt = sender === 'user' ? 'User' : 'AI';

//   const contentDiv = document.createElement('div');
//   contentDiv.classList.add('content');
//   contentDiv.textContent = text;

//   messageDiv.appendChild(img);
//   messageDiv.appendChild(contentDiv);

//   chatContainer.appendChild(messageDiv);
//   chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// // Voice recognition
// if ('webkitSpeechRecognition' in window) {
//   const recognition = new webkitSpeechRecognition();
//   recognition.lang = 'en-US';
//   recognition.interimResults = false;
//   recognition.maxAlternatives = 1;

//   voiceBtn.addEventListener('click', () => {
//     recognition.start();
//     voiceBtn.textContent = '🎙️ Listening...';
//   });

//   recognition.addEventListener('result', (event) => {
//     const voiceText = event.results[0][0].transcript;
//     userInput.value = voiceText;
//     voiceBtn.textContent = '🎤';
//   });

//   recognition.addEventListener('end', () => {
//     voiceBtn.textContent = '🎤';
//   });
// } else {
//   voiceBtn.disabled = true;
//   voiceBtn.title = "Speech Recognition Not Supported";
// }

// // Handle form submit
// chatForm.addEventListener('submit', async (e) => {
//   e.preventDefault();
//   const text = userInput.value.trim();
//   if (!text) return;

//   addMessage(text, 'user');
//   userInput.value = '';

//   // Typing indicator
//   const typingMsg = document.createElement('div');
//   typingMsg.classList.add('message', 'ai');
//   typingMsg.innerHTML = `<img src="/static/img/ai.png" alt="AI"><div class="content">Typing...</div>`;
//   chatContainer.appendChild(typingMsg);
//   chatContainer.scrollTop = chatContainer.scrollHeight;

//   try {
//     const response = await fetch('/ask', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ question: text })
//     });

//     const data = await response.json();
//     typingMsg.remove(); // Remove "Typing..." bubble
//     addMessage(data.answer, 'ai');
//   } catch (err) {
//     typingMsg.remove();
//     addMessage('Error getting response. Please try again.', 'ai');
//   }
// });

// // Toggle theme
// themeToggle.addEventListener('click', () => {
//   if (currentTheme === 'light') {
//     currentTheme = 'dark';
//     document.body.classList.remove('light-theme');
//     document.body.classList.add('dark-theme');
//     themeToggle.textContent = '☀️';
//   } else {
//     currentTheme = 'light';
//     document.body.classList.remove('dark-theme');
//     document.body.classList.add('light-theme');
//     themeToggle.textContent = '🌙';
//   }
// });

// // Reset chat
// resetBtn.addEventListener('click', async () => {
//   chatContainer.innerHTML = '';
//   try {
//     await fetch('/reset', { method: 'POST' });
//   } catch (err) {
//     console.error('Reset failed');
//   }
// });

// // Set default theme on page load
// document.body.classList.add('light-theme');
// themeToggle.textContent = '🌙';








// const chatContainer = document.getElementById('chat-container');
// const chatForm = document.getElementById('chat-form');
// const userInput = document.getElementById('user-input');
// const themeToggle = document.getElementById('theme-toggle');
// const resetBtn = document.getElementById('reset-btn');
// const voiceBtn = document.getElementById('voice-btn');

// let currentTheme = 'light'; // default

// // Function to add messages
// function addMessage(text, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.classList.add('message', sender);

//   const img = document.createElement('img');
//   img.src = sender === 'user' ? '/static/img/user.png' : '/static/img/ai.png';
//   img.alt = sender === 'user' ? 'User' : 'AI';

//   const contentDiv = document.createElement('div');
//   contentDiv.classList.add('content');
//   contentDiv.innerHTML = text.replace(/\n/g, '<br>');

//   messageDiv.appendChild(img);
//   messageDiv.appendChild(contentDiv);

//   chatContainer.appendChild(messageDiv);
//   chatContainer.scrollTop = chatContainer.scrollHeight;
// }

// // Voice recognition
// if ('webkitSpeechRecognition' in window) {
//   const recognition = new webkitSpeechRecognition();
//   recognition.lang = 'en-US';
//   recognition.interimResults = false;
//   recognition.maxAlternatives = 1;

//   voiceBtn.addEventListener('click', () => {
//     recognition.start();
//     voiceBtn.textContent = '🎙️ Listening...';
//   });

//   recognition.addEventListener('result', (event) => {
//     const voiceText = event.results[0][0].transcript;
//     userInput.value = voiceText;
//     voiceBtn.textContent = '🎤';
//   });

//   recognition.addEventListener('end', () => {
//     voiceBtn.textContent = '🎤';
//   });
// } else {
//   voiceBtn.disabled = true;
//   voiceBtn.title = "Speech Recognition Not Supported";
// }

// // Handle form submit
// chatForm.addEventListener('submit', async (e) => {
//   e.preventDefault();
//   const text = userInput.value.trim();
//   if (!text) return;

//   addMessage(text, 'user');
//   userInput.value = '';

//   // Typing indicator
//   const typingMsg = document.createElement('div');
//   typingMsg.classList.add('message', 'ai');
//   typingMsg.innerHTML = `
//     <img src="/static/img/ai.png" alt="AI">
//     <div class="content">Typing...</div>`;
//   chatContainer.appendChild(typingMsg);
//   chatContainer.scrollTop = chatContainer.scrollHeight;

//   try {
//     const response = await fetch('/ask', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ question: text })
//     });

//     const data = await response.json();
//     typingMsg.remove();
//     addMessage(data.answer || 'Sorry, I couldn’t understand that.', 'ai');
//   } catch (err) {
//     typingMsg.remove();
//     addMessage('Error getting response. Please try again.', 'ai');
//   }

//   userInput.focus();
// });

// // Toggle theme
// themeToggle.addEventListener('click', () => {
//   if (currentTheme === 'light') {
//     currentTheme = 'dark';
//     document.body.classList.remove('light-theme');
//     document.body.classList.add('dark-theme');
//     themeToggle.textContent = '☀️';
//   } else {
//     currentTheme = 'light';
//     document.body.classList.remove('dark-theme');
//     document.body.classList.add('light-theme');
//     themeToggle.textContent = '🌙';
//   }
// });

// // Reset chat
// resetBtn.addEventListener('click', async () => {
//   chatContainer.innerHTML = '';
//   try {
//     await fetch('/reset', { method: 'POST' });
//   } catch (err) {
//     console.error('Reset failed');
//   }
// });

// // Set default theme on page load
// document.body.classList.add('light-theme');
// themeToggle.textContent = '🌙';
















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
