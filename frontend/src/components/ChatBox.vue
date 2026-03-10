<template>
  <div :class="['chat-container', theme]">
    <div class="card chat-card shadow-lg">

      <!-- Header -->
      <div class="card-header d-flex justify-content-between align-items-center bg-gradient">
        <h5 class="mb-0 text-white">AI Chatbot</h5>
        <div class="d-flex gap-2">
          <button class="btn btn-outline-light btn-sm" @click="toggleTheme">
            {{ theme === 'dark' ? 'Light Mode' : 'Dark Mode' }}
          </button>
          <button class="btn btn-outline-warning btn-sm" @click="clearChat">Clear Chat</button>
        </div>
      </div>

      <!-- Chat Messages -->
      <div class="card-body chat-body">
        <div v-for="(msg, index) in messages" :key="index" 
             class="d-flex mb-2" 
             :class="msg.role === 'user' ? 'justify-content-end' : 'justify-content-start'">
          <div :class="['chat-bubble', msg.role === 'user' ? 'user-bubble' : 'ai-bubble']">
            {{ msg.content }}
            <small class="d-block text-muted text-end mt-1">{{ msg.time }}</small>
          </div>
        </div>

        <!-- Typing Animation -->
        <div v-if="isTyping" class="d-flex mb-2 justify-content-start">
          <div class="chat-bubble ai-bubble">
            <em>AI is typing...</em>
          </div>
        </div>

        <div ref="messagesEndRef"></div>
      </div>

      <!-- Input -->
      <div class="card-footer bg-light p-3">
        <div class="input-group">
          <input
            v-model="input"
            @keydown.enter="sendMessage"
            type="text"
            class="form-control"
            placeholder="Type your message..."
          />
          <button class="btn btn-primary" @click="sendMessage">Send</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { ref, reactive, watch } from "vue";
import axios from "axios";

export default {
  setup() {
    const input = ref("");
    const messages = reactive([]);
    const messagesEndRef = ref(null);
    const isTyping = ref(false);

    // Unique user ID per session
    let user_id = localStorage.getItem("user_id");
    if (!user_id) {
      user_id = crypto.randomUUID();
      localStorage.setItem("user_id", user_id);
    }

    // Theme toggle
    const theme = ref(localStorage.getItem("theme") || "dark");
    const toggleTheme = () => {
      theme.value = theme.value === "dark" ? "light" : "dark";
      localStorage.setItem("theme", theme.value);
    };

    // Scroll to bottom on new messages
    const scrollToBottom = () => {
      messagesEndRef.value?.scrollIntoView({ behavior: "smooth" });
    };
    watch(messages, scrollToBottom);

    // Send message to backend
    const sendMessage = async () => {
      if (!input.value) return;

      const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      messages.push({ role: "user", content: input.value, time: timestamp });

      try {
        isTyping.value = true;

        const res = await axios.post("http://127.0.0.1:8000/chat", {
          user_id,
          message: input.value
        });

        isTyping.value = false;

        if (res.data.error) {
          messages.push({ role: "assistant", content: "⚠️ Error: " + res.data.error, time: timestamp });
        } else {
          messages.push({ role: "assistant", content: res.data.response, time: timestamp });
        }

        input.value = "";

      } catch (err) {
        isTyping.value = false;
        messages.push({ role: "assistant", content: "⚠️ Network error", time: timestamp });
      }
    };

    const clearChat = () => {
      messages.splice(0);
    };

    return { input, messages, messagesEndRef, isTyping, sendMessage, clearChat, theme, toggleTheme };
  },
};
</script>

<style scoped>
/* Chat container */
.chat-container {
  background: #1e1e2f;
  padding: 20px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Light theme */
.chat-container.light {
  background: #f5f5f5;
}

/* Chat card */
.chat-card {
  width: 100%;
  max-width: 700px;
  height: 90vh;
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  overflow: hidden;
  background-color: #2c2c3c;
}

/* Light theme card */
.chat-container.light .chat-card {
  background-color: #ffffff;
}

/* Header gradient */
.bg-gradient {
  background: linear-gradient(135deg, #4a90e2, #9013fe);
}

/* Chat body scrollable */
.chat-body {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

/* Chat bubbles */
.chat-bubble {
  padding: 10px 15px;
  border-radius: 20px;
  max-width: 60%;
  word-wrap: break-word;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  font-size: 0.95rem;

  /* fix long messages */
  max-height: 200px;
  overflow-y: auto;
  white-space: pre-wrap;
}

/* User bubble */
.user-bubble {
  background: linear-gradient(135deg, #4a90e2, #0077ff);
  color: #fff;
}

/* AI bubble */
.ai-bubble {
  background: linear-gradient(135deg, #6c6c80, #4a4a60);
  color: #f0f0f0;
}

/* Scrollbar for AI bubble */
.ai-bubble::-webkit-scrollbar {
  width: 6px;
}

.ai-bubble::-webkit-scrollbar-thumb {
  background-color: rgba(255,255,255,0.3);
  border-radius: 3px;
}

/* Light theme bubbles */
.chat-container.light .user-bubble {
  background: linear-gradient(135deg, #0077ff, #4a90e2);
  color: #fff;
}

.chat-container.light .ai-bubble {
  background: #e0e0e0;
  color: #333;
}

/* Input group styling */
.card-footer {
  background: #1e1e2f;
  border-top: 1px solid #444;
}

.chat-container.light .card-footer {
  background: #f5f5f5;
  border-top: 1px solid #ccc;
}

/* Rounded input buttons */
.input-group .form-control {
  border-radius: 25px 0 0 25px;
  border: none;
}

.input-group .btn {
  border-radius: 0 25px 25px 0;
}
</style>