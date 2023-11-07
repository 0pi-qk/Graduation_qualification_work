<template>
  <div class="Add_article"><br>
    <input class="reg_body_input" v-model="title">
    <div class="shop">
      <form @submit.prevent="submit" class="shop_elem">
        <img :src="PhotoPath+image" class="prod_img" alt=""/>
        <input type="file" class="reg_body_input" accept="image/*" @change="imageUpload"><br>
        <textarea class="reg_body_input2" v-model="description"></textarea><br>
        <button class="reg_body_button" type="submit">Сохранить</button>
      </form>
    </div>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'
import {mapActions, mapGetters} from "vuex";
import axios from "axios";

export default {
  name: "Add_article",

  data(){
    return {
      title: "",
      description: "",
      image: "1.jpg",
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  methods: {
    ...mapActions(['POST_ARTICLE']),

    imageUpload(event){
      let formData=new FormData();
      formData.append('file',event.target.files[0]);
      axios.post(variables_url.API_URL+"article/savefile",formData)
          .then((response)=>{
            this.image=response.data;
          });
    },

    submit(){
      this.POST_ARTICLE( {
        user: this.GET_ID,
        title: this.title,
        description: this.description,
        date_of_publication: new Date().toISOString().slice(0, 10),
        image: this.image,
      })
      this.$router.push('/article')
    }
  },

  computed: mapGetters(['GET_ID']),
}
</script>

<style>
.Add_article{
  min-height: calc(100vh - 93px);
  text-align: center;

}
.reg_body_input{
  background: #AECAD9;
  border: 2px solid #FFFFFF;
  color: #2c53a8;
  font-size: 20px;
  font-weight: 700;
  width: 325px;
}
.reg_body_input2{
  background: #AECAD9;
  border: 2px solid #FFFFFF;
  color: #2c53a8;
  font-size: 20px;
  font-weight: 700;
  width: 900px;
  height: 450px;
  overflow-y:scroll;

}
.prod_img{
  width: 900px;
  height: 450px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.reg_title{
  margin-top: 20px;
  color: #FFFFFF;
  font-size: 72px;
}
.prod_text{
  margin: 20px 10px 10px 10px;
  font-size: 24px;
  color: #FFFFFF;
  word-break: break-all;
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
.reg_body_button2{
  font-size: 24px;
  color: #FFFFFF;
  background: #85A1B0;
  margin: 25px 25px;
  padding: 4px 10px 4px 10px;
  border-radius: 10px;
  border: none;
}
.shop{
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(1, 1fr);
  justify-items: center;
  align-items: center;
}
.shop_elem{
  background: #85A1B0;
  width: calc(100% - 332px);
  margin: 20px 10px 10px 10px;
  border-radius: 10px;
  text-align: center;
}

</style>
