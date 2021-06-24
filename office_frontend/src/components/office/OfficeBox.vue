<template>
      <div class="box" @click="showDetailOffice(office.id)">
          <div class="box__inner">
              {{office.get_full_title}}
              <br>
              {{office.title}}
          </div>
          
      </div>
      
</template>

<script>
export default {
    name: 'office-box',
    props:{
        office:{
            type: Object,
            default: ()=>{}
        }
    },
    methods:{
        showDetailOffice(id){
            this.$emit('showDetailOffice', id)
        }
    }
}
</script>

<style>
    .action_box{
        width: 200px;
        height: 50px;
    }
    .box, .action_box{
        border: 1px solid black;
        text-align: center;
        margin-bottom: 20px;
    }
    .box{
        width: 200px;
        height: 75px;
    }
    .box:hover{
        transition: all 0.5s ease;
        background:lightgrey;
    }
    .action_box:hover{
        transition: all 0.5s ease;
        background:lightgoldenrodyellow;
    }
    .action_box__inner{
        margin-top: 10px;
        cursor: pointer;
    }
    .box__inner{
        margin-top: 10px;
    }
</style>