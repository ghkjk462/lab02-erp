# 哈尔滨工业大学计算学部
# 2025 年春季学期《软件工程》
# Lab 2：项目计划与原型设计

## 1 实验要求

根据实验指导书中的要求完成的实验目标与过程。

实验目标：
- 根据项目需求建立用户故事清单，使用敏捷开发方法为用户故事建模卡片，设计优先级，估计工作量，构造迭代计划。
- 练习使用 CodeArts 或其他适当的 Scrum 项目管理工具为项目建立代计划。
- 练习使用大模型设计软件界面。
- 练习使用 MockPlus 或其他合适的原型设计工具为每个用户故事设计软件原型。

实验步骤：
科学小组数完成的 Project，完成以下任务：
- 整理讨论问题，提取所有用户故事清单；
- 为每个用户故事制作卡片；
- 分析用户故事的优先级；
- 组内成员共同表决和按重要程度，估算每用户故事的工作量；
- 整理以上结果，设计项目的迭代开发计划；
- 使用 CodeArts 或其他自选的 Scrum 项目管理工具建立和管理代计划；
- 选取一个用户故事，使用大模型进行界面设计；
- 使用 MockPlus 或其他合适的原型设计工具为选择的用户故事进行原型设计（GUI）。一一注意，此处至少需要 5 个用户故事的原型设计，且均为优先级最高的用户故事，不能包含重复、用户管理等自选任的故事。

## 2 项目概述

我们小组开发的是一个面向中小型企业的ERP仓储管理系统，旨在提供完整的企业资源管理解决方案，帮助企业实现业务流程自动化和数据可视化。该系统采用B/S架构，前端使用Vue框架开发，后端基于Django框架实现，数据库采用MySQL。系统主要功能模块包括库存管理（支持库存查询、入库管理、出库管理、库存预警）、采购管理（采购计划、采购开单、采购退货、供应商管理）、销售管理（销售开单、销售退货、客户管理）、基础数据管理（产品信息、产品分类、计量单位）以及系统管理（用户权限、系统设置、数据备份）等模块，通过这些功能模块的有机结合，为企业提供从采购、入库、销售到出库的完整业务流程管理，帮助企业提高运营效率、降低库存成本并优化资源配置。

系统名称：ERP仓储管理系统
团队成员：张三、李四、王五

## 3 用户故事

根据项目需求，分析用户故事。

### 3.1 用户故事清单及优先级

根据需求提取的用户故事，按照上业务价值和紧急程度排列优先级，优先级从高到低分为：最高、高、中、低、最低。

| 用户故事编号 | 用户角色 | 用户故事简称 | 用户故事描述 | 优先级(5-最高,1-最低) | 上游故事编号 |
|------------|---------|------------|------------|-------------------|--------------| 
| 1 | 仓库管理员 | 库存查询 | 作为仓库管理员，我希望能够查询当前所有产品的库存状态，以便及时了解库存情况 | 5 | - |
| 2 | 仓库管理员 | 入库管理 | 作为仓库管理员，我希望能够记录产品入库信息，以便准确跟踪库存增加情况 | 5 | 1, 9 |
| 3 | 仓库管理员 | 出库管理 | 作为仓库管理员，我希望能够记录产品出库信息，以便准确跟踪库存减少情况 | 5 | 1, 9 |
| 4 | 销售人员 | 销售记录查询 | 作为销售人员，我希望能够查询历史销售记录，以便了解销售情况和客户购买习惯 | 4 | 5, 13 |
| 5 | 销售人员 | 销售开单 | 作为销售人员，我希望能够创建销售订单，以便记录客户购买的产品和数量 | 4 | 1, 9, 13 |
| 6 | 采购人员 | 采购记录查询 | 作为采购人员，我希望能够查询历史采购记录，以便了解采购情况和供应商供货情况 | 4 | 7, 14 |
| 7 | 采购人员 | 采购开单 | 作为采购人员，我希望能够创建采购订单，以便记录从供应商购买的产品和数量 | 4 | 9, 14 |
| 8 | 系统管理员 | 员工账号管理 | 作为系统管理员，我希望能够管理员工账号，以便控制系统访问权限 | 3 | - |
| 9 | 产品经理 | 产品信息管理 | 作为产品经理，我希望能够管理产品信息，以便保持产品数据的准确性 | 3 | 15 |
| 10 | 数据分析师 | 库存报表查看 | 作为数据分析师，我希望能够查看库存报表，以便分析库存趋势和优化库存管理 | 2 | 1, 2, 3 |
| 11 | 数据分析师 | 销售报表查看 | 作为数据分析师，我希望能够查看销售报表，以便分析销售趋势和制定销售策略 | 2 | 4, 5 |
| 12 | 数据分析师 | 采购报表查看 | 作为数据分析师，我希望能够查看采购报表，以便分析采购趋势和优化采购策略 | 2 | 6, 7 |
| 13 | 客户关系经理 | 客户管理 | 作为客户关系经理，我希望能够管理客户信息，以便维护客户关系 | 2 | - |
| 14 | 采购经理 | 供应商管理 | 作为采购经理，我希望能够管理供应商信息，以便维护供应商关系 | 2 | - |
| 15 | 产品分类管理员 | 产品分类管理 | 作为产品分类管理员，我希望能够管理产品分类，以便更好地组织产品信息 | 2 | - |
| 16 | 系统用户 | 数据看板 | 作为系统用户，我希望能够在登录后看到重要数据的可视化展示，以便快速了解业务状况 | 1 | 1-15 |

