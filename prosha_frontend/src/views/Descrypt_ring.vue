<template>
  <div class="Descrypt_ring">
    <p class="reg_title">Расшифровка кольца</p>
    <div class="reg_form">
      <div class="ring">
        <div class="column">
          <img src="@/assets/ring_2.jpg" class="ring_img" alt=""/>
        </div>
        <div class="column">
          <p class="ring_text">Введите номер кольца</p>
          <input class="reg_body_input" v-model="number_bird" placeholder="ECOG44C12003"><br>
          <p class="ring_text">Расшифрованная информация</p>
          <p class="ring_text">{{ number_bird.substr(0, 3) }} - Страна</p>
          <p class="ring_text">{{ number_bird.substr(3, 1) }} - Клуб</p>
          <p class="ring_text">{{ number_bird.substr(4, 2) }} - Заводчик</p>
          <p class="ring_text">{{ number_bird.substr(6, 1) }} - Размер кольца</p>
          <p class="ring_text">{{ number_bird.substr(7, 2) }} - Год рождения</p>
          <p class="ring_text">{{ number_bird.substr(9, 3) }} - Порядковый номер</p>
          <button class="reg_body_button" @click="$router.push('/')">Вернуться назад</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Descrypt_ring",

  data() {
    return {
      number_bird: "",
    }
  },
}
</script>

<style>
.Descrypt_ring{
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
.ring_text{
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
.ring_img{
  width: 350px;
  height: 500px;
  margin-top: 25px;
  margin-bottom: 14px;
  border-radius: 10px;
}
.ring{
  margin: 0 166px;
  display: flex;
  justify-content: center;
}
</style>
