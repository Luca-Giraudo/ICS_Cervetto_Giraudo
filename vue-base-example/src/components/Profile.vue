<template>
    <div class="profile-container">
      <h1>Perfil de Usuario</h1>
      <form @submit.prevent="updateUser">
        <div>
          <label for="nombre">Nombre:</label>
          <input v-model="nombre" id="nombre" placeholder="Introduce tu nombre" />
        </div>
        <div>
          <label for="localidad">Localidad:</label>
          <input v-model="localidad" id="localidad" placeholder="Introduce tu localidad" />
        </div>
        <div>
          <label for="telefono">Teléfono:</label>
          <input v-model="telefono" id="telefono" placeholder="Introduce tu teléfono" />
        </div>
        <button type="submit">Guardar Cambios</button>
      </form>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        nombre: '',
        localidad: '',
        telefono: ''
      };
    },
    mounted() {
      this.fetchUserData();
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

          // Asignar los valores a los campos, comenzando en blanco
          this.nombre = response.data.perfil_usuario ? response.data.perfil_usuario.nombre || '' : '';
          this.localidad = response.data.perfil_usuario ? response.data.perfil_usuario.localidad || '' : '';
          this.telefono = response.data.perfil_usuario ? response.data.perfil_usuario.telefono || '' : '';
        } catch (error) {
          console.error('Error al obtener los datos del usuario:', error);
        }
      },
      async updateUser() {
        try {
          const token = localStorage.getItem('token');
          await axios.put('http://127.0.0.1:8000/api/profile/', {
            nombre: this.nombre,
            localidad: this.localidad,
            telefono: this.telefono
          }, {
            headers: {
              Authorization: `Token ${token}`,
            },
          });
          alert('Perfil actualizado con éxito');
        } catch (error) {
          console.error('Error al actualizar el perfil:', error);
        }
      }
    }
  };
  </script>

  <style scoped>
  .profile-container {
    max-width: 400px;
    margin: 20px auto;
    text-align: left;
  }
  .profile-container h1 {
    text-align: center;
  }
  .profile-container label {
    display: block;
    margin: 10px 0 5px;
  }
  .profile-container input {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .profile-container button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
  }
  </style>
