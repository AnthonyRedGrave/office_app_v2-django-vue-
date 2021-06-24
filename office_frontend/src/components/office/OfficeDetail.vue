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
    <div class="hr" style="width: 900px; margin: 0 auto;">
          <hr>
    </div>
    <div class="actions">
      <div class="rooms_list_show_btn action_box" @click="showElem('.rooms_box')">
        <div class="action_box__inner">
          Комнаты офиса
        </div> 
      </div>
      <div class="images_show_btn action_box" @click="showImages()">
        <div class="action_box__inner">
          Фото офиса
        </div> 
      </div>
    </div>
    
    <div class="rooms_wrapper">
      <div class="rooms_box">
      <div class="rooms_list">
        <div class="box" v-for="room in office_info.rooms" :key="room.id" @click="showPlaces(room.id)">
          <div class="box__inner">
              Кабинет №{{room.title_number}}
          </div>
      </div>
    </div>
    </div>
    <place-box 
    v-for="room in office_info.rooms"
    :key="room.id"
    :room_info="room"
    
    />
    </div>
    <div class="hr_rooms_box">
            <hr>
    </div>
    
    
    
      <br>
      <div class="office_image_wrapper">
        <div class="images_list">
          <img class="office_image" v-bind:src="office_info.image_url">
          <img class="office_image" v-bind:src="office_info.image_url">
          <img class="office_image" v-bind:src="office_info.image_url">
          <img class="office_image" v-bind:src="office_info.image_url">
          <img class="office_image" v-bind:src="office_info.image_url">
        </div>
        
      </div>
      
  </div>
</template>

<script>
import axios from 'axios'
import PlaceBox from './PlaceBox.vue'
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
        places_count: null,
        rooms: {},
        places: [],
        placesForPlaceBox: {}
      }
    }
  },
  components:{
    PlaceBox
  },
  created(){
        this.get_office_info()
    },
  methods:{
    get_office_info(){
      axios.get(`http://127.0.0.1:8000/api/office/list/${this.$route.query.officeId}/`)
      .then(responce=>{
        console.log(responce)
        this.office_info.address = responce.data.get_full_title
        this.office_info.count_rooms = responce.data.get_count_rooms
        this.office_info.type = responce.data.type
        this.office_info.image_url = responce.data.image
        this.office_info.places_count = responce.data.places_count
        this.office_info.title = responce.data.title
        this.office_info.rooms=responce.data.rooms
        //заполение массивов с местами и их комнатами
        for(let i = 0;i<responce.data.get_count_rooms;i++){
          this.office_info.places.push({
            id: responce.data.rooms[i].id,
            places: responce.data.rooms[i].places
          })
          
        }
        // this.office_info.places = responce.data.places
      })
    },
    back_to_main(){
      this.$router.push(-1)
    },
    showElem(className){

      let elem = document.querySelector(className)
      let hr = document.querySelector('.hr_rooms_box')
      let images_show_btn = document.querySelector('.images_show_btn')
      let images = document.querySelector('.office_image_wrapper')
      if(elem.style.opacity == '0' | elem.style.opacity == ''){
        hr.style.top = '520px'
        hr.style.opacity = '100'
        
        images_show_btn.style.top = '300px'
        images.style.top = '800px'

        elem.style.top = '10px'
        elem.style.opacity = '100'
      }
      else if(elem.style.opacity == '100'){
        hr.style.top = '480px'
        hr.style.opacity = '0'

        images_show_btn.style.top = '20px'
        images.style.top = '500px'
        
        elem.style.opacity = '0' 
        elem.style.top = '0px'
      }
    },
    showImages(){
      let elem = document.querySelector('.office_image_wrapper')
      let images_show_btn = document.querySelector('.images_show_btn')
      if(elem.style.opacity == '0' | elem.style.opacity == '' && images_show_btn.style.top !== '300px'){
        elem.style.top = '500px'
        elem.style.opacity = '100'
      }
      else if(elem.style.opacity == '100' && elem.style.top !== '800px'){
        elem.style.opacity = '0' 
        elem.style.top = '480px'
      }
      else if(elem.style.opacity == '' && images_show_btn.style.top == '300px'){

        elem.style.top = '800px'
        elem.style.opacity = '100'
      }
      else if(elem.style.opacity == '100' && elem.style.top == '800px'){
        elem.style.opacity = '0' 
        elem.style.top = '800px'
      }
      else if(elem.style.opacity == '0' && images_show_btn.style.top == '300px'){
        elem.style.top = '800px'
        elem.style.opacity = '100'
      }
    },
    showPlaces(room_id){
      console.log(room_id)
      let clickedRoom = this.office_info.places.find(item=>item.id == room_id)
      
      this.placesForPlaceBox = clickedRoom
    }
  }
}
</script>

<style scoped>
    .images_show_btn{
      position: relative;
      transition: all 0.3s ease-in-out;
      top: 20px;
    }

    .hr_rooms_box{
      margin:0 auto; 
      margin-top: 90px;
      margin-bottom: 10px;
      width: 900px;
      opacity: 0;
      left: 500px; 
      top: 480px;
      position: absolute; 
      /* width: 100%; */
      transition: all 0.3s ease-in-out;
    }
    .action_box{
      margin: 0 auto;

    }
    .rooms_wrapper{
      width: 700px;
      margin: 0 auto;
      height: auto;
    }
    .rooms_list{
      margin-top: 20px;
      display: flex;
      
      justify-content: space-between;
      /* opacity: 100; */
      width: 100%;
      flex-wrap: wrap;
      
    }
    .rooms_box{
      margin-top: 30px;
      margin-bottom: 30px;
      position: relative;
      top: 0px;
      opacity: 0;
      margin: 0 auto;
      margin-top: 20px;
      width: 100%;
      transition: all 0.3s ease-in-out;
      /* flex-flow: wrap; */
      
    }
    .box{
        border: 1px solid black;
        text-align: center;
        margin-bottom: 20px;
        width: 200px;
        height: 50px;
    }

  .images_list{
    position: relative;
    display: flex;
    flex-flow: wrap;
    width: 1200px;
    margin: 0 auto;
    justify-content: space-between;
  }

  .office_image_wrapper{
    opacity: 0;
    position: absolute;
    top: 480px;
    width: 100%;
    transition: all 0.3s ease-in-out;
    
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