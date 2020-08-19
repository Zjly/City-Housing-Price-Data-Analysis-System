<template>
  <div class="container">
    <div class="row">
      <div class="col-md-offset-3 col-md-6">
        <form @submit.prevent="onSubmit" class="form-horizontal">
          <span class="heading">重置密码</span>
          <div class="form-group" v-bind:class="{'u-has-error-v1': resetPasswordForm.emailError}">
            <input type="email" v-model="resetPasswordForm.email" class="form-control" id="email"
              aria-describedby="emailHelp" placeholder="请输入账户邮箱">
            <i class="fa fa-envelope"></i>
            <small class="form-control-feedback"
              v-show="resetPasswordForm.emailError">{{ resetPasswordForm.emailError }}</small>
          </div>
          <div class="form-group">

            <button type="submit" class="btn btn-default">重置密码</button>
            <router-link v-bind:to="{ name: 'Login' }">
              <button class="btn btn-default" style="margin-right:248px">返回登录</button>
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'ResetPassword', // this is the name of the component
    data() {
      return {
        resetPasswordForm: {
          email: '',
          errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
          emailError: null,
        }
      }
    },
    methods: {
      onSubmit(e) {
        this.resetPasswordForm.errors = 0 // 重置
        if (!this.resetPasswordForm.email) {
          this.resetPasswordForm.errors++
          this.resetPasswordForm.emailError = 'Email required.'
        } else if (!this.validEmail(this.resetPasswordForm.email)) {
          this.resetPasswordForm.errors++
          this.resetPasswordForm.emailError = 'Valid email required.'
        } else {
          this.resetPasswordForm.emailError = null
        }
        if (this.resetPasswordForm.errors > 0) {
          // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
          return false
        }
        const path = '/api/reset-password-request'
        const payload = {
          confirm_email_base_url: window.location.href.split('/', 4).join('/') + '/reset-password/?token=',
          email: this.resetPasswordForm.email
        }
        this.$axios.post(path, payload)
          .then((response) => {
            // handle success
            this.$toasted.success(response.data.message, {
              icon: 'fingerprint'
            })
            this.$router.push('/login')
          })
          .catch((error) => {
            // handle error
            console.log(error.response.data)
            this.$toasted.error(error.response.data.message, {
              icon: 'fingerprint'
            })
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
    margin-left: 315px;
    margin-top: -70px;
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