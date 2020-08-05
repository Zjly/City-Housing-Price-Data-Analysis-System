<template>
    <div class="Login">
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
                <el-aside width="500px" v-show="showDatabase">
                    <div class="re_left">
                        <label>房价云大数据库</label>
                        <p><span>Big Database</span></p>
                        <p><small>获取超过5年的时间序列房产数据
                                <br>持续稳定的数据来源，周度更新频率
                                <br>应用广泛的房产大数据库
                            </small>
                        </p>

                    </div>
                </el-aside>

                <el-main>
                    <div class="login-wrapper" v-show="showLogin">
                        <div id="login">
                            <p class="title">登录</p>
                            <el-form :model="ruleForm1" status-icon :rules="rules2" ref="ruleForm1" label-width="0"
                                class="demo-ruleForm">
                                <el-form-item prop="Mail">
                                    <el-input v-model="ruleForm1.Mail" auto-complete="off" placeholder="请输入邮箱号码">
                                    </el-input>
                                </el-form-item>
                                <el-form-item prop="smscode" class="code">
                                    <el-input v-model="ruleForm1.smscode" placeholder="验证码"></el-input>
                                    <img :src="imgList[r_num].idView" :id="r_num" class="image">
                                </el-form-item>
                                <el-form-item prop="pass">
                                    <el-input type="password" v-model="ruleForm1.pass" auto-complete="off"
                                        placeholder="输入密码"></el-input>
                                </el-form-item>
                                <template class="checkbox1">
                                    <!-- `checked` 为 true 或 false -->
                                    <el-checkbox v-model="checked">同意</el-checkbox>&nbsp;
                                    <el-link type="primary" style="margin-top:2px">房价云制订的用户协议和免责条款</el-link>
                                </template>
                                <br>
                                <br>
                                <el-form-item>
                                    <el-button type="primary" @click="submitForm('ruleForm1')" style="width:100%;">
                                        登录</el-button>
                                    <p class="Regiter" @click="gotoRegister">没有账号？立即注册</p>
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
    import {
        setCookie,
        getCookie
    } from '../../assets/js/cookie.js'

    // 注册页面
    export default {
        name: 'Register',
        data() {
            // 生成随机整数
            var r_num = Math.floor(Math.random() * 2 + 1);

            var imgList = [{
                    id: 0,
                    name: 'wy71',
                    idView: require('../assets/images/randomCode.jpg')
                },
                {
                    id: 1,
                    name: 'k5b2',
                    idView: require('../assets/images/randomCode1.jpg')
                },
                {
                    id: 2,
                    name: 'umt8',
                    idView: require('../assets/images/randomCode2.jpg')
                }
            ];
            // <!--验证邮箱号是否合法-->
            let checkmail = (rule, value, callback) => {

                if (value === '') {
                    callback(new Error('请输入邮箱'))
                } else if (!this.checkMail(value)) {
                    callback(new Error('邮箱不合法'))
                } else {
                    callback()
                }
            };
            //  <!--验证码是否为空-->
            let checkSmscode = (rule, value, callback) => {
                if (value === '') {
                    console.log(r_num)
                    callback(new Error('请输入验证码'))
                } else if (value !== imgList[r_num].name) {
                    console.log(imgList[r_num].name)
                    callback(new Error('验证码错误'))

                } else {
                    callback()
                }
            };
            // <!--验证密码-->
            let validatePass = (rule, value, callback) => {
                if (value === "") {
                    callback(new Error("请输入密码"))
                } else {
                    if (this.ruleForm1.checkPass !== "") {
                        this.$refs.ruleForm1.validateField("checkPass");
                    }
                    callback()
                }
            };

            // <!--二次验证密码-->
            let validatePass2 = (rule, value, callback) => {
                if (value === "") {
                    callback(new Error("请再次输入密码"));
                } else if (value !== this.ruleForm1.pass) {
                    callback(new Error("两次输入密码不一致!"));
                } else {
                    callback();
                }
            };
            return {
                activeIndex: '5',
                checked: false,
                showLogin: true,
                showDatabase: true,
                imgList: [{
                        id: 0,
                        name: 'wy71',
                        idView: require('../assets/images/randomCode.jpg')
                    },
                    {
                        id: 1,
                        name: 'k5b2',
                        idView: require('../assets/images/randomCode1.jpg')
                    },
                    {
                        id: 2,
                        name: 'umt8',
                        idView: require('../assets/images/randomCode2.jpg')
                    }
                ],
                ruleForm1: {
                    pass: "",
                    checkPass: "",
                    Mail: "",
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
                    Mail: [{
                        validator: checkmail,
                        trigger: 'change'
                    }],
                    smscode: [{
                        validator: checkSmscode,
                        trigger: 'change'
                    }],
                },
                r_num,
                buttonText: '发送验证码',
                isDisabled: false, // 是否禁止点击发送验证码按钮
                flag: true
            };
        },
        mounted() {
            if (getCookie("username")) {
                this.$router.push('/home')
            }
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
                let Mail = this.ruleForm1.Mail
                if (this.checkMail(Mail)) {
                    console.log(Mail)
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
            // <!--提交登录-->
            submitForm(formName) {
                this.$refs[formName].validate(valid => {
                    if (this.checked == false) {
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
                                    message: '已经自动同意协议条款！请重新登录'
                                });
                            }).catch(() => {
                                this.$message({
                                    type: 'warning',
                                    message: '请同意协议条款!'
                                });
                            });
                            // alert('您没有同意房价云制订的用户协议和免责条款')
                        }, 300);
                    } else if (valid) {
                        setTimeout(() => {
                            // URLSearchParams对象是为了让参数以form data形式
                            let params = new URLSearchParams();
                            params.append('username', this.ruleForm1.Mail);
                            params.append('password', this.ruleForm1.pass);
                            this.axios.post("http://127.0.0.1:5000/login", params).then((res) => {
                                console.log(res.data)
                                console.log(typeof res.data)
                                if (res.data == -1) {
                                    this.$alert('该用户不存在', '提示', {
                                        type: 'warning',
                                        confirmButtonText: '确定',
                                        center: true
                                    });
                                } else if (res.data == 0) {
                                    this.$alert('密码输入错误', '提示', {
                                        type: 'warning',
                                        confirmButtonText: '确定',
                                        center: true
                                    });
                                    this.showTishi = true
                                } else if (res.data == "admin") {
                                    this.$router.push("/home")
                                } else {
                                    this.$alert('登录成功', '提示', {
                                        type: 'success',
                                        confirmButtonText: '确定',
                                        center: true,
                                        callback: action => {
                                            this.$message({
                                                type: 'success',
                                                message: `${ action } ：已成功跳转到个人中心！ `
                                            });
                                        }
                                    });
                                    // alert('登录成功')
                                    setCookie("username", this.ruleForm1.Mail, 1000 * 60)
                                    setTimeout(function () {
                                        this.$router.push("/home")
                                    }.bind(this), 1000)
                                }
                            })


                        }, 400);
                    } else {
                        setTimeout(() => {
                            this.$confirm('您没有输入正确的验证码或账号密码匹配不成功?', '提示', {
                                confirmButtonText: '提交修改',
                                cancelButtonText: '重新输入',
                                type: 'error',
                                center: true
                            }).then(() => {
                                this.$message({
                                    type: 'warning',
                                    message: '请修改输入表单！'
                                });
                            }).catch(() => {
                                this.$refs[formName].resetFields();
                                this.$message({
                                    type: 'info',
                                    message: '已刷新表单！'
                                });
                            });
                            // alert('验证码错误或密码和账号不匹配')
                        }, 300);

                        console.log("error submit!!");
                        return false;
                    }
                })
            },
            // <!--进入登录页-->
            gotoRegister() {
                this.$router.push({
                    path: "/Register"
                });
            },
            // 验证邮箱号
            checkMail(str) {
                let re = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
                if (re.test(str)) {
                    return true;
                } else {
                    return false;
                }
            },
            // 验证验证码





        },
        components: {


        },

    }
</script>
<style scoped>
    .Login {
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

        color: #333;
        text-align: center;
        background-image: url("../assets/images/re_left.png");
    }

    .re_left {
        text-align: left;
        margin-left: 20px;
        margin-top: 40px;
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

    .login-wrapper img {
        /* position: absolute; */
        z-index: 1;
    }

    .login-wrapper {
        /* position: fixed; */
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
    }

    #login {
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

    .Regiter {
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

    .el-checkbox {
        margin-left: -130px;
    }

    .image {
        height: 50px;
        margin-left: 20px;
        width: 130px;
    }
</style>