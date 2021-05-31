import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Courses from '../views/Courses.vue'
import Course from '../views/Course.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/courses',
    name: 'Courses',
    component: Courses
  },
  {
    path: '/courses/info/:id',
    name: 'Course',
    component: Course
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
