<template>
  <div class="container">
    <div class="container recommend">
      <div class="expertcatlist">
        <div class="tabs-wrapper">
          <div class="tabs-mark-group plm ptm">
            <div class="tabs-group">
              <ul class="content clearfix">
                <li v-for="(province, index) in provincedata" v-bind:key="index">
                  <!-- <a class="nav-link" href="housedata/housediji">{{province}}</a> -->
                  <router-link v-bind:to="{ path: `/housedata/housediji` }"
                    v-bind:active-class="'active g-color-primary--active g-bg-gray-light-v5--active'"
                    class="d-block align-middle u-link-v5 g-color-text g-color-primary--hover g-bg-gray-light-v5--hover rounded g-pa-3">
                    <!-- `/housedata/${sharedState.user_id}` -->
                    {{province}}
                  </router-link>
                </li>

              </ul>
            </div>
            <div class="tabs-group">
              <ul class="content clearfix" >
                <!-- <li class="active" v-for="(city, index) in city" v-bind:key="index"> -->
                
                <li><a class="nav-link" href="">北京</a></li>
                <li><a class="nav-link" href="">上海</a></li>
                <li><a class="nav-link" href="">天津</a></li>
                <li><a class="nav-link" href="">重庆</a></li>
              </ul>
            </div>
            <div class="tabs-group">
              <ul class="content clearfix">
                <li><a class="nav-link" href="">宣武区</a></li>
                <li><a class="nav-link" href="">西城区</a></li>
                <li><a class="nav-link" href="">通州区</a></li>
                <li><a class="nav-link" href="">顺义区</a></li>
                <li><a class="nav-link" href="">石景山区</a></li>
                <li><a class="nav-link" href="">平谷区</a></li>
                <li><a class="nav-link" href="">门头沟区</a></li>
                <li><a class="nav-link" href="">怀柔区</a></li>
                <li><a class="nav-link" href="">海淀区</a></li>
                <li><a class="nav-link" href="">丰台区</a></li>
                <li><a class="nav-link" href="">房山区</a></li>
                <li><a class="nav-link" href="">大兴区</a></li>
                <li><a class="nav-link" href="">东城区</a></li>
                <li><a class="nav-link" href="">朝阳区</a></li>
                <li><a class="nav-link" href="">崇文区</a></li>
                <li><a class="nav-link" href="">昌平区</a></li>
                <li><a class="nav-link" href="">延庆区</a></li>
                <li><a class="nav-link" href="">密云区</a></li>
                <li><a class="nav-link" href="">市区</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="listcontent">
          <div>
            <h1 class="zsbt zsbtb mart0b10">北京房价排行榜</h1>
          </div>
          <ul class="toplist w600 ablue">
            <li class="ws_text huise"><span class="txuh">排名</span><b class="diqu">地区</b><b class="btm">单价<span
                  style="font-weight: 500;">(元/㎡)</span></b><b class="bv">环比</b><b class="blm">同比</b></li>
            <li class="ws_art_text "><span class="xuh">1</span><span class="citysy"><a target="_blank"
                  href="">西城区</a></span><span class="tmonthsy">120,182</span><span class="bil green">-2.49%</span><span
                class="lmonthsy green">-6.28%</span></li>
            <li class="ws_art_text huise"><span class="xuh">2</span><span class="citysy"><a target="_blank"
                  href="">宣武区</a></span><span class="tmonthsy">100,807</span><span class="bil green">--</span><span
                class="lmonthsy green">--</span></li>
            <li class="ws_art_text "><span class="xuh">3</span><span class="citysy"><a target="_blank"
                  href="">东城区</a></span><span class="tmonthsy">96,691</span><span class="bil red ">+1.16%</span><span
                class="lmonthsy green">-9.55%</span></li>
            <li class="ws_art_text huise"><span class="xuh">4</span><span class="citysy"><a target="_blank"
                  href="">海淀区</a></span><span class="tmonthsy">88,951</span><span class="bil green">-2.36%</span><span
                class="lmonthsy red ">+1.59%</span></li>
            <li class="ws_art_text "><span class="xuh">5</span><span class="citysy"><a target="_blank"
                  href="">崇文区</a></span><span class="tmonthsy">87,934</span><span class="bil green">--</span><span
                class="lmonthsy green">--</span></li>
            <li class="ws_art_text huise"><span class="xuh">6</span><span class="citysy"><a target="_blank"
                  href="">朝阳区</a></span><span class="tmonthsy">71,186</span><span class="bil red ">+0.24%</span><span
                class="lmonthsy green">-1.06%</span></li>
            <li class="ws_art_text "><span class="xuh">7</span><span class="citysy"><a target="_blank"
                  href="">丰台区</a></span><span class="tmonthsy">58,771</span><span class="bil green">-2.23%</span><span
                class="lmonthsy red ">+1.33%</span></li>
            <li class="ws_art_text huise"><span class="xuh">8</span><span class="citysy"><a target="_blank"
                  href="">石景山区</a></span><span class="tmonthsy">51,471</span><span class="bil green">-1.41%</span><span
                class="lmonthsy green">-6.25%</span></li>
            <li class="ws_art_text "><span class="xuh">9</span><span class="citysy"><a target="_blank"
                  href="">通州区</a></span><span class="tmonthsy">44,594</span><span class="bil green">-0.63%</span><span
                class="lmonthsy green">-2.08%</span></li>
            <li class="ws_art_text huise"><span class="xuh">10</span><span class="citysy"><a target="_blank"
                  href="">大兴区</a></span><span class="tmonthsy">40,453</span><span class="bil green">-0.47%</span><span
                class="lmonthsy green">-6.71%</span></li>
            <li class="ws_art_text "><span class="xuh">11</span><span class="citysy"><a target="_blank"
                  href="">顺义区</a></span><span class="tmonthsy">40,358</span><span class="bil red ">+2.88%</span><span
                class="lmonthsy green">-3.48%</span></li>
            <li class="ws_art_text huise"><span class="xuh">12</span><span class="citysy"><a target="_blank"
                  href="">昌平区</a></span><span class="tmonthsy">39,000</span><span class="bil red ">+1.67%</span><span
                class="lmonthsy green">-3.49%</span></li>
            <li class="ws_art_text "><span class="xuh">13</span><span class="citysy"><a target="_blank"
                  href="">门头沟区</a></span><span class="tmonthsy">36,620</span><span class="bil red ">+1.1%</span><span
                class="lmonthsy green">-9.07%</span></li>
            <li class="ws_art_text huise"><span class="xuh">14</span><span class="citysy"><a target="_blank"
                  href="">怀柔区</a></span><span class="tmonthsy">31,063</span><span class="bil green">-4.58%</span><span
                class="lmonthsy red ">+1%</span></li>
            <li class="ws_art_text "><span class="xuh">15</span><span class="citysy"><a target="_blank"
                  href="">房山区</a></span><span class="tmonthsy">29,092</span><span class="bil green">-1.09%</span><span
                class="lmonthsy green">-3.93%</span></li>
            <li class="ws_art_text huise"><span class="xuh">16</span><span class="citysy"><a target="_blank"
                  href="">平谷区</a></span><span class="tmonthsy">23,344</span><span class="bil green">-2.02%</span><span
                class="lmonthsy green">-2.49%</span></li>
            <li class="ws_art_text "><span class="xuh">17</span><span class="citysy"><a target="_blank"
                  href="">密云区</a></span><span class="tmonthsy">22,725</span><span class="bil green">-1.54%</span><span
                class="lmonthsy green">-2.55%</span></li>
            <li class="ws_art_text huise"><span class="xuh">18</span><span class="citysy"><a target="_blank"
                  href="">延庆区</a></span><span class="tmonthsy">22,030</span><span class="bil red ">+1.97%</span><span
                class="lmonthsy green">-13.07%</span></li>
          </ul>
        </div>
      </div>
    </div>
    <!-- <button type="button" class="btn btn-primary">{{ msg }}</button> -->


  </div>
