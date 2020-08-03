<template>
    <div class="register">
        <el-container direction="vertical">
            <el-header>
                <el-menu :default-active="activeIndex" id="el-menu-nav" class="el-menu-nav" mode="horizontal"
                    @select="handleSelect" active-text-color="#3196FF" text-color="#95C9FF">
                    <el-menu-item style="min-inline-size: 30px;"></el-menu-item>
                    <el-menu-item style="min-inline-size: 200px;"><img style="height:80px;" src="img/bird2.gif">
                    </el-menu-item>
                    <el-menu-item index="1" class="el-menu-item-nav">首页</el-menu-item>
                    <el-menu-item index="2" class="el-menu-item-nav">房价查询</el-menu-item>
                    <el-menu-item index="3" class="el-menu-item-nav">政策信息</el-menu-item>
                    <el-menu-item index="4" class="el-menu-item-nav">房价预测</el-menu-item>
                    <el-menu-item></el-menu-item>
                    <el-menu-item style="min-inline-size: 150px;"></el-menu-item>
                    <el-menu-item style="min-inline-size: 110px;text-align:center;margin:0 auto"
                        class="el-menu-item-nav" index="5">
                        <u>登录</u>
                    </el-menu-item>
                    <el-menu-item style="min-inline-size: 0px;margin-left:-20px">|
                    </el-menu-item>
                    <el-menu-item style="min-inline-size: 100px;margin-left:-10px" index="6" class="el-menu-item-nav">
                        <u>注册</u>
                    </el-menu-item>
                </el-menu>
            </el-header>
            <el-container>
                <el-aside width="300px">Aside</el-aside>

                <el-main>
                    <div class="register-wrapper">
                        <div id="register">
                            <p class="title">注册</p>
                            <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" label-width="0"
                                class="demo-ruleForm">
                                <el-form-item prop="tel">
                                    <el-input v-model="ruleForm2.tel" auto-complete="off" placeholder="请输入手机号">
                                    </el-input>
                                </el-form-item>
                                <el-form-item prop="smscode" class="code">
                                    <el-input v-model="ruleForm2.smscode" placeholder="验证码"></el-input>
                                    <el-button type="primary" :disabled='isDisabled' @click="sendCode">
                                        {{buttonText}}</el-button>
                                </el-form-item>
                                <el-form-item prop="pass">
                                    <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"
                                        placeholder="输入密码"></el-input>
                                </el-form-item>
                                <el-form-item prop="checkPass">
                                    <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off"
                                        placeholder="确认密码"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="submitForm('ruleForm2')" style="width:100%;">
                                        注册</el-button>
                                    <p class="login" @click="gotoLogin">已有账号？立即登录</p>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-main>
            </el-container>
        </el-container>


    </div>
</template>

<script>
    // @ is an alias to /src

    // 注册页面
    export default {
        name: 'Register',
        data() {
            // <!--验证手机号是否合法-->
            let checkTel = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入手机号码'))
                } else if (!this.checkMobile(value)) {
                    callback(new Error('手机号码不合法'))
                } else {
                    callback()
                }
            };
            //  <!--验证码是否为空-->
            let checkSmscode = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入手机验证码'))
                } else {
                    callback()
                }
            };
            // <!--验证密码-->
            let validatePass = (rule, value, callback) => {
                if (value === "") {
                    callback(new Error("请输入密码"))
                } else {
                    if (this.ruleForm2.checkPass !== "") {
                        this.$refs.ruleForm2.validateField("checkPass");
                    }
                    callback()
                }
            };

            // <!--二次验证密码-->
            let validatePass2 = (rule, value, callback) => {
                if (value === "") {
                    callback(new Error("请再次输入密码"));
                } else if (value !== this.ruleForm2.pass) {
                    callback(new Error("两次输入密码不一致!"));
                } else {
                    callback();
                }
            };
            return {
                activeIndex: '6',
                ruleForm2: {
                    pass: "",
                    checkPass: "",
                    tel: "",
                    smscode: ""
                },
                rules2: {
                    pass: [{
                        validator: validatePass,
                        trigger: 'change'
                    }],
                    checkPass: [{
                        validator: validatePass2,
                        trigger: 'change'
                    }],
                    tel: [{
                        validator: checkTel,
                        trigger: 'change'
                    }],
                    smscode: [{
                        validator: checkSmscode,
                        trigger: 'change'
                    }],
                },
                buttonText: '发送验证码',
                isDisabled: false, // 是否禁止点击发送验证码按钮
                flag: true
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
            // <!--发送验证码-->
            sendCode() {
                let tel = this.ruleForm2.tel
                if (this.checkMobile(tel)) {
                    console.log(tel)
                    let time = 60
                    this.buttonText = '已发送'
                    this.isDisabled = true
                    if (this.flag) {
                        this.flag = false;
                        let timer = setInterval(() => {
                            time--;
                            this.buttonText = time + ' 秒'
                            if (time === 0) {
                                clearInterval(timer);
                                this.buttonText = '重新获取'
                                this.isDisabled = false
                                this.flag = true;
                            }
                        }, 1000)
                    }
                }
            },
            // <!--提交注册-->
            submitForm(formName) {
                this.$refs[formName].validate(valid => {
                    if (valid) {
                        setTimeout(() => {
                            alert('注册成功')
                        }, 400);
                    } else {
                        console.log("error submit!!");
                        return false;
                    }
                })
            },
            // <!--进入登录页-->
            gotoLogin() {
                this.$router.push({
                    path: "/login"
                });
            },
            // 验证手机号
            checkMobile(str) {
                let re = /^1\d{10}$/
                if (re.test(str)) {
                    return true;
                } else {
                    return false;
                }
            }


        },
        components: {

        },
    }
</script>
<style scoped>
    .register {
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

    .el-aside {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 600px;
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

    .loading-wrapper {
        /* position: fixed; */
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        background: #aedff8;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .register-wrapper img {
        /* position: absolute; */
        z-index: 1;
    }

    .register-wrapper {
        /* position: fixed; */
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
    }

    #register {
        max-width: 400px;
        margin: 60px auto;
        background: #fff;
        padding: 20px 40px;
        border-radius: 10px;
        position: relative;
        z-index: 9;
    }

    .title {
        font-size: 27px;
        line-height: 150px;
        font-weight: bold;
        margin-top: -100px;
        /* margin: 10px; */
        text-align: center;
    }

    .el-form-item {
        text-align: center;
    }

    .login {
        margin-top: 10px;
        font-size: 14px;
        line-height: 22px;
        color: #1ab2ff;
        cursor: pointer;
        text-align: left;
        text-indent: 8px;
        width: 160px;
    }

    .login:hover {
        color: #2c2fd6;
    }

    .code>>>.el-form-item__content {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .code button {
        margin-left: 20px;
        width: 140px;
        text-align: center;
    }

    .el-button--primary:focus {
        background: #409EFF;
        border-color: #409EFF;
        color: #fff;
    }
</style>