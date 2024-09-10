<template>
  <div>
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Iniciar Sesión</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p> <!-- Muestra el mensaje de error -->
    <router-link to="/register">¿No tienes cuenta? Regístrate aquí</router-link>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: null, // Para manejar el mensaje de error
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          email: this.email,
          password: this.password
        });

        // Guarda el token y la información del usuario en localStorage
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', JSON.stringify(response.data.user));

        // Redirige a la página principal (WelcomeUser)
        this.$router.push('/welcome-user');
      } catch (error) {
        console.error('Error logging in:', error);
        if (error.response && error.response.status === 400) {
          this.error = "Credenciales incorrectas. Inténtalo de nuevo.";
        } else {
          this.error = "Hubo un problema al iniciar sesión. Inténtalo más tarde.";
        }
      }
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
  margin-top: 10px;
}
</style>
