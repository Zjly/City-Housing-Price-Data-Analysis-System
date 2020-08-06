<template>
  <div class="container">
    <h2>快速注册</h2>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" v-model="registerForm.username" class="form-control" v-bind:class="{'is-invalid': registerForm.usernameError}" id="username" placeholder="">
            <div v-show="registerForm.usernameError" class="invalid-feedback">{{ registerForm.usernameError }}</div>
          </div>
          <div class="form-group">
            <label for="email">电子邮件</label>
            <input type="email" v-model="registerForm.email" class="form-control" v-bind:class="{'is-invalid': registerForm.emailError}" id="email" aria-describedby="emailHelp" placeholder="">
            <small v-if="!registerForm.emailError" id="emailHelp" class="form-text text-muted">我们不会将您的邮箱泄露给他人。</small>
            <div v-show="registerForm.emailError" class="invalid-feedback">{{ registerForm.emailError }}</div>
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" v-model="registerForm.password" class="form-control" v-bind:class="{'is-invalid': registerForm.passwordError}" id="password" placeholder="">
            <div v-show="registerForm.passwordError" class="invalid-feedback">{{ registerForm.passwordError }}</div>
          </div>
          <div class="form-group">
            <label for="password2">确认密码</label>
            <input type="password" v-model="registerForm.password2" class="form-control" v-bind:class="{'is-invalid': registerForm.passwordError2}" id="password2" placeholder="">
            <div v-show="registerForm.passwordError2" class="invalid-feedback">{{ registerForm.passwordError2 }}</div>
          </div>
          <button type="submit" class="btn btn-primary">立即注册</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../store.js'
export default {
  name: 'Register', //this is the name of the component
  data () {
    return {
      registerForm: {
        username: '',
        email: '',
        password: '',
        password2: '',
        submitted: false,  // 是否点击了 submit 按钮
        errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
        usernameError: null,
        emailError: null,
        passwordError: null,
        passwordError2: null
      }
    }
  },
  methods: {
    onSubmit (e) {
      this.registerForm.submitted = true  // 先更新状态
      this.registerForm.errors = 0
      if (!this.registerForm.username) {
        this.registerForm.errors++
        this.registerForm.usernameError = '请输入用户名！'
      } else {
        this.registerForm.usernameError = null
      }
      if (!this.registerForm.email) {
        this.registerForm.errors++
        this.registerForm.emailError = '请输入邮箱号！'
      } else if (!this.validEmail(this.registerForm.email)) {
        this.registerForm.errors++
        this.registerForm.emailError = '邮箱不合法！'
      } else {
        this.registerForm.emailError = null
      }
      if (!this.registerForm.password) {
        this.registerForm.errors++
        this.registerForm.passwordError = '请输入密码'
      } else {
        this.registerForm.passwordError = null
      }
      if (this.registerForm.password != this.registerForm.password2) {
        this.registerForm.errors++
        this.registerForm.passwordError2 = '两次密码不一致'
      } else {
        this.registerForm.passwordError2 = null
      }
      if (this.registerForm.errors > 0) {
        // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }
      const path = 'http://localhost:5000/api/users'
      const payload = {
        username: this.registerForm.username,
        email: this.registerForm.email,
        password: this.registerForm.password
      }
      axios.post(path, payload)
        .then((response) => {
          // handle success
          store.setNewAction()
          this.$router.push('/login')
        })
        .catch((error) => {
          // handle error
          for (var field in error.response.data.message) {
            if (field == 'username') {
              this.registerForm.usernameError = error.response.data.message.username
            } else if (field == 'email') {
              this.registerForm.emailError = error.response.data.message.email
            } else if (field == 'password') {
              this.registerForm.passwordError = error.response.data.message.password
            } else if (field == 'password2'){
              this.registerForm.passwordError2 = error.response.data.message.password2
            }
          }
        })
    },
    validEmail: function (email) {
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }
  }
}
</script>
<style scoped>
  .container {
      font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
</style>