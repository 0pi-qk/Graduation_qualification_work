<template>
  <div class="Open_product">
    <p class="reg_title">{{ name }}</p>
    <form class="reg_form" @submit.prevent="submit">
      <div class="prod">
        <div class="column">
          <img :src="PhotoPath+image" class="prod_img" alt=""/>
        </div>
        <div class="column">
          <star-rating v-if="GET_AUTH === 0" :read-only="true" class="prod_text" :rating="star1" @update:rating="setRating" :star-size="20"></star-rating>
          <star-rating v-else class="prod_text" :rating="star1" @update:rating="setRating" :star-size="20"></star-rating>
          <p class="prod_text">Цена: {{ price }}</p>
          <p class="prod_text">Описание: {{ description }}</p>
          <p class="prod_text">Доступно: {{ quantity }}</p>
          <p class="prod_text">Введите необходимое количество</p>
          <input class="reg_body_input" v-model="quantity_now">
          <button v-if="GET_AUTH === 0" class="reg_body_button" @click="$router.push('/authorization')">Добавить в корзину</button>
          <button  v-else class="reg_body_button" type="submit">Добавить в корзину</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'
import {mapActions, mapGetters} from "vuex";
import StarRating from 'vue-star-rating'

export default {
  name: "Open_product",
  components: {
    StarRating
  },

  data() {
    return{
      quantity_now: "",
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  methods: {
    ...mapActions(['GET_PRODUCT_ID', 'POST_CART', 'GET_STARPRODUCT', 'POST_STARPRODUCT', 'PUT_STARPRODUCT']),

    setRating(star){
      const tmp = this.ALL_STARPRODUCT.filter(t => t.user === this.GET_ID)
      if (tmp[0]?.user > -1)
        this.PUT_STARPRODUCT({
          id: tmp[0]?.id,
          user: this.GET_ID,
          product: this.$route.params.id,
          evaluation: star,
        })
      else{
        this.POST_STARPRODUCT({
          user: this.GET_ID,
          product: this.$route.params.id,
          evaluation: star,
        })
      }
    },

    submit(){
      if (this.quantity_now > this.quantity)
        this.quantity_now = this.quantity;
      this.POST_CART({
        user: this.$store.state.account.thisId,
        product: this.$route.params.id,
        quantity: this.quantity_now,
      })
      this.$router.push('/cart')
    }
  },

  computed: {
    ...mapGetters((['GET_AUTH', 'GET_ID', 'ALL_STARPRODUCT'])),
    star1: function (){
      const tmp = this.ALL_STARPRODUCT.filter(t => t.user === this.GET_ID)
      if (tmp[0]?.user > -1)
        return tmp[0]?.evaluation
      else {
        let sum = 0;
        for(const item in this.ALL_STARPRODUCT)
          sum += this.ALL_STARPRODUCT[item].evaluation;
        if (Object.keys(this.ALL_STARPRODUCT).length === 0)
          return 0
        else
          return sum / Object.keys(this.ALL_STARPRODUCT).length;
      }
    },

    name: function() {
      return (this.$store.state.product.product)[0]?.name
    },
    description: function() {
      return (this.$store.state.product.product)[0]?.description
    },
    price: function() {
      return (this.$store.state.product.product)[0]?.price
    },
    quantity: function() {
      return (this.$store.state.product.product)[0]?.quantity
    },
    image: function() {
      return (this.$store.state.product.product)[0]?.image
    },
  },

  async mounted() {
    this.GET_PRODUCT_ID(this.$route.params.id);
  }
}
</script>

<style>
.Open_product{
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
  margin: 25px 350px;
  border-radius: 10px;
}
.prod_text{
  width: 400px;
  margin: 20px 10px 10px 10px;
  font-size: 24px;
  color: #FFFFFF;
}
.reg_body_input{
  background: #AECAD9;
  border: 2px solid #FFFFFF;
  color: #2c53a8;
  font-size: 20px;
  font-weight: 700;
  width: 325px;
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
.prod_img{
  width: 350px;
  height: 500px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.prod{
  margin: 0 166px;
  display: flex;
  justify-content: center;
}
</style>
