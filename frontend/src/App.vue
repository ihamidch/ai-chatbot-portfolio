<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-dark bg-primary p-3">
      <span class="navbar-brand mb-0 h1">AI Chatbot</span>
    </nav>

    <!-- ChatBox component -->
    <ChatBox />
  </div>
</template>

<script>
import ChatBox from './components/ChatBox.vue'

export default {
  name: 'App',
  components: {
    ChatBox
  }
}
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>