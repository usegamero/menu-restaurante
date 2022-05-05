<template>
  <article class="calendar">
    <section class="name-month">
      <button class="button-change-month btn" @click="prevMonth">⬅</button>
      <!-- <h2 @click="comeBackCurrentMonth()"> -->
      <h2>
        {{ nameMonths[this.currentMonth] }} {{ currentYear }}
      </h2>
      <button class="button-change-month btn" @click="nextMonth">➡</button>
    </section>
    <ul class="name-of-week">
      <li v-for="index in nameDaysOfWeek" :key="index">{{ index }}</li>
    </ul>
    <ul class="days-of-month">
      <li
        class="empty-list"
        v-for="i in initialPositionOfFirstDay"
        :key="i"
      ></li>
      <li
        @click="onClickDay(index.day)"
        v-for="index of daysOfMonthSelected"
        class="not-empty-list"
        :key="index"
        v-bind:class="{ underline: index.menuExists }"
      >
        {{ index.day }}
      </li>
    </ul>
  </article>
</template>

<script>
import { getListOfMenus } from "@/services/api.js";
export default {
  name: "Calendar",
  data() {
    return {
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      nameDaysOfWeek: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
      nameMonths: [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
      ],
      listOfMenus: [],
      days: [],
      months: [],
    };
  },
  mounted() {
    this.loadData();
  },

  computed: {
    initialPositionOfFirstDay() {
      let initialDayWeek = new Date(
        this.currentYear,
        this.currentMonth,
        1
      ).getDay();
      if (initialDayWeek === 0) {
        return (initialDayWeek = 6);
      }
      let currentInitialDayweek = initialDayWeek - 1;
      return currentInitialDayweek;
    },
    daysOfMonthSelected() {
      let bindMenusOfMonthToCal = [];
      let totaldays = new Date(
        this.currentYear,
        this.currentMonth + 1,
        0
      ).getDate();
      let menusOfTheMonth = this.extractMenusOfTheMonth();
      for (let i = 1; i <= totaldays; i++) {
        let menuExists = false;
        let dayToStr = i.toString();
        if (menusOfTheMonth.includes(dayToStr)) {
          menuExists = true;
        }
        if (dayToStr < 10) {
          dayToStr = "0" + dayToStr;
        }
        bindMenusOfMonthToCal.push({ day: dayToStr, menuExists: menuExists });
      }
      return bindMenusOfMonthToCal;
    },
  },
  methods: {
    async loadData() {
      this.listOfMenus = await getListOfMenus();
    },
    extractMenusOfTheMonth() {
      let monthExtracted = "";
      let daysConnected = [];
      let current_month = this.currentMonth + 1;
      let day = "";
      if (current_month < 10) {
        current_month = "0" + current_month;
      }
      for (let menu of this.listOfMenus) {
        monthExtracted = menu.date.slice(5, 7);
        if (monthExtracted === current_month) {
          day = menu.date.slice(8, 10);
          if (day.slice(0, 1) === "0") {
            day = day.slice(1, 2);
          }
          daysConnected.push(day);
        }
      }
      return daysConnected;
    },
    nextMonth() {
      this.currentMonth = this.currentMonth + 1;
      if (this.currentMonth > 11) {
        this.currentMonth = 11;
      }
    },
    prevMonth() {
      this.currentMonth -= 1;
      if (this.currentMonth < 0) {
        this.currentMonth = 0;
      }
    },
    onClickDay(day) {
      let month = this.currentMonth + 1;
      if (month < 10) {
        month = "0" + month;
      }
      const clickedDay = this.currentYear + "-" + month + "-" + day;
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      };
      for (let menu of this.listOfMenus) {
        if (menu.date === clickedDay) {
          this.$router.push("/menus/by-date/" + clickedDay, settings);
          return;
        }
      }
      this.$router.push("/menu/add/" + clickedDay);
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-size: 16px;
  box-sizing: border-box;
}

.calendar {
  width: 100%;
  max-width: 300px;
  margin: 2em auto;
}

.name-of-week {
  background: #db5246;
  color:rgb(247, 225, 181);
  padding: 0.5em;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 10px;
  align-items: center;
}
.days-of-month {
  font-size: 1rem;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 40px;
  border: 1px solid #db5246;
  color: #a31d1e;
}
.days-of-month > li {
  padding: 25% 25%;
}
.days-of-month > .empty-list {
  background: none;
}
.days-of-month > .not-empty-list:hover {
  font-size: 1.07rem;
  font-weight: bolder;
  color: rgb(247, 225, 181);
  background-color: #a31d1e;
  border-radius: 50%;
  cursor: pointer;
}
.name-month {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color:#a31d1e;
  color:rgb(247, 225, 181);
}

.button-change-month{
  border: 2px solid #a31d1e;
  padding: 0.8em 0.5em;
  font-size: 0.9em;
  font-weight: bold;
  background-color:#a31d1e;
  color:rgb(247, 225, 181);
  
}
.button-change-month:hover{
  background-color:rgb(247, 225, 181);
  color:#a31d1e;
}


.underline {
  text-decoration: underline double;
  cursor: pointer;
  font-weight: bold;
}
</style>