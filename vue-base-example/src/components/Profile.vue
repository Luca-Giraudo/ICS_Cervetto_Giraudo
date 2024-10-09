<template>
  <div class="profile-page">
    <!-- Cabecera -->
    <header class="header">
      <h1 class="logo">ServiPro</h1>
    </header>

    <!-- Contenedor del perfil -->
    <div class="profile-container">

      <!-- Imagen de perfil -->
      <div class="profile-avatar" @click="triggerFileInput">
        <img :src="imageUrl" alt="Imagen de perfil" />
        <input type="file" ref="fileInput" @change="onFileSelected" style="display: none;" />
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
            <option v-for="choice in provinceChoices" :value="choice[0]" :key="choice[0]" >
              {{ choice[1] }}
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

        <button type="button" class="empresa-btn" @click="irAPerfilEmpresa">
          Crear/Modificar Perfil de Empresa
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
      localidad: 'X',
      telefono: '',
      email: '',
      descripcion: '',  // Campo adicional para empresa
      enlaces: '',  // Campo adicional para empresa
      imageUrl: require('@/assets/perfilplaceholder.png'),  // Placeholder para la imagen de perfil
      imageFile: null,
      isEmpresa: false,  // Campo para verificar si es empresa
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
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem('token');
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
        this.localidad = response.data.perfil ? response.data.perfil.localidad || 'X' : 'X';
        this.telefono = response.data.perfil ? response.data.perfil.telefono || '' : '';
        this.email = response.data.email || '';
        this.imageUrl = response.data.perfil.imagen || '@/assets/perfilplaceholder.png';  // Establecer imagen
        this.isEmpresa = response.data.perfil.is_empresa || false;
        if (this.isEmpresa) {
          this.descripcion = response.data.perfil.descripcion || '';
          this.enlaces = response.data.perfil.enlaces || '';
        }
      } catch (error) {
        console.error('Error al obtener los datos del usuario:', error);
      }
    },

    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    onFileSelected(event) {
      const file = event.target.files[0];
      this.imageFile = file;
      this.imageUrl = URL.createObjectURL(file);  // Mostrar vista previa de la imagen
    },

    async updateUser() {
      const token = localStorage.getItem('token');  // Obtener el token
      const formData = new FormData();  // Usar FormData para manejar imágenes y otros datos

      formData.append('nombre', this.nombre || '');
      formData.append('localidad', this.localidad || '');
      formData.append('telefono', this.telefono || '');

      // Si hay un archivo de imagen seleccionado, adjuntarlo al formulario
      if (this.imageFile) {
        formData.append('imagen', this.imageFile);
      }

      // Si el usuario es una empresa, agregar los campos correspondientes
      if (this.isEmpresa) {
        formData.append('descripcion', this.descripcion || '');
        formData.append('enlaces', this.enlaces || '');
      }

      try {
        const response = await axios.put('http://127.0.0.1:8000/api/update-profile/', formData, {
          headers: {
            Authorization: `Token ${token}`,  // Incluir el token en el encabezado
            'Content-Type': 'multipart/form-data',  // Importante para subir archivos
          }
        });
        console.log('Perfil actualizado:', response.data);
      } catch (error) {
        console.error('Error al actualizar el perfil:', error.response.data);
      }
    },
    irAPerfilEmpresa() {
      this.$router.push('/empresa-profile'); // Navegación al componente de perfil de empresa
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

/* Botón de empresa */
.empresa-btn {
  width: 100%;
  background-color: #1815AA;
  color: white;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
