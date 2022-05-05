<template>
  <div class="home">
    <img alt="menu logo" src="@/assets/img/logo-restaurant.png" />
    <h1>Bienvenido</h1>
  

  
    <div class="login-wrapper">
      <label for="user-name">Usuario</label>
      <input type="text" id="user-name" v-model="restaurants.id_restaurant">
    
      <label for="password">Contraseña</label>
      <input type="password" id="password" v-model="restaurants.password" @keyup.enter="onButtonClicked">
      
      <button @click="onButtonClicked()" @keyup.enter="onButtonClicked" class="btn login-btn">Acceder</button> 
    </div>
    
  </div>
    

</template>

<script>

import { login } from "@/services/auth.js";
import { useStorage } from "@vueuse/core";


export default {
  name: 'Home',
  data(){
    return{
      restaurants:[],
      selectedRestaurant:null,
      auth: useStorage("auth", {}),
      
    }
  },
  
  methods:{
    
    async onButtonClicked(){
      const response = await login(this.restaurants.id_restaurant, this.restaurants.password);
      const loginStatus = response.status;
      console.log("response", response);

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        const auth = await response.json();
        console.log("auth", auth);

        this.auth = auth;

      this.$router.push('/menus')
      }
    }
  },
}
</script>

<style scoped>
.home{
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  
}
.home h1{
  font-size: 2.5em;
  font-weight: normal;
  color: #a31d1e;
} 
.home .login-wrapper{
  font-size: 1.2em;
  font-weight: bold;
  height: 30vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.home .login-wrapper input{
  border: none;
  box-shadow: 0px 0px 8px 0px rgb(247, 225, 181) inset;
  padding: 0.5em 0.2em;
  margin-top: 0.3em;
  font-family: "Ubuntu", sans-serif;
  font-size: 1em;

}

.login-wrapper{
  display: flex;
  flex-direction: column;
  max-width: 300px;
 
}

@media (min-width:550px){

  .home{
    max-width: 300px;
    margin: 0 auto;
    font-size: 0.8rem;
  }

}


</style>
