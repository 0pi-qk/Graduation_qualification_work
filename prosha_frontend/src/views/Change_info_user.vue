<template>
  <div class="Change_info_user">
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
          <td><p class="menu_text">Сменить пароль:</p></td>
        </tr>
        <tr>
          <td><p class="menu_text">Пароль</p></td>
          <td><input class="reg_body_input" v-model="password"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Пароль 2</p></td>
          <td><input class="reg_body_input" v-model="password2"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Роль</p></td>
          <td>
            <select class="reg_body_input" v-model="role">
              <option class="reg_body_input" value="">-- Выберите роль--</option>
              <option class="reg_body_input" value="User">User</option>
              <option class="reg_body_input" value="Breeder">Breeder</option>
            </select>
          </td>
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
  name: "Change_info_user",

  data() {
    return {
      name: "",
      last_name: "",
      email: "",
      login: "",
      password: "",
      password2: "",
      role: "",
    }
  },

  methods: {
    ...mapActions(['PUT_USER']),

    submit(){
      this.PUT_USER({
        id: this.id,
        name: this.name,
        last_name: this.last_name,
        email: this.email,
        login: this.login,
        password: this.password,
        role: this.role
      })

    }
  },
  computed: {
    id: function() {
      return (this.$store.state.account.user)[0]?.id
    },
  },

}
</script>

<style>
.Change_info_user{
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
