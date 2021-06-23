<template>
  <div class="nav">
      <div class="nav-bar">
        <ul>
            <li><router-link to="/">Главная</router-link></li>
            <li><a href="#">Профиль</a></li>
            <li><a href="#">Места</a></li>
            <li><a href="#">Чат</a></li>
        </ul>
    </div>
  </div>
</template>

<script>
export default {
    name: 'NavBar',

}
</script>

<style>
    .nav-bar{
        width: 2000px;
    }   
    ul{
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #333;
    }
    li{
        display: inline;
        float: left;
    }

    li a {
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }

    li a:hover {
        background-color: #111;
        color: lightgoldenrodyellow;
    }

    .active {
        background-color: #04AA6D;
    }
</style>