<template>
  <div class="Bird_list">
    <p class="reg_title">Список птиц</p>
    <div class="reg_form">
      <table class="reg_tbl">
        <tbody>
        <td><p class="menu_text">Номер птицы</p></td>
        <tr v-for="item in paginatedData">
          <td><p class="menu_text">{{ item.number }}</p></td>
          <td><button class="reg_body_button" @click="$router.push('/info_bird/'+item.id)">Информация</button></td>
          <td><button class="reg_body_button" @click="DEL_BIRD(item)">Удалить</button></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
      <button class="reg_body_button" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
      <p class="menu_text">Текущая страница: {{ pageNumber +1}}</p>
      <br><button class="reg_body_button" @click="$router.push('/add_bird')">Добавить птицу</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Bird_list",

  data(){
    return {
      pageNumber: 0
    }
  },

  props:{
    size:{
      type:Number,
      required:false,
      default: 8
    }
  },

  computed: {
    ...mapGetters(['ALL_BIRD']),

    pageCount(){
      let l = this.ALL_BIRD.length,
          s = this.size;
      return Math.ceil(l/s);
    },

    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size;
      return this.ALL_BIRD?.slice(start, end);
    },
  },

  methods: {
    ...mapActions(['GET_BIRD', 'DEL_BIRD']),

    nextPage(){
      this.pageNumber++;
    },
    prevPage(){
      this.pageNumber--;
    }
  },

  async mounted() {
    this.GET_BIRD(false);
  }
}
</script>

<style>
.Bird_list{
  min-height: calc(100vh - 93px);
  text-align: center;
}
.reg_title{
  margin-top: 20px;
  color: #FFFFFF;
  font-size: 72px;
}
.reg_form{
  background: #85A1B0;
  margin: 25px 200px;
  border-radius: 10px;
}
.reg_tbl{
  display: flex;
  justify-content: center;
}
.menu_text{
  margin: 20px 10px 10px 10px;
  font-size: 24px;
  color: #FFFFFF;
}
.reg_body_button{
  font-size: 24px;
  color: #FFFFFF;
  background: #4C758C;
  margin: 25px 25px;
  padding: 4px 10px 4px 10px;
  border-radius: 10px;
  border: none;
}
</style>
