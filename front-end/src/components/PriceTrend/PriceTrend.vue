<template>
  <div>
    <div class="tabs-group">
      <form @submit.prevent="getProvince">
        <Select v-model="cityChoose.selectProvince" style="width:100px" @on-change="changeProvince($event)"
          placeholder="请选择省份">
          <Option v-for="item in cityChoose.province" :value="item.province">{{item.province}}</Option>
        </Select>
      </form>
      <form @submit.prevent="getCity(cityChoose.selectProvince)">
        <Select v-model="cityChoose.selectCity" style="width:100px" @on-change="changeCity($event)" placeholder="请选择城市">
          <Option v-for="item in cityChoose.city" :value="item.city">{{item.city}}</Option>
        </Select>
      </form>
      <button type="submit" class="btn btn-primary" @change="getTrend(cityChoose.selectCity)">确定</button>
    </div>
    <div class="listcontent">
      <div>
        <h1 class="zsbt zsbtb mart0b10" v-text="cityChoose.selectCity">房均价较上月变动</h1>
      </div>
      <ul class="toplist w600 ablue">
        <li class="ws_text huise"><span class="txuh" v-text="cityChoose.selectCity">新房房价</span><b class="diqu"
            v-text="cityChoose.selectCity">二手房房价</b></li>
        <li class="ws_text huise"><b class="txuh" v-text="trendData.avg_new"><span class="diqu">(元/㎡)</span></b>
          <b class="txuh">环比上月<span class="diqu" v-text="trendData.trend_new"></span></b>
          <b class="txuh" v-text="trendData.avg_esf"><span class="diqu">(元/㎡)</span></b>
          <b class="txuh">环比上月<span class="diqu" v-text="trendData.trend_esf"></span></b></li>
      </ul>
    </div>
    <div class="que">
      <p v-text="cityChoose.selectCity">
        房价走势
      </p>
      <Select v-model="trendMap.selectMap" style="width:100px" placeholder="请选择显示内容" @change="changeMap($event)">
        <Option v-for="item in trendMap.mapChoose" :value="item.mapChoose">{{item.mapChoose}}</Option>
      </Select>
      <button type="submit" class="btn btn-primary" @change="initChart()">确定显示内容</button>
      <br>
      <div :class="trendMap.classPrefix">
        <div ref='myEchart' :class="trendMap.classPrefix+'_chart'"></div>
      </div>
      <br>
    </div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    name: "PriceTrend",
    data() {
      return {
        cityChoose: {
          selectProvince: "省份",
          province: [],
          selectCity: "城市",
          city: []
        },
        trendData: {
          avg_new: null,
          trend_new: null,
          avg_esf: null,
          trend_esf: null
        },
        trendMap: {
          classPrefix: "qst-tecs-src-teacher-dean-brokenLine_",
          mapChoose: ['近三年', '近一年'],
          selectMap: null,
          xNum: [],
          yNum: ['新房', '二手房'],
          series: [{
              name: '新房',
              type: 'line',
              stack: 'new',
              data: []
            },
            {
              name: '二手房',
              type: 'line',
              stack: 'esf',
              data: []
            },
          ], // 折线图数据
        }
      }
    },
    methods: {
      //获取省份
      getProvince() {
        const self = this;
        const path = '/api/tokens'
        self.$axios.get(path, {
            getProvince: {}
          })
          .then(function (response) {
            console.log(response);
            self.cityChoose.province = response.data.province; //赋值
          }).catch(function (error) {
            console.log(error);
          });
      },
      //选择省份
      changeProvince(event) {
        const self = this;
        self.selectProvince = event.target.value.province;
      },
      //获取城市
      getCity(province) {
        const self = this;
        const path = '/api/tokens'
        self.$axios.get(path, {
            getCity: {
              "province": province
            }
          })
          .then(function (response) {
            console.log(response);
            self.cityChoose.city = response.data.city;
          }).catch(function (error) {
            console.log(error);
          });
      },
      //选择城市
      changeCity(event) {
        const self = this;
        self.selectCity = event.target.value.city;
      },
      //获取趋势
      getTrend(city) {
        const self = this;
        const path = '/api/tokens'
        self.$axios.get(path, {
            getTrend: {
              "city": city
            }
          })
          .then(function (response) {
            console.log(response);
            self.trendData.avg_new = response.data.avg_new;
            self.trendData.trend_new = response.data.trend_new;
            self.trendData.avg_esf = response.data.avg_esf;
            self.trendData.trend_esf = response.data.trend_esf;
          }).catch(function (error) {
            console.log(error);
          });
      },
      //选择展示图
      changeMap(event) {
        const self = this;
        self.trendMap.selectMap = event.target.value.mapChoose;
        if (self.trendMap.selectMap = '近三年')
          self.trendMap.xNum = ['2018', '2019', '2020']
        const path1 = '/api/tokens'
        self.$axios.get(path1, {
            getThree: {
              "city": self.cityChoose.selectCity
            }
          })
          .then(function (response) {
            console.log(response);
            self.trendMap.series = [{
              name: '新房',
              type: 'line',
              stack: 'new',
              data: response.data.avg_new
            }, {
              name: '新房',
              type: 'line',
              stack: 'new',
              data: response.data.avg_esf
            }]
          }).catch(function (error) {
            console.log(error);
          });
        if (self.trendMap.selectMap = '近一年')
          self.trendMap.xNum = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
        const path2 = '/api/tokens'
        self.$axios.get(path2, {
            getOne: {
              "city": self.cityChoose.selectCity
            }
          })
          .then(function (response) {
            console.log(response);
            self.trendMap.series = [{
              name: '新房',
              type: 'line',
              stack: 'new',
              data: response.data.avg_new
            }, {
              name: '新房',
              type: 'line',
              stack: 'new',
              data: response.data.avg_esf
            }]
          }).catch(function (error) {
            console.log(error);
          });
      },
      // 图表初始化数据
      initChart() {
        let myChart = echarts.init(this.$refs.myEchart);
        myChart.setOption({
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: this.trendMap.yNum,
          },
          grid: {
            left: '3%',
            right: '6%',
            bottom: '3%',
            top: '12%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: this.trendMap.xNum,
            axisLabel: {
              interval: 0,
              rotate: -60
            }
          },
          yAxis: {
            type: 'value',
            min: 0,
            max: 100,
            interval: 20,
            axisLabel: {
              formatter: '{value} %'
            }
          },
          series: this.trendMap.series,
        })
      },
    },
  }
</script>

<style scoped>

</style>