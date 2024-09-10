<template>
    <div class="welcome-user">
      <h1>Bienvenido, {{ user.first_name }}!</h1>
      <button @click="logout">Cerrar sesión</button>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        user: null, // Aquí se almacenarán los datos del usuario
      };
    },
    mounted() {
      const token = localStorage.getItem('token');
      if (token) {
        axios
          .get('http://127.0.0.1:8000/api/user/', {
            headers: {
              Authorization: `Token ${token}`,
            },
          })
          .then((response) => {
            this.user = response.data;
          })
          .catch((error) => {
            console.error('Error fetching user data:', error);
          });
      }
    },
    methods: {
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        this.$router.push('/'); // Redirige al componente Welcome.vue
      },
    },
  };
  </script>

  <style scoped>
  .welcome-user {
    text-align: center;
    margin-top: 50px;
  }
  </style>
