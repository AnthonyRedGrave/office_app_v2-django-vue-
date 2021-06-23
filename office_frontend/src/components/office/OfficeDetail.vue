<template>
  <div class="v-office-detail">
    <div class="back-to-main-box">
      <router-link to="/">На главную</router-link>
    </div>
    <br>
    <h2>{{office_info.title}}</h2>
    <br>
    <div class="office_info_wrapper">
      <div class="office_info_block">
        <div class="row">
          <div class="col-6">
            <div class="class_info">Адрес офиса: <b>{{office_info.address}}</b></div>
            <div class="class_info">Количество комнат: <b>{{office_info.count_rooms}}</b></div>
            <div class="class_info">Тип офиса: <b>{{office_info.type}}</b></div>
          </div>
          <div class="col-6">
            <div class="class_info">Количество мест в офисе: <b>{{office_info.places_count}}</b></div>
            <div class="class_info">Количество этажей: <b>х</b></div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <hr>
    <br>
      
      
      <div class="office_image_wrapper">
        <img class="office_image" v-bind:src="office_info.image_url">
        <img class="office_image" v-bind:src="office_info.image_url">
        <img class="office_image" v-bind:src="office_info.image_url">
        <img class="office_image" v-bind:src="office_info.image_url">
        <img class="office_image" v-bind:src="office_info.image_url">
      </div>
      
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'OfficeDetail',
  data(){
    return{
      office_info: {
        title: null,
        address: null,
        count_rooms: null,
        type: null,
        image_url: null,
        places_count: null
      }
    }
  },
  created(){
        this.get_office_info()
    },
  methods:{
    get_office_info(){
      axios.get(`http://127.0.0.1:8000/api/office/list/${this.$route.query.officeId}/`)
      .then(responce=>{
        this.office_info.address = responce.data.get_full_title
        this.office_info.count_rooms = responce.data.get_count_rooms
        this.office_info.type = responce.data.type
        this.office_info.image_url = responce.data.image
        this.office_info.places_count = responce.data.places_count
        this.office_info.title = responce.data.title
      })
    },
    back_to_main(){
      this.$router.push(-1)
    }
  }
}
</script>

<style>

  .office_image_wrapper{
    display: flex;
    flex-flow: wrap;
    width: 1200px;
    margin: 0 auto;
    justify-content: space-between;
    
  }
  .office_image{
    height: auto;
    width: 250px;
    margin-bottom: 50px;
  }

  .office_info_wrapper{
    text-align: left;
    position: relative;
    width: 700px;
    height: auto;
    margin: 0 auto;
  }

  .office_info_block{
    left: 100px;
  }

  
</style>