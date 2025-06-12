export default [
  {
    key: '2', name: '基础管理', icon: 'table', submenus: [
      { key: '/basicData/warehouse', name: '仓库管理'},
    ]
  },
  {
    key: '3', name: '产品管理', icon: 'appstore', submenus: [
      { key: '/goods/information', name: '产品信息' },
    ]
  },
  {
    key: '4', name: '采购管理', icon: 'shopping-cart', submenus: [
      { key: '/purchasing/purchase_create', name: '采购开单' },
      { key: '/purchasing/purchase_record', name: '采购记录' },
      { key: '/report/purchase_report', name: '采购报表'}
    ]
  },
  {
    key: '5', name: '销售管理', icon: 'shopping', submenus: [
      { key: '/sale/sale_create', name: '销售开单' },
      { key: '/sale/sale_record', name: '销售记录' },
      { key: '/report/sale_report', name: '销售报表'}
    ]
  },
  {
    key: '7', name: '库存管理', icon: 'database', submenus: [
      { key: '/warehouse/inStock', name: '入库管理' },
      { key: '/warehouse/outStock', name: '出库管理' },
      { key: '/report/stock_report', name: '库存报表' },
    ]
  },
  {
    key: '9', name: '系统管理', icon: 'team', submenus: [
      { key: '/account', name: '员工账号' },
      { key: '/basicData/client', name: '客户管理' },
      { key: '/basicData/supplier', name: '供应商管理' },
    ]
  },
]