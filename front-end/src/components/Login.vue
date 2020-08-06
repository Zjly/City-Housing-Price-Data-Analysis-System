<template>
  <div class="Login">
  <div class="container">
    <alert 
      v-if="sharedState.is_new"
      v-bind:variant="alertVariant"
      v-bind:message="alertMessage">
    </alert>
    <h2>登录</h2>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" v-model="loginForm.username" class="form-control" v-bind:class="{'is-invalid': loginForm.usernameError}" id="username" placeholder="">
            <div v-show="loginForm.usernameError" class="invalid-feedback">{{ loginForm.usernameError }}</div>
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" v-model="loginForm.password" class="form-control" v-bind:class="{'is-invalid': loginForm.passwordError}" id="password" placeholder="">
            <div v-show="loginForm.passwordError" class="invalid-feedback">{{ loginForm.passwordError }}</div>
          </div>
          <button type="submit" class="btn btn-primary">立即登录</button>
        </form>
      </div>
    </div>
    <br>
    <p>没有账号？ <router-link to="/register">点击这里立即注册！</router-link></p>
    <p>
        忘记密码了？
        <a href="#">点击这里重置密码</a>
    </p>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert'
import store from '../store.js'
export default {
  name: 'Login',  //this is the name of the component
  components: {
    alert: Alert
  },
  data () {
    return {
      sharedState: store.state,
      alertVariant: 'info',
      alertMessage: '注册成功, 快点登录成为房价云高级用户吧 !',
      loginForm: {
        username: '',
        password: '',
        submitted: false,  // 是否点击了 submit 按钮
        errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
        usernameError: null,
        passwordError: null
      }
    }
  },
  methods: {
    onSubmit (e) {
      this.loginForm.submitted = true  // 先更新状态
      this.loginForm.errors = 0
      if (!this.loginForm.username) {
        this.loginForm.errors++
        this.loginForm.usernameError = 'Username required.'
      } else {
        this.loginForm.usernameError = null
      }
      if (!this.loginForm.password) {
        this.loginForm.errors++
        this.loginForm.passwordError = 'Password required.'
      } else {
        this.loginForm.passwordError = null
      }
      if (this.loginForm.errors > 0) {
        // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }
      const path = 'http://localhost:5000/api/tokens'
      // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
      axios.post(path, {}, {
        auth: {
          'username': this.loginForm.username,
          'password': this.loginForm.password
        }
      }).then((response) => {
          // handle success
          window.localStorage.setItem('madblog-token', response.data.token)
          store.resetNotNewAction()
          store.loginAction()
          if (typeof this.$route.query.redirect == 'undefined') {
            this.$router.push('/')
          } else {
            this.$router.push(this.$route.query.redirect)
          }
        })
        .catch((error) => {
          // handle error
          if (error.response.status == 401) {
            this.loginForm.usernameError = '不合法的用户名或密码.'
            this.loginForm.passwordError = '不合法的用户名或密码.'
          } else {
            console.log(error.response)
          }
        })
    }
  }
}
</script>
<style scoped>
  .container {
      font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
      
      
      width:100%;
  }
  
  
</style>