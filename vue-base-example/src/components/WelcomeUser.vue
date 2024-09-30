<template>
  <div v-if="!loading" class="welcome-container">
    <!-- Nombre de la página "Servipro" arriba a la izquierda -->
    <div class="header">
      <div class="logo-left">
        <h2>Servipro</h2>
      </div>

      <!-- Botón de cerrar sesión centrado arriba -->
      <div class="logout-center">
        <button @click="logout">Cerrar sesión</button>
      </div>
    </div>

    <div v-if="user" class="content">
      <!-- Logo del proyecto centrado -->
      <div class="logo-container">
        <img src="@/assets/logocompleto.png" alt="Logo de Servipro" class="project-logo">
      </div>

      <!-- Mensaje de bienvenida con el nombre del usuario -->
      <h1>Bienvenido, {{ user.first_name }}!</h1>

      <!-- Barra de búsqueda centrada -->
      <div class="search-bar">
        <input type="text" class="input" placeholder="Buscar...">
        <span class="icon">🔍</span>
      </div>

      <!-- Botón para ir al perfil -->
      <button @click="goToProfile" class="profile-btn">Ir al Perfil</button>

      <!-- Texto de "🔥Populares" pegado a la izquierda -->
      <p class="populares-text">🔥 Populares</p>
    </div>

    <!-- Mensaje en caso de no estar logueado -->
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
      user: null,
      loading: true
    };
  },
  async mounted() {
    await this.fetchUserData();
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
        console.log('Datos del usuario:', response.data);
        this.user = response.data;
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
        this.$router.push('/');
      } finally {
        this.loading = false;
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.user = null;
      this.$router.push('/');
    },
    goToProfile() {
      this.$router.push('/profile');  // Redirige a la página de perfil
    },
  },
};
</script>

<style scoped>
.welcome-container {
  position: relative;
  text-align: center;
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 5px;
}

.logo-left h2 {
  font-size: 32px;
  font-weight: bold;
  color: #333;
}

.logout-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.logout-center button {
  background-color: transparent;
  border: 2px solid black;
  padding: 10px 20px;
  cursor: pointer;
}

.logout-center button:hover {
  background-color: #d32f2f;
}

.content {
  margin-top: 25px;
}

.project-logo {
  width: 300px;
  height: 300px;
  margin: 20px 0;
}

.search-bar {
  margin-top: 20px;
  width: 280px;
  position: relative;
  margin: 0 auto;
}

.profile-btn {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  margin-top: 20px;
}

.profile-btn:hover {
  background-color: #45a049;
}

.input-container {
  margin-top: 20px;
  width: 220px;
  position: relative;
  margin: 0 auto;
}

.input {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 2.5px solid black;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.input:focus {
  outline: none;
  border: 0.5px solid black;
  box-shadow: -5px -5px 0px black;
}

.icon {
  position: absolute;
  right: 10px;
  top: calc(50% + 5px);
  transform: translateY(calc(-50% - 5px));
}

.input-container:hover > .icon {
  animation: anim 1s linear infinite;
}

@keyframes anim {
  0%, 100% {
    transform: translateY(calc(-50% - 5px)) scale(1);
  }
  50% {
    transform: translateY(calc(-50% - 5px)) scale(1.1);
  }
}

.populares-text {
  text-align: left;
  margin-top: 30px;
  margin-left: 20px;
  font-size: 20px;
}
</style>
