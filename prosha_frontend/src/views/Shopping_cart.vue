<template>
  <div class="Shopping_cart">
    <p class="reg_title">Корзина</p>
    <div class="shop">
      <form class="shop_elem" @submit.prevent="submit" v-for="item in paginatedData">
        <img :src="PhotoPath+(ALL_PRODUCT.filter(function (el) {
          return el.id === item.product;
        }))[0]?.image" class="shop_img" alt=""/>
        <p class="shop_text">{{ (ALL_PRODUCT.filter(function (el) {
          return el.id === item.product;
        }))[0]?.name }}</p>
        <p class="shop_text">{{ item.quantity }}</p>
        <p class="shop_text">Итого: {{ item.quantity*(ALL_PRODUCT.filter(function (el) {
          return el.id === item.product;
        }))[0]?.price }} Р</p>
        <button class="reg_body_button" @click="DEL_CART(item)">Убрать</button>
      </form>
    </div>
    <button class="reg_body_button2" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
    <button class="reg_body_button2" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
    <p class="shop_text">Текущая страница: {{ pageNumber +1}}</p>
    <button class="reg_body_button2" @click="$router.push('/add_order')">Оформить заказ</button>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Shopping_cart",

  data(){
    return {
      pageNumber: 0,
      id: "",
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  props:{
    size:{
      type:Number,
      required:false,
      default: 4
    }
  },

  methods: {
    ...mapActions(['GET_CART', 'GET_PRODUCT', 'DEL_CART']),

    nextPage(){
      this.pageNumber++;
    },
    prevPage(){
      this.pageNumber--;
    },
  },

  computed: {
    ...mapGetters(['ALL_CART', 'ALL_PRODUCT']),

    pageCount(){
      let l = this.ALL_CART.length,
          s = this.size;
      return Math.ceil(l/s);
    },

    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size;
      return this.ALL_CART?.slice(start, end);
    },
  },

  async mounted() {
    this.GET_CART();
    this.GET_PRODUCT();
  }
}
</script>

<style>
.Shopping_cart{
  min-height: calc(100vh - 93px);
  text-align: center;
  margin: 0 166px;
}
.reg_title{
  margin-top: 20px;
  color: #FFFFFF;
  font-size: 72px;
}
.shop_text{
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
.reg_body_button2{
  font-size: 24px;
  color: #FFFFFF;
  background: #85A1B0;
  margin: 25px 25px;
  padding: 4px 10px 4px 10px;
  border-radius: 10px;
  border: none;
}
.shop{
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(2, 1fr);
  justify-items: center;
  align-items: center;
}
.shop_elem{
  background: #85A1B0;
  width: 300px;
  margin: 20px 10px 10px 10px;
  border-radius: 10px;
  text-align: center;
}
.shop_img{
  width: 200px;
  height: 200px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.shop_img2{
  width: 35px;
  height: 35px;
margin-left: 100px;
}
</style>
