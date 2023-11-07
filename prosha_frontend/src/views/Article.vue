<template>
  <div class="Article">
    <p class="reg_title">Статьи</p>
    <div class="shop">
      <div class="shop_elem" v-for="item in paginatedData">
        <img :src="PhotoPath+item.image" class="prod_img" alt=""/>
        <p class="prod_text">{{ item.title }}</p>
        <p class="prod_text">{{ item.description.substr(0, 20) }} ...</p>
        <button class="reg_body_button" @click="$router.push('/open_article/' + item.id)">Прочитать</button>
        <button v-if="GET_AUTH === 4" class="reg_body_button" @click="DEL_ARTICLE(item)">Убрать</button>
        <button v-if="GET_AUTH === 4" class="reg_body_button" @click="$router.push('/change_article/' + item.id)">Изменить</button>
      </div>
    </div>
    <button class="reg_body_button2" @click="prevPage" :disabled="pageNumber == 0">Предыдущая страница</button>
    <button class="reg_body_button2" @click="nextPage" :disabled="pageNumber >= pageCount -1">Следующая страница</button>
    <p class="prod_text">Текущая страница: {{ pageNumber +1}}</p>
    <button v-if="GET_AUTH === 4" class="reg_body_button2" @click="$router.push('/add_article')">Добавить статью</button>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Article",

  data(){
    return {
      pageNumber: 0,
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  props:{
    size:{
      type:Number,
      required:false,
      default: 4
    }
  },

  methods: {
    ...mapActions(['GET_ARTICLE', 'DEL_ARTICLE']),

    nextPage(){
      this.pageNumber++;
    },
    prevPage(){
      this.pageNumber--;
    },
  },

  computed: {
    ...mapGetters(['ALL_ARTICLE', 'GET_AUTH']),

    pageCount(){
      let l = this.ALL_ARTICLE.length,
          s = this.size;
      return Math.ceil(l/s);
    },

    paginatedData(){
      const start = this.pageNumber * this.size,
          end = start + this.size;
      return this.ALL_ARTICLE?.slice(start, end);
    },
  },

  async mounted() {
    this.GET_ARTICLE();
  }
}
</script>

<style>
.Article{
  min-height: calc(100vh - 93px);
  text-align: center;
}
.prod_img{
  width: 350px;
  height: 200px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.prod{
  margin: 0 25px;
  display: flex;
  justify-content: center;
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
  grid-template-columns: repeat(2, 1fr);
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
