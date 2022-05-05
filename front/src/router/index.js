import { createRouter, createWebHistory } from 'vue-router'
import menu from '../pages/menu/MenuPage.vue'
import home from '../pages/home/HomePage.vue'
import menus from '../pages/menus/MenusPage.vue'
import MenuAddPage from '../pages/menu-add/MenuAddPage.vue'
import MenuModifyPage from '../pages/menu-modify/MenuModifyPage.vue'
import landing from '../pages/landing/LandingPage.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path :'/menus/by-date/:date',
    name : 'Menu',
    component: menu
  },
  {
    path :'/menus',
    name : 'Menus',
    component: menus
  },
  {
    path: '/menu/add/:date',
    name: 'MenuAddPage',
    component: MenuAddPage
  },
  {
    path: '/menu/modify',
    name: 'MenuModifyPage',
    component: MenuModifyPage
  },
  {
    path :'/menus/today/:name_restaurant',
    name : 'MenuToday',
    component: landing
  },
  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
