<template>
  <div>
    <a-card style="height: calc(50vh - 40px);">
      <div slot="title">
        <span>销售走势</span>
        <a-range-picker v-model="dateRange" :ranges="ranges" :disabled="loading" :allowClear="false"
          @change="changeDateRange" style="float: right;" />
        <div id="salesTrend" style="margin-top: 36px;"></div>
      </div>
    </a-card>
  </div>
</template>

<script>
  import { salesTrendList } from '@/api/system'
  import moment from 'moment'

  export default {
    name: 'Saleskucun',
    data() {
      return {
        ranges: {
          '7天': [moment().add(-7, 'days').startOf('day'), moment().endOf('day')],
          '15天': [moment().add(-15, 'days').startOf('day'), moment().endOf('day')],
          '30天': [moment().add(-30, 'days').startOf('day'), moment().endOf('day')],
        },
        dateRange: [moment().add(-7, 'days').startOf('day'), moment().endOf('day')],
        chart: null,
        loading: false,
      };
    },
    methods: {
      initialize() {
        let height = window.innerHeight / 2 - 141;
        this.chart = new window.G2.Chart({ container: 'salesTrend', autoFit: true, height, });
        this.chart.scale({ date: { range: [0, 1] }, total_sales_amount: { nice: true } });
        this.chart.tooltip({ showCrosshairs: true, shared: true });
        this.chart.line().position('date*total_sales_amount').color('#50799e').shape('smooth');
        this.chart.point().position('date*total_sales_amount').color('#50799e').shape('circle');
        this.list();
      },
      list() {
        let form = {
          start_date: this.dateRange[0].format('YYYY-MM-DD'),
          end_date: this.dateRange[1].format('YYYY-MM-DD'),
        };

        if (form.end_date) {
          form.end_date = moment(form.end_date).add(1, 'days').format('YYYY-MM-DD');
        }

        this.loading = true;
        salesTrendList(form).then(resp => {
          console.log('sealetrend');
          console.log(resp);
          let data = [...resp, ...this.fillData(resp)];
          this.chart.changeData(data);
          this.chart.forceFit();
        }).finally(() => {
          this.loading = false;
        });
      },
      changeDateRange(dateRange) {
        this.dateRange = dateRange;
        this.list();
      },
      fillData(items) {
        let startDate = moment(this.dateRange[0]);
        let endDate = moment(this.dateRange[1]);
        let days = endDate.diff(startDate, 'days');
        let fillItems = [];
        
        for (let i = 0; i <= days; i++) {
          let dateStr = startDate.format('YYYY-MM-DD');
          if (items.findIndex(item => item.date === dateStr) === -1) {
            fillItems.push({ date: dateStr, total_sales_amount: 0 });
          }
          startDate.add(1, 'days');
        }
        return fillItems;
      },
    },
    mounted() {
      this.initialize();
    },
  }
</script>

<style scoped>
</style>