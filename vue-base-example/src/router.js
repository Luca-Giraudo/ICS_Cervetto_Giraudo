// router.js
/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Welcome from './components/Welcome.vue';
import WelcomeUser from './components/WelcomeUser.vue';
import Profile from './components/Profile.vue'; // Importa el componente del perfil de usuario
import CompanyProfileCreate from './components/CompanyProfileCreate.vue'; // Importa el componente para crear perfil de empresa

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Welcome },
    { path: '/welcome-user', component: WelcomeUser },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/profile', component: Profile }, // Ruta para el perfil de usuario
    { path: '/company/create', component: CompanyProfileCreate } // Ruta para crear perfil de empresa
  ]
});
