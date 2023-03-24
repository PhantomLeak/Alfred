import Vue from 'vue';
import Router from 'vue-router';
import Alfred from '@/views/Alfred'
import Imitari from '@/views/Imitari'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Alfred',
      component: Alfred,
    },
    {
      path: '/imitari',
      name: 'Imitari',
      component: Imitari
    },
  ],
});