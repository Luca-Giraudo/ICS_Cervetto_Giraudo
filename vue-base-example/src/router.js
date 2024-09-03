// router.js
import Vue from 'vue';
import Router from 'vue-router';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Welcome from './components/Welcome.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/', component: Welcome }
  ]
});
