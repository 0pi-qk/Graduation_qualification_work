import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/authorization',
    name: 'authorization',
    component: () => import('../views/Authorization.vue')
  },
  {
    path: '/registration',
    name: 'registration',
    component: () => import('../views/Registration.vue')
  },
  {
    path: '/info_user',
    name: 'info_user',
    component: () => import('../views/Info_user.vue')
  },
  {
    path: '/change_info_user',
    name: 'change_info_user',
    component: () => import('../views/Change_info_user.vue')
  },
  {
    path: '/bird_list',
    name: 'bird_list',
    component: () => import('../views/Bird_list.vue')
  },
  {
    path: '/add_bird',
    name: 'add_bird',
    component: () => import('../views/Add_bird.vue')
  },
  {
    path: '/info_bird/:id',
    name: 'info_bird',
    component: () => import('../views/Info_bird.vue')
  },
  {
    path: '/change_info_bird/:id',
    name: 'change_info_bird',
    component: () => import('../views/Change_info_bird.vue')
  },
  {
    path: '/product_list',
    name: 'product_list',
    component: () => import('../views/Product_list.vue')
  },
  {
    path: '/add_product',
    name: 'add_product',
    component: () => import('../views/Add_product.vue')
  },
  {
    path: '/change_info_product/:id',
    name: 'change_info_product',
    component: () => import('../views/Change_info_product.vue')
  },
  {
    path: '/online_store',
    name: 'online_store',
    component: () => import('../views/Online_store.vue')
  },
  {
    path: '/open_product/:id',
    name: 'open_product',
    component: () => import('../views/Open_product.vue')
  },
  {
    path: '/cart',
    name: 'cart',
    component: () => import('../views/Shopping_cart.vue')
  },
  {
    path: '/add_order',
    name: 'add_order',
    component: () => import('../views/Add_order')
  },
  {
    path: '/order_list',
    name: 'order_list',
    component: () => import('../views/Order_list.vue')
  },
  {
    path: '/descrypt_ring',
    name: 'descrypt_ring',
    component: () => import('../views/Descrypt_ring.vue')
  },
  {
    path: '/tree',
    name: 'tree',
    component: () => import('../views/Tree.vue')
  },
  {
    path: '/news',
    name: 'news',
    component: () => import('../views/News_feed.vue')
  },
  {
    path: '/open_news/:id',
    name: 'open_news',
    component: () => import('../views/Open_news.vue')
  },
  {
    path: '/add_news',
    name: 'add_news',
    component: () => import('../views/Add_news.vue')
  },
  {
    path: '/change_news/:id',
    name: 'change_news',
    component: () => import('../views/Change_news.vue')
  },
  {
    path: '/article',
    name: 'article',
    component: () => import('../views/Article.vue')
  },
  {
    path: '/open_article/:id',
    name: 'open_article',
    component: () => import('../views/Open_article.vue')
  },
  {
    path: '/add_article',
    name: 'add_article',
    component: () => import('../views/Add_article.vue')
  },
  {
    path: '/change_article/:id',
    name: 'change_article',
    component: () => import('../views/Change_article.vue')
  },
  {
    path: '/change_owner_bird',
    name: 'change_owner_bird',
    component: () => import('../views/Change_owner_bird.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
