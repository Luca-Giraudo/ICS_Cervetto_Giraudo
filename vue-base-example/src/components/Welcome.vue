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
  padding-top: 10px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  background-image: url('~@/assets/fondo1.jpg'); /* Usa require para que Webpack gestione la ruta */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 10px; /* Ajusta para reducir el padding superior */
}

.logo-left h2 {
  font-size: 42px;
  font-weight: bold;
  color: #000000;
  font-family: 'Inter', sans-serif;
}

.logo-container {
  margin-top: 20px; /* Reduce el margen superior del logo */
}

.project-logo {
  width: 300px;
  height: 300px;
  margin: 10px 0; /* Ajusta el margen para subir el logo */
  border-radius: 10px;
}

h1 {
  font-size: 28px;
  margin-top: 10px; /* Reduce el margen superior del mensaje de bienvenida */
  font-family: 'Inter', sans-serif;
  background-color: rgba(9, 22, 162, 0.593);
  border-radius: 8px;
  margin-left: auto;
  margin-right: auto;
  width: fit-content;
  font-weight: bold;
  color: #ffffff;
}

.auth-buttons {
  margin-top: 10px; /* Reduce el espacio entre el mensaje y los botones */
}

.auth-buttons button {
  background-color: rgb(5, 0, 93);
  border: 2px solid rgb(255, 255, 255);
  padding: 10px 20px;
  margin-right: 10px;
  cursor: pointer;
  color:#ffffff;
  font-size: 16px;
  font-family: 'Inter', sans-serif;
  font-weight: bold;
}

.auth-buttons button:hover {
  background-color: #db730b;
  color: white;
}

.register-link {
  background-color: rgb(5, 0, 93);
  font-size: 16px;
  border: 2px solid rgb(255, 255, 255);
  padding: 10px 20px;
  margin-right: 10px;
  cursor: pointer;
  color:#ffffff;
  font-family: 'Inter', sans-serif;
  font-weight: bold;
}

.register-link:hover {
  background-color: #db730b;
  color: white;
}
</style>