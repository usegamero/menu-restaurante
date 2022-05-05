<template>
<div class="menu-list-page">
  <HeaderMenu/>
  <h2>{{loggedRestaurant}}</h2>
     <button @click="checkMenuTodayExist" class="menu-day-btn btn">Menú del día</button>

    <button @click="changeViewOfMenus" class="menu-day-btn btn" v-if="viewList">Ver calendario</button>
    <button @click="changeViewOfMenus" class="menu-day-btn btn" v-if="viewCalendar">Ver lista</button>
    <Calendar v-if="viewCalendar" />

    <ListOfMenus v-if="viewList" />
   
</div>
</template>

<script>
import HeaderMenu from '@/components/HeaderMenu.vue';
import ListOfMenus from './ListOfMenu.vue'
import Calendar from './Calendar.vue'
import {getRestaurantName} from "@/services/localStorage.js";
import { getMenuToday } from "@/services/api.js";
export default {
  components: {Calendar,ListOfMenus, HeaderMenu},
  data() {
    return {
      loggedRestaurant: getRestaurantName(),
      menuToday : true,
      viewCalendar:true,
      viewList:false,
      
    };
  },
  methods:{
    async  checkMenuTodayExist(){
        const response = await getMenuToday(this.loggedRestaurant)
        if ( response !== 404){
          this.$router.push({ name: 'Menu', params: { date: this.getToday } })
        }else{
          this.$router.push( {name: 'MenuAddPage', params: { date: this.getToday } })
        }
    },
    changeViewOfMenus(){
      if (this.viewList == false && this.viewCalendar){
        this.viewList = true
        this.viewCalendar = false
      }else{
        this.viewCalendar = true
        this.viewList = false
      }
    }
    

  },
  computed: {
      getToday() {
        let current = new Date();
      let year = current.getFullYear();
      let month = current.getMonth() + 1;
      let day = current.getDate();
      if (day < 10) {
        day = "0" + day;
      }
      if (month < 10) {
        month = "0" + month;
      }

      const today = year + "-" + month + "-" + day;
      return today;
    },
  },

};
</script>

<style scoped>

.menu-list-page{
  background-color: #fae8b9;
}
.menu-list-page h2{
  margin: 1.5em 0 1em;
  color: #a31d1e;
  font-size: 1.8em;
  font-weight: normal;
}

.menu-day-btn{
  margin: 0 0.2em;
}
.menu-day-btn:hover{
  background-color:rgb(247, 225, 181);
  color:#a31d1e;
}
@media (min-width:550px){

.menu-list-page h2{
  margin: 1em;
  font-size: 1.4em;
  font-weight: bold;
}

}

</style>