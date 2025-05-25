export default {
  path: '/goods',
  name: 'goods',
  component: () => import('@/layouts/BaseLayout'),
  redirect: '/goods/information',
  children: [
    {
      path: 'information',
      meta: { title: '产品信息', permission: 'information' },
      component: () => import('@/views/goods/information/index'),
    },
  ],
}