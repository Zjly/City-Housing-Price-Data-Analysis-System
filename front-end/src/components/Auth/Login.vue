<template>
  <div class="container">
    <div class="row">
      <div class="col-md-offset-3 col-md-6">
        <form @submit.prevent="onSubmit" class="form-horizontal">
          <span class="heading">用户登录</span>
          <div class="form-group" v-bind:class="{'u-has-error-v1': loginForm.usernameError}">

            <input type="text" v-model="loginForm.username" class="form-control" id="username" placeholder="请输入用户名">
            <i class="fa fa-user"></i>
            <small class="form-control-feedback" v-show="loginForm.usernameError">{{ loginForm.usernameError }}</small>
          </div>
          <div class="form-group help" v-bind:class="{'u-has-error-v1': loginForm.passwordError}">

            <input type="password" v-model="loginForm.password" class="form-control" id="password" placeholder="请输入密码">
            <i class="fa fa-lock"></i>
            <small class="form-control-feedback" v-show="loginForm.passwordError">{{ loginForm.passwordError }}</small>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-default">登录</button>
          </div>
          
        </form>
        <div class="attention">
            <br>
            <p class="attention1">新用户？ <router-link to="/register">点击这里注册！</router-link>
            </p>
            <p class="attention2">
              忘记密码了？
              <router-link v-bind:to="{ name: 'ResetPasswordRequest' }">点击这里重置密码！</router-link>
            </p>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
  import store from '../../store'
  export default {
    name: 'Login', //this is the name of the component
    data() {
      return {
        sharedState: store.state,
        loginForm: {
          username: '',
          password: '',
          errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
          usernameError: null,
          passwordError: null
        }
      }
    },
    methods: {
      onSubmit(e) {
        this.loginForm.errors = 0 // 重置
        if (!this.loginForm.username) {
          this.loginForm.errors++
          this.loginForm.usernameError = '需要输入用户名.'
        } else {
          this.loginForm.usernameError = null
        }
        if (!this.loginForm.password) {
          this.loginForm.errors++
          this.loginForm.passwordError = '密码未输入.'
        } else {
          this.loginForm.passwordError = null
        }
        if (this.loginForm.errors > 0) {
          // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
          return false
        }
        const path = '/api/tokens'
        // axios 实现Basic Auth需要在config中设置 auth 这个属性即可
        this.$axios.post(path, {}, {
            auth: {
              'username': this.loginForm.username,
              'password': this.loginForm.password
            }
          }).then((response) => {
            // handle success
            window.localStorage.setItem('madblog-token', response.data.token)
            store.loginAction()
            this.$toasted.success(`欢迎 ${this.sharedState.user_name}!`, {
              icon: 'fingerprint'
            })
            if (typeof this.$route.query.redirect == 'undefined') {
              this.$router.push('/')
            } else {
              this.$router.push(this.$route.query.redirect)
            }
          })
          .catch((error) => {
            // handle error
            // console.log('failed', error.response);
            if (typeof error.response != 'undefined') {
              if (error.response.status == 401) {
                this.loginForm.usernameError = '不合法的用户名或密码.'
                this.loginForm.passwordError = '不合法的用户名或密码.'
              } else {
                console.log(error.response)
              }
            }
          })
      }
    }
  }
</script>
<style scoped>
  .container {
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .form-bg {
    background: #00b4ef;
  }

  .form-horizontal {
    background: #fff;
    padding-bottom: 40px;
    border-radius: 15px;
    text-align: center;
    margin-left: 270px;
    margin-right: -270px;

  }

  .form-horizontal .heading {
    display: block;
    font-size: 30px;
    font-weight: 700;
    padding: 35px 0;
    border-bottom: 1px solid #f0f0f0;
    margin-bottom: 30px;
  }

  .form-horizontal .form-group {
    padding: 0 40px;
    margin: 0 0 55px 0;
    position: relative;
  }

  .form-horizontal .form-control {
    background: #f0f0f0;
    border: none;
    border-radius: 20px;
    box-shadow: none;
    padding: 0 20px 0 45px;
    height: 40px;
    transition: all 0.3s ease 0s;
  }

  .form-horizontal .form-control:focus {
    background: #e0e0e0;
    box-shadow: none;
    outline: 0 none;
  }

  .form-horizontal .form-group i {
    position: absolute;
    top: 12px;
    left: 60px;
    font-size: 17px;
    color: #c8c8c8;
    transition: all 0.5s ease 0s;
  }

  .form-horizontal .form-control:focus+i {
    color: #00b4ef;
  }

  .form-horizontal .fa-question-circle {
    display: inline-block;
    position: absolute;
    top: 12px;
    right: 60px;
    font-size: 20px;
    color: #808080;
    transition: all 0.5s ease 0s;
  }

  .form-horizontal .fa-question-circle:hover {
    color: #000;
  }


  .form-horizontal .main-checkbox label:after {
    content: "";
    width: 10px;
    height: 5px;
    position: absolute;
    top: 5px;
    left: 4px;
    border: 3px solid #fff;
    border-top: none;
    border-right: none;
    background: transparent;
    opacity: 0;
    -webkit-transform: rotate(-45deg);
    transform: rotate(-45deg);
  }

  .form-horizontal .main-checkbox input[type=checkbox] {
    visibility: hidden;
  }

  .form-horizontal .main-checkbox input[type=checkbox]:checked+label:after {
    opacity: 1;
  }

  .form-horizontal .text {
    float: left;
    margin-left: 7px;
    line-height: 20px;
    padding-top: 5px;
    text-transform: capitalize;
  }

  .form-horizontal .btn {
    float: right;
    font-size: 14px;
    color: #fff;
    background: #34f53e;
    border-radius: 30px;
    padding: 10px 25px;
    border: none;
    text-transform: capitalize;
    transition: all 0.5s ease 0s;
  }

  .attention {
    margin-left:315px;
    margin-top:-70px;
  }
  .attention .attention1 {
    margin-top: 0px;
  }

  @media only screen and (max-width: 659px) {
    .form-horizontal .form-group {
      padding: 0 25px;
    }

    .form-horizontal .form-group i {
      left: 45px;
      margin-top: 20px;
    }

    .form-horizontal .btn {
      padding: 10px 20px;
    }
  }
</style>