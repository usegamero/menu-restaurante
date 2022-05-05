<template>
    <div class="menus-list">
      <h3>Menus disponibles</h3>
      <ul class="available-menus-list">
        <li class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
          <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
        {{ menu.date }}
        </router-link>
        </li>
      
      </ul>
    </div>
</template>

<script>
import {getListOfMenus} from "@/services/api.js"
export default {
    name : "ListOfMenus",
    data() {
    return {
      listOfMenus : [],
    };
  },
 mounted(){
     this.loadData();
 },
 methods:{
    async loadData(){
         this.listOfMenus = await getListOfMenus()
     }
 }
}
</script>

<style scoped>

.menus-list{
  margin-top: 2em;
}
.menu-date {
  list-style: none;
  text-align: center;
  margin: 1em 0.6em;
  
  
}
.menu-date a{
  color:#a31d1e;
}
.menu-date a:hover{
  font-weight:bold;
}
.available-menus-list{
  display: grid;
  grid-template-columns: 1fr 1fr;
  max-width: 80%;
  margin: 0 auto;
}

@media(min-width:600px) {
  .available-menus-list{
 
  grid-template-columns: 1fr 1fr 1fr;
  max-width: 800px;
 
}

}

</style>