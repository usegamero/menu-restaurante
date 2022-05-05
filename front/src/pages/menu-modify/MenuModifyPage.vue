<template>
    <HeaderMenu/>
  <form class="add-menu-container">
    <div class="menu-detail-header">
      <div class="header-text-wrapper">
        <h2>{{loggedRestaurant}}</h2>
        <p>Menú del {{ dateParsed() }}</p>
      </div>
      </div>

    <MenuForm :dictMenu="dict_menu.desc" @changed="onMenuChanged" />

    <button @click.prevent="onSaveClicked" class="btn">
      Guardar Menú
    </button>
  </form>
</template>
<script>
import HeaderMenu from '@/components/HeaderMenu.vue';
import config from "@/config.js";
import { getMenuModify } from "@/services/api.js";
import MenuForm from "@/components/MenuForm.vue";
import {getRestaurantName,getRestaurantId} from "@/services/localStorage.js";
export default {
  name: "modifymenu",
  components: { MenuForm, HeaderMenu },
  data() {
    return {
      dateReceived: this.$route.params.date,
      dict_menu: { desc: {} },
      loggedRestaurant:getRestaurantName() ,
      areThereEmpties: true,
    };
  },

  mounted() {
    this.loadData();
  
    
  },

  methods: {
    onMenuChanged(newValue) {
      this.dict_menu.desc = newValue;
    },

    async loadData() {
      this.dict_menu = await getMenuModify();
      return this.dict_menu;
    },
    dateParsed() {
      let completeDate = this.dateReceived;
      let year = completeDate.slice(0, 4);
      let day = completeDate.slice(8, 10);
      let month = completeDate.slice(5, 7);
      return day + "-" + month + "-" + year;
    },
    areValidInputsFromMenu() {
      let platesTot = [];
      let countEmpties = 0;
      for (let plate of this.dict_menu.desc.firsts) {
        let platesFirsts = String(plate.name_dish);
        platesTot.push(platesFirsts);
      }
      for (let plate of this.dict_menu.desc.seconds) {
        let platesSeconds = String(plate.name_dish);
        platesTot.push(platesSeconds);
      }
      for (let plate of this.dict_menu.desc.desserts) {
        let platesDesserts = String(plate.name_dish);
        platesTot.push(platesDesserts);
      }
      for (let dish of platesTot) {
        if (dish === "") {
          countEmpties += 1;
        }
      }
      if (countEmpties === 0) {
        return true;
      } else {
        return false, alert("Hay campos vacios");
      }
    },

    async onSaveClicked() {
      if (this.areValidInputsFromMenu() === true) {
        let desc = this.dict_menu.desc;
        this.dictToSend = {
          date: this.dateReceived,
          desc: desc,
          id: this.dict_menu.id,
          id_restaurant: getRestaurantId(),
        };
        const settings = {
          method: "PUT",
          body: JSON.stringify(this.dictToSend),
          headers: {
            Authorization: getRestaurantId(),
            "Content-Type": "application/json",
          },
        };
        var response = await fetch(`${config.API_PATH}/menus`, settings);
        if (response.status === 200) {
          alert("Menu modificado con éxito!");
          this.$router.push("/menus/by-date/" + this.dateReceived);
        }
      } else {
        this.areThereEmpties = false;
      }
    },

  },
};
</script>
<style scoped>


.add-menu-button {
  padding: 0.5em;
  margin: 2em 0;
}
.menu-detail-header {
  display: flex;
  justify-content: space-between;
  padding: 1.3em 0;
  border-bottom: 1px solid #a31d1e;
  margin: 0 0 1.3em 0;
  align-items: center;
  text-align: left;
}

.dateNameRestaurant {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2em;
}
.add-menu-container{
  padding: 1em;
}
</style>