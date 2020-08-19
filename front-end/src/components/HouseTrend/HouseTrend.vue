<template>
  <!-- <div class="container">
    <div class="container recommend"> -->

  <!-- 右边子路由匹配后，显示对应的组件 -->

  <!-- <li v-for="(province, index) in provincedata" v-bind:key="index">
        <a class="nav-link" href="housedata/SecondHand">{{province}}</a>
        <router-link v-bind:to="{ path: `/housedata/SecondHand` }"
          v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'"
          class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
          `/housedata/${sharedState.user_id}`
          {{province}}
        </router-link>
      </li> -->

  <div class="container g-pt-20">
    <div class="row">
      <!-- 左边菜单栏 -->
      <div class="col-lg-4 g-mb-50">
        <aside class="g-brd-around g-brd-gray-light-v4 rounded g-px-20 g-py-30">

          <h2 class="text-center g-color-primary g-font-weight-600 g-line-height-1 g-font-size-60 g-pos-rel g-mb-30">
            HouseTrend</h2>

          <hr class="g-brd-gray-light-v4 g-my-30">
          <hr class="g-brd-gray-light-v4 g-my-30">

          <!-- 菜单列表 -->
          <ul class="list-unstyled mb-0">
            <li class="g-pb-3">
              <router-link v-bind:to="{ name: 'HouseQushi' }"
                v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'"
                v-bind:class="isHouseQushi"
                class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
                <span class="u-icon-v1 g-color-gray-dark-v5 mr-2">
                  <i class="icon-media-024 u-line-icon-pro"></i></span>
                房价趋势查询
              </router-link>
            </li>
            <li class="g-pb-3">
              <router-link v-bind:to="{ name: 'HouseDuibi' }"
                v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'"
                class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
                <span class="u-icon-v1 g-color-gray-dark-v5 mr-2"><i
                    class="icon-media-022 u-line-icon-pro"></i></span>
                房价对比图表
              </router-link>
            </li>
          </ul>
          <!-- End 菜单列表 -->
           <hr class="g-brd-gray-light-v4 g-my-30">



          <hr class="g-brd-gray-light-v4 g-my-30">
          <div class="recommend" v-show="isShow"  >
            <h4><span style="font-size:17px">热门城市房价排行</span>
              <div  style="font-size:14px" class="inline-block small_text">（2020年7月）</div>
            </h4>

            <table class="table table-striped ablue">
              <thead>
                <tr>
                  <th width="80" class="tcenter">城市</th>
                  <th width="100" class="tcenter">单价(元/㎡)</th>
                  <th width="100" class="tcenter">同比</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td width="80" class="tcenter"><a href="">深圳</a></td>
                  <td width="100" class="tcenter">73,129</td>
                  <td width="100" class="tcenter red ">+18.67%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">北京</a></td>
                  <td width="100" class="tcenter">62,212</td>
                  <td width="100" class="tcenter green">-1.88%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">上海</a></td>
                  <td width="100" class="tcenter">55,256</td>
                  <td width="100" class="tcenter red ">+5.65%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">厦门</a></td>
                  <td width="100" class="tcenter">45,583</td>
                  <td width="100" class="tcenter red ">+3.94%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">广州</a></td>
                  <td width="100" class="tcenter">37,729</td>
                  <td width="100" class="tcenter red ">+12.95%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">三亚</a></td>
                  <td width="100" class="tcenter">37,075</td>
                  <td width="100" class="tcenter red ">+13.83%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">南京</a></td>
                  <td width="100" class="tcenter">30,947</td>
                  <td width="100" class="tcenter red ">+0.76%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">杭州</a></td>
                  <td width="100" class="tcenter">29,524</td>
                  <td width="100" class="tcenter green">-3.71%</td>
                </tr>

                <tr>
                  <td width="80" class="tcenter"><a href="">福州</a></td>
                  <td width="100" class="tcenter">25,838</td>
                  <td width="100" class="tcenter green">-2.54%</td>
                </tr>


              </tbody>
            </table>
          </div>
        </aside>
      </div>
      <!-- End 左边菜单栏 -->

      <!-- 右边子路由匹配后，显示对应的组件 -->
      <div class="col-lg-8 g-mb-50">

        <div class="rounded g-brd-around g-brd-gray-light-v4 g-overflow-x-scroll g-overflow-x-visible--lg g-pa-30">
          <router-view></router-view>

        </div>
      </div>
      <!-- End 嵌套路由 -->
    </div>
  </div>

</template>

<script>
  import store from '../../store'
  export default {
    name: 'HouseTrend', // this is the name of the component
    data() {
      return {
        sharedState: store.state,
        isShow: true,
      }
    },
    computed: {
      isHouseQushi: function () {
        const tabs = ['HouseDuibi', 'HouseQushi']
        if (tabs.indexOf(this.$route.name) == -1) {
          return 'active g-color-primary--active g-bg-gray-light-v5--active'
        } else {
          return ''
        }
      },
    },
    methods: {
      getUser(id) {
        const path = `/api/users/${id}`
        this.$axios.get(path)
          .then((response) => {
            // handle success
            this.user = response.data
          })
          .catch((error) => {
            // handle error
            console.error(error)
          })
      },
    },
    created() {
      const user_id = this.sharedState.user_id
      this.getUser(user_id)
      // tooltip
      $(document).ready(function () {
        $('[data-toggle="tooltip"]').tooltip();
      })
    },
    mounted() {
    },
  }
</script>
<style scoped>
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