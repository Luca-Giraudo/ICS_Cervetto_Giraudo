<template>
  <div v-if="!loading" class="welcome-container">
    <!-- Header -->
    <div class="header">
      <div class="logo-left">
        <h2>Servipro</h2>
      </div>
      <div class="logout-center">
        <button @click="logout">Cerrar sesión</button>
      </div>
    </div>

    <div class="content">
      <!-- Logo del proyecto -->
      <div class="logo-container">
        <img src="@/assets/logocompleto.png" alt="Logo de Servipro" class="project-logo">
      </div>

      <!-- Mensaje de Favoritos -->
      <h1>Favoritos de {{ user.first_name }}</h1>

      <!-- Listado de favoritos en formato de cards -->
      <div class="empresa-list">
        <div v-for="perfil in favoritos" :key="perfil.id" class="empresa-card">
          <!-- Botón de eliminar de favoritos -->
          <button @click="toggleFavorito(perfil.id)" class="favorito-btn"></button>

          <img :src="perfil.imagen ? perfil.imagen : require('@/assets/perfilplaceholder.png')" alt="Imagen de perfil" class="empresa-avatar" />
          <div class="empresa-details">
            <h3>{{ perfil.nombre }}</h3>
            <p>{{ perfil.descripcion }}</p>
          </div>
        </div>
      </div>
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
      user: null,
      favoritos: [],
      loading: true,
    };
  },
  async mounted() {
    await this.fetchUserData();
    await this.fetchFavoritos();
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:8000/api/user/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        this.user = response.data;
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
      }
    },
    async fetchFavoritos() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:8000/api/favoritos/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        this.favoritos = response.data.favoritos.map(favorito => ({
          ...favorito,
          imagen: favorito.imagen ? `http://127.0.0.1:8000${favorito.imagen}` : require('@/assets/perfilplaceholder.png'),
        }));
      } catch (error) {
        console.error('Error al obtener los favoritos:', error);
      } finally {
        this.loading = false;
      }
    },
    async toggleFavorito(perfil_id) {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.post(`http://127.0.0.1:8000/api/favorito/${perfil_id}/`, {}, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        console.log(response.data.message);
        await this.fetchFavoritos(); // Refrescar la lista de favoritos
      } catch (error) {
        console.error('Error al eliminar de favoritos:', error);
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
/* Estilos idénticos a los de welcome-user */
.welcome-container {
  width: 100%;
  min-height: 100vh;
  background-image: url('~@/assets/fondo1.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 5px;
}

.logo-left h2 {
  font-size: 42px;
  font-weight: bold;
  font-family: 'Inter', sans-serif;
  color: black;
}

.logout-center button {
  background-color: rgb(5, 0, 93);
  border: 2px solid rgb(255, 255, 255);
  border-radius: 10px;
  padding: 10px 20px;
  cursor: pointer;
  color: white;
  font-size: 16px;
}

.logout-center button:hover {
  background-color: #db730b;
  color: white;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 25px;
}

.project-logo {
  width: 300px;
  height: 300px;
  border-radius: 10px;
}

.empresa-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 1282px;
  margin-top: 50px;
}

.empresa-card {
  position: relative;
  width: 404px;
  height: 366px;
  border-radius: 8px;
  background: #F7F7F7;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 24px;
  cursor: pointer;
  background-color: #b9c4c6;
}

.empresa-avatar {
  width: 364px;
  height: 250px;
  border-radius: 8px;
}

.empresa-details {
  margin-top: 10px;
  text-align: left;
  font-family: 'Inter', sans-serif;
  color: black;
}

.favorito-btn {
  position: absolute;
  width: 45px;
  height: 45px;
  top: 10px;
  right: 10px;
  background: #F7F7F7;
  border: 2.1px solid #000000;
  border-radius: 10px;
  cursor: pointer;
}

.favorito-btn::before {
  content: '★';
  position: absolute;
  font-size: 20px;
  color: #DEC543;
  top: 12px;
  left: 15px;
}
</style>
