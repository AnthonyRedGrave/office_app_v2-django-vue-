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
          <div class="filter_offices_btn action_box" @click="showElem('.filter_offices')">
              <div class="action_box__inner">
                  Фильтрация офисов
              </div>
          </div>
          
      </div>
      <div class="hr" style="width: 900px; margin: 0 auto;">
          <hr>
      </div>
      
      <div class="offices_list" id="info_box">
          <div class="v-office-box">
              <officeBox
                v-for="office_box in office_boxes" 
                :key="office_box.address"
                :office="office_box"
                @showDetailOffice="showDetailOffice($event)"/>
          </div>
      </div>

      <div class="search_offices" id="info_box">
          <h3>Поиск офиса</h3>
          <br>
          <input type="text" v-model="searchOfficeInputText" class="form-control search_office_input">
          <h3 v-if="searchOfficeInputText">Результаты поиска по запросу {{searchOfficeInputText}}:</h3>
      </div>

      <div class="filter_offices" id="info_box">
          <h3>Фильтрация офисов</h3>
          <br>
          <h4>По типу</h4>
          <div class="v-filter-box">
            <div class="box">
                <div class="action_box__inner">
                    Классический
                </div>
            </div>
            <div class="box">
              <div class="action_box__inner">
                  Открытый
              </div>
            </div>
            <div class="box">
              <div class="action_box__inner">
                  Открытый
              </div>
            </div>
            <div class="box">
              <div class="action_box__inner">
                  Открытый
              </div>
            </div>
          </div>
          <br>
          <h4>По адресу</h4>
          <div class="v-filter-box-address">
            <div class="box">
                <div class="action_box__inner">
                    От А до Я
                </div>
            </div>
            <div class="box">
              <div class="action_box__inner">
                  От Я до А
              </div>
            </div>
          </div>
          </div>
          
    </div>
</template>

<script>
import officeBox from '@/components/office/OfficeBox.vue'
import axios from 'axios'
export default {
    name: 'main',
    components:{
        officeBox
    },
    data(){
        return{
            searchOfficeInputText: null,
            office_boxes: []
        }
    },
    created(){
        this.getOfficeList()
    },
    methods:{
        getOfficeList(){
            axios.get('http://127.0.0.1:8000/api/office/list')
            .then(responce=>{
                this.office_boxes = responce.data
            })
        },
        showElem(classname){
            let boxes = document.querySelectorAll('#info_box')
            let elem = document.querySelector(classname)
            
            
            boxes.forEach(element => {
                element.style.display = 'block';
                
                if(element != elem){
                    element.style.opacity = '0'
                    element.style.display = 'none';
                }
            });
            if(elem.style.opacity == '0' | elem.style.opacity == ''){
                elem.style.top = '260px'
                elem.style.opacity = '100'
                
            }
            else if(elem.style.opacity == '100'){
                elem.style.opacity = '0'
                
                elem.style.top = '250px'
            }
            
        },
        showDetailOffice(id){
            this.$router.push({path: 'office-detail', query: {'officeId': id}})
        }
    }
}
</script>

<style>
    .v-main{
        margin-top: 80px;
        z-index: 3;
    }

    .offices_list{
        margin-top: 20px;
        position: absolute;
        width: 100%;
        top: 230px;
        opacity: 0;
        
        transition: all 0.3s ease-in-out;
    }

    .search_offices{
        margin-top: 20px;
        position: absolute;
        width: 100%;
        top: 250px;
        opacity: 0;
        transition: all 0.3s ease-in-out;
    }
    
    .filter_offices{
        margin-top: 20px;
        position: absolute;
        width: 100%;
        top: 250px;
        opacity: 0;
        
        transition: all 0.3s ease-in-out;
    }

    .search_office_input{
        width: 300px;
        margin: 0 auto;
        margin-bottom: 20px;
    }


    .v-office-box, .v-main__actions{
        display: flex;
        justify-content: space-between;
        margin: 0 auto;
        margin-top: 20px;
        width: 700px;
        flex-flow: wrap;
    }

    .v-filter-box{
        display: flex;
        flex-direction: row;
        /* align-items: center; */
        justify-content: space-around;
        margin: 0 auto;
        margin-top: 20px;
        width: 900px;
        flex-wrap: wrap;
    }
    .v-filter-box-address{
        display: flex;
        flex-direction: row;
        /* align-items: center; */
        justify-content: space-around;
        margin: 0 auto;
        margin-top: 20px;
        width: 450px;
        flex-wrap: wrap;
    }
</style>