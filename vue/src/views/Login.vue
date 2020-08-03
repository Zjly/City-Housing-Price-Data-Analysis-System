<template>
    <div class="login">
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
                    登录<br><br>
                    <el-main>
                        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                            class="demo-ruleForm">
                            <el-form-item label="账号" prop="pass">
                                <el-input type="text"  autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="密码" prop="pass">
                                <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="确认密码" prop="checkPass">
                                <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="年龄" prop="age">
                                <el-input v-model.number="ruleForm.age"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                                <el-button @click="resetForm('ruleForm')">重置</el-button>
                            </el-form-item>
                        </el-form>

                    </el-main>
                </el-main>
            </el-container>

        </el-container>

    </div>
</template>

<script>
    // @ is an alias to /src

    // 主页
    export default {
        name: 'Login',
        data() {
            var checkAge = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('年龄不能为空'));
                }
                setTimeout(() => {
                    if (!Number.isInteger(value)) {
                        callback(new Error('请输入数字值'));
                    } else {
                        if (value < 18) {
                            callback(new Error('必须年满18岁'));
                        } else {
                            callback();
                        }
                    }

                }, 1000)

            };
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    if (this.ruleForm.checkPass !== '') {
                        this.$refs.ruleForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.pass) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };

            return {
                activeIndex: '5',
                ruleForm: {
                    pass: '',
                    checkPass: '',
                    age: ''
                },
                rules: {
                    pass: [{
                        validator: validatePass,
                        trigger: 'blur'
                    }],
                    checkPass: [{
                        validator: validatePass2,
                        trigger: 'blur'
                    }],
                    age: [{
                        validator: checkAge,
                        trigger: 'blur'
                    }]
                }
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
<style scoped>
    .login {
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
</style>