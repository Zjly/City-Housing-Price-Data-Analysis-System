<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" style="margin-bottom: 20px;">
    <div class="container">
      <router-link to="/" class="navbar-brand">
        <img src="https://getbootstrap.com/docs/4.1/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
          房价云
      </router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <router-link to="/" class="nav-link">首页 <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">其他</a>
          </li>
        </ul>
        
        <form v-if="sharedState.is_authenticated" class="form-inline navbar-left mr-auto">
          <input class="form-control mr-sm-2" type="search" placeholder="Search">
          <!-- 暂时先禁止提交，后续实现搜索再改回 type="submit" -->
          <button class="btn btn-outline-success my-2 my-sm-0" type="button">搜索</button>
        </form>

        <ul v-if="sharedState.is_authenticated" class="nav navbar-nav navbar-right">          
          <li class="nav-item">
            <a class="nav-link disabled" href="#">消息</a>
          </li>
          <li class="nav-item">
            <router-link to="/profile" class="nav-link">个人</router-link>
          </li>
          <li class="nav-item">
            <a v-on:click="handlerLogout" class="nav-link" href="#">注销登录</a>
          </li>
        </ul>
        <ul v-else class="nav navbar-nav navbar-right">          
          <li class="nav-item">
            <router-link to="/login" class="nav-link">登录</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import store from '../store.js'
export default {
  name: 'Navbar',  //组件名称
  data () {
    return {
      sharedState: store.state
    }
  },
  methods: {
    handlerLogout (e) {
      store.logoutAction()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
  .container {
      font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
</style>