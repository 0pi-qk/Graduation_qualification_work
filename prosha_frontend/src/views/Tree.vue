<template>
  <div class="Tree">
    <p class="reg_title">Генеалогическое древо</p>
    <form @submit.prevent="submit" class="reg_form">
      <table class="reg_tbl">
        <tbody>
          <td><p class="menu_text">Номер птицы:</p></td>
          <td><input class="reg_body_input" v-model="number_bird"></td>
          <td><button class="reg_body_button" type="submit">Найти</button></td>
        </tbody>
      </table>
    </form>
    <div class="tree" v-html="tree"></div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";


export default {
  name: "Tree",

  data(){
    return {
      number_bird: "",
      tree: ""
    }
  },

  computed: mapGetters(['ALL_BIRD']),

  methods: {
    ...mapActions(['GET_BIRD']),

    submit(){
      function toHTML(bird_list, number) {
        const result = bird_list.find(e => e.number == number);
        if (result) {
          let out = "<li>" + result.number, get_res;
          if (result.parent1 || result.parent2) {
            out += "<ul>";
            if (result.parent1) {
              get_res = toHTML(bird_list, result.parent1);
              if (typeof get_res != 'undefined')
                out += get_res;
              else
                out += "<li>" + result.parent1 + "</li>";
            }
            if (result.parent2) {
              get_res = toHTML(bird_list, result.parent2);
              if (typeof get_res != 'undefined')
                out += get_res;
              else
                out += "<li>" + result.parent2 + "</li>";
            }
            out += "</ul>";
          }
          out += "</li>";
          return out;
        }
      }
      this.tree = "<ul>" + toHTML(this.ALL_BIRD, this.number_bird) + "</ul>";
    }
  },

  async mounted() {
    this.GET_BIRD(true);
  }
}
</script>

<style>
.Tree{
  min-height: calc(100vh - 93px);
  text-align: center;
}
.tree{
  background: #85A1B0;
  margin: 25px 200px;
  height: 600px;
  border-radius: 10px;
  overflow-y:scroll;
  overflow-x:scroll;
}
.tree ul {
  padding-top: 20px; position: relative;

  transition: all 0.5s;
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;

  margin: 20px 10px 10px 10px;
  font-size: 24px;
  color: #FFFFFF;
}

.tree li {
  float: left; text-align: center;
  list-style-type: none;
  position: relative;
  padding: 20px 5px 0 5px;

  transition: all 0.5s;
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;

  margin: 20px 10px 10px 10px;
  font-size: 24px;
  color: #FFFFFF;
}

.tree li::before, .tree li::after{
  content: '';
  position: absolute; top: 0; right: 50%;
  border-top: 1px solid #ccc;
  width: 50%; height: 20px;
}
.tree li::after{
  right: auto; left: 50%;
  border-left: 1px solid #ccc;
}

.tree li:only-child::after, .tree li:only-child::before {
  display: none;
}
.tree li:only-child{ padding-top: 0;}
.tree li:first-child::before, .tree li:last-child::after{
  border: 0 none;
}
.tree li:last-child::before{
  border-right: 1px solid #ccc;
  border-radius: 0 5px 0 0;
  -webkit-border-radius: 0 5px 0 0;
  -moz-border-radius: 0 5px 0 0;
}
.tree li:first-child::after{
  border-radius: 5px 0 0 0;
  -webkit-border-radius: 5px 0 0 0;
  -moz-border-radius: 5px 0 0 0;
}
.tree ul ul::before{
  content: '';
  position: absolute; top: 0; left: 50%;
  border-left: 1px solid #ccc;
  width: 0; height: 20px;
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
.reg_title{
  margin-top: 20px;
  color: #FFFFFF;
  font-size: 72px;
}
.reg_form{
  background: #85A1B0;
  margin: 25px 200px;
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
