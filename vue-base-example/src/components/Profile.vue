<template>
    <div>
      <h2>Perfil de Usuario</h2>
      <form @submit.prevent="updateUserProfile">
        <label>Nombre:</label>
        <input v-model="userProfile.name" type="text" />
        
        <label>Localidad:</label>
        <select v-model="userProfile.location">
          <option v-for="location in locations" :key="location" :value="location">
            {{ location }}
          </option>
        </select>
        
        <label>Teléfono:</label>
        <input v-model="userProfile.phone" type="text" />
        
        <button type="submit">Guardar Cambios</button>
      </form>
  
      <h2 v-if="!hasCompanyProfile">¿Deseas ofrecer un servicio?</h2>
      <button v-if="!hasCompanyProfile" @click="createCompanyProfile">Crear perfil de empresa</button>
  
      <div v-if="hasCompanyProfile">
        <h2>Perfil de Empresa</h2>
        <form @submit.prevent="updateCompanyProfile">
          <label>Nombre de Empresa:</label>
          <input v-model="companyProfile.company_name" type="text" />
          
          <label>Descripción:</label>
          <input v-model="companyProfile.description" type="text" maxlength="144" />
  
          <label>Localidad:</label>
          <select v-model="companyProfile.location">
            <option v-for="location in locations" :key="location" :value="location">
              {{ location }}
            </option>
          </select>
  
          <label>Teléfono:</label>
          <input v-model="companyProfile.phone" type="text" />
          
          <label>Enlaces Alternos:</label>
          <input v-model="companyProfile.links" type="text" />
  
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
          name: '',
          location: '',
          phone: ''
        },
        companyProfile: {
          company_name: '',
          description: '',
          location: '',
          phone: '',
          links: ''
        },
        hasCompanyProfile: false,
        locations: ['Ciudad A', 'Ciudad B', 'Ciudad C']  // Lista de localidades
      };
    },
    methods: {
      fetchUserProfile() {
        axios.get('/api/user/profile/')
          .then(response => {
            this.userProfile = response.data;
          });
      },
      updateUserProfile() {
        axios.put('/api/user/profile/', this.userProfile)
          .then(() => {
            alert('Perfil de usuario actualizado');
          });
      },
      fetchCompanyProfile() {
        axios.get('/api/company/profile/')
          .then(response => {
            this.companyProfile = response.data;
            this.hasCompanyProfile = true;
          })
          .catch(() => {
            this.hasCompanyProfile = false;
          });
      },
      createCompanyProfile() {
        axios.post('/api/company/profile/', this.companyProfile)
          .then(() => {
            alert('Perfil de empresa creado');
            this.hasCompanyProfile = true;
          });
      },
      updateCompanyProfile() {
        axios.put('/api/company/profile/', this.companyProfile)
          .then(() => {
            alert('Perfil de empresa actualizado');
          });
      }
    },
    mounted() {
      this.fetchUserProfile();
      this.fetchCompanyProfile();
    }
  };
  </script>
  