<template>
  <div class="Change_owner_bird">
    <p class="reg_title">Смена владельца</p>
    <div class="reg_form">
      <p class="menu_text">Передать права</p>
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Номер птицы</p></td>
          <td><input class="reg_body_input" v-model="number"></td>
        </tr>
        <tr>
          <td><button class="reg_body_button" @click="generate_code">Сгенерировать</button></td>
          <td><button class="reg_body_button" @click="cancellation">Отменить</button></td>
        </tr>
        <tr>
          <td><p class="menu_text">Код для получения</p></td>
          <td><input class="reg_body_input" v-model="get_code"></td>
        </tr>
        </tbody>
      </table>
      <p class="menu_text">Получить права</p>
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Введите код</p></td>
          <td><input class="reg_body_input" v-model="set_code"></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" @click="add">Добавить</button>
      <p></p>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import uniqid from 'uniqid';

export default {
  name: "Change_owner_bird",

  data() {
    return {
      number: "",
      get_code: "",
      set_code: "",
    }
  },

  methods: {
    ...mapActions(['GET_BIRD', 'GET_EXCHANGE', 'POST_EXCHANGE', 'PUT_EXCHANGE', 'POST_BIRD', 'DEL_BIRD']),

    generate_code(){
      const bird = this.ALL_BIRD.filter(t => t.number === this.number);
      const exch = this.ALL_EXCHANGE.filter(t => t.bird === bird[0]?.id);
      if(bird[0]?.user > -1) {
        for(const item in exch)
          if (exch[item].status === 'Active') {
            this.get_code = exch[item].code;
            return
          }
        this.get_code = uniqid()
        this.POST_EXCHANGE({
          user_former: this.GET_ID,
          bird: bird[0]?.id,
          code: this.get_code,
          status: "Active",
        })
      }
    },

    cancellation(){
      const bird = this.ALL_BIRD.filter(t => t.number === this.number);
      const exch = this.ALL_EXCHANGE.filter(t => t.bird === bird[0]?.id);
      if(bird[0]?.user > -1)
        for(const item in exch)
          if (exch[item].status === 'Active')
            this.PUT_EXCHANGE({
              id: Number(exch[item].id),
              user_former: this.GET_ID,
              bird: bird[0]?.id,
              code: this.get_code,
              status: "Canceled",
            })
      this.get_code = "";
      this.number = "";
    },

    add() {
      const exch = this.ALL_EXCHANGE.filter(t => t.code === this.set_code);
      console.log(exch)
      if (exch.length === 0 || this.set_code === "")
        return
      const bird = this.ALL_BIRD.filter(t => t.id === exch[0]?.bird);
      this.POST_BIRD({
        user: this.GET_ID,
        number: bird[0]?.number,
        name: bird[0]?.name,
        date_of_birth: bird[0]?.date_of_birth,
        parent1: bird[0]?.parent1,
        parent2: bird[0]?.parent2,
        gender: bird[0]?.gender,
      })
      this.DEL_BIRD({
        id: Number(bird[0]?.id),
      })
      this.set_code = "";
    }

  },
  computed: {
    ...mapGetters(['ALL_BIRD', 'ALL_EXCHANGE', 'GET_ID']),
  },

  async mounted() {
    this.GET_BIRD(true);
    this.GET_EXCHANGE();
  }
}
</script>

<style>
.Change_owner_bird{
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
.reg_size{
  width: 200px;
  height: 200px;
}
</style>
