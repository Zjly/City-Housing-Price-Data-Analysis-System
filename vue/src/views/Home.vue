<template>
  <div class="home">
    <el-container direction="vertical">
      <el-header>
        <el-menu :default-active="activeIndex" id="el-menu-nav" class="el-menu-nav" mode="horizontal"
          @select="handleSelect" active-text-color="#3196FF" text-color="#95C9FF">
          <el-menu-item style="min-inline-size: 30px;"></el-menu-item>
          <el-menu-item style="min-inline-size: 200px;"><img style="height:80px;" src="img/bird2.gif"></el-menu-item>
          <el-menu-item index="1" class="el-menu-item-nav">首页</el-menu-item>
          <el-menu-item index="2" class="el-menu-item-nav">房价查询</el-menu-item>
          <el-menu-item index="3" class="el-menu-item-nav">政策信息</el-menu-item>
          <el-menu-item index="4" class="el-menu-item-nav">房价预测</el-menu-item>
          <el-menu-item></el-menu-item>
          <el-menu-item style="min-inline-size: 150px;"></el-menu-item>
          <el-menu-item style="min-inline-size: 110px;text-align:center;margin:0 auto" class="el-menu-item-nav"
            index="5"><u>{{name}}</u>
          </el-menu-item>
          <el-menu-item style="min-inline-size: 0px;margin-left:-20px">|
          </el-menu-item>
          <el-menu-item style="min-inline-size: 100px;margin-left:-10px" index="6" class="el-menu-item-nav"><u><a
                href="/" v-on:click="quit">登录</a></u>
          </el-menu-item>
        </el-menu>
      </el-header>
    </el-container>
    <el-container>
      <el-main>
        <template>
          <el-carousel :interval="5000" height="350px" arrow="always">
            <!-- v-for="(item, index) in news" :key="item.id" title="" -->
            <el-carousel-item v-for="item in imgList" :key="item.id">
              <el-row>
                <el-col :span="24"><img ref="imgHeight" :src="item.idView" class="banner_img" /></el-col>
              </el-row>
            </el-carousel-item>
          </el-carousel>
        </template>

        <div class="introduce">

          <p class="title">
            房产介绍
          </p>

          <p>
            房价网走势频道提供城市精准及时、权威全面的房价行情走势，
          </p>
          为各城市随时免费提供查询最新季度房价、最近半年房价走势。
          <p>
            并且结合城市的环境状况、最新房产政策，预测出来的房价，具有一定权威性、精准性。
          </p>
          <p>
            希望每周的房价走势数据，能让你更好的判断当前房价形势和更好的预计的房价走向。
          </p>

        </div>
        <div class="que">
          <p>
            为什么选择我们
          </p>
          <br>
        </div>
        <el-collapse v-model="activeName" accordion>
          <el-collapse-item name="1">
            <template slot="title">
              <p class="item-title">一致性 Consistency</p><i class="header-icon el-icon-info"></i>
            </template>
            <br>
            <div class="item-content">与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
            <div class="item-content">在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
          </el-collapse-item>
          <el-collapse-item name="2">
            <template slot="title">
              <p class="item-title">反馈 Feedback</p><i class="header-icon el-icon-info"></i>
            </template>
            <br>
            <div class="item-content">控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
            <div class="item-content">页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
          </el-collapse-item>
          <el-collapse-item name="3">
            <template slot="title">
              <p class="item-title">效率 Efficiency</p><i class="header-icon el-icon-info"></i>
            </template>
            <br>
            <div class="item-content">简化流程：设计简洁直观的操作流程；</div>
            <div class="item-content">清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
            <div class="item-content">帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
          </el-collapse-item>
          <el-collapse-item name="4">
            <template slot="title">
              <p class="item-title">可控 Controllability</p><i class="header-icon el-icon-info"></i>
            </template>
            <br>
            <div class="item-content">用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
            <div class="item-content">结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
          </el-collapse-item>
          <el-collapse-item name="5">
            <template slot="title">
              <p class="item-title">其他 Others</p><i class="header-icon el-icon-info"></i>
            </template>
            <br>
            <div class="item-content">用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
            <div class="item-content">结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
          </el-collapse-item>

        </el-collapse>


        主页

        <div class="que">
          <p>
            最新行情
          </p>
          <br>
        </div>
        <div id="container">
        </div>
        <br>


      </el-main>
      <el-footer>
        <div class="footer">
          <template>
            <div>
              <el-row :gutter="12">
                <el-col :span="8">
                  <span>
                    <el-card class="box-card" shadow="hover">
                      <div class="text item" id="item-title">
                        小组成员
                      </div>
                      <div class="text item">
                        组长：张雷
                      </div>
                      <div class="text item">
                        组员：王亮
                      </div>
                      <div class="text item">
                        组员：汪志豪
                      </div>
                      <div class="text item">
                        组员：夏宇航
                      </div>
                    </el-card>
                  </span>
                </el-col>
                <el-col :span="8">
                  <span>
                    <el-card class="box-card" shadow="hover">
                      <div class="text item" id="item-title">
                        关于我们
                      </div>
                      <div class="text item">
                        小组简介
                      </div>
                      <div class="text item">
                        联系我们
                      </div>
                      <div class="text item">
                        合作伙伴
                      </div>
                      <div class="text item">
                        人才招募
                      </div>
                    </el-card>
                  </span>

                </el-col>

                <el-col :span="8">
                  <span>
                    <el-card class="box-card" shadow="hover">
                      <div class="text item" id="item-title">
                        网页说明
                      </div>
                      <div class="text item">
                        用户协议
                      </div>
                      <div class="text item">
                        版权声明
                      </div>
                      <div class="text item">
                        免责条款
                      </div>
                    </el-card>
                  </span>
                </el-col>
              </el-row>
            </div>
          </template>
        </div>
        <span>©<label>2020</label> 武汉大学 28组 房价云 版权所有</span><br>

      </el-footer>


    </el-container>







  </div>
