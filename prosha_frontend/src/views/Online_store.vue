<template>
  <div class="Online_store">
    <p class="reg_title">Интернет-магазин<img v-if="GET_AUTH !== 0" src="@/assets/shoping.png" class="shop_img2" alt="" @click="$router.push('/cart')"/></p>
    <div class="shop">
      <div class="shop_elem" v-for="item in paginatedData">
        <img :src="PhotoPath+item.image" class="shop_img" alt=""/>
        <p class="shop_text">{{ item.name }}</p>
        <p class="shop_text">{{ item.price }} P</p>
        <button class="reg_body_button" @click="$router.push('/open_product/'+item.id)">Подробнее</button>
      </div>
    </div>
    <button class="reg_body_button2" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
    <button class="reg_body_button2" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
    <p class="shop_text">Текущая страница: {{ pageNumber +1}}</p>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'

import {mapActions, mapGetters} from "vuex";

export default {
  name: "Online_store",

  data(){
    return {
      pageNumber: 0,
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  props:{
    size:{
      type:Number,
      required:false,
      default: 9
    }
  },

  computed: {
    ...mapGetters(['ALL_PRODUCT', 'GET_AUTH']),

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
.Online_store{
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
  grid-template-columns: repeat(3, 1fr);
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
