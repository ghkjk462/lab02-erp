import VueRouter from 'vue-router'
import user from './user'
import account from './account'
import manage from './manage'
import system from './system'
import report from './report'
import basicData from './basicData'
import goods from './goods'
import purchasing from './purchasing'
import sale from './sale'
import warehouse from './warehouse'


const index = {
  path: '/',
  component: () => import('@/layouts/BaseLayout'),
  redirect: '/user/login',
  children: [
    {
      path: '/home',
      name: 'home',
      meta: { title: '首页' },
      component: () => import('@/views/home/Home'),
    },
  ]
}

const routes = [index, user, account, manage, system, report, basicData, goods, purchasing, sale, warehouse];

export default new VueRouter({ mode: 'hash', routes })
