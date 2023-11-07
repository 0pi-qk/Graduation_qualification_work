<template>
  <div class="My_nav">
    <div class="nav_logo">
      <button class="logo" @click="$router.push('/')">PROSHA</button>
    </div>
    <div class="nav_button" v-if="GET_AUTH === 0">
      <button class="nav_auto" @click="$router.push('/authorization')">Авторизироваться</button>
      <button class="nav_reg" @click="$router.push('/registration')">Присоединиться</button>
    </div>
    <div class="nav_button" v-else>
      <button class="nav_auto" @click="$router.push('/info_user')">Данные аккаунта</button>
      <form @submit.prevent="submit">
        <button class="nav_reg" type="submit" @click="$router.push('/')">Выйти из аккаунта</button>
      </form>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import store from "@/store";

export default {
  computed: mapGetters((['GET_AUTH'])),
  methods: {
    submit() {
      store.commit('EXC_AUTH')
    }
  },
  name: 'My_nav',
}
</script>

<style scoped>

.My_nav{
  background: url("@/assets/main fon.jpg") 0 0/100% auto no-repeat;
  display: flex;
  flex-direction: row;
  height: 58px;
  position:relative;
}
.nav_logo{
  padding: 8px 0 8px 196px;
}
.logo{
  font-size: 36px;
  color: #FFFFFF;
  background: none;
  border: none;
}
.nav_button{
  position:absolute;
  right: 0;
  margin-right: 196px;
  top: 50%;
  transform: translate(0, -50%);
  display: flex;
  flex-direction: row;
}
.nav_reg{
  font-size: 24px;
  color: #FFFFFF;
  padding: 4px 10px 4px 10px;
  background: #4C758C;
  border-radius: 10px;
  border: none;
}
.nav_auto{
  font-size: 24px;
  color: #FFFFFF;
  padding: 4px 10px 4px 10px;
  margin-right: 10px;
  background: none;
  border: none;
}
</style>