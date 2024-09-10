<template>
    <div>
      <h2>Iniciar Sesion</h2>
      <form @submit.prevent="login">
        <div>
          <label for="email">Email:</label>
          <input type="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Contraseña:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Iniciar Sesion</button>
      </form>
      <router-link to="/register">No tienes cuenta? Regístrate aquí</router-link>
    </div>
  </template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
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

        // Redirige a la página principal (Welcome)
        this.$router.push('/welcome-user');
      } catch (error) {
        console.error('Error logging in:', error);
        // Muestra un mensaje de error o maneja el error
      }
    }
  }
};
</script>

