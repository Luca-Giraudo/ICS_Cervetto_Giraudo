<template>
  <div class="profile-page">
    <!-- Cabecera -->
    <header class="header">
      <h1 class="logo">ServiPro</h1>
    </header>

    <!-- Contenedor del perfil -->
    <div class="profile-container">
      <!-- Imagen de perfil -->
      <div class="profile-avatar">
        <img src="@/assets/perfilplaceholder.png" alt="Imagen de perfil">
      </div>

      <!-- Formulario de perfil -->
      <form @submit.prevent="updateUser" class="profile-form">
        <!-- Nombre -->
        <div class="form-group">
          <label for="nombre">Nombre</label>
          <input type="text" v-model="nombre" id="nombre" placeholder="Introduce tu nombre" />
        </div>

        <!-- Localidad -->
        <div class="form-group">
          <label for="localidad">Localidad</label>
          <select v-model="localidad" id="localidad">
            <option value="" disabled>Selecciona tu provincia</option>
            <option v-for="province in provinceChoices" :key="province" :value="province">
              {{ province }}
            </option>
          </select>
        </div>

        <!-- Teléfono -->
        <div class="form-group">
          <label for="telefono">Teléfono</label>
          <input type="text" v-model="telefono" id="telefono" placeholder="Introduce tu teléfono" />
        </div>

        <!-- Email (no editable) -->
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="email" id="email" readonly />
        </div>

        <!-- Botón de guardar -->
        <button type="submit" class="submit-btn">Guardar Cambios</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      nombre: '',
      localidad: 'Buenos Aires',
      telefono: '',
      email: '',
      descripcion: '',  // Campo adicional para empresa
      enlaces: '',  // Campo adicional para empresa
      isEmpresa: false,  // Nuevo campo para verificar si es empresa
      provinceChoices: [
      'Buenos Aires', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes',
      'Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza',
      'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis',
      'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'
      ]
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem('token');
        console.log('Token:', token);  // Verifica el token
        if (!token) {
          throw new Error('Token no encontrado');
        }
        const response = await axios.get('http://127.0.0.1:8000/api/profile/', {
          headers: {
            Authorization: `Token ${token}`,  // Agregar el token al encabezado
          },
        });

        // Rellenar los datos del formulario con la respuesta
        this.nombre = response.data.perfil ? response.data.perfil.nombre || '' : '';
        this.localidad = response.data.perfil ? response.data.perfil.localidad || '' : '';
        this.telefono = response.data.perfil ? response.data.perfil.telefono || '' : '';
        this.email = response.data.email || ''; // Email no editable
        this.isEmpresa = response.data.perfil.is_empresa || false;  // Verificar si es empresa
        if (this.isEmpresa) {
          this.descripcion = response.data.perfil.descripcion || '';
          this.enlaces = response.data.perfil.enlaces || '';
        }
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
      }
    },
    async updateUser() {
      const token = localStorage.getItem('token');  // Obtener el token

      const data = {
        perfil: {
          nombre: this.nombre || '',
          localidad: this.localidad || '',
          telefono: this.telefono || ''
        }
      };

      if (this.isEmpresa) {
        data.perfil.descripcion = this.descripcion;
        data.perfil.enlaces = this.enlaces;
      }

      try {
        const response = await axios.put('http://127.0.0.1:8000/api/update-profile/', data, {
          headers: {
            Authorization: `Token ${token}`  // Incluir el token en el encabezado
          }
        });
        console.log('Perfil actualizado:', response.data);
      } catch (error) {
        console.error('Error al actualizar el perfil:', error.response.data);
      }
    }
  }
};
</script>


<style scoped>
/* Estilos generales de la página */
.profile-page {
  width: 100%;
  height: 100vh;
  background-color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Cabecera */
.header {
  width: 100%;
  height: 164px;
  background-color: #FFFFFF;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo {
  font-family: 'Inter', sans-serif;
  font-size: 40px;
  font-weight: 500;
  color: #1815AA;
}

/* Contenedor del perfil */
.profile-container {
  width: 300px;
  margin-top: 50px;
  background-color: #FFFFFF;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* Imagen de perfil */
.profile-avatar img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 20px;
}

/* Estilos del formulario */
.profile-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  font-size: 14px;
  color: #1F2937;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  height: 31px;
  padding: 5px;
  border: 2px solid #767676;
  border-radius: 6px;
  background-color: #FFFFFF;
}

.form-group input[readonly] {
  background-color: #F0F0F0;
}

/* Botón de guardar */
.submit-btn {
  width: 100px;
  height: 40px;
  background-color: #1815AA;
  color: #F7F7F7;
  border: none;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 5px 5px 0px #000000;
  margin-top: 20px;
}
</style>
