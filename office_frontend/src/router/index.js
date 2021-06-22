import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/components/Main.vue'
import OfficeDetail from '@/components/office/OfficeDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/office-detail',
    name: 'OfficeDetail',
    component: OfficeDetail
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
