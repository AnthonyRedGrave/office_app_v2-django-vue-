<template>
  <div class="v-main">
      <div class="v-main__title">
          Главная
      </div>
      <div class="v-main__actions">
          <div class="get_offices_btn action_box" @click="showElem('.offices_list')">
              <div class="action_box__inner">
                  Список офисов
              </div>
              
          </div>
          <div class="search_office_btn action_box" @click="showElem('.search_offices')">
              <div class="action_box__inner">
                  Поиск офисов
              </div>
              
          </div>
          <div class="filter_offices_btn action_box">
              <div class="action_box__inner">
                  Фильтрация офисов
              </div>
              
          </div>
          
      </div>
      <div class="hr" style="width: 900px; margin: 0 auto;">
          <hr>
      </div>
      
      <div class="offices_list">
          <div class="v-office-box">
              <officeBox
                v-for="office_box in office_boxes" 
                :key="office_box.address"
                :office="office_box"/>
          </div>
      </div>
      <div class="search_offices">
          <input type="text" v-model="searchOfficeInputText" class="form-control search_office_input">
          <h3 v-if="searchOfficeInputText">Результаты поиска по запросу {{searchOfficeInputText}}:</h3>
      </div>
  </div>
</template>

<script>
import officeBox from '@/components/office/OfficeBox.vue'
export default {
    name: 'main',
    components:{
        officeBox
    },
    data(){
        return{
            searchOfficeInputText: null,
            office_boxes: [
                {
                    'address': 'Адрес1'
                },
                {
                    'address': 'Адрес2'
                },
                {
                    'address': 'Адрес3'
                },
                {
                    'address': 'Адрес4'
                },
                {
                    'address': 'Адрес5'
                },
                {
                    'address': 'Адрес6'
                }
                
            ]
        }
    },
    created(){
        this.getOfficeList()
    },
    methods:{
        getOfficeList(){
            console.log("получить список офисов")
        },
        showElem(classname){
            console.log(classname)
            let elem = document.querySelector(classname)
            if(elem.style.display == '' || elem.style.display == 'none' ){
                elem.style.display = 'block'
            }
            else if(elem.style.display == 'block'){
                elem.style.display = 'none'
            }
            
        }
    }
}
</script>

<style>
    .offices_list{
        margin-top: 20px;
        display: none;
    }

    .search_offices{
        display: none;
    }

    .search_office_input{
        width: 300px;
        margin: 0 auto;
        margin-bottom: 20px;
    }

    .v-office-box, .v-main__actions{
        display: flex;
        flex-direction: row;
        /* align-items: center; */
        justify-content: space-around;
        margin: 0 auto;
        margin-top: 20px;
        width: 700px;
        flex-wrap: wrap;
        
        /* width: 300px; */
    }
</style>