</template>

<script>

  // 主页
  export default {
    name: 'Home',
    data() {
      return {
        activeName: '1',
        activeIndex: '1',
        name: '注册',
        imgList: [{
            id: 0,
            idView: require('../assets/images/333.png')
          },
          {
            id: 1,
            name: '详情',
            idView: require('../assets/images/333.png')
          },
          {
            id: 2,
            name: '推荐',
            idView: require('../assets/images/333.png')
          }
        ]
      };
    },
    
    components: {

    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        // 跳页面
        if (key == 1) {
          // 使用代码切换路径 (路由)
          this.$router.push('/');
        }
        if (key == 2) {
          this.$router.push('/house');
        }
        if (key == 3) {
          this.$router.push('/news');
        }
        if (key == 4) {
          this.$router.push('/forecast');
        }
        if (key == 5) {
          this.$router.push('/login');
        }
        if (key == 6) {
          this.$router.push('/register');
        }

      },
    },
    mounted() {
      // aixos 请求数据

      this.axios.get('http://127.0.0.1:5000/line').then(res => {
        console.log(res)
        var data = res.data.data
        var city = new Array()
        var money = new Array()
        for (var i = 0; i < data.length; i++) {
          city.push(data[i].name)
          money.push(data[i].money)
        }
        var Highcharts = require('highcharts');
        // 在 Highcharts 加载之后加载功能模块
        require('highcharts/modules/exporting')(Highcharts);
        Highcharts.chart('container', {
            title: {
              text: '一线城市平均房价'
            },
            yAxis: {
              title: {
                text: '房价'
              }
            },
            xAxis: {
              title: {
                text: '城市'
              },
              categories: city
            },
            series: [{
              name: '平均房价',
              data: money
            }]
          }

        )
      })




    },

  }
</script>

<style>
  .home {
    text-align: center;
    margin: 0 auto;
    width: 1240px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .el-header {
    background-color: #ffffff;
    margin: 0 auto;
    text-align: center;
    line-height: 70px;
    min-height: 80px;
    margin-left: -30px;
    margin-top: -8px;

  }

  .footer {
    background-color: #eeeeee;
    height: 200px;
    margin-left: 10px;
  }

  .el-menu--horizontal {
    margin: 0 auto;
    text-align: center;
    min-inline-size: 160px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }


  .el-menu--horizontal .el-menu-item {
    min-height: 80px;
    max-width: 70px;
    min-inline-size: 130px;
    text-align: center;
    font-size: 22px;
  }

  .el-menu--horizontal>.el-submenu .el-submenu__title {
    text-align: center;
    font-size: 22px;
    min-inline-size: 130px;
    min-height: 80px;
    max-width: 70px;
  }

  .el-carousel__item {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .el-select {
    size: medium;
  }

  .banner_img {
    width: 100%;
    height: 100%
  }

  .el-select {
    min-height: 150px;
  }

  .introduce .title {
    text-align: left;
    font-size: 28px;
  }

  .introduce {
    text-align: left;
    background-image: url("../assets/images/introduce_banner.png");
    height: 290px;
    background-size: 1400px 290px;
    font-size: 15px;
  }

  .que {
    text-align: left;
    font-size: 28px;
  }

  .el-collapse-item {
    text-align: left;
    font-size: 25px;

  }

  .item-title {
    font-size: 18px;
  }

  .item-content {
    font-size: 15px;
  }

  /* 卡片 */
  .text {
    font-size: 16px;
    text-align: left;
    margin-left: 80px;

  }

  .text#item-title {
    font-size: 23px;
    text-align: left;
    margin-left: 80px;
  }

  .item {
    margin-bottom: -20px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 410px;
    height: 280px;
    background-color: #eeeeee;

  }

  #container {
    max-width: 800px;
    height: 400px;
    margin: 0 auto;
    border: solid orange 1px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;

  }
</style>