### 3.2 用户故事详细描述

#### 3.2.1 用户故事1：库存查询

**正面：**

作为一个仓库管理员，我想要查询当前所有产品的库存状态，以便于及时了解库存情况，防止缺货或积压。

![库存查询示意图](img/inventory_query_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统显示所有产品的当前库存数量、库存状态（正常、预警、缺货）和库存位置信息
- 执行失败情况：
  - 无库存数据时显示"暂无库存数据"提示
  - 筛选条件无匹配结果时显示"未找到符合条件的库存信息"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.2 用户故事2：入库管理

**正面：**

作为一个仓库管理员，我想要记录产品入库信息，以便于准确跟踪库存增加情况，保证库存数据的准确性。

![入库管理示意图](img/stock_in_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建入库单据，更新相关产品库存数量，并生成入库操作记录
- 执行失败情况：
  - 产品信息不存在时提示"所选产品不存在，请先添加产品信息"
  - 入库数量为非正数时提示"入库数量必须大于0"
  - 入库单审核未通过时系统保留单据但标记状态为"未审核"
  - 系统故障时提示"保存失败，请重试"并记录错误日志

#### 3.2.3 用户故事3：出库管理

**正面：**

作为一个仓库管理员，我想要记录产品出库信息，以便于准确跟踪库存减少情况，确保库存数据实时反映实际情况。

![出库管理示意图](img/stock_out_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建出库单据，减少相关产品库存数量，并生成出库操作记录
- 执行失败情况：
  - 库存不足时提示"库存不足，无法完成出库操作"
  - 出库数量为非正数时提示"出库数量必须大于0"
  - 出库单审核未通过时系统保留单据但标记状态为"未审核"
  - 系统故障时提示"保存失败，请重试"并记录错误日志

#### 3.2.4 用户故事4：销售记录查询

**正面：**

作为一个销售人员，我想要查询历史销售记录，以便于了解销售情况和客户购买习惯，为销售策略提供数据支持。

![销售记录查询示意图](img/sales_record_query_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统显示符合查询条件的销售记录，包括客户信息、产品信息、销售金额和销售时间等
- 执行失败情况：
  - 无销售记录时显示"暂无销售记录"提示
  - 筛选条件无匹配结果时显示"未找到符合条件的销售记录"
  - 日期范围无效时提示"请输入有效的日期范围"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.5 用户故事5：销售开单

**正面：**

作为一个销售人员，我想要创建销售订单，以便于记录客户购买的产品和数量，准确追踪销售情况。

![销售开单示意图](img/sales_order_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建销售订单，更新相关产品库存，生成相应的出库单据，记录客户购买信息
- 执行失败情况：
  - 客户信息不存在时提示"请先选择或创建客户信息"
  - 产品库存不足时提示"产品库存不足，无法完成销售"
  - 销售金额为非正数时提示"销售金额必须大于0"
  - 订单审核未通过时系统保留订单但标记状态为"未审核"
  - 系统故障时提示"保存失败，请重试"并记录错误日志

#### 3.2.6 用户故事6：采购记录查询

**正面：**

作为一个采购人员，我想要查询历史采购记录，以便于了解采购情况和供应商供货情况，优化采购决策。

![采购记录查询示意图](img/purchase_record_query_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统显示符合查询条件的采购记录，包括供应商信息、产品信息、采购金额和采购时间等
- 执行失败情况：
  - 无采购记录时显示"暂无采购记录"提示
  - 筛选条件无匹配结果时显示"未找到符合条件的采购记录"
  - 日期范围无效时提示"请输入有效的日期范围"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.7 用户故事7：采购开单

**正面：**

作为一个采购人员，我想要创建采购订单，以便于记录从供应商购买的产品和数量，保证采购流程规范化。

![采购开单示意图](img/purchase_order_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建采购订单，生成相应的入库单据，记录供应商供货信息
- 执行失败情况：
  - 供应商信息不存在时提示"请先选择或创建供应商信息"
  - 产品信息不存在时提示"请先添加产品信息"
  - 采购金额为非正数时提示"采购金额必须大于0"
  - 订单审核未通过时系统保留订单但标记状态为"未审核"
  - 系统故障时提示"保存失败，请重试"并记录错误日志

#### 3.2.8 用户故事8：员工账号管理

**正面：**

作为一个系统管理员，我想要管理员工账号，以便于控制系统访问权限，保障系统安全。

![员工账号管理示意图](img/employee_account_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建、修改或删除员工账号，更新权限设置
- 执行失败情况：
  - 用户名已存在时提示"用户名已存在，请使用其他用户名"
  - 密码不符合安全要求时提示"密码必须包含字母和数字，且长度不少于8位"
  - 可以删除任何类型的账号，包括管理员账号
  - 系统故障时提示"操作失败，请重试"并记录错误日志

#### 3.2.9 用户故事9：产品信息管理

**正面：**

作为一个产品经理，我想要管理产品信息，以便于保持产品数据的准确性，支持库存管理和销售活动。

![产品信息管理示意图](img/product_info_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建、修改或删除产品信息，更新相关分类和属性
- 执行失败情况：
  - 产品编码已存在时提示"产品编码已存在，请使用其他编码"
  - 产品价格为非正数时提示"产品价格必须大于0"
  - 删除已有库存或交易记录的产品时提示"该产品有库存或交易记录，无法删除"
  - 系统故障时提示"操作失败，请重试"并记录错误日志

#### 3.2.10 用户故事10：库存报表查看

**正面：**

作为一个数据分析师，我想要查看库存报表，以便于分析库存趋势和优化库存管理，降低库存成本。

![库存报表示意图](img/inventory_report_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统生成并显示库存报表，包括库存统计、库存周转率、库存预警等数据
- 执行失败情况：
  - 无库存数据时显示"暂无库存数据，无法生成报表"
  - 日期范围无效时提示"请输入有效的日期范围"
  - 报表生成超时时提示"报表生成超时，请缩小查询范围或稍后再试"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.11 用户故事11：销售报表查看

**正面：**

作为一个数据分析师，我想要查看销售报表，以便于分析销售趋势和制定销售策略，提升销售业绩。

![销售报表示意图](img/sales_report_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统生成并显示销售报表，包括销售额统计、产品销量、客户购买频率等数据
- 执行失败情况：
  - 无销售数据时显示"暂无销售数据，无法生成报表"
  - 日期范围无效时提示"请输入有效的日期范围"
  - 报表生成超时时提示"报表生成超时，请缩小查询范围或稍后再试"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.12 用户故事12：采购报表查看

**正面：**

作为一个数据分析师，我想要查看采购报表，以便于分析采购趋势和优化采购策略，控制采购成本。

![采购报表示意图](img/purchase_report_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统生成并显示采购报表，包括采购额统计、供应商分析、采购频率等数据
- 执行失败情况：
  - 无采购数据时显示"暂无采购数据，无法生成报表"
  - 日期范围无效时提示"请输入有效的日期范围"
  - 报表生成超时时提示"报表生成超时，请缩小查询范围或稍后再试"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

#### 3.2.13 用户故事13：客户管理

**正面：**

作为一个客户关系经理，我想要管理客户信息，以便于维护客户关系，提供个性化服务。

![客户管理示意图](img/customer_management_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建、修改或删除客户信息，更新客户联系方式和交易记录
- 执行失败情况：
  - 客户编码已存在时提示"客户编码已存在，请使用其他编码"
  - 联系电话格式无效时提示"请输入有效的联系电话"
  - 删除有交易记录的客户时提示"该客户有交易记录，无法删除"
  - 系统故障时提示"操作失败，请重试"并记录错误日志

#### 3.2.14 用户故事14：供应商管理

**正面：**

作为一个采购经理，我想要管理供应商信息，以便于维护供应商关系，保证采购渠道畅通。

![供应商管理示意图](img/supplier_management_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建、修改或删除供应商信息，更新供应商联系方式和交易记录
- 执行失败情况：
  - 供应商编码已存在时提示"供应商编码已存在，请使用其他编码"
  - 联系电话格式无效时提示"请输入有效的联系电话"
  - 删除有交易记录的供应商时提示"该供应商有交易记录，无法删除"
  - 系统故障时提示"操作失败，请重试"并记录错误日志

#### 3.2.15 用户故事15：产品分类管理

**正面：**

作为一个产品分类管理员，我想要管理产品分类，以便于更好地组织产品信息，方便用户浏览和查询产品。

![产品分类管理示意图](img/product_category_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统成功创建、修改或删除产品分类，更新产品分类层次结构
- 执行失败情况：
  - 分类名称已存在时提示"分类名称已存在，请使用其他名称"
  - 分类层级超过限制时提示"分类层级最多支持三级"
  - 删除包含产品的分类时提示"该分类下有产品，无法删除"
  - 系统故障时提示"操作失败，请重试"并记录错误日志

#### 3.2.16 用户故事16：数据看板

**正面：**

作为一个系统用户，我想要在登录后看到重要数据的可视化展示，以便于快速了解业务状况，做出及时决策。

![数据看板示意图](img/dashboard_sketch.png)

**反面：**

确认信息：
- 执行成功结果：系统显示包含库存、销售、采购等关键数据的可视化图表和统计信息
- 执行失败情况：
  - 无数据时显示"暂无数据，无法生成看板"
  - 数据加载超时时提示"数据加载超时，请刷新页面或稍后再试"
  - 用户权限不足时只显示允许查看的数据，其他部分显示"无权限查看"
  - 系统故障时提示"系统繁忙，请稍后再试"并记录错误日志

## 4 用户故事的工作量估算

针对识别出的每一个故事，使用 Story Point 估算工作量，工作量的单位是天。
使用的范围是：1、2、1、2、3、5、8、13、20，单位为"小时"。
团队成员分别给出，拿结果大时讨论，达成分歧，再统计。

通常下列表格（表格里的估计工作量是三轮，每轮一位成员估计的结果，最不一致的地方，大家要讨论）：

| 故事编号 | 故事简称 | 小组成员对工作量估算 | | | 最终估算 |
|---------|--------|-------------------|---|---|--------|
| | | 第一轮 | 第二轮 | 第三轮 | |
| 1 | 库存查询 | 5 | 5 | 5 | 5 |
| 2 | 入库管理 | 8 | 8 | 8 | 8 |
| 3 | 出库管理 | 8 | 8 | 8 | 8 |
| 4 | 销售记录查询 | 5 | 5 | 5 | 5 |
| 5 | 销售开单 | 8 | 8 | 8 | 8 |
| 6 | 采购记录查询 | 5 | 5 | 5 | 5 |
| 7 | 采购开单 | 8 | 8 | 8 | 8 |
| 8 | 员工账号管理 | 5 | 5 | 5 | 5 |
| 9 | 产品信息管理 | 8 | 8 | 8 | 8 |
| 10 | 库存报表查看 | 5 | 5 | 5 | 5 |
| 11 | 销售报表查看 | 8 | 8 | 8 | 8 |
| 12 | 采购报表查看 | 8 | 8 | 8 | 8 |
| 13 | 客户管理 | 5 | 5 | 5 | 5 |
| 14 | 供应商管理 | 5 | 5 | 5 | 5 |
| 15 | 产品分类管理 | 5 | 5 | 5 | 5 |
| 16 | 数据看板 | 13 | 13 | 13 | 13 |

不是必须填写，可以有行选择某些用户故事进行，详细以填写为准，不以整个表格大模型生成为准。

## 5 迭代计划

基于项目目前需求设计，根据各用户故事的优先级和工作量估算，将用户故事分配到各次迭代中。计划总共进行两次迭代，每轮迭代的任务量、确保交付的任务排期合理，以及次迭代的总工作量。

请根据需求加如下表格的内容，加入你能想到的次迭代：

| 迭代轮数 | 包含的用户故事 | 故事的优先级 | 故事的工作量估计 | 计划完成时间 | 本次迭代的总工作量 |
|---------|-------------|------------|--------------|------------|---------------|
| 1 | 库存查询 | 5 | 5 | 第1周 | 60小时 |
| 1 | 入库管理 | 5 | 8 | 第1-2周 | |
| 1 | 出库管理 | 5 | 8 | 第1-2周 | |
| 1 | 销售记录查询 | 4 | 5 | 第2周 | |
| 1 | 销售开单 | 4 | 8 | 第2-3周 | |
| 1 | 采购记录查询 | 4 | 5 | 第3周 | |
| 1 | 采购开单 | 4 | 8 | 第3-4周 | |
| 1 | 员工账号管理 | 3 | 5 | 第4周 | |
| 1 | 产品信息管理 | 3 | 8 | 第4-5周 | |
| 2 | 库存报表查看 | 2 | 5 | 第6周 | 52小时 |
| 2 | 销售报表查看 | 2 | 8 | 第6-7周 | |
| 2 | 采购报表查看 | 2 | 8 | 第7-8周 | |
| 2 | 客户管理 | 2 | 5 | 第8周 | |
| 2 | 供应商管理 | 2 | 5 | 第8-9周 | |
| 2 | 产品分类管理 | 2 | 5 | 第9周 | |
| 2 | 数据看板 | 1 | 13 | 第9-10周 | |

## 6 使用 CodeArts 或其他工具管理用户故事和迭代计划

根据第3、4、5章节的内容，使用 CodeArts 或其他 Scrum 项目管理工具建立的项目管理计划，相应截图如下：

### 6.1 建立团队、项目、成员

![团队项目建立截图](img/team_setup.png)

### 6.2 Product Backlog（全部用户故事）

![Product Backlog截图](img/product_backlog.png)

### 6.3 Sprint Planning（规划迭代）

![Sprint Planning截图](img/sprint_planning.png)

### 6.4 形成每个 Sprint 的 Story Board

![Story Board截图](img/story_board.png)

### 6.5 形成每个 Sprint 的 Burndown Chart

![Burndown Chart截图](img/burndown_chart.png)

## 7 使用大模型辅助生成用户故事和迭代计划

如果采用了大模型辅助生成用户故事和迭代计划，此部分分析其优缺点。

大模型可以帮助我们快速生成用户故事的初始版本，提供了一个良好的起点。但在实际应用中，我们需要结合项目具体需求进行调整，确保用户故事的准确性和完整性。

## 8 原型设计

针对第3节识别出的用户故事，选取了5个用户故事使用大模型生成原型。

针对第3节识别出的每个用户故事，采用 MockPlus 或其他原型设计工具进行界面设计。

此处至少少需要 5 个用户故事的原型设计，且均为优先级最高的用户故事，不能包含重复、用户管理等自选任的故事。

### 8.1 用户故事名称(大模型生成的原型)

给出大模型生成的效果截图

### 8.2 用户故事1：库存查询

![库存查询原型](img/inventory_query.png)

### 8.3 用户故事2：入库管理

![入库管理原型](img/stock_in.png)

### 8.4 用户故事n：出库管理

![出库管理原型](img/stock_out.png)

## 9 计划与实际进度

| 任务名称 | 计划时间（小时） | 实际耗费时间（小时） | 提前或延期的原因分析 |
|---------|-------------------|-------------------|-------------------|
| 库存查询 | 5 | 4 | 团队成员对数据库查询有丰富经验，提前完成 |
| 入库管理 | 8 | 10 | 表单验证逻辑复杂，处理边缘情况耗时 |
| 出库管理 | 8 | 9 | 库存校验规则调整，增加了开发工作量 |
| 销售记录查询 | 5 | 5 | 按计划完成 |
| 销售开单 | 8 | 12 | 与财务模块集成遇到问题，解决接口冲突耗时 |
| 采购记录查询 | 5 | 4 | 复用了销售记录查询的部分代码，提高效率 |
| 采购开单 | 8 | 11 | 供应商数据格式不统一，数据处理耗时 |
| 员工账号管理 | 5 | 6 | 增加了权限验证的安全措施，增加工作量 |
| 产品信息管理 | 8 | 7 | 采用现有组件库，加快了开发进度 |

## 10 小结

利用大模型生成用户故事和项目计划，同小组进行讨论和效果检验等方面的评比；
利用大模型生成界面，同利用工具完成，在效果和效率等方面的对比。
其他方面的评价和总结。 