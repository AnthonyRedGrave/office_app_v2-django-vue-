<template>
  <div class="v-place-box">
      <div class="place_list">
          <div class="place_box" v-if="room_info">
              {{room_info.id}}
              ФЫВ
          </div>
          
      </div>
  </div>
</template>

<script>
export default {
    name: 'PlaceBox',
    props:{
        room_info:{
            type: Object,
            default: () => {}
        }
    },
    methods:{
        show(){
            console.log(this.room_info)

        }
    }
}
</script>

<style>

</style>