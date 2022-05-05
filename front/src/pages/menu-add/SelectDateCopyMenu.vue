<template>
  <div class="modal-wrapper" >
      <div class="modal-inner-wrapper">
          <p class="close-btn" @click="copyModalClose">x</p>
          <p>¿En qué fecha quieres copiar el menú?</p>
          <input type="date" v-model="newDate" class="calendar-input">
    <router-link :to="{name: 'MenuModifyPage', params: {date:this.newDate}}">
          <button class="copy-btn btn" @click="sendDate">Copiar en esta fecha</button>
    </router-link>
      </div>
  </div>
</template>

<script>


export default {
    
    name: "CopyCalendar",
    
    data() {
    return {
      newDate: "",
      modalOpened: true,
      
    };
    },


    methods: {
    sendDate(){
      this.$emit("changedDate",this.newDate)

    },
    copyModalClose(){
      this.modalOpened = false
      this.$emit("modaltoFALSE" , this.modalOpened)
      console.log("clicc modal" + this.modalOpened)

    },


    
  },
  
}
</script>

<style scoped>

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.modal-wrapper{
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(250, 246, 246, 0.589);
    position: fixed;
    top: 0;
    left:0;
    z-index: 999;

}
.modal-inner-wrapper{
    width:70%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #a31d1e;
    padding: 1em 1em 3em;
    color:#fae8b9;
}

.modal-inner-wrapper p{
    font-size: 1.2em;
    margin-bottom: 2em;
    font-weight: bold;
}
.modal-inner-wrapper input{
    margin-bottom: 1.5em;
   
}

.modal-inner-wrapper .copy-btn{
    color:#a31d1e;
    background-color:#fae8b9;
}

.modal-inner-wrapper .close-btn {
    color:#a31d1e;
    background-color:#fae8b9;
    width: 25px;
    height: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    align-self: flex-end;
}

.calendar-input{
  background-color: #fae8b9;
}

</style>