<template>
  <div class="Info_user">
    <p class="reg_title">Данные аккаунта</p>
    <form class="reg_form" @submit.prevent="submit">
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Имя</p></td>
          <td><input class="reg_body_input" v-model="name"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Фамилия</p></td>
          <td><input class="reg_body_input" v-model="last_name"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Email</p></td>
          <td><input class="reg_body_input" v-model="email"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Логин</p></td>
          <td><input class="reg_body_input" v-model="login"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Роль</p></td>
          <td><input class="reg_body_input" v-model="role"></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" type="submit">Изменить данные</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "Info_user",

  methods: {
    ...mapActions(['GET_USER']),

    submit(){
      this.$router.push('/change_info_user')
    }
  },
  computed: {
    name: function() {
      return (this.$store.state.account.user)[0]?.name
    },
    last_name: function() {
      return (this.$store.state.account.user)[0]?.last_name
    },
    email: function() {
      return (this.$store.state.account.user)[0]?.email
    },
    login: function() {
      return (this.$store.state.account.user)[0]?.login
    },
    role: function() {
      return (this.$store.state.account.user)[0]?.role
    },
  },

  async mounted() {
    this.GET_USER();
  }
}
</script>

<style>
.Info_user{
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
