<template>
  <div class="v-place-box room_info" :id="`room_info_${room_info.id}`">
      <div class="place_list">
          <div class="place_box" v-if="room_info.places.length !== 0">
              <div class="place" :class="placeStatusClass" v-for="place in room_info.places" :key="place.id" :id="place.id" @click="showPopup(place)">
                  <div class="place__inner">
                      Место №{{place.title_number}}
                  </div>
                  
              </div>
          </div>
          <div class="place_box" v-else>
              В комнате пока нет мест
          </div>
      </div>
  </div>
  
</template>

<script>


export default {
    name: 'PlaceBox',
    components:{
    },
    data(){
        return{
            
        }
    },
    props:{
        room_info:{
            type: Object,
            default: () => {}
        }
    },
    computed:{
        placeStatusClass: function(){
            return{
                place__free: !this.room_info.is_occupied,
                place__occupied: this.room_info.is_occupied
            }
        }
    },
    methods:{
        showPopup(place){

            this.$emit('showPopup', place)
        }
    }
}
</script>

<style>
    .v-place-box{
        display: none;
    }

    .place_box{
        display: flex;
        justify-content: space-between;
        /* opacity: 100; */
        width: 100%;
        flex-wrap: wrap;
    }
    .place{
        border: 2px solid black;
        text-align: center;
        margin-bottom: 20px;
        width: 200px;
        height: 50px;
    }
    .place__inner{
        margin-top: 10px;
    }
    .place:hover{
        transition: all 0.5s ease;
        background:lightgrey;
    }

    .place__free{
        border: 1px solid green;

    }

    .place__free:hover{
        transition: background 0.5s ease;
        border: 2px solid green;
        background:#71c451;
    }

    .place__occupied:hover{
        transition: background 0.5s ease;
        border: 2px solid red;
        background:#DC143C;
    }

    .place__occupied{
        border: 1px solid red;
    }
</style>