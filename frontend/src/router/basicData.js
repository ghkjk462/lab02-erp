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
    {
      path: 'client',
      meta: { title: '客户管理', permission: 'client' },
      component: () => import('@/views/basicData/client/index'),
    },
  ],
}