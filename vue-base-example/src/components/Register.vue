<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <div>
          <label for="email">Email:</label>
          <input type="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <div>
          <label for="confirmPassword">Confirm Password:</label>
          <input type="password" v-model="confirmPassword" required />
        </div>
        <div>
          <label for="firstName">First Name:</label>
          <input type="text" v-model="firstName" required />
        </div>
        <div>
          <label for="lastName">Last Name:</label>
          <input type="text" v-model="lastName" required />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>

  <script>
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
      register() {
        // Lógica para enviar datos al backend usando Axios o Fetch
      }
    }
  };
  </script>
