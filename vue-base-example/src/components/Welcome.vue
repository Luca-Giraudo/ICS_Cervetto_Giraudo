<template>
  <div class="welcome-container">
    <!-- Nombre de la página "Servipro" arriba a la izquierda -->
    <div class="header">
      <div class="logo-left">
        <h2>Servipro</h2>
      </div>
    </div>

    <!-- Logo del proyecto centrado -->
    <div class="logo-container">
      <img src="@/assets/logocompleto.png" alt="Logo de Servipro" class="project-logo">
    </div>

    <!-- Mensaje de bienvenida -->
    <h1>Bienvenido!</h1>

    <!-- Botones de inicio de sesión y registro -->
    <div class="auth-buttons">
      <button @click="goToLogin">Iniciar sesión</button>
      <router-link to="/register" class="register-link">Regístrate aquí</router-link>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToLogin() {
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.welcome-container {
  position: relative;
  text-align: center;
  padding-top: 10px; /* Reduce el espacio superior */
  min-height: 100vh; /* Asegura que ocupe toda la pantalla */
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Mueve el contenido más arriba */
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 10px; /* Ajusta para reducir el padding superior */
}

.logo-left h2 {
  font-size: 32px;
  font-weight: bold;
  color: #333;
}

.logo-container {
  margin-top: 20px; /* Reduce el margen superior del logo */
}

.project-logo {
  width: 300px;
  height: 300px;
  margin: 10px 0; /* Ajusta el margen para subir el logo */
}

h1 {
  font-size: 28px;
  margin-top: 10px; /* Reduce el margen superior del mensaje de bienvenida */
}

.auth-buttons {
  margin-top: 10px; /* Reduce el espacio entre el mensaje y los botones */
}

.auth-buttons button {
  background-color: transparent;
  border: 2px solid black;
  padding: 10px 20px;
  margin-right: 10px;
  cursor: pointer;
}

.auth-buttons button:hover {
  background-color: #d32f2f;
  color: white;
}

.register-link {
  font-size: 16px;
  text-decoration: none;
  padding: 10px 20px;
  border: 2px solid black;
}

.register-link:hover {
  background-color: #4caf50;
  color: white;
}
</style>
