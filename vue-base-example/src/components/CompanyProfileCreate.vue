<template>
  <div>
    <h2>Crear Perfil de Empresa</h2>
    <form @submit.prevent="createCompanyProfile">
      <label>Nombre de Empresa:</label>
      <input v-model="companyProfile.nombre" type="text" required />

      <label>Descripción:</label>
      <textarea v-model="companyProfile.descripcion" maxlength="144" required></textarea>

      <label>Localidad:</label>
      <select v-model="companyProfile.localidad" required>
        <option v-for="location in locations" :key="location" :value="location">
          {{ location }}
        </option>
      </select>

      <label>Teléfono:</label>
      <input v-model="companyProfile.telefono" type="text" required />

      <label>Enlaces Alternos:</label>
      <input v-model="companyProfile.enlaces" type="text" />

      <button type="submit">Crear Perfil de Empresa</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      companyProfile: {
        nombre: '',
        descripcion: '',
        localidad: '',
        telefono: '',
        enlaces: ''
      },
      locations: ['Ciudad A', 'Ciudad B', 'Ciudad C']  // Lista de localidades
    };
  },
  methods: {
    createCompanyProfile() {
      // Realiza la solicitud POST a la API
      axios.post('/api/perfil-empresa/', this.companyProfile)
        .then(() => {
          alert('Perfil de empresa creado exitosamente');
          this.$router.push('/profile');  // Redirige al perfil de usuario después de crear el perfil de empresa
        })
        .catch(error => {
          console.error('Error al crear el perfil de empresa:', error);
          alert('Ocurrió un error al crear el perfil de empresa.');
        });
    }
  }
};
</script>
