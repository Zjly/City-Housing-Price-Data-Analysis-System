<template>
  <div class="container">
    <div class="row">
      <div class="col-md-offset-3 col-md-6">
        <form @submit.prevent="onSubmit" class="form-horizontal">
          <span class="heading">注册新用户</span>
          <div class="form-group" v-bind:class="{'u-has-error-v1': registerForm.usernameError}">
            <input type="text" v-model="registerForm.username" class="form-control" id="username" placeholder="用户名">
            <i class="fa fa-user"></i>
            <small v-if="!registerForm.emailError" id="usernameHelp"
              style="font-size:13px;text-align:left;margin-left:15px" class="form-text text-muted">用户名具有唯一性.</small>
            <small class="form-control-feedback"
              v-show="registerForm.usernameError">{{ registerForm.usernameError }}</small>
          </div>
          <div class="form-group" v-bind:class="{'u-has-error-v1': registerForm.emailError}">
            <input type="email" v-model="registerForm.email" class="form-control" id="email"
              aria-describedby="emailHelp" placeholder="输入注册邮箱">
            <i class="fa fa-envelope"></i>
            <small v-if="!registerForm.emailError" id="emailHelp"
              style="font-size:13px;text-align:left;margin-left:15px" class="form-text text-muted">我们不会泄露您的隐私.</small>
            <small class="form-control-feedback" v-show="registerForm.emailError">{{ registerForm.emailError }}</small>
          </div>
          <div class="form-group" v-bind:class="{'u-has-error-v1': registerForm.passwordError}">
            <input type="password" v-model="registerForm.password" class="form-control" id="password"
              placeholder="请输入密码">
            <i class="fa fa-lock"></i>
            <small class="form-control-feedback"
              v-show="registerForm.passwordError">{{ registerForm.passwordError }}</small>
          </div>
          <div class="form-group">
            <el-checkbox v-model="checked" style="margin-left:-110px;margin-top:10px">
              <span>同意</span>
              <span>
                <router-link v-bind:to="{ name: 'Agreement' }">房价云制订的用户协议和免责条款</router-link>
              </span>
            </el-checkbox>
            <button type="submit" class="btn btn-default">注册</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Register', //this is the name of the component
    data() {
      return {
        checked: true,
        registerForm: {
          username: '',
          email: '',
          password: '',
          errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
          usernameError: null,
          emailError: null,
          passwordError: null
        }
      }
    },
    methods: {
      onSubmit(e) {
        this.registerForm.errors = 0 // 重置
        if (!this.registerForm.username) {
          this.registerForm.errors++
          this.registerForm.usernameError = 'Username required.'
        } else {
          this.registerForm.usernameError = null
        }

        if (!this.registerForm.email) {
          this.registerForm.errors++
          this.registerForm.emailError = 'Email required.'
        } else if (!this.validEmail(this.registerForm.email)) {
          this.registerForm.errors++
          this.registerForm.emailError = 'Valid email required.'
        } else {
          this.registerForm.emailError = null
        }
        if (!this.registerForm.password) {
          this.registerForm.errors++
          this.registerForm.passwordError = 'Password required.'
        } else if (this.checked == false) {
          this.registerForm.errors++
          setTimeout(() => {
            this.$confirm('您没有同意房价云制订的用户协议和免责条款?', '提示', {
              confirmButtonText: '确定',
              cancelButtonText: '取消',
              type: 'error',
              center: true
            }).then(() => {
              this.checked = true;
              this.$message({
                type: 'success',
                message: '已经自动同意协议条款！请重新注册'
              });
            }).catch(() => {
              this.$message({
                type: 'warning',
                message: '请同意协议条款!'
              });
            });
            // alert('您没有同意房价云制订的用户协议和免责条款')
          }, 300);
        } else {
          this.registerForm.passwordError = null
        }

        if (this.registerForm.errors > 0) {
          // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
          return false
        }
        const path = '/api/users'
        const payload = {
          confirm_email_base_url: window.location.href.split('/', 4).join('/') + '/unconfirmed/?token=',
          username: this.registerForm.username,
          email: this.registerForm.email,
          password: this.registerForm.password
        }
        this.$axios.post(path, payload)
          .then((response) => {
            // handle success
            this.$toasted.success('A confirmation email has been sent to you by email.', {
              icon: 'fingerprint'
            })
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
              }
            }
          })
      },
      validEmail: function (email) {
        var re =
          /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
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
    margin: 0 0 35px 0;
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

  .form-horizontal .main-checkbox {
    float: left;
    width: 20px;
    height: 20px;
    background: #11a3fc;
    border-radius: 50%;
    position: relative;
    margin: 5px 0 0 5px;
    border: 1px solid #11a3fc;
  }

  .form-horizontal .main-checkbox label {
    width: 20px;
    height: 20px;
    position: absolute;
    top: 0;
    left: 0;
    cursor: pointer;
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
    font-size: 13px;
    margin-top: 10px;
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