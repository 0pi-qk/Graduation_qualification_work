import { createStore } from 'vuex'

import account from "@/store/modules/account";
import address from "@/store/modules/address";
import bird from "@/store/modules/bird";
import exchange from "@/store/modules/exchange";
import news from "@/store/modules/news";
import starnews from "@/store/modules/starnews";
import article from "@/store/modules/article";
import stararticle from "@/store/modules/stararticle";
import product from "@/store/modules/product";
import starproduct from "@/store/modules/starproduct";
import onlineorder from "@/store/modules/onlineorder";
import orderproduct from "@/store/modules/orderproduct";
import cart from "@/store/modules/cart";


export default createStore({
  modules: {
    account,
    address,
    bird,
    exchange,
    news,
    starnews,
    article,
    stararticle,
    product,
    starproduct,
    onlineorder,
    orderproduct,
    cart,
  }
})