</template>

<script>
  // import Alert from './Base/Alert'

  export default {
    name: 'HouseData',
    components: {
      // alert: Alert
    },
    data() {
      return {
        provincedata: [],
        data: '',
        housedata:'',
        //   msg: '',
        //   alerts: [
        //     {
        //       variant: 'info',
        //       message: 'Hi'
        //     },
        //     {
        //       variant: 'danger',
        //       message: 'Oops..'
        //     },
        //     {
        //       variant: 'success',
        //       message: 'OK'
        //     },
        //     {
        //        province: '安徽',
        //        city:[
        //           'xx',
        //           'xx',
        //           'xx'      
        //        ]  
        //     }
        //   ]
      }
    },
    methods: {
      getMessage() {
        const path = '/api/houseaddress'
        this.$axios.get(path)
          .then((res) => {
            var data = res.data.data
            this.data = data
            var metadata = {
              province: '',
              city: []
            }
            console.log(metadata)
            var housedata = [
            ]
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
                  housedata.push({province: metadata.province,city:metadata.city})
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
                housedata.push({province: metadata.province,city:metadata.city})
                city = []
                metadata.province = ''
                metadata.city = []
              }

            }
            console.log(housedata)
            this.housedata = housedata

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
      }
    },
    created() {
      this.getMessage()
    }
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