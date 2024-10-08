// router.js
/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Welcome from './components/Welcome.vue'
import WelcomeUser from './components/WelcomeUser.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Welcome },
    { path: '/welcome-user', component: WelcomeUser },
    { path: '/login', component: Login },
    { path: '/register', component: Register }
  ]
});
