<template>

  <div>

    <!-- Panel Header -->
    <div class="card-block g-pa-0">
      <form class="form-inline" @submit.prevent="onSubmit">
        <div class="form-group">

          <label for="exampleInputName2">省份：</label>
          <div class="col-sm-2">
            <select id="citySel" v-model="proval" @change="pr_onchange($this.options[this.options.selectedIndex].text)"
              placeholder="请选择省份" class='form-control' style="width:200px;" data-live-search="true" name='province'>
              <option value="">请选择省份</option>
              <option v-for="(item, index) in newhousedata" v-bind:key="index">{{item.province}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="exampleInputEmail2">城市：</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="city" style="width:200px;" size="1" data-live-search="true" id='city'
              name='city'>
              <option v-for="(item, index) in choosecity" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div>
          <button type="submit" style="margin-left:20px" class="btn btn-primary">Submit</button>
        </div>
      </form>
      <hr class="g-brd-gray-light-v4 g-my-30">
    </div>
    <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
      <div>
      </div>
      <h3 class="h6 mb-0">
        <i class="icon-media-043  g-pos-rel g-top-2 g-mr-5"></i> 房价走势图 <small v-if="newhouse">(共
          {{ newhouse._meta.total_items }} 个, {{ newhouse._meta.total_pages }} 页)</small>
      </h3>
      <div class="dropdown g-mb-10 g-mb-0--md">
        <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown"
          aria-haspopup="true" aria-expanded="false">
        </span>
      </div>
    </div>
    <!-- End Panel Header -->

    <!-- Striped Rows -->
    <div class="card g-brd-teal rounded-0 g-mb-30">

   
      <div id="container">
      </div>
    
    </div>
    <!-- End Striped Rows -->


    <!-- Pagination #04 -->
    <!-- element风格按钮 -->
    <!-- <el-button type="success" icon="el-icon-arrow-left" @click="prevPage()">上一页</el-button>
    <span>第{{currentPage}}页/共{{totalPage}}页</span>
    <el-button type="success" @click="nextPage()">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button> -->
    <!-- End Pagination #04 -->

  </div>
</template>


<script>
  export default {
    name: 'HouseQushi',
    components: {

    },
    data() {
      return {
        proval: '',
        data: '',
        chooseprovince: '',
        newhousedata: [],
        provincedata: [],
        choosecity: [],
        housedata: [],
        province: '',
        city: '',
        // 趋势数据
        trenddatas: '',

      }
    },
    methods: {

      getMessage() {
        const path = '/api/houseaddress3'
        this.$axios.get(path)
          .then((res) => {
            var data = res.data.data
            this.data = data
            var metadata = {
              province: '',
              city: []
            }
            var housedata = []
            var city = new Array()
            var province = new Array()
            var province2 = new Array()
            for (var i = 0; i < data.length; i++) {
              if (i > 0) {
                if (data[i].province != data[i - 1].province) {
                  metadata.province = data[i - 1].province
                  metadata.city = city
                  console.log(metadata.province)
                  console.log(metadata.city)
                  housedata.push({
                    province: metadata.province,
                    city: metadata.city
                  })
                  city = []
                  metadata.province = ''
                  metadata.city = []
                }
              }
              city.push(data[i].city)
              province.push(data[i].province)
              province2.push(data[i].province)
              if (i == data.length - 1) {
                metadata.province = data[i].province
                metadata.city = city
                housedata.push({
                  province: metadata.province,
                  city: metadata.city
                })
                city = []
                metadata.province = ''
                metadata.city = []
              }
            }
            console.log(housedata)
            // 合并同类项
            var tprovince = [];
            var narr = [];
            for (var i = 0; i < data.length; i++) {
              var n = tprovince.indexOf(data[i].province);
              if (n == -1) {
                tprovince.push(data[i].province);
                narr.push({
                  city: [data[i].city],
                  province: data[i].province
                });
              } else {
                narr[n].city.push(data[i].city);
              }
            }
            console.log(narr)
            this.housedata = housedata
            var newhousedata = narr
            this.newhousedata = newhousedata

            // 取省份定城市
            for (var i in newhousedata) {
              if (newhousedata[i].province == this.chooseprovince) {
                var choosecity = newhousedata[i].city
                this.choosecity = choosecity
                console.log(choosecity)
              }
            }

            function newData(data) {
              var nData = new Array();
              for (var i = 0; i < data.length; i++) {
                if (nData.indexOf(data[i]) == -1) {
                  nData.push(data[i]);
                }
              }
              return nData;
            }
            var provincedata = newData(province2)
            this.provincedata = provincedata
            this.$toasted.info('Success connect to Flask API', {
              icon: 'fingerprint'
            })
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })

      },
      onSubmit(e) {
        const path = `/api/trendinfo/${this.proval}/${this.city}`
        const payload = {
          province: this.proval,
          city: this.city,
        }
        this.$axios.post(path, payload)
          .then((response) => {
            // handle success
            this.trenddatas = response.data
            var trenddatas = response.data
            var price = trenddatas[0][1]
            var month = trenddatas[0][3]
            var year = trenddatas[0][4]
            
            //var year = trenddatas[0][]
            // 去除冒号
            var month = month.replace(/[&\|\\\*'^%$#@\-]/g, "");
            var year = year.replace(/[&\|\\\*'^%$#@\-]/g, "");
            // 逗号分隔
            var price_price = price.split(",");
            var price_month = month.split(",");
            var price_year = year.split(",");
            // 房价数据转化为整数
            var price_int = new Array();
            for (var i = 0; i < price_price.length; i++) {
              var temp = parseInt(price_price[i])
              price_int.push(temp)
            }
            // date year合并
            var price_date = new Array()
            for (var i = 0; i < price_month.length; i++) {
              var temp = price_year[i] + price_month[i]
              price_date.push(temp)
            }
            // console.log(price_int)
            console.log(trenddatas)
            // console.log(price)
            // console.log(date)
            //console.log(price_price)
            // console.log(price_date)
            // 在 Highcharts 加载之后加载功能模块
            var title = this.city + '市房价走势图'
            var Highcharts = require('highcharts');
            require('highcharts/modules/exporting')(Highcharts);
            Highcharts.chart('container', {
                title: {
                  text: title
                },
                yAxis: {
                  title: {
                    text: '房价'
                  }
                },
                xAxis: {
                  title: {
                    text: '月份'
                  },
                  categories: price_date
                },
                series: [{
                  name: '房产价格',
                  data: price_int
                }]
              }

            )
          })
          .catch((error) => {
            // handle error
            console.error(error)
          })

      }

    },
    watch: {
      proval(val, oldval) {
        console.log(val, oldval)
        this.chooseprovince = val
        var newhousedata = this.newhousedata
        this.currentPage = 1
        for (var i in newhousedata) {
          if (newhousedata[i].province == this.chooseprovince) {
            var choosecity = newhousedata[i].city
            this.choosecity = choosecity
            console.log(choosecity)
          }
        }
      }
    },
    created() {
      this.getMessage()
    },

  }
</script>
<style scoped>
  .bootstrap-select {
    width: 100% !important;
  }
</style>