<template>
  <HeaderMenu />
  <main class="main-menu-detail-wrapper">
    <header class="menu-detail-header">
      <div class="header-text-wrapper">
        <h2>{{ loggedRestaurant }}</h2>
        <p>Menú del {{ dateParsed }}</p>
      </div>
      <div class="buttons-wrapper">
        <router-link
          :to="{
            name: 'MenuModifyPage',
            params: { date: this.$route.params.date },
          }"
        >
          <button @click="saveMenuId" class="btn">Modificar menu</button>
        </router-link>
        <button class="btn" @click="copyModalClicked">Copiar Menu</button>
        <router-link  v-if="date === getToday" :to="{name:'MenuToday',params:{name_restaurant:loggedRestaurant}}">
          <button class="btn">Compartir</button>
        </router-link>
      </div>
    </header>

    <section class="courses-wrapper">
      <h3>Primeros</h3>
      <ul v-for="menu in this.firsts" :key="menu.id_dish">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>

    <section class="courses-wrapper">
      <h3>Segundos</h3>
      <ul v-for="menu in this.seconds" :key="menu.id_dish">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>

    <section class="courses-wrapper">
      <h3>Postres</h3>
      <ul v-for="menu in this.desserts" :key="menu.id_dish">
        <li>{{ menu.name_dish }}</li>
        <li
          class="allergen-detail"
          v-for="allergen in menu.allergens"
          :key="allergen.id"
        >
          <img
            alt="allergensIcons.lactose"
            :src="
              require('@/assets/img/allergens_icons/' +
                allergensIcons[allergen])
            "
          />
        </li>
      </ul>
    </section>
    <source />
  </main>

  <SelectDateCopyMenu
    v-show="modalOpened"
    @changedDate="copyMenu"
    @modaltoFALSE="modaltoFalse()"
  />
</template>

<script>
import HeaderMenu from "@/components/HeaderMenu.vue";
import { getMenuByDate } from "@/services/api.js";
import SelectDateCopyMenu from "@/pages/menu-add/SelectDateCopyMenu.vue";
import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";
import { getRestaurantName, getRestaurantId } from "@/services/localStorage.js";

export default {
  components: { SelectDateCopyMenu, HeaderMenu },
  data() {
    return {
      allergensIcons: {
        lactose: "lactose.png",
        gluten: "gluten.png",
        egg: "egg.png",
        seafood: "seafood.png",
        soy: "soy.png",
        nuts: "nut.png",
      },
      firsts: [],
      seconds: [],
      desserts: [],
      date: this.$route.params.date,
      dateToCopy: "",
      parsedDate: "",
      loggedRestaurant: getRestaurantName(),
      menu: {},
      modalOpened: false,
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {
    async copyMenu(newDate) {
      this.dateToCopy = newDate;
      let desc = this.menu.desc;
      this.dictToSend = {
        date: this.dateToCopy,
        desc: desc,
        id_restaurant: getRestaurantId(),
      };
      this.dictToSend.id = uuidv4();
      localStorage.id_menu = this.dictToSend.id;

      const settings = {
        method: "POST",
        body: JSON.stringify(this.dictToSend),
        headers: {
          Authorization: getRestaurantId(),
          "Content-Type": "application/json",
        },
      };
      await fetch(
        `${config.API_PATH}/menus/${this.date}/copy/${this.dateToCopy}`,
        settings
      );
    },
    async loadData() {
      this.menus = await getMenuByDate(this.date);

      this.firsts = this.menus.desc.firsts;
      this.seconds = this.menus.desc.seconds;
      this.desserts = this.menus.desc.desserts;
    },
    saveMenuId() {
      localStorage.id_menu = this.menus.id;
    },
    copyModalClicked() {
      this.modalOpened = true;
      console.log("clicc modal" + this.modalOpened);
    },

    modaltoFalse(newvalue) {
      this.modalOpened = newvalue;
    },
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
    dateParsed() {
      let year = this.date.slice(0, 4);
      let day = this.date.slice(8, 10);
      let month = this.date.slice(5, 7);
      let months = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
      };
      let fullDate = day + " de " + months[month] + " de " + year;
      return fullDate;
    },
  },
};
</script>

<style scoped>
.main-menu-detail-wrapper {
  text-align: left;
  padding-bottom: 3em;
}
.courses-wrapper {
  margin-bottom: 2em;
  font-family: "Oswald", sans-serif;
  font-size: 1em;
  text-align: center;
  color: #3b0b06;
  letter-spacing: 0.1em;
}
.courses-wrapper h3 {
  font-weight: 500;
  margin: 1.5em 0 1em;
}
.courses-wrapper li {
  font-weight: 300;
  margin-top: 0.4em;
  
}
.allergen-detail {
  font-size: 11px;
  font-style: italic;
  display: inline;
}
.allergen-detail img{
  width: 6%;
  margin-right: 0.5em;
}
.buttons-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.buttons-wrapper .btn {
  padding: 0.3em 0.2em;
  font-weight: normal;
  display: block;
  width: 8em;
  font-size: 0.8em;
  margin-top: 0.2em;
}
.menu-detail-header {
  display: flex;
  justify-content: space-between;
  padding: 1.3em 0;
  border-bottom: 1px solid #a31d1e;
  margin: 0 0 1.3em 0;
  align-items: center;
}

@media (min-width:550px){
.allergen-detail img{
  width: 2.5em;
}
.menu-detail-header{
  max-width: 800px;
  margin: 0 auto;
}
.courses-wrapper{
  max-width: 500px;
  margin: 0 auto;
}

}
</style>
