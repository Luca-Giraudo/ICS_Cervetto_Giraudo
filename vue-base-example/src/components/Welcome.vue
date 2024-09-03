<template>
    <div class="welcome">
      <h1>Bienvenido</h1>
      <button @click="goToLogin">Iniciar sesión</button>
      <router-link to="/register">Regístrate aquí</router-link>
    </div>
  </template>

  <script>
  export default {
    methods: {
      goToLogin() {
        this.$router.push('/login');
      }
    }
  };
  </script>

  <style scoped>
  .welcome {
    text-align: center;
    margin-top: 50px;
  }
  </style>
