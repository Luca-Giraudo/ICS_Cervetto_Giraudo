<template>
  <div>
    <h2>Registrarse</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <div>
        <label for="confirmPassword">Confirmar Contraseña:</label>
        <input type="password" v-model="confirmPassword" id="confirmPassword" required />
      </div>
      <div>
        <label for="firstName">Nombre:</label>
        <input type="text" v-model="firstName" id="firstName" required />
      </div>
      <div>
        <label for="lastName">Apellido:</label>
        <input type="text" v-model="lastName" id="lastName" required />
      </div>
      <button type="submit">Registrarse</button>
    </form>
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
      confirmPassword: '',
      firstName: '',
      lastName: ''
    };
  },
  methods: {
  async register() {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/register/', {
        email: this.email,
        password: this.password,
        first_name: this.firstName,
        last_name: this.lastName
      });
      console.log('User registered:', response.data);
      // Maneja la respuesta, por ejemplo, redirigiendo al usuario o mostrando un mensaje.
    } catch (error) {
      console.error('Error registering user:', error);
      // Maneja errores de registro.
    }
  }
}
};
</script>

