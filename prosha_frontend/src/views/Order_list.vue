<template>
  <div class="Order_list">
    <p class="reg_title">Список заказов</p>
    <div class="reg_form">
      <table class="reg_tbl">
        <tbody>
        <td><p class="menu_text">#</p></td>
        <td><p class="menu_text">Способ оплаты</p></td>
        <td><p class="menu_text">Способ доставки</p></td>
        <td><p class="menu_text">Пользователь</p></td>
        <tr v-for="item in paginatedData">
          <td><p class="menu_text">{{ item.id }}</p></td>
          <td><p class="menu_text">{{ item.payment_metod }}</p></td>
          <td><p class="menu_text">{{ item.metod_of_receipt }}</p></td>
          <td><p class="menu_text">{{ item.user }}</p></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
      <button class="reg_body_button" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
      <p class="menu_text">Текущая страница: {{ pageNumber +1}}</p>
      <br><button class="reg_body_button" @click="$router.push('/')">Вернуться назад</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Order_list",

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
    ...mapGetters(['ALL_ONLINEORDER']),

    pageCount(){
      let l = this.ALL_ONLINEORDER.length,
          s = this.size;
      return Math.ceil(l/s);
    },

    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size;
      return this.ALL_ONLINEORDER?.slice(start, end);
    },
  },

  methods: {
    ...mapActions(['GET_ONLINEORDER']),

    nextPage(){
      this.pageNumber++;
    },
    prevPage(){
      this.pageNumber--;
    }
  },

  async mounted() {
    this.GET_ONLINEORDER();
  }
}
</script>

<style>
.Order_list{
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
