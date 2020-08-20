<template>

  <div>

    <!-- Panel Header -->
    <div class="card-block g-pa-0">
      <h2>北京市未来房价预测</h2>
      <template>
        <el-tabs v-model="activeName">
          <el-tab-pane label="2019-2020" name="first">
            <template>
              <el-tabs v-model="activeName1">
                <el-tab-pane label="折线图" name="first">
                  <div id="line_container1" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="柱状图" name="second">
                  <div id="columnar_container1" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="预测对比表" name="third">
                  <div class="recommend" v-show="isShow">
                    <table class="table table-striped ablue">
                      <thead>
                        <tr>
                          <th width="80" class="tcenter">房屋地址</th>
                          <th width="80" class="tcenter">年份</th>
                          <th width="80" class="tcenter">情感分析值</th>
                          <th width="120" class="tcenter">实际房价(元/㎡)</th>
                          <th width="100" class="tcenter">预测房价(元/㎡)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in divid_data[3]" v-bind:key="index">
                          <td width="80" class="tcenter"><a href="">北京</a></td>
                          <td width="80" class="tcenter">{{item[0]}}</td>
                          <td width="80" class="tcenter">{{item[1]}}</td>
                          <td width="120" class="tcenter">{{item[2]}}</td>
                          <td width="100" class="tcenter red">{{item[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </el-tab-pane>
              </el-tabs>
            </template>
          </el-tab-pane>
          <el-tab-pane label="2018-2019" name="second"><template>
              <el-tabs v-model="activeName2">
                <el-tab-pane label="折线图" name="first">
                  <div id="line_container2" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="柱状图" name="second">
                  <div id="columnar_container2" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="预测对比表" name="third">
                  <div class="recommend" v-show="isShow">
                    <table class="table table-striped ablue">
                      <thead>
                        <tr>
                          <th width="80" class="tcenter">房屋地址</th>
                          <th width="80" class="tcenter">年份</th>
                          <th width="80" class="tcenter">情感分析值</th>
                          <th width="120" class="tcenter">实际房价(元/㎡)</th>
                          <th width="100" class="tcenter">预测房价(元/㎡)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in divid_data[2]" v-bind:key="index">
                          <td width="80" class="tcenter"><a href="">北京</a></td>
                          <td width="80" class="tcenter">{{item[0]}}</td>
                          <td width="80" class="tcenter">{{item[1]}}</td>
                          <td width="120" class="tcenter">{{item[2]}}</td>
                          <td width="100" class="tcenter red">{{item[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </el-tab-pane>
              </el-tabs>
            </template></el-tab-pane>
          <el-tab-pane label="2017-2018" name="third"><template>
              <el-tabs v-model="activeName3">
                <el-tab-pane label="折线图" name="first">
                  <div id="line_container3" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="柱状图" name="second">
                  <div id="columnar_container3" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="预测对比表" name="third">
                  <div class="recommend" v-show="isShow">
                    <table class="table table-striped ablue">
                      <thead>
                        <tr>
                          <th width="80" class="tcenter">房屋地址</th>
                          <th width="80" class="tcenter">年份</th>
                          <th width="80" class="tcenter">情感分析值</th>
                          <th width="120" class="tcenter">实际房价(元/㎡)</th>
                          <th width="100" class="tcenter">预测房价(元/㎡)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in divid_data[1]" v-bind:key="index">
                          <td width="80" class="tcenter"><a href="">北京</a></td>
                          <td width="80" class="tcenter">{{item[0]}}</td>
                          <td width="80" class="tcenter">{{item[1]}}</td>
                          <td width="120" class="tcenter">{{item[2]}}</td>
                          <td width="100" class="tcenter red">{{item[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </el-tab-pane>
              </el-tabs>
            </template></el-tab-pane>
          <el-tab-pane label="2016-2017" name="fourth">
            <template>
              <el-tabs v-model="activeName4">
                <el-tab-pane label="折线图" name="first">
                  <div id="line_container4" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="柱状图" name="second">
                  <div id="columnar_container4" style="height:500px">
                  </div>
                </el-tab-pane>
                <el-tab-pane label="预测对比表" name="third">
                  <div class="recommend" v-show="isShow">
                    <table class="table table-striped ablue">
                      <thead>
                        <tr>
                          <th width="80" class="tcenter">房屋地址</th>
                          <th width="80" class="tcenter">年份</th>
                          <th width="80" class="tcenter">情感分析值</th>
                          <th width="120" class="tcenter">实际房价(元/㎡)</th>
                          <th width="100" class="tcenter">预测房价(元/㎡)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in divid_data[0]" v-bind:key="index">
                          <td width="80" class="tcenter"><a href="">北京</a></td>
                          <td width="80" class="tcenter">{{item[0]}}</td>
                          <td width="80" class="tcenter">{{item[1]}}</td>
                          <td width="120" class="tcenter">{{item[2]}}</td>
                          <td width="100" class="tcenter red">{{item[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </el-tab-pane>
              </el-tabs>
            </template>

          </el-tab-pane>
        </el-tabs>
      </template>

      <hr class="g-brd-gray-light-v4 g-my-30">
    </div>

    <!-- End Panel Header -->

    <!-- Striped Rows -->

    <div class="card g-brd-teal rounded-0 g-mb-30">

    </div>


    <!-- End Striped Rows -->


  </div>
</template>


<script>
  import * as GridLight from 'highcharts/themes/grid-light';

  export default {
    name: 'HouseFuture',
    components: {

    },
    data() {
      return {
        isShow: true,
        activeName: 'first',
        activeName1: 'first',
        activeName2: 'first',
        activeName3: 'first',
        activeName4: 'first',
        data: '',
        divid_data:'',
        date: [],
        emotion: [],
        factprice: [],
        predictprice: [],

      }
    },
    methods: {

      getMessage() {
        const path = '/forecastdatas'

        function arr(arr, num) {
          var newArr = [];
          for (var i = 0; i < arr.length; i += num) {
            newArr.push(arr.slice(i, i + num));
          }
          return newArr;
        }
        this.$axios.get(path)
          .then((res) => {
            var data = res.data.data
            console.log(data)
            this.data = data
            var divid_data = arr(data,12)
            
            divid_data[3].push(divid_data[4][0])
            divid_data[3].push(divid_data[4][1])
            this.divid_data = divid_data
            console.log(divid_data)
            var date = new Array()
            var emotion = new Array()
            var factprice = new Array()
            var predictprice = new Array()
            for (var i = 0; i < data.length; i++) {
              date.push(data[i][0])
              emotion.push(data[i][1])
              factprice.push(data[i][2])
              predictprice.push(data[i][3])
            }
            this.date = date
            this.emotion = emotion
            this.factprice = factprice
            this.predictprice = predictprice
            var divid_date = arr(date, 12)
            var divid_emotion = arr(emotion, 12)
            var divid_factprice = arr(factprice, 12)
            var divid_predictprice = arr(predictprice, 12)
            divid_date[3].push(divid_date[4][0])
            divid_date[3].push(divid_date[4][1])
            divid_emotion[3].push(divid_emotion[4][0])
            divid_emotion[3].push(divid_emotion[4][1])
            divid_factprice[3].push(divid_factprice[4][0])
            divid_factprice[3].push(divid_factprice[4][1])
            divid_predictprice[3].push(divid_predictprice[4][1])
            divid_predictprice[3].push(divid_predictprice[4][0])

            console.log(divid_date[0])


            var Highcharts = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts);
            Highcharts.chart('columnar_container4', {
              chart: {
                type: 'bar'
              },
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[0]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[0]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[0]
                }
              ]
            })

            var Highcharts2 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts2);
            Highcharts2.chart('line_container4', {
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[0]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[0]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[0]
                }
              ]
            })

            var Highcharts3 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts3);
            Highcharts3.chart('columnar_container3', {
              chart: {
                type: 'bar'
              },
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[1]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[1]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[1]
                }
              ]
            })

            var Highcharts4 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts4);
            Highcharts4.chart('line_container3', {
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[1]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[1]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[1]
                }
              ]
            })

            var Highcharts5 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts);
            Highcharts5.chart('columnar_container2', {
              chart: {
                type: 'bar'
              },
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[2]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[2]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[2]
                }
              ]
            })

            var Highcharts6 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts6);
            Highcharts6.chart('line_container2', {
              title: {
                text: '北京市历史平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[2]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[2]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[2]
                }
              ]
            })

            var Highcharts7 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts7);
            Highcharts7.chart('columnar_container1', {
              chart: {
                type: 'bar'
              },
              title: {
                text: '北京市平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[3]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[3]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[3]
                }
              ]
            })

            var Highcharts8 = require('highcharts');
            // 在 Highcharts 加载之后加载功能模块
            //require('highcharts/modules/exporting')(Highcharts);
            GridLight(Highcharts8);
            Highcharts8.chart('line_container1', {
              title: {
                text: '北京市平均房价'
              },
              yAxis: {
                title: {
                  text: '房价'
                }
              },
              xAxis: {
                title: {
                  text: '年月份'
                },
                categories: divid_date[3]
              },

              series: [{
                  name: '平均房价',
                  data: divid_factprice[3]
                },
                {
                  name: '预测平均房价',
                  data: divid_predictprice[3]
                }
              ]
            })

            this.$toasted.info('Success connect to Flask API', {
              icon: 'fingerprint'
            })
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })

      },

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