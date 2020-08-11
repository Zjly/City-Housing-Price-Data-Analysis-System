<template>
  <div class="house">
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
            index="5"><u>登录</u>
          </el-menu-item>
          <el-menu-item style="min-inline-size: 0px;margin-left:-20px">|
          </el-menu-item>
          <el-menu-item style="min-inline-size: 100px;margin-left:-10px" index="6" class="el-menu-item-nav"><u>注册</u>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
      房价数据
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
  // @ is an alias to /src

  // 主页
  export default {
    name: 'House',
    data() {
      return {
        activeIndex: '2',
      };
    },

    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
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
    components: {

    },
  }
</script>
<style>
  .house {
    text-align: center;
    margin: 0 auto;
    width: 1240px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .el-header,
  .el-footer {
    background-color: #ffffff;
    margin: center;
    text-align: center;
    line-height: 70px;
    min-height: 80px;
    margin-left: -30px;
    margin-top: -8px;

  }

  .el-menu--horizontal {
    min-inline-size: 160px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .el-menu--horizontal .el-menu-item {
    min-height: 80px;
    max-width: 70px;
    min-inline-size: 120px;
    text-align: center;
    font-size: 22px;
  }

  .el-menu--horizontal>.el-submenu .el-submenu__title {
    text-align: center;
    font-size: 22px;
    min-inline-size: 120px;
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
</style>