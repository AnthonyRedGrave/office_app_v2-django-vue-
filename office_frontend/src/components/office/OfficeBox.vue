<template>
      <div class="box">
          <div class="box__inner">
              {{office.address}}
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
    }
}
</script>

<style>
    .box, .action_box{
        border: 1px solid black;
        text-align: center;
        margin-bottom: 20px;
        width: 200px;
        height: 50px;
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