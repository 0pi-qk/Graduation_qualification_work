<template>
  <div class="Add_product">
    <p class="reg_title">Добавить товар</p>
    <form class="reg_form" @submit.prevent="submit">
      <table class="reg_tbl">
        <tbody>
        <tr>
          <td><p class="menu_text">Название</p></td>
          <td><input class="reg_body_input" v-model="name"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Описание</p></td>
          <td><input class="reg_body_input" v-model="description"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Цена</p></td>
          <td><input class="reg_body_input" v-model="price"></td>
        </tr>
        <tr>
          <td><p class="menu_text">Количество</p></td>
          <td><input class="reg_body_input" v-model="quantity"></td>
        </tr>
        <tr>
          <td><img class="reg_size" :src="PhotoPath+image" alt=""/></td>
          <td><input type="file" class="reg_body_input" accept="image/*" @change="imageUpload"></td>
        </tr>
        </tbody>
      </table>
      <button class="reg_body_button" type="submit">Добавить</button>
    </form>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import {variables_url} from "@/URLs";
import axios from "axios";

export default {
  name: "Add_product",

  data() {
    return {
      name: "",
      description: "",
      price: "",
      quantity: "",
      image: "1.jpg",
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  methods: {
    ...mapActions(['POST_PRODUCT']),

    imageUpload(event){
      let formData=new FormData();
      formData.append('file',event.target.files[0]);
      axios.post(variables_url.API_URL+"product/savefile",formData)
          .then((response)=>{
            this.image=response.data;
          });
    },

    submit(){
      this.POST_PRODUCT({
        name: this.name,
        description: this.description,
        price: this.price,
        quantity: this.quantity,
        image: this.image,
      })
      this.$router.push('/')
    }
  },
}
</script>

<style>
.Add_product{
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
.reg_size{
  width: 200px;
  height: 200px;
}
</style>
