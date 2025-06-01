export default {
  path: '/report',
  name: 'report',
  component: () => import('@/layouts/BaseLayout'),
  redirect: '/report/stock_report', // 默认
  children: [
    {
      path: 'stock_report',
      meta: { title: '库存报表', permission: 'stock_report' },
      component: () => import('@/views/report/stockReport/index'),
    },
    {
      path: 'sale_report',
      meta: { title: '销售报表', permission: 'sale_report' },
      component: () => import('@/views/report/saleReport/index'),
    },
  ],
}