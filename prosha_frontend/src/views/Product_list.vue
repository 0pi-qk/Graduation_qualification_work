<template>
  <div class="Product_list">
    <p class="reg_title">Список товаров</p>
    <div class="reg_form">
      <table class="reg_tbl">
        <tbody>
        <td><p class="menu_text">Название</p></td>
        <td><p class="menu_text">Описание</p></td>
        <td><p class="menu_text">Цена</p></td>
        <td><p class="menu_text">Количество</p></td>
        <td><p class="menu_text">Image</p></td>
        <tr v-for="item in paginatedData">
          <td><p class="menu_text">{{ item.name }}</p></td>
          <td><p class="menu_text">{{ item.description.substr(0, 5) }} ...</p></td>
          <td><p class="menu_text">{{ item.price }}</p></td>
          <td><p class="menu_text">{{ item.quantity }}</p></td>
          <td><p class="menu_text">{{ item.image }}</p></td>
          <td><button class="reg_body_button" @click="$router.push('/change_info_product/'+item.id)">Изменить</button></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
      <button class="reg_body_button" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
      <p class="menu_text">Текущая страница: {{ pageNumber +1}}</p>
      <br><button class="reg_body_button" @click="$router.push('/add_product')">Добавить товар</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Product_list",

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
    ...mapGetters(['ALL_PRODUCT']),

    pageCount(){
      let l = this.ALL_PRODUCT.length,
          s = this.size;
      return Math.ceil(l/s);
    },

    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size;
      return this.ALL_PRODUCT?.slice(start, end);
    },
  },

  methods: {
    ...mapActions(['GET_PRODUCT']),

    nextPage(){
      this.pageNumber++;
    },
    prevPage(){
      this.pageNumber--;
    }
  },

  async mounted() {
    this.GET_PRODUCT();
  }
}
</script>

<style>
.Product_list{
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
