<template>
  <div v-if="!loading">
    <div v-if="user">
      <h1>Bienvenido, {{ user.first_name }}!</h1>
      <button @click="logout">Cerrar sesión</button>
    </div>
    <div v-else>
      <h1>Inicia sesión o regístrate</h1>
      <router-link to="/login">Iniciar sesión</router-link> |
      <router-link to="/register">Regístrate</router-link>
    </div>
  </div>
  <div v-else>
    <h1>Cargando...</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: null, // Almacena datos del usuario
      loading: true // Controla el estado de carga
    };
  },
  async mounted() {
    await this.fetchUserData(); // Llama a la función para obtener los datos del usuario al montar
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          throw new Error('Token no encontrado');
        }
        const response = await axios.get('http://127.0.0.1:8000/api/user/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        console.log('Datos del usuario:', response.data); // Agregado para ver los datos del usuario
        this.user = response.data; // Asigna los datos del usuario
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
        this.$router.push('/'); // Redirige a la página de bienvenida si hay error
      } finally {
        this.loading = false; // Cambia el estado de carga
      }
    },
    logout() {
      localStorage.removeItem('token'); // Elimina el token al cerrar sesión
      this.user = null; // Borra los datos del usuario
      this.$router.push('/'); // Redirige a la página de bienvenida
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
