<template>
  <div class="Authorization">
      <p class="auth_title">Авторизация</p>
      <form class="auth_body">
        <p class="auth_body_text">Логин</p>
        <input class="auth_body_input">
        <p class="auth_body_text">Пароль</p>
        <input type="password" class="auth_body_input" autocomplete="on"><br>
        <button class="auth_body_button">Войти</button>
        <p class="auth_body_text"  @click="$router.push('/registration')">Создать аккаунт</p>
      </form>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  computed: mapGetters((['GET_ID'])),
  name: 'Authorization',
}
</script>

<style scoped>
.Authorization{
  min-height: calc(100vh - 93px);
  text-align: center;
}
.auth_title{
  margin-top: 20px;
  color: #FFFFFF;
  font-size: 72px;
}
.auth_body{
  background: #85A1B0;
  margin: 25px 500px;
  height: 450px;
  border-radius: 10px;
}
.auth_body_text{
  padding: 25px 0;
  color: #FFFFFF;
  font-size: 24px;
}
.auth_body_input{
  background: #AECAD9;
  border: 2px solid #FFFFFF;
  width: 350px;
  color: #2c53a8;
  font-size: 20px;
  font-weight: 700;
}
.auth_body_button{
  font-size: 24px;
  color: #FFFFFF;
  background: #4C758C;
  margin: 50px 20%;
  padding: 4px 10px 4px 10px;
  border-radius: 10px;
  border: none;
}
</style>