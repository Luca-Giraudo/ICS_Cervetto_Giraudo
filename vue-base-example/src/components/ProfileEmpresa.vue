<template>
  <div class="empresa-profile-page">
    <!-- Cabecera -->
    <header class="header">
      <h1 class="logo">ServiPro</h1>
    </header>

    <!-- Contenedor del perfil de empresa -->
    <div class="profile-container">
      <!-- Imagen de perfil -->
      <div class="profile-avatar">
        <img src="@/assets/perfilplaceholder.png" alt="Imagen de perfil">
      </div>

      <!-- Formulario de perfil de empresa -->
      <form @submit.prevent="updateEmpresaProfile" class="profile-form">
        <!-- Nombre de la Empresa -->
        <div class="form-group">
          <label for="nombre">Nombre de la Empresa</label>
          <input type="text" v-model="nombre" id="nombre" placeholder="Introduce el nombre de la empresa" />
        </div>

        <!-- Descripción -->
        <div class="form-group">
          <label for="descripcion">Descripción</label>
          <textarea v-model="descripcion" id="descripcion" maxlength="144" placeholder="Introduce una descripción"></textarea>
        </div>

        <!-- Enlaces alternos -->
        <div class="form-group">
          <label for="enlaces">Enlaces alternos</label>
          <input type="text" v-model="enlaces" id="enlaces" placeholder="Introduce enlaces" />
        </div>

        <!-- Localidad -->
        <div class="form-group">
          <label for="localidad">Localidad</label>
          <select v-model="localidad" id="localidad">
            <option value="" disabled>Selecciona tu provincia</option>
            <option v-for="choice in provinceChoices" :value="choice[0]" :key="choice[0]">
              {{ choice[1] }}
            </option>
          </select>
        </div>

        <!-- Teléfono -->
        <div class="form-group">
          <label for="telefono">Teléfono</label>
          <input type="text" v-model="telefono" id="telefono" placeholder="Introduce tu teléfono" />
        </div>

        <!-- Botón de guardar -->
        <button type="submit" class="submit-btn">Guardar Cambios</button>

        <!-- Botón para volver al perfil de usuario -->
        <button type="button" class="usuario-btn" @click="irAPerfilUsuario">
          Volver al Perfil de Usuario
        </button>
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
      descripcion: '',
      enlaces: '',
      localidad: 'X',
      telefono: '',
      provinceChoices: [
        ['B', 'Buenos Aires'], ['K', 'Catamarca'], ['H', 'Chaco'], ['U', 'Chubut'],
        ['C', 'Ciudad Autónoma de Buenos Aires'], ['X', 'Córdoba'], ['W', 'Corrientes'],
        ['E', 'Entre Ríos'], ['P', 'Formosa'], ['Y', 'Jujuy'], ['L', 'La Pampa'],
        ['F', 'La Rioja'], ['M', 'Mendoza'], ['N', 'Misiones'], ['Q', 'Neuquén'],
        ['R', 'Río Negro'], ['A', 'Salta'], ['J', 'San Juan'], ['D', 'San Luis'],
        ['Z', 'Santa Cruz'], ['S', 'Santa Fe'], ['G', 'Santiago del Estero'],
        ['V', 'Tierra del Fuego'], ['T', 'Tucumán']
      ]
    };
  },
  mounted() {
    this.fetchEmpresaData();
  },
  methods: {
    async fetchEmpresaData() {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          throw new Error('Token no encontrado');
        }

        // Obtener datos del perfil de empresa
        const empresaResponse = await axios.get('http://127.0.0.1:8000/api/update-empresa/', {
          headers: {
            Authorization: `Token ${token}`,
          },
        });

        // Si no hay perfil de empresa, obtener datos del perfil de usuario
        if (!empresaResponse.data.perfil.nombre) {
          const userResponse = await axios.get('http://127.0.0.1:8000/api/profile/', {
            headers: {
              Authorization: `Token ${token}`,
            },
          });

          // Copiar los datos del perfil de usuario al perfil de empresa
          this.nombre = userResponse.data.perfil.nombre || '';
          this.localidad = userResponse.data.perfil.localidad || 'X';
          this.telefono = userResponse.data.perfil.telefono || '';
        } else {
          // Si ya hay perfil de empresa, cargar los datos de la empresa
          this.nombre = empresaResponse.data.perfil.nombre;
          this.localidad = empresaResponse.data.perfil.localidad;
          this.telefono = empresaResponse.data.perfil.telefono;
          this.descripcion = empresaResponse.data.perfil.descripcion;
          this.enlaces = empresaResponse.data.perfil.enlaces;
        }
      } catch (error) {
        console.error('Error al obtener los datos del perfil de empresa:', error);
      }
    },
    async updateEmpresaProfile() {
      const token = localStorage.getItem('token');  // Obtener el token
      const data = {
        nombre: this.nombre || '',
        descripcion: this.descripcion || '',
        enlaces: this.enlaces || '',
        localidad: this.localidad || '',
        telefono: this.telefono || ''
      };

      try {
        const response = await axios.put('http://127.0.0.1:8000/api/update-empresa/', { perfil: data }, {
          headers: {
            Authorization: `Token ${token}`  // Incluir el token en el encabezado
          }
        });
        console.log('Perfil de empresa actualizado:', response.data);
      } catch (error) {
        console.error('Error al actualizar el perfil de empresa:', error.response.data);
      }
    },
    irAPerfilUsuario() {
      this.$router.push('/profile');  // Navegar de vuelta al perfil de usuario
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

.form-group input,
.form-group select {
  width: 100%;
  height: 31px;
  padding: 5px;
  border: 2px solid #767676;
  border-radius: 6px;
  background-color: #FFFFFF;
}

.form-group textarea {
  width: 100%;
  padding: 5px;
  border: 2px solid #767676;
  border-radius: 6px;
  background-color: #FFFFFF;
  min-height: 80px;
  resize: vertical;
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

/* Botón de perfil de usuario */
.usuario-btn {
  width: 100%;
  background-color: #1815AA;
  color: white;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

/* Campo adicional de descripción */
.form-group.description-group textarea {
  font-size: 14px;
  line-height: 20px;
}

/* Campo de enlaces */
.form-group.enlaces-group input {
  font-size: 14px;
}
</style>
