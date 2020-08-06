<template>
  <div class="alert" role="alert" v-bind:class="'alert-' + variant">
    {{ message }}
  </div>
</template>

<script>
export default {
  props: ['variant', 'message']
}
</script>
<style scoped>
  .container {
      font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
</style>