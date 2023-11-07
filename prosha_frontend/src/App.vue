<template>
  <div class="app">
    <My_nav/>
    <router-view/>
    <My_footer/>
  </div>
</template>

<script>
import My_nav from "@/components/My_nav";
import My_footer from "@/components/My_footer";

export default {
  components:{
    My_nav,
    My_footer
  }
}

</script>

<style>
:root { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  :root { font-family: 'Inter var', sans-serif; }
}
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Inter;
}
.app{
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

</style>

