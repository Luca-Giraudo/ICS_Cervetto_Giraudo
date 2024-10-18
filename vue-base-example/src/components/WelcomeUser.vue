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

    <div v-if="user" class="content">
      <!-- Logo del proyecto -->
      <div class="logo-container">
        <img src="@/assets/logocompleto.png" alt="Logo de Servipro" class="project-logo">
      </div>

      <!-- Mensaje de bienvenida -->
      <h1>Bienvenido, {{ user.first_name }}!</h1>

      <!-- Botón para ir al perfil -->
      <button @click="goToProfile" class="profile-btn">Ir al Perfil</button>

      <!-- Buscador -->
      <div class="InputContainer">
        <input type="text" class="input" placeholder="Buscar..." />
        <div class="border"></div>
      </div>

      <div class="nav-buttons">
        <button @click="goToWelcomeUser" class="nav-btn">Populares</button>
        <button class="nav-btn">Cercanos</button>
        <button @click="goToFavorites" class="nav-btn">Favoritos</button>
      </div>

      <!-- Populares -->
      <p class="populares-text">🔥 Servicios Populares</p>

      <!-- Listado de empresas en formato de cards -->
      <div class="empresa-list">
        <div v-for="perfil in empresas" :key="perfil.id" class="empresa-card">
          <!-- Botón de favoritos -->
          <button @click="toggleFavorito(perfil.id)" class="favorito-btn"></button>

          <img :src="perfil.imagen ? perfil.imagen : require('@/assets/perfilplaceholder.png')" alt="Imagen de empresa" class="empresa-avatar" />
          <div class="empresa-details">
            <h3>{{ perfil.nombre }}</h3>
            <p>{{ perfil.descripcion }}</p>
          </div>
        </div>
      </div>

      <!-- Paginación -->
      <div class="pagination">
        <button @click="cambiarPagina('prev')" :disabled="!paginacion.previous">Anterior</button>
        <button @click="cambiarPagina('next')" :disabled="!paginacion.next">Siguiente</button>
      </div>
    </div>

    <!-- Mensaje si no está logueado -->
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
      loading: true,
      empresas: [],
      paginacion: {
        next: null,
        previous: null,
      },
    };
  },
  async mounted() {
    await this.fetchUserData();
    await this.fetchEmpresas();
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
        this.$router.push('/');
      } finally {
        this.loading = false;
      }
    },
    async fetchEmpresas(url = 'http://127.0.0.1:8000/api/empresas/') {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get(url, {
          headers: {
            Authorization: `Token ${token}`,
          },
        });
        console.log('Empresas:', response.data.results);
        this.empresas = response.data.results.map(empresa => ({
          ...empresa,
          imagen: `http://127.0.0.1:8000${empresa.imagen}`  // Construir la URL completa de la imagen
        }));
        this.paginacion.next = response.data.next;
        this.paginacion.previous = response.data.previous;
      } catch (error) {
        console.error('Error al obtener los perfiles de empresa:', error);
      }
    },
    cambiarPagina(direccion) {
      const url = direccion === 'next' ? this.paginacion.next : this.paginacion.previous;
      if (url) {
        this.fetchEmpresas(url);
      }
    },
    irAlPerfilDeEmpresa(empresaId) {
      this.$router.push(`/empresa-profile/${empresaId}`);
    },
    logout() {
      localStorage.removeItem('token');
      this.user = null;
      this.$router.push('/');
    },
    goToProfile() {
      this.$router.push('/profile');
    },
    goToWelcomeUser() {
      this.$router.push('/welcome-user');
    },
    goToFavorites() {
      this.$router.push('/favorites');
    },
    async toggleFavorito(perfil_id) {
      console.log('ID del perfil:', perfil_id); // Verificar si el ID está siendo capturado correctamente
      if (!perfil_id) {
        console.error('Error: El perfil_id es undefined');
        return;
      }
      try {
        const response = await axios.post(`http://127.0.0.1:8000/api/favorito/${perfil_id}/`, {}, {
          headers: {
            Authorization: `Token ${localStorage.getItem('token')}`
          }
        });
        console.log(response.data.message);
        this.fetchEmpresas(); // Refrescar la lista de empresas para mostrar el cambio en los favoritos
      } catch (error) {
        console.error('Error al agregar/quitar favorito:', error);
      }
    },
  }
};
</script>

<style scoped>
/* Estilos ajustados al diseño que proporcionaste */
.welcome-container {
  width: 100%;
  min-height: 100vh; /* Asegura que la altura mínima sea la del viewport */
  background-image: url('~@/assets/fondo1.jpg'); /* Ruta de la imagen de fondo */
  background-size: cover; /* Asegura que la imagen cubra todo el fondo */
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed; /* Mantiene la imagen de fondo fija durante el scroll */
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* Asegura que el contenido esté arriba */
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

.content h1 {
  font-family: 'Inter', sans-serif;
  background-color: rgba(9, 22, 162, 0.593);
  border-radius: 8px;
  color: white;
  width: fit-content;
  font-weight: bold;
}

.project-logo {
  width: 300px;
  height: 300px;
  border-radius: 10px;
}

.InputContainer {
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  padding-left: 15px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.075);
  margin-top: 10%;
  width: 300px; /* Ajustar el ancho para que coincida con el logo */
  border-color: black;
}

.input {
  width: 170px;
  height: 100%;
  border: none;
  outline: none;
  font-size: 0.9em;
  caret-color: rgb(255, 81, 0);
}

.labelforsearch {
  cursor: text;
  padding: 0px 12px;
}

.searchIcon {
  width: 13px;
}

.searchIcon path {
  fill: rgb(114, 114, 114);
}

.profile-btn {
  background-color: rgb(5, 0, 93);
  border: 2px solid rgb(255, 255, 255);
  border-radius: 10px;
  padding: 10px 20px;
  cursor: pointer;
  color: white;
  font-size: 16px
}

.profile-btn:hover {
  background-color: #db730b;
  color: white;
}

.nav-buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 15px;
}

.nav-btn {
  background-color: rgb(5, 0, 93);
  color: white;
  border: 2px solid rgb(255, 255, 255);
  border-radius: 10px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
}

.nav-btn:hover {
  background-color: #db730b;
  color: white;
}

.populares-text {
  font-size: 20px;
  margin-top: 60px;
  margin-left: 120px;
  font-family: 'Inter', sans-serif;
  font-weight: bold;
  color: white;
  background-color: rgba(9, 22, 162, 0.593);
  border-radius: 8px;
  width: fit-content;
  text-align: left;
  align-self: flex-start;
}

.empresa-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 1282px;
  margin-top: 50px;
}

.empresa-card {
  margin-top: 0.005px;
  position: relative;
  width: 404px;
  height: 376px;
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
  margin-top: 0.00001%;
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
  content: '★'; /* Estrella de favorito */
  position: absolute;
  font-size: 20px;
  color: #DEC543;
  top: 12px;
  left: 15px;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
}
</style>
