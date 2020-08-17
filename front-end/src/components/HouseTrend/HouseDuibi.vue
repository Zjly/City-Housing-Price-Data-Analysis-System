<template>

  <div>

    <!-- Panel Header -->
    <div class="card-block g-pa-0">
      <form class="form-inline" @submit.prevent="onSubmit">
        <div class="form-group">

          <label for="exampleInputProvince">省份</label>
          <div class="col-sm-2" style="margin-left:28px">
            <select id="citySel" v-model="proval" @change="pr_onchange($this.options[this.options.selectedIndex].text)"
              placeholder="请选择省份" class='form-control' style="width:200px;" data-live-search="true" name='province'>
              <option value="">请选择省份</option>
              <option v-for="(item, index) in newhousedata" v-bind:key="index">{{item.province}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="exampleInputCity">城市</label>
          <div class="col-sm-2" style="margin-left:28px">
            <select class='form-control' v-model="city" style="width:200px;" size="1" data-live-search="true" id='city'
              name='city'>
              <option v-for="(item, index) in choosecity" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div class="form-group">

          <label for="exampleInputProvince2">对比省份</label>
          <div class="col-sm-2">
            <select id="citySel" v-model="proval2" @change="pr_onchange($this.options[this.options.selectedIndex].text)"
              placeholder="请选择省份" class='form-control' style="width:200px;" data-live-search="true" name='province2'>
              <option value="">请选择省份</option>
              <option v-for="(item, index) in newhousedata2" v-bind:key="index">{{item.province}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="exampleInputCity2">对比城市</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="city2" style="width:200px;" size="1" data-live-search="true"
              id='city2' name='city'>
              <option v-for="(item, index) in choosecity2" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div>
          <button type="submit" style="margin-left:20px" class="btn btn-primary">提交</button>
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


      <div id="container" style="border: solid grey 1px">
      </div>

    </div>
    <div class="card g-brd-teal rounded-0 g-mb-30">
      <div class="recommend" v-show="isShow">
        <h4><span style="font-size:17px">{{trenddatas[0][0][9]}}与{{trenddatas[1][0][9]}}房价对比表</span>
          <div style="font-size:14px" class="inline-block small_text">（2020年7月）</div>
        </h4>
        <table class="table table-striped ablue">
          <thead>
            <tr>
              <th width="80" class="tcenter">城市</th>
              <th width="100" class="tcenter">新房单价(元/㎡)</th>
              <th width="100" class="tcenter">新房同比</th>
              <th width="100" class="tcenter">二手房单价(元/㎡)</th>
              <th width="100" class="tcenter">二手同比</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td width="80" class="tcenter"><a href="">{{trenddatas[0][0][9]}}</a></td>
              <td width="100" class="tcenter">{{trenddatas[0][0][5]}}</td>
              <td width="100" class="tcenter">{{trenddatas[0][0][7]}}</td>
              <td width="100" class="tcenter">{{trenddatas[0][0][6]}}</td>
              <td width="100" class="tcenter">{{trenddatas[0][0][8]}}</td>
            </tr>
            <tr>
              <td width="80" class="tcenter"><a href="">{{trenddatas[1][0][9]}}</a></td>
              <td width="100" class="tcenter">{{trenddatas[1][0][5]}}</td>
              <td width="100" class="tcenter">{{trenddatas[1][0][7]}}</td>
              <td width="100" class="tcenter">{{trenddatas[1][0][6]}}</td>
              <td width="100" class="tcenter">{{trenddatas[1][0][8]}}</td>
            </tr>
          </tbody>
        </table>
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
    name: 'HouseDuibi',
    components: {

    },
    data() {
      return {
        isShow: true,
        proval: '',
        proval2: '',
        data: '',
        chooseprovince: '',
        chooseprovince2: '',
        newhousedata: [],
        newhousedata2: [],
        provincedata: [],
        choosecity: [],
        choosecity2: [],
        housedata: [],
        province: '',
        city: '',
        city2: '',
        // 趋势数据
        trenddatas: [
          [
            [
              '暂无'
            ],
          ],
          [
            [
              '暂无'
            ],
          ],
        ],

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
            var newhousedata2 = narr
            this.newhousedata = newhousedata
            this.newhousedata2 = newhousedata

            // 取省份定城市
            for (var i in newhousedata) {
              if (newhousedata[i].province == this.chooseprovince) {
                var choosecity = newhousedata[i].city
                this.choosecity = choosecity
                console.log(choosecity)
              }
            }

            // 取省份定城市
            for (var i in newhousedata2) {
              if (newhousedata2[i].province == this.chooseprovince2) {
                var choosecity2 = newhousedata2[i].city
                this.choosecity2 = choosecity2
                console.log(choosecity2)
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
        const path = `/api/trendinfo2/${this.proval}/${this.city}/${this.proval2}/${this.city2}`
        const payload = {
          province: this.proval,
          city: this.city,
          province2: this.proval2,
          city2: this.city2,
        }
        this.$axios.post(path, payload)
          .then((response) => {
            // handle success
            this.trenddatas = response.data
            var trenddatas = response.data
            console.log(trenddatas)
            var price = trenddatas[0][0][1]
            var month = trenddatas[0][0][3]
            var year = trenddatas[0][0][4]
            var esf = trenddatas[0][0][2]
            var price2 = trenddatas[1][0][1]
            var month2 = trenddatas[1][0][3]
            var year2 = trenddatas[1][0][4]
            var esf2 = trenddatas[1][0][2]


            //var year = trenddatas[0][]
            // 去除冒号
            var month = month.replace(/[&\|\\\*'^%$#@\-]/g, "");
            var year = year.replace(/[&\|\\\*'^%$#@\-]/g, "");
            // 去除冒号
            var month2 = month2.replace(/[&\|\\\*'^%$#@\-]/g, "");
            var year2 = year2.replace(/[&\|\\\*'^%$#@\-]/g, "");
            // 逗号分隔
            var price_price = price.split(",");
            var price_month = month.split(",");
            var price_year = year.split(",");
            var price_esf = esf.split(",");
            // 逗号分隔
            var price_price2 = price2.split(",");
            var price_month2 = month2.split(",");
            var price_year2 = year2.split(",");
            var price_esf2 = esf2.split(",");
            // 房价数据转化为整数
            var price_int = new Array();
            for (var i = 0; i < price_price.length; i++) {
              var temp = parseInt(price_price[i])
              price_int.push(temp)
            }
            // 房价数据转化为整数
            var price_int2 = new Array();
            for (var i = 0; i < price_price2.length; i++) {
              var temp = parseInt(price_price2[i])
              price_int2.push(temp)
            }
            // 二手房房价数据转化为整数
            var esf_int = new Array();
            for (var i = 0; i < price_esf.length; i++) {
              var temp = parseInt(price_esf[i])
              esf_int.push(temp)
            }
            // 二手房房价数据转化为整数
            var esf_int2 = new Array();
            for (var i = 0; i < price_esf2.length; i++) {
              var temp = parseInt(price_esf2[i])
              esf_int2.push(temp)
            }
            // date year合并
            var price_date = new Array()
            for (var i = 0; i < price_month.length; i++) {
              var temp = price_year[i] + price_month[i]
              price_date.push(temp)
            }
            // date year合并
            var price_date2 = new Array()
            for (var i = 0; i < price_month.length; i++) {
              var temp = price_year2[i] + price_month2[i]
              price_date2.push(temp)
            }
            // console.log(price_int)
            console.log(trenddatas)
            // console.log(price)
            // console.log(date)
            //console.log(price_price)
            // console.log(price_date)
            // 在 Highcharts 加载之后加载功能模块
            var title = this.city + '市与' + this.city2 + '市房价对比图'
            var Highcharts = require('highcharts');
            require('highcharts/modules/exporting')(Highcharts);
            Highcharts.chart('container', {
                title: {
                  text: title
                },
                subtitle: {
                  text: '二手房可能未显示部分原因为暂且没有数据',
                },
                yAxis: {
                  title: {
                    text: '房价（元/平方米'
                  }
                },
                xAxis: {
                  title: {
                    text: '年月份'
                  },
                  categories: price_date
                },
                series: [{
                    name: this.city + '新房',
                    data: price_int
                  },
                  {
                    name: this.city2 + '新房',
                    data: price_int2
                  },
                  {
                    name: this.city + '二手房',
                    data: esf_int
                  },
                  {
                    name: this.city2 + '二手房',
                    data: esf_int2
                  }
                ]
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
        for (var i in newhousedata) {
          if (newhousedata[i].province == this.chooseprovince) {
            var choosecity = newhousedata[i].city
            this.choosecity = choosecity
            console.log(choosecity)
          }
        }

      },
      proval2(val, oldval) {
        console.log(val, oldval)
        this.chooseprovince2 = val
        var newhousedata2 = this.newhousedata2
        for (var i in newhousedata2) {
          if (newhousedata2[i].province == this.chooseprovince2) {
            var choosecity2 = newhousedata2[i].city
            this.choosecity2 = choosecity2
            console.log(choosecity2)
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

  .recommend {
    text-align: center;
  }

  .container {
    width: 1100px;
    padding: 0px;
    position: relative;
    background-color: #ffffff;
  }

  .expertcatlist {
    width: 100%;
  }

  *,
  :after,
  :before {
    box-sizing: border-box;
  }

  .tabs-wrapper {
    border: 1px solid #e4ecf3;
    background-color: #ffffff;
    font-size: 13px;
    width: 100%;
  }

  .tabs-wrapper .tabs-mark-group {
    border-bottom: 1px dashed #e4ecf3;
  }

  .tabs-wrapper .tabs-group {
    position: relative;
    overflow-y: hidden;
  }

  .tabs-wrapper .tabs-group .content {
    list-style: none;
    padding: 10px 20px;
    margin: 0;
  }

  .tabs-wrapper .tabs-group .content>li {
    float: left;
    padding: 5px;
  }

  li {
    list-style-type: none;
  }

  li {
    line-height: 20px;
  }

  .tabs-wrapper .tabs-group .content>li:hover>a,
  .tabs-wrapper .tabs-group .content>li:focus>a,
  .tabs-wrapper .tabs-group .content>li.active>a {
    color: red;
  }

  .tabs-wrapper .tabs-group .content>li>a {
    display: block;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    color: #919191;
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
  }

  .tabs-wrapper .tabs-group+.tabs-group {
    border-top: 1px dashed #e4ecf3;
  }

  .tabs-wrapper .tabs-group {
    position: relative;
    overflow-y: hidden;
  }

  /* 房价排行榜 */
  .listcontent {
    padding: 20px;
    background: #ffffff;
    border: 2px solid #e4ecf3;
    margin-top: 15px;
    min-height: 360px;
  }

  .zsbt {
    font-weight: bold;
    color: #333;
    margin-top: 20px;
    display: inline-block;
    font-size: 20px;
  }

  .zsbtb {
    margin-bottom: 20px;
  }

  .mart0b10 {
    margin-top: 0 !important;
    margin-bottom: 10px !important;
  }

  .w600 {
    width: 800px;
    margin: 0 auto;
    overflow: hidden;
    display: inline-block;
  }

  ul {
    padding-left: 0;
  }

  .toplist li {
    height: 45px;
    line-height: 45px;
  }

  .ws_text {
    font-weight: 700;
    padding-left: 0px !important;
  }

  .ws_text {
    font-weight: 700;
  }

  .huise {
    background-color: #f9f9f9;
  }

  li {
    list-style-type: none;
  }

  /* 排名 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .txuh {
    float: left;
    width: 10%;
  }

  .txuh,
  .xuh {
    float: left;
    width: 10%;
    text-align: center;
  }

  /* 地区 */
  .toplist b {
    font-size: 14px;
    color: #000;
  }

  .limagesy,
  .diqu,
  .citysy {
    width: 30%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  .diqu {
    width: 24%;
    float: left;
    height: 42px;
    overflow: hidden;
    color: #333 !important;
  }

  /* 单元 */
  .toplist b {
    font-size: 14px;
    color: #000;
  }

  .blm,
  .btm,
  .tmonthsy,
  .lmonthsy,
  .lbil,
  .lcity,
  .ltmonthsy {
    width: 20%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  /* 单位 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  /* 环比 */
  .toplist b {
    font-size: 14px;
    color: #000;
  }

  b,
  strong {
    font-weight: 700;
  }

  /* 同比 */
  .toplist b {
    font-size: 14px;
    color: #000;
  }

  .blm {
    padding-right: 0px;
  }

  .blm,
  .btm,
  .tmonthsy,
  .lmonthsy,
  .lbil,
  .lcity,
  .ltmonthsy {
    width: 20%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  /* 行 */
  .toplist li {
    height: 45px;
    line-height: 45px;
  }

  li {
    list-style-type: none;
  }

  /* 第一项 */

  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .xuh {
    float: left;
    width: 10%;
  }

  .txuh,
  .xuh {
    float: left;
    width: 10%;
    text-align: center;
  }

  /* 第二项 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .limagesy,
  .diqu,
  .citysy {
    width: 30%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  /* 第三项 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .blm,
  .btm,
  .tmonthsy,
  .lmonthsy,
  .lbil,
  .lcity,
  .ltmonthsy {
    width: 20%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  .toplist span {
    font-size: 14px;
    color: #000;
  }

  /* 第四项 */
  .bil {
    width: 20%;
    float: left;
  }

  .green {
    color: #55a500 !important;
    font-family: arial;
  }

  /* 第五项 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .blm,
  .btm,
  .tmonthsy,
  .lmonthsy,
  .lbil,
  .lcity,
  .ltmonthsy {
    width: 20%;
    float: left;
    height: 45px;
    overflow: hidden;
  }

  /* 灰格子 */
  .toplist li {
    height: 45px;
    line-height: 45px;
  }

  .huise {
    background-color: #f9f9f9;
  }

  li {
    list-style-type: none;
  }

  /* 增长 */
  .toplist span {
    font-size: 14px;
    color: #000;
  }

  .bil {
    width: 20%;
    float: left;
  }

  .red {
    font-family: arial;
    color: #ff5256 !important;
  }
</style>