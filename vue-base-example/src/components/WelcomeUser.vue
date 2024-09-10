<template>
  <div v-if="user">
    <h1>Bienvenido, {{ user.first_name }}!</h1>
    <button @click="logout">Cerrar sesión</button>
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
      user: null, // Almacenará los datos del usuario
      loading: true, // Indicador de carga
    };
  },
  async mounted() {
    await this.fetchUserData(); // Al montar el componente, llama a la función para obtener datos
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
        this.user = response.data;
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
        this.$router.push('/'); // Si hay un error, redirige a la página de inicio
      } finally {
        this.loading = false;
      }
    },
    logout() {
      localStorage.removeItem('token'); // Elimina el token de localStorage
      localStorage.removeItem('user');
      this.$router.push('/'); // Redirige a la página Welcome.vue
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