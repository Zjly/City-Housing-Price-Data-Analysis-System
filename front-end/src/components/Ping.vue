<template>
<!-- 用于测试vue前端的功能是否正常 -->
  <div class="container">
      <!-- 测试bootstrap风格按钮 -->
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>


<script>
// 引入axios，用于前后端交互
import axios from 'axios'

export default {
  name: 'Ping',
  data() {
    return {
      // 空值，其值需要后端传递
      msg: ''
    }
  },
  methods: {
      getMessage() {
          const path = 'http://127.0.0.1:5000/api/ping'
          axios.get(path)
            .then((res) => {
                this.msg = res.data;
            })
            .catch((error) =>{
                // eslint-disable-next-line
                console.error(error);
            })
      }
  },
  created() {
      this.getMessage()
  }
}
</script>