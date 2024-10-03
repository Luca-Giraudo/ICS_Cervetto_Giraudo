<template>
  <div>
      <h2>Perfil de Usuario</h2>
      <form @submit.prevent="updateUserProfile">
          <label>Nombre:</label>
          <input v-model="userProfile.nombre" type="text" />
          
          <label>Localidad:</label>
          <select v-model="userProfile.localidad">
              <option v-for="location in locations" :key="location" :value="location">
                  {{ location }}
              </option>
          </select>
          
          <label>Teléfono:</label>
          <input v-model="userProfile.telefono" type="text" />
          
          <button type="submit">Guardar Cambios</button>
      </form>

      <h2 v-if="!hasCompanyProfile">¿Deseas ofrecer un servicio?</h2>
      <button v-if="!hasCompanyProfile" @click="redirectToCompanyProfileCreate">Crear perfil de empresa</button>

      <div v-if="hasCompanyProfile">
          <h2>Perfil de Empresa</h2>
          <form @submit.prevent="updateCompanyProfile">
              <label>Nombre de Empresa:</label>
              <input v-model="companyProfile.nombre" type="text" />
              
              <label>Descripción:</label>
              <input v-model="companyProfile.descripcion" type="text" maxlength="144" />

              <label>Localidad:</label>
              <select v-model="companyProfile.localidad">
                  <option v-for="location in locations" :key="location" :value="location">
                      {{ location }}
                  </option>
              </select>

              <label>Teléfono:</label>
              <input v-model="companyProfile.telefono" type="text" />
              
              <label>Enlaces Alternos:</label>
              <input v-model="companyProfile.enlaces" type="text" />

              <button type="submit">Guardar Cambios</button>
          </form>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
      return {
          userProfile: {
              nombre: '',
              localidad: '',
              telefono: ''
          },
          companyProfile: {
              nombre: '',
              descripcion: '',
              localidad: '',
              telefono: '',
              enlaces: ''
          },
          hasCompanyProfile: false,
          locations: ['Ciudad A', 'Ciudad B', 'Ciudad C']  // Lista de localidades
      };
  },
  methods: {
      fetchUserProfile() {
          axios.get('/api/perfil-usuario/')
              .then(response => {
                  this.userProfile = response.data;
              });
      },
      updateUserProfile() {
          axios.put('/api/perfil-usuario/', this.userProfile)
              .then(() => {
                  alert('Perfil de usuario actualizado');
              });
      },
      fetchCompanyProfile() {
          axios.get('/api/perfil-empresa/')
              .then(response => {
                  this.companyProfile = response.data;
                  this.hasCompanyProfile = true;
              })
              .catch(() => {
                  this.hasCompanyProfile = false;
              });
      },
      updateCompanyProfile() {
          axios.put('/api/perfil-empresa/', this.companyProfile)
              .then(() => {
                  alert('Perfil de empresa actualizado');
              });
      },
      redirectToCompanyProfileCreate() {
          this.$router.push('/company/create');  // Redirige a la vista para crear el perfil de empresa
      }
  },
  mounted() {
      this.fetchUserProfile();
      this.fetchCompanyProfile();
  }
};
</script>
