<template>
<HeaderMenu/>
  <div id="add-menu-container">
      
      <div class="add-page-header">
        <h2>{{ loggedRestaurant }}</h2>
        <p>{{this.date}}</p>
      </div>
    <MenuForm :dictMenu="dict_plates" @changed="onMenuChanged"/>
    <button @click.prevent="onSaveClicked" class="btn">Agregar Menú</button>
  </div>
</template>

<script>
import HeaderMenu from '@/components/HeaderMenu.vue';
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
import MenuForm from "@/components/MenuForm.vue" 
import {getRestaurantName,getRestaurantId} from "@/services/localStorage.js"
export default {
  name: "MenuAdd",
  components:{MenuForm, HeaderMenu},
  data() {
    return {
      date: this.$route.params.date,
      categoryDishes: null,
      nameDish: "",
      allergens: [],
      dict_plates: {
        firsts: [{name_dish:"", allergens:[]}],
        seconds: [{name_dish:"", allergens:[]}],
        desserts: [{name_dish:"", allergens:[]}],
      },
      loggedRestaurant: getRestaurantName(),
    };
  },

  methods: {
    onMenuChanged(newValue){
        this.dict_plates = newValue

    },
    
    areValidInputsFromMenu() {
      if (
        this.dict_plates.firsts.name_dish ||
        this.dict_plates.seconds.name_dish ||
        this.dict_plates.desserts.name_dish
      ) {
        return false;
      } else {
        return true;
      }
    },
    async onSaveClicked() {
      if (this.areValidInputsFromMenu() === true && this.date !== "") {
        let desc = this.dict_plates;
        this.dictToSend = { date: this.date, desc: desc,id_restaurant:getRestaurantId() };
        this.dictToSend.id = uuidv4();
        const settings = {
          method: "POST",
          body: JSON.stringify(this.dictToSend),
          headers: {
            Authorization: getRestaurantId(),
            "Content-Type": "application/json",
          },
        };
        var response = await fetch(`${config.API_PATH}/menus`, settings);

        if (response.status === 200) {
          alert("Menu agregado con éxito!");
          this.$router.push("/menus");
        }
      } else {
        if (this.date === "") {
          alert("Fecha vacía");
        }
        if (this.areValidInputsFromMenu() === false) {
          alert("Inputs vacíos!");
        }
      }
    },
  },
};
</script>
<style scoped>
#add-menu-container{
  padding: 1em;
}
.add-page-header{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 0.8em;
}

</style>