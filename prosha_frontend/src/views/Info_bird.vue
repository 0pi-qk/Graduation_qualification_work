<template>
  <div class="Info_bird">
    <p class="reg_title">Информация о птице</p>
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
          <td><input class="reg_body_input" v-model="gender"></td>
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
      <button class="reg_body_button" type="submit">Изменить</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "Info_bird",

  methods: {
    ...mapActions(['GET_BIRD_ID']),

    submit(){
      this.$router.push('/change_info_bird/'+this.$route.params.id)
    }
  },
  computed: {
    number: function() {
      return (this.$store.state.bird.bird)[0]?.number
    },
    name: function() {
      return (this.$store.state.bird.bird)[0]?.name
    },
    date_of_birth: function() {
      return (this.$store.state.bird.bird)[0]?.date_of_birth
    },
    gender: function() {
      return (this.$store.state.bird.bird)[0]?.gender
    },
    parent1: function() {
      return (this.$store.state.bird.bird)[0]?.parent1
    },
    parent2: function() {
      return (this.$store.state.bird.bird)[0]?.parent2
    },
  },

  async mounted() {
    this.GET_BIRD_ID(this.$route.params.id);
  }
}
</script>

<style>
.Info_bird{
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
