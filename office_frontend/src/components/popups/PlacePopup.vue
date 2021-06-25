<template>
    <div class="popup_wrapper">
        <div class="place-popup">
      <div class="popup__header">
          <span>
              header
          </span>
          <span>
              <i class="material-icons" @click="closePopup()">close</i>
          </span>
      </div>
      <div class="popup__content">
          <slot>

          </slot>
      </div>
      <div class="popup__footer">
          <button class="" @click="closePopup()">Закрыть</button>
          <button class="">Занять место</button>
      </div>
  </div>
    </div>
  
</template>

<script>
export default {
    name: 'place-popup',
    methods:{
        closePopup(){
            this.$emit('closePopup')
        }
    },
    mounted:{
        
    }
}
</script>

<style scoped>
    .popup_wrapper{
        background: rgba(64, 64, 64, .4);
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        right: 0;
        left: 0;
        top: 0;
        bottom: 0;
    }
    .place-popup{
        padding: 16px;
        position: fixed;
        top: 70px;
        left: 30%;
        z-index: 5;
        margin: 0 auto;
        width: 40%;
        background: #ffffff;
        box-shadow: 0 0 17px 0 #e7e7e7;
    }
    .popup__header, .popup__footer{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .popup__content{
        display: flex;
        justify-content: center;
        align-items: center;
    }

</style>