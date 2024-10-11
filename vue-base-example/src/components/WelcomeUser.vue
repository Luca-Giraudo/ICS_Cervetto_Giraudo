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

      <!-- Buscador -->
      <div class="search-bar">
        <input type="text" class="input" placeholder="Buscar...">
        <span class="icon">🔍</span>
      </div>

      <!-- Botón para ir al perfil -->
      <button @click="goToProfile" class="profile-btn">Ir al Perfil</button>

      <!-- Populares -->
      <p class="populares-text">🔥 Populares</p>

      <!-- Listado de empresas en formato de cards -->
      <div class="empresa-list">
        <div v-for="empresa in empresas" :key="empresa.id" class="empresa-card" @click="irAlPerfilDeEmpresa(empresa.id)">
          <img :src="empresa.imagen ? empresa.imagen : require('@/assets/perfilplaceholder.png')" alt="Imagen de empresa" class="empresa-avatar" />
          <div class="empresa-details">
            <h3>{{ empresa.nombre }}</h3>
            <p>{{ empresa.descripcion }}</p>
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
  },
};
</script>

<style scoped>
/* Estilos ajustados al diseño que proporcionaste */
.welcome-container {
  width: 1440px;
  height: 1024px;
  background: #FFFFFF;
}

.header {
  display: flex;
  justify-content: space-between;
  padding: 5px;
}

.logo-left h2 {
  font-size: 32px;
  font-weight: bold;
  color: #1815AA;
}

.logout-center button {
  background-color: transparent;
  border: 2px solid black;
  padding: 10px 20px;
  cursor: pointer;
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
}

.search-bar {
  margin-top: 20px;
  width: 280px;
  position: relative;
}

.profile-btn {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  margin-top: 20px;
}

.populares-text {
  font-size: 20px;
  color: #1815AA;
}

.empresa-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 1282px;
  margin-top: 50px;
}

.empresa-card {
  width: 404px;
  height: 366px;
  border-radius: 8px;
  background: #F7F7F7;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 24px;
  cursor: pointer;
}

.empresa-avatar {
  width: 404px;
  height: 250px;
  border-radius: 8px;
}

.empresa-details {
  margin-top: 10px;
  text-align: left;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
