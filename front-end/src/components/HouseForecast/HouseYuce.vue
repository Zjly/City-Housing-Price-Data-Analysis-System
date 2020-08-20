<template>

  <div>

    <!-- Panel Header -->
    <div class="card-block g-pa-0">
      <form class="form-inline" @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="Room">房间数量</label>
          <div class="col-sm-2">
            <select id="citySel" v-model="Room" @change="pr_onchange($this.options[this.options.selectedIndex].text)"
              placeholder="请选择房间数量" class='form-control' style="width:150px;" data-live-search="true" name='sitting'>
              <option v-for="(item, index) in room" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="Sitting">客厅数量</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="Sitting" style="width:150px;" size="1" data-live-search="true"
              id='room' name='room'>
              <option v-for="(item, index) in sitting" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div><br><br><br></div>
        <div class="form-group">
          <label for="Area">房屋面积</label>
          <div class="col-sm-2">
            <input class='form-control' v-model="Area" style="width:150px;" size="1" data-live-search="true" id='area'
              name='area'>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="toward">房屋朝向 </label>
          <div class="col-sm-2">
            <select class='form-control' v-model="Toward" style="width:100px;" size="1" data-live-search="true"
              id='toward' name='city'>
              <option v-for="(item, index) in toward" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="floor">房屋楼层</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="Floor" style="width:100px;" size="1" data-live-search="true"
              id='Floor' name='Floor'>
              <option v-for="(item, index) in floor" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div><br><br><br></div>
        <div class="form-group">
          <label for="Address">房屋地址</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="Address" style="width:150px;" size="1" data-live-search="true"
              id='Address' name='Address'>
              <option v-for="(item, index) in address" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="Buildyear">建造年份</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="Buildyear" style="width:100px;" size="1" data-live-search="true"
              id='Buildyear' name='Buildyear'>
              <option v-for="(item, index) in buildyear" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div><br><br><br></div>
        <div>
          <button type="submit" style="margin-left:20px" class="btn btn-primary">提交</button>
        </div>
      </form>
      <hr class="g-brd-gray-light-v4 g-my-30">
    </div>
    
    <!-- End Panel Header -->

    <!-- Striped Rows -->

    <div class="card g-brd-teal rounded-0 g-mb-30">
      <div class="recommend" v-show="isShow">
        <h4><span style="font-size:17px">房价预测表</span>
          <div style="font-size:14px" class="inline-block small_text"></div>
        </h4>
        <table class="table table-striped ablue">
          <thead>
            <tr>
              <th width="80" class="tcenter">房屋地址</th>
              <th width="100" class="tcenter">房屋单价(元/㎡)</th>
              <th width="100" class="tcenter">房屋总价（万元）</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td width="80" class="tcenter"><a href="">{{forecastdatas[0]}}</a></td>
              <td width="100" class="tcenter">{{forecastdatas[1]}}</td>
              <td width="100" class="tecenter">{{forecastdatas[2]}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>


    <!-- End Striped Rows -->


  </div>
</template>


<script>
  export default {
    name: 'HouseYuce',
    components: {

    },
    data() {
      return {
        isShow: true,
        data: '',
        room: '',
        sitting: '',
        area: '',
        toward: '',
        address: '',
        floor: '',
        buildyear: '',
        Room: '',
        Sitting: '',
        Area: '',
        Toward: '',
        Address: '',
        Floor: '',
        Buildyear: '',
        forecastdata: [],
        // 预测数据
        forecastdatas: [],
      }
    },
    methods: {

      getMessage() {
        const path = '/forecastdata'
        this.$axios.get(path)
          .then((res) => {
            var data = res.data.data
            console.log(data)
            this.data = data
            // 传入数据
            var sitting = data[0].Sitting
            this.sitting = sitting
            var room = data[0].Room
            this.room = room
            var toward = data[0].toward
            this.toward = toward
            var floor = data[0].floor
            this.floor = floor
            var address = data[0].address
            this.address = address
            var buildyear = data[0].buildyear
            this.buildyear = buildyear
            //console.log(sitting)


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
        var forecastdata = []
        forecastdata.push(this.Room)
        forecastdata.push(this.Sitting)
        forecastdata.push(this.Area)
        forecastdata.push(this.Toward)
        forecastdata.push(this.Floor)
        forecastdata.push(this.Address)
        forecastdata.push(this.Buildyear)
        this.forecastdata = forecastdata
        const path =
          `/api/forecast/${this.forecastdata}`
        const payload = {
          forecastdata: this.forecastdata
        }
        this.$axios.post(path, payload)
          .then((response) => {
              var forecastdatas = response.data
              console.log(forecastdatas)
              this.forecastdatas = response.data
          })
          .catch((error) => {
            // handle error
            console.error(error)
          })

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