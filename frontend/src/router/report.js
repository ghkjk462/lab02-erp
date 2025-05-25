export default {
  path: '/report',
  name: 'report',
  component: () => import('@/layouts/BaseLayout'),
  redirect: '/report/stock_report',
  children: [
    {
      path: 'stock_report',
      meta: { title: '库存报表', permission: 'stock_report' },
      component: () => import('@/views/report/stockReport/index'),
    },
  ],
}