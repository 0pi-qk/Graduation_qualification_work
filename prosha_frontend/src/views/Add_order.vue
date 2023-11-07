<template>
  <div class="Add_order">
    <p class="reg_title">Оформление заказа</p>
    <form class="reg_form" @submit.prevent="submit">
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Сумма заказа</p></td>
          <td><input class="reg_body_input" v-model="amount"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Способ оплаты</p></td>
          <td>
            <select class="reg_body_input" v-model="payment_metod">
              <option class="reg_body_input" value="">-- Способ оплаты --</option>
              <option class="reg_body_input" value="online">online</option>
              <option class="reg_body_input" value="offline">offline</option>
            </select>
            </td>
        </tr>
        <tr>
          <td><p class="menu_text">Способ получения</p></td>
          <td>
            <select class="reg_body_input" v-model="metod_of_receipt">
              <option class="reg_body_input" value="">-- Способ оплаты --</option>
              <option class="reg_body_input" value="delivery">delivery</option>
              <option class="reg_body_input" value="self-delivery">self-delivery</option>
            </select>
          </td>
        </tr>
        <tr>
          <td><p class="menu_text">Страна</p></td>
          <td><input class="reg_body_input" v-model="country"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Город</p></td>
          <td><input class="reg_body_input" v-model="city"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Улица</p></td>
          <td><input class="reg_body_input" v-model="street"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Здание, помещение</p></td>
          <td><input class="reg_body_input" v-model="flat"></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" type="submit">Оформить</button>
    </form>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Add_order",

  data() {
    return {
      payment_metod: "",
      metod_of_receipt: "",

      country: "Россия",
      city: "",
      street: "",
      flat: "",
    }
  },

  methods: {
    ...mapActions(['POST_ONLINEORDER', 'POST_ADDRESS', 'POST_ORDERPRODUCT', 'DEL_CART', 'GET_CART', 'GET_ONLINEORDER']),

    submit(){
      this.POST_ADDRESS({
        user: this.id,
        country: this.country,
        city: this.city,
        street: this.street,
        flat: this.flat,
      })
      this.POST_ONLINEORDER({
        user: this.id,
        payment_metod: this.payment_metod,
        metod_of_receipt: this.metod_of_receipt,
        date_of_order: new Date().toISOString().slice(0, 10),
        order_time: new Date().toISOString().slice(11, 19),
        amount: this.amount,
      })
      for (const item in this.ALL_CART) {
        this.POST_ORDERPRODUCT({
          order: this.GET_NOW_ORDER,
          product: this.ALL_CART[item]?.product,
          quantity: this.ALL_CART[item]?.quantity,
        })
        this.DEL_CART({
          id: this.ALL_CART[item]?.id
        })
      }
      this.$router.push('/')
    }
  },
  computed: {
    ...mapGetters(['ALL_ONLINEORDER', 'GET_NOW_ORDER', 'ALL_CART']),

    id: function() {
      return (this.$store.state.account.thisId)
    },
    amount: function (){
      let sum = 0
      for (const item_cart in this.$store.state.cart.cart) {
          sum = sum + this.$store.state.cart.cart[item_cart].quantity * (this.$store.state.product.product.filter(function (el) {
            return el.id === this.$store.state.cart.cart[item_cart].product;
          }, this))[0]?.price
      }
      return sum
    }

  },

  async mounted() {
    this.GET_CART();
    this.GET_ONLINEORDER();
  }
}
</script>

<style>
.Add_order{
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
.reg_tbl{
  display: flex;
  justify-content: center;
}
.menu_text{
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
</style>
