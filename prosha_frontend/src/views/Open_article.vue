<template>
  <div class="Open_article">
    <p class="reg_title"> {{ (this.ALL_ARTICLE)[0]?.title }} </p>
    <div class="shop">
      <div class="shop_elem">
        <star-rating v-if="GET_AUTH === 0" :read-only="true" class="prod_text" :rating="star1" @update:rating="setRating" :star-size="20"></star-rating>
        <star-rating v-else class="prod_text" :rating="star1" @update:rating="setRating" :star-size="20"></star-rating>
        <img :src="PhotoPath+(this.ALL_ARTICLE)[0]?.image" class="prod_img" alt=""/>
        <p class="prod_text">{{ (this.ALL_ARTICLE)[0]?.description }}</p>
        <button class="reg_body_button" @click="$router.push('/article')">Вернуться к списку</button>
      </div>
    </div>
  </div>
</template>

<script>
import {variables_url} from '@/URLs'
import {mapActions, mapGetters} from "vuex";
import StarRating from 'vue-star-rating'

export default {
  name: "Open_article",

  components: {
    StarRating
  },

  data(){
    return {
      PhotoPath: variables_url.MEDIA_URL,
    }
  },

  methods: {
    ...mapActions(['GET_STARARTICLE', 'GET_ARTICLE_ID', 'POST_STARARTICLE', 'PUT_STARARTICLE']),

    setRating(star){
      const tmp = this.ALL_STARARTICLE.filter(t => t.user === this.GET_ID)
      if (tmp[0]?.user > -1)
        this.PUT_STARARTICLE({
          id: tmp[0]?.id,
          user: this.GET_ID,
          article: this.$route.params.id,
          evaluation: star,
        })
      else{
        this.POST_STARARTICLE({
          user: this.GET_ID,
          article: this.$route.params.id,
          evaluation: star,
        })
      }
    },
  },

  computed: {
    ...mapGetters((['GET_AUTH', 'GET_ID', 'ALL_STARARTICLE', 'ALL_ARTICLE'])),

    star1: function (){
      const tmp = this.ALL_STARARTICLE.filter(t => t.user === this.GET_ID)
      if (tmp[0]?.user > -1)
        return tmp[0]?.evaluation
      else {
        let sum = 0;
        for(const item in this.ALL_STARARTICLE)
          sum += this.ALL_STARARTICLE[item].evaluation;
        if (Object.keys(this.ALL_STARARTICLE).length === 0)
          return 0
        else
          return sum / Object.keys(this.ALL_STARARTICLE).length;
      }
    },

  },
  async mounted() {
    this.GET_ARTICLE_ID(this.$route.params.id);
    this.GET_STARARTICLE(this.$route.params.id);
  }
}
</script>

<style>
.Open_article{
  min-height: calc(100vh - 93px);
  text-align: center;

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
