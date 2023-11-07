<template>
  <div class="home">
    <div class="main">
      <p class="title">PROSHA</p>
      <p class="subtitle">Наша цель:</p>
      <p class="subtitle">Мониторинг популяции</p>
      <p class="subtitle">попугаев всех видов </p>
      <img src="@/assets/big_ara.png" class="big_ara" alt=""/>
    </div>
    <div class="menu">
      <div class="column">
        <div class="menu_elem" v-if="GET_AUTH === 0  || GET_AUTH === 1 || GET_AUTH === 2 || GET_AUTH === 4">
          <img src="@/assets/article.jpg" class="menu_img" alt="" @click="$router.push('/article')"/>
          <p class="menu_title">Статьи</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 0  || GET_AUTH === 1 || GET_AUTH === 2">
          <img src="@/assets/shop.jpg" class="menu_img" alt="" @click="$router.push('/online_store')"/>
          <p class="menu_title">Интернет-магазин</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 1 || GET_AUTH === 2">
          <img src="@/assets/prosha.jpg" class="menu_img" alt="" @click="$router.push('/bird_list')"/>
          <p class="menu_title">Список птиц</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 3 || GET_AUTH === 4">
          <img src="@/assets/cart.jpg" class="menu_img" alt=""  @click="$router.push('/order_list')"/>
          <p class="menu_title">Интернет-заказы</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 4">
          <img src="@/assets/prosha.jpg" class="menu_img" alt="" @click="$router.push('/bird_list')"/>
          <p class="menu_title">Список птиц в БД</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 1 || GET_AUTH === 2">
          <img src="@/assets/handshake.jpg" class="menu_img" alt="" @click="$router.push('/change_owner_bird')"/>
          <p class="menu_title">Смена владельца</p>
        </div>
      </div>
      <div class="column">
        <div class="menu_elem" v-if="GET_AUTH === 0  || GET_AUTH === 1 || GET_AUTH === 2 || GET_AUTH === 4">
          <img src="@/assets/news.jpg" class="menu_img" alt="" @click="$router.push('/news')"/>
          <p class="menu_title">Новости</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 0  || GET_AUTH === 1 || GET_AUTH === 2">
          <img src="@/assets/ring.jpg" class="menu_img" alt="" @click="$router.push('/descrypt_ring')"/>
          <p class="menu_title">Расшифровка кольца</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 1 || GET_AUTH === 2">
          <img src="@/assets/tree.jpg" class="menu_img" alt="" @click="$router.push('/tree')"/>
          <p class="menu_title">Генеалогическое древо</p>
        </div>
        <div class="menu_elem" v-if="GET_AUTH === 3 || GET_AUTH === 4">
          <img src="@/assets/product.jpg" class="menu_img" alt="" @click="$router.push('/product_list')"/>
          <p class="menu_title">Работа с товарами</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  computed: mapGetters((['GET_AUTH'])),
  name: 'Home',
}
</script>

<style>
.home{
  min-height: calc(100vh - 93px);
}
.main{
  margin-top: -58px;
  background: url("@/assets/main fon.jpg") 0 0/100% auto no-repeat;
  width: 100%;
  height: 600px;
}
.title{
  font-size: 68px;
  color: #FFFFFF;
  padding: 250px 0 20px 166px;
}
.subtitle{
  font-size: 32px;
  color: #FFFFFF;
  padding-left: 166px;
}
.big_ara{
  position: absolute;
  width: 350px;
  left: 850px;
  top: 56px;
}
.menu{
  margin: 0 166px;
  display: flex;
  justify-content: center;
}
.menu_elem{
  background: #85A1B0;
  width: 400px;
  height: 300px;
  margin: 20px 10px 10px 10px;
  border-radius: 10px;
  text-align: center;
}
.menu_img{
  width: 350px;
  height: 200px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.menu_title{
  font-size: 32px;
  color: #FFFFFF;
}
</style>
