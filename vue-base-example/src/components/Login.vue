<template>
  <div class="login-box">
    <p>Iniciar Sesión</p>
    <form @submit.prevent="login">
      <div class="user-box">
        <input type="email" v-model="email" required />
        <label for="email">Email</label>
      </div>
      <div class="user-box">
        <input type="password" v-model="password" required />
        <label for="password">Contraseña</label>
      </div>
      <a href="#" @click="login">Iniciar Sesión
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </a>
    </form>
    <p v-if="error" class="error">{{ error }}</p> <!-- Muestra el mensaje de error -->
    <p>¿No tienes cuenta? <router-link to="/register" class="a2">Regístrate aquí</router-link></p>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: null, // Para manejar el mensaje de error
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          email: this.email,
          password: this.password
        });

        // Guarda el token y la información del usuario en localStorage
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', JSON.stringify(response.data.user));

        // Redirige a la página principal (WelcomeUser)
        this.$router.push('/welcome-user');
      } catch (error) {
        console.error('Error logging in:', error);
        if (error.response && error.response.status === 400) {
          this.error = "Credenciales incorrectas. Inténtalo de nuevo.";
        } else {
          this.error = "Hubo un problema al iniciar sesión. Inténtalo más tarde.";
        }
      }
    }
  }
};
</script>

<style scoped>
/* Estilos de Uiverse.io */
.login-box {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  padding: 40px;
  margin: 20px auto;
  transform: translate(-50%, -55%);
  background: rgba(0,0,0,.9);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  border-radius: 10px;
}

.login-box p:first-child {
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}

.login-box .user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #fff;
  font-size: 12px;
}

.login-box form a {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  font-weight: bold;
  color: #fff;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 40px;
  letter-spacing: 3px
}

.login-box a:hover {
  background: #fff;
  color: #272727;
  border-radius: 5px;
}

.login-box a span {
  position: absolute;
  display: block;
}

.login-box a span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #fff);
  animation: btn-anim1 1.5s linear infinite;
}

@keyframes btn-anim1 {
  0% {
    left: -100%;
  }

  50%,100% {
    left: 100%;
  }
}

.login-box a span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, #fff);
  animation: btn-anim2 1.5s linear infinite;
  animation-delay: .375s
}

@keyframes btn-anim2 {
  0% {
    top: -100%;
  }

  50%,100% {
    top: 100%;
  }
}

.login-box a span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, #fff);
  animation: btn-anim3 1.5s linear infinite;
  animation-delay: .75s
}

@keyframes btn-anim3 {
  0% {
    right: -100%;
  }

  50%,100% {
    right: 100%;
  }
}

.login-box a span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, #fff);
  animation: btn-anim4 1.5s linear infinite;
  animation-delay: 1.125s
}

@keyframes btn-anim4 {
  0% {
    bottom: -100%;
  }

  50%,100% {
    bottom: 100%;
  }
}

.error {
  color: red;
  margin-top: 10px;
}

.login-box p:last-child {
  color: #aaa;
  font-size: 14px;
}

.login-box a.a2 {
  color: #fff;
  text-decoration: none;
}

.login-box a.a2:hover {
  background: transparent;
  color: #aaa;
  border-radius: 5px;
}
</style>