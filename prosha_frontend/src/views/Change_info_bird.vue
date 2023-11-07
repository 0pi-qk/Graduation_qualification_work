<template>
  <div class="Change_info_bird">
    <p class="reg_title">Изменить данные о птице</p>
    <form class="reg_form" @submit.prevent="submit">
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Номер</p></td>
          <td><input class="reg_body_input" v-model="number"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Имя</p></td>
          <td><input class="reg_body_input" v-model="name"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Д/Р</p></td>
          <td><input class="reg_body_input" v-model="date_of_birth" placeholder="2000-09-31"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Пол</p></td>
          <td>
            <select class="reg_body_input" v-model="gender">
              <option class="reg_body_input" value="">-- Выберите пол--</option>
              <option class="reg_body_input" value="Male">Male</option>
              <option class="reg_body_input" value="Female">Female</option>
              <option class="reg_body_input" value="None">None</option>
            </select>
          </td>
        </tr>
        <tr>
          <td><p class="menu_text">Род. 1</p></td>
          <td><input class="reg_body_input" v-model="parent1"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Род. 2</p></td>
          <td><input class="reg_body_input" v-model="parent2"></td>
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
  name: "Change_info_bird",

  data() {
    return {
      number: "",
      name: "",
      date_of_birth: "",
      gender: "",
      parent1: "",
      parent2: "",
    }
  },

  methods: {
    ...mapActions(['PUT_BIRD']),

    submit(){
      this.PUT_BIRD({
        id: this.$route.params.id,
        user: this.user,
        number: this.number,
        name: this.name,
        date_of_birth: this.date_of_birth,
        parent1: this.parent1,
        parent2: this.parent2,
        gender: this.gender
      })
      this.$router.push('/')
    }
  },
  computed: {
    user: function() {
      return (this.$store.state.account.thisId)
    },
  },

}
</script>

<style>
.Change_info_bird{
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
