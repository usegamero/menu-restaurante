<template>
   <section class="menu-form">
   <div class="wrappedNameDish">
        <p>Primeros</p> 
        <button class="add-btn btn" @click.prevent="addNewDish(dict_plates.firsts)">Añadir plato</button>
    </div>
    <div class="firsts" v-for="dish in dict_plates.firsts" :key="dish.id_dish">
        <div class="input-button-wrapper">
            <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
            <button @click.prevent="deleteDish(dish,dict_plates.firsts)" class="btn delete-btn"> x </button>
        </div>
        <div class="allergens-wrapped">
            <label for="lactose"><img src="@/assets/img/allergens_icons/lactose.png" alt="">Lactosa </label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten"><img src="@/assets/img/allergens_icons/gluten.png" alt="">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg"><img src="@/assets/img/allergens_icons/egg.png" alt="">Huevo</label>
            <input @change="onMenuChanges"   id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood"><img src="@/assets/img/allergens_icons/seafood.png" alt="">Marisco</label>
            <input  @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy"><img src="@/assets/img/allergens_icons/soy.png" alt="">Soja</label>
            <input @change="onMenuChanges" id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts" ><img src="@/assets/img/allergens_icons/nut.png" alt="" >Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
        
    </div>
    <div class="wrappedNameDish">
        
        <p>Segundos</p> 
        <button class="add-btn btn" @click.prevent="addNewDish(dict_plates.seconds)">Añadir plato</button>
        </div>
    <div class="seconds" v-for="dish in dict_plates.seconds" :key="dish.id_dish">
        <div class="input-button-wrapper">
        <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
        <button @click.prevent="deleteDish(dish,dict_plates.seconds)" class="btn delete-btn"> x </button>
        </div>
        <div class="allergens-wrapped">
            <label for="lactose"><img src="@/assets/img/allergens_icons/lactose.png"  alt="">Lactosa </label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten"><img src="@/assets/img/allergens_icons/gluten.png" alt="">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg"><img src="@/assets/img/allergens_icons/egg.png" alt="">Huevo</label>
            <input @change="onMenuChanges"   id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood"><img src="@/assets/img/allergens_icons/seafood.png" alt="">Marisco</label>
            <input  @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy"><img src="@/assets/img/allergens_icons/soy.png" alt="">Soja</label>
            <input @change="onMenuChanges" id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts"><img src="@/assets/img/allergens_icons/nut.png" alt="">Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
    </div>
    <div class="wrappedNameDish">
        <p>Postres</p> 
        <button class="add-btn btn" @click.prevent="addNewDish(dict_plates.desserts)">Añadir plato</button></div>  
    <div class="desserts" v-for="dish in dict_plates.desserts" :key="dish.id_dish">
        <div class="input-button-wrapper">
        <input @keyup="onMenuChanges" class="input_plate" type="text"  v-model="dish.name_dish">
        <button @click.prevent="deleteDish(dish,dict_plates.desserts)" class="btn delete-btn"> x </button>
        </div>
        <div class="allergens-wrapped">
            <label for="lactose"><img src="@/assets/img/allergens_icons/lactose.png" alt="">Lactosa </label>
            <input @change="onMenuChanges" id="lactose" type="checkbox" value="lactose" v-model="dish.allergens"/>
            <label for="gluten"><img src="@/assets/img/allergens_icons/gluten.png" alt="" class="allergens-icons">Gluten</label>
            <input @change="onMenuChanges" id="gluten" type="checkbox" value="gluten" v-model="dish.allergens"/>
            <label for="egg"><img src="@/assets/img/allergens_icons/egg.png" alt="">Huevo</label>
            <input @change="onMenuChanges"   id="egg" type="checkbox" value="egg" v-model="dish.allergens" />
            <label for="seafood"><img src="@/assets/img/allergens_icons/seafood.png" alt="">Marisco</label>
            <input  @change="onMenuChanges" id="seafood" type="checkbox" value="seafood" v-model="dish.allergens"/>
            <label for="soy"><img src="@/assets/img/allergens_icons/soy.png" alt="">Soja</label>
            <input @change="onMenuChanges" id="soy" type="checkbox" value="soy" v-model="dish.allergens" />
            <label for="nuts"><img src="@/assets/img/allergens_icons/nut.png" alt="">Frutos de cascara</label>
            <input @change="onMenuChanges" id="nuts" type="checkbox" value="nuts" v-model="dish.allergens"/>
        </div>
        
    </div>
    </section>
</template>

<script>
export default {
    props:{
        dictMenu:{
            type: Object,
            required: true,
        }
    },
    emits:["changed"],
    watch:{
        dictMenu: {
            handler(newValue){
                let menuAsJson = JSON.stringify(newValue)
                this.dict_plates = JSON.parse(menuAsJson)

            },
            inmediate: true
        }
    },
    data(){
        return{
            dict_plates:{firsts: [],seconds: [],desserts: [],},

        }
    },

    methods:{
    onMenuChanges(){
        this.$emit("changed",this.dict_plates)
    },

    addNewDish(typeOfDish){
        typeOfDish.push({name_dish:"", allergens:[]})
        this.$emit("changed",this.dict_plates)
    },

    deleteDish(dish,menu){
      let indice = menu.indexOf(dish)
      menu.splice(indice,1)
      this.$emit("changed",this.dict_plates)
    },


    
    },
}
</script>

<style scoped>

.add-btn, .delete-btn{
    margin:0;
    padding: 0.3em;
    font-weight: normal;
    font-size: 0.8em;
    width: fit-content;
}
.menu-form p{
    text-align: left;
    font-size: 1.1em;
    margin-bottom: 0.2em;
}
.wrappedNameDish {
    display: flex;
    flex-direction: column;
    margin-bottom: 1.5em;
}
.input-button-wrapper{
    width: 100%;
    display: flex;
    justify-content: space-between;
}
.allergens-wrapped label{
    display: inline;
    font-size: 0.8em;
   
}
.allergens-wrapped img{
    width: 1.5em;
}
.allergens-wrapped input{
    margin-right: 0.5em;
}


.input-button-wrapper input{
  border: none;
  box-shadow: 0px 0px 8px 0px rgb(247, 225, 181) inset;
  padding: 0.5em 0.2em;
  font-family: "Ubuntu", sans-serif;
  font-size: 1em;
  width:92%;
  margin: 0.2em 0;

}
.input-button-wrapper .delete-btn{
    width: 6%;
    margin: 0.2em 0;
 
}

.menu-form{
    margin-bottom: 2em;
}


</style>