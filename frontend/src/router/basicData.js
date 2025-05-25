export default {
  path: '/basicData',
  name: 'basicData',
  component: () => import('@/layouts/BaseLayout'),
  redirect: '/basicData/warehouse',
  children: [
    {
      path: 'warehouse',
      meta: { title: '仓库', permission: 'warehouse' },
      component: () => import('@/views/basicData/warehouse/index'),
    },
  ],
}