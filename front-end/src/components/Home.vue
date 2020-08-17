<template>
  <div class="container">

    <!-- Modal: Edit Post -->
    <div class="modal fade" id="editPostModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editPostModalTitle">更新文章</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">

            <form id="editPostForm" @submit.prevent="onSubmitUpdatePost" @reset.prevent="onResetUpdatePost">
              <div class="form-group" v-bind:class="{'u-has-error-v1': editPostForm.titleError}">
                <input type="text" v-model="editPostForm.title" class="form-control" id="editPostFormTitle"
                  placeholder="标题">
                <small class="form-control-feedback"
                  v-show="editPostForm.titleError">{{ editPostForm.titleError }}</small>
              </div>
              <div class="form-group">
                <input type="text" v-model="editPostForm.summary" class="form-control" id="editPostFormSummary"
                  placeholder="摘要">
              </div>
              <div class="form-group">
                <textarea v-model="editPostForm.body" class="form-control" id="editPostFormBody" rows="5"
                  placeholder=" 内容"></textarea>
                <small class="form-control-feedback"
                  v-show="editPostForm.bodyError">{{ editPostForm.bodyError }}</small>
              </div>
              <button type="reset" class="btn btn-secondary">Cancel</button>
              <button type="submit" class="btn btn-primary">Update</button>
            </form>

          </div>
        </div>
      </div>
    </div>

    <form id="addPostForm" v-if="sharedState.is_authenticated && sharedState.user_perms.includes('write')"
      @submit.prevent="onSubmitAddPost" class="g-mb-40">
      <div class="form-group" v-bind:class="{'u-has-error-v1': postForm.titleError}">
        <input type="text" v-model="postForm.title" class="form-control" id="postFormTitle" placeholder="标题">
        <small class="form-control-feedback" v-show="postForm.titleError">{{ postForm.titleError }}</small>
      </div>
      <div class="form-group">
        <input type="text" v-model="postForm.summary" class="form-control" id="postFormSummary" placeholder="摘要">
      </div>
      <div class="form-group">
        <textarea v-model="postForm.body" class="form-control" id="postFormBody" rows="5" placeholder=" 内容"></textarea>
        <small class="form-control-feedback" v-show="postForm.bodyError">{{ postForm.bodyError }}</small>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <template>
      <el-carousel :interval="5000" height="300px" wight="1000px" arrow="always" style="margin-top:-20px">
        <!-- v-for="(item, index) in news" :key="item.id" title="" -->
        <el-carousel-item v-for="item in imgList" :key="item.id">
          <el-row>
            <el-col :span="24"><img ref="imgHeight" :src="item.idView" class="banner_img" />

              <div v-if="item.id == 0 " class="introduce"
                style="position:absolute;width:450px;height:100px;z-indent:2;left:0;top:0;">

                <p class="title">
                  房产介绍
                </p>

                <p>
                  房价网走势频道提供城市精准及时、权威全面的房价行情走势
                </p>
                <p>
                  为各城市随时免费提供查询最新季度房价、最近半年房价走势。
                </p>
                <p>
                  希望每周的房价走势数据，能让你更好的判断当前房价形势和更好的预计的房价走向。
                </p>

              </div>
              <div v-if="item.id == 1 " class="introduce"
                style="position:absolute;width:450px;height:100px;z-indent:2;left:0;top:0;">

                <p class="title">
                  大数据预测
                </p>

                <p>
                  房价网预测频道提供城市精准及时、权威全面的房价预测数据
                </p>
                <p>
                  结合基于地址的大数据，更进一步精准营销，发现地址价值
                </p>
                <p>
                  我们会对每一个地址、以及每一个地理空间位置，赋予地址背后的更多维度画像，助力更加精准的地理位置营销。
                </p>

              </div>
              <div v-if="item.id == 2 " class="introduce"
                style="position:absolute;width:450px;height:100px;z-indent:2;left:0;top:0;">

                <p class="title">
                  房价查询
                </p>

                <p>
                  房价云频道提供城市精准及时、权威全面的房价行情数据
                </p>
                <p>
                  高效率、高智能的批量地址标准化分析与处理
                </p>
                <p>
                  房价网基于强大的CPDB数据库和人机技术，为各行业提供高效智能的地址标准化服务。
                </p>

              </div>

            </el-col>

          </el-row>
        </el-carousel-item>
      </el-carousel>
    </template>
    <template>
      <p></p>
      <div class="que">
        <p>
          为什么选择我们
          <br>
        </p>
        <p></p>

      </div>
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item name="1">
          <template slot="title">
            <p class="item-title">一致性 Consistency</p><i class="header-icon el-icon-info"></i>
          </template>
          <br>
          <div class="item-content">与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
          <div class="item-content">在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
        </el-collapse-item>
        <el-collapse-item name="2">
          <template slot="title">
            <p class="item-title">反馈 Feedback</p><i class="header-icon el-icon-info"></i>
          </template>
          <br>
          <div class="item-content">控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
          <div class="item-content">页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
        </el-collapse-item>
        <el-collapse-item name="3">
          <template slot="title">
            <p class="item-title">效率 Efficiency</p><i class="header-icon el-icon-info"></i>
          </template>
          <br>
          <div class="item-content">简化流程：设计简洁直观的操作流程；</div>
          <div class="item-content">清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
          <div class="item-content">帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
        </el-collapse-item>
        <el-collapse-item name="4">
          <template slot="title">
            <p class="item-title">可控 Controllability</p><i class="header-icon el-icon-info"></i>
          </template>
          <br>
          <div class="item-content">用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
          <div class="item-content">结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
        </el-collapse-item>
        <el-collapse-item name="5">
          <template slot="title">
            <p class="item-title">其他 Others</p><i class="header-icon el-icon-info"></i>
          </template>
          <br>
          <div class="item-content">用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
          <div class="item-content">结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
        </el-collapse-item>

      </el-collapse>
    </template>
    <div class="que">
      <p>
        最新行情
      </p>
      <br>
    </div>
    <div id="container">
    </div>
    <br>

    <div class="card border-0 g-mb-15">
      <!-- Panel Header -->
      <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
        <h3 class="h6 mb-0">
          <i class="icon-bubbles g-pos-rel g-top-1 g-mr-5"></i> 所有资讯 <small v-if="posts">(共
            {{ posts._meta.total_items }} 篇, {{ posts._meta.total_pages }} 页)</small>
        </h3>

        <div class="dropdown g-mb-10 g-mb-0--md">
          <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown"
            aria-haspopup="true" aria-expanded="false">
            <i class="icon-options-vertical g-pos-rel g-top-1"></i>
          </span>
          <div class="dropdown-menu dropdown-menu-right rounded-0 g-mt-10">
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 1 }}"
              class="dropdown-item g-px-10">
              <i class="icon-plus g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 1 篇
            </router-link>
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 5 }}"
              class="dropdown-item g-px-10">
              <i class="icon-layers g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 5 篇
            </router-link>
            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 10 }}"
              class="dropdown-item g-px-10">
              <i class="icon-wallet g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 10 篇
            </router-link>

            <div class="dropdown-divider"></div>

            <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 20 }}"
              class="dropdown-item g-px-10">
              <i class="icon-fire g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 20 篇
            </router-link>

          </div>
        </div>
      </div>
      <!-- End Panel Header -->

      <!-- Panel Body -->
      <div v-if="posts" class="card-block g-pa-0">

        <post v-for="(post, index) in posts.items" v-bind:key="index" v-bind:post="post"
          v-on:edit-post="onEditPost(post)" v-on:delete-post="onDeletePost(post)">
        </post>

      </div>
      <!-- End Panel Body -->
    </div>

    <!-- Pagination #04 -->
    <div v-if="posts && posts._meta.total_pages > 1">
      <pagination v-bind:cur-page="posts._meta.page" v-bind:per-page="posts._meta.per_page"
        v-bind:total-pages="posts._meta.total_pages">
      </pagination>
    </div>
    <!-- End Pagination #04 -->
    <el-footer>
      <div class="footer">
        <template>
          <div>
            <el-row :gutter="12">
              <el-col :span="8">
                <span>
                  <el-card class="box-card" shadow="hover">
                    <div class="text item" id="item-title">
                      小组成员
                    </div>
                    <div class="text item">
                      组长：张雷
                    </div>
                    <div class="text item">
                      组员：王亮
                    </div>
                    <div class="text item">
                      组员：汪志豪
                    </div>
                    <div class="text item">
                      组员：夏宇航
                    </div>
                  </el-card>
                </span>
              </el-col>
              <el-col :span="8">
                <span>
                  <el-card class="box-card" shadow="hover">
                    <div class="text item" id="item-title">
                      关于我们
                    </div>
                    <div class="text item">
                      小组简介
                    </div>
                    <div class="text item">
                      联系我们
                    </div>
                    <div class="text item">
                      合作伙伴
                    </div>
                    <div class="text item">
                      人才招募
                    </div>
                  </el-card>
                </span>

              </el-col>

              <el-col :span="8">
                <span>
                  <el-card class="box-card" shadow="hover">
                    <div class="text item" id="item-title">
                      网页说明
                    </div>
                    <div class="text item">
                      用户协议
                    </div>
                    <div class="text item">
                      版权声明
                    </div>
                    <div class="text item">
                      免责条款
                    </div>
                  </el-card>
                </span>
              </el-col>
            </el-row>
          </div>
        </template>
      </div>
      <span style="text-align: center;margin-left:350px;font-size:20px">©<label>2020</label> 武汉大学 28组 房价云 版权所有</span><br>

    </el-footer>

  </div>


</template>

<script>
  import store from '../store'
  import Post from './Base/Post'
  import Pagination from './Base/Pagination'
  // bootstrap-markdown 编辑器依赖的 JS 文件，初始化编辑器在组件的 created() 方法中，同时它需要 JQuery 支持哦
  import '../assets/bootstrap-markdown/js/bootstrap-markdown.js'
  import '../assets/bootstrap-markdown/js/bootstrap-markdown.zh.js'
  import '../assets/bootstrap-markdown/js/marked.js'


  export default {
    name: 'Home', //this is the name of the component
    components: {
      Post,
      Pagination
    },
    data() {
      return {
        activeName: '1',
        sharedState: store.state,
        posts: '',
        postForm: {
          title: '',
          summary: '',
          body: '',
          errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
          titleError: null,
          bodyError: null
        },
        editPostForm: {
          title: '',
          summary: '',
          body: '',
          errors: 0, // 表单是否在前端验证通过，0 表示没有错误，验证通过
          titleError: null,
          bodyError: null
        },
        imgList: [{
            id: 0,
            name: '介绍',
            idView: require('../assets/images/introduce_banner2.jpg')
          },
          {
            id: 1,
            name: '详情',
            idView: require('../assets/images/dmp_banner2.jpg')
          },
          {
            id: 2,
            name: '推荐',
            idView: require('../assets/images/standardization_banner3.jpg')
          }
        ]
      }
    },
    methods: {
      getPosts() {
        let page = 1
        let per_page = 5
        if (typeof this.$route.query.page != 'undefined') {
          page = this.$route.query.page
        }

        if (typeof this.$route.query.per_page != 'undefined') {
          per_page = this.$route.query.per_page
        }

        const path = `/api/posts/?page=${page}&per_page=${per_page}`
        this.$axios.get(path)
          .then((response) => {
            // handle success
            this.posts = response.data
          })
          .catch((error) => {
            // handle error
            console.log(error.response.data)
            this.$toasted.error(error.response.data.message, {
              icon: 'fingerprint'
            })
          })
      },
      onSubmitAddPost(e) {
        this.postForm.errors = 0 // 重置

        if (!this.postForm.title) {
          this.postForm.errors++
          this.postForm.titleError = 'Title is required.'
        } else {
          this.postForm.titleError = null
        }

        if (!this.postForm.body) {
          this.postForm.errors++
          this.postForm.bodyError = 'Body is required.'
          // 给 bootstrap-markdown 编辑器内容添加警示样式，而不是添加到 #postFormBody 上
          $('#addPostForm .md-editor').closest('.form-group').addClass('u-has-error-v1') // Bootstrap 4
        } else {
          this.postForm.bodyError = null
          $('#addPostForm .md-editor').closest('.form-group').removeClass('u-has-error-v1')
        }

        if (this.postForm.errors > 0) {
          // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
          return false
        }

        const path = '/api/posts'
        const payload = {
          title: this.postForm.title,
          summary: this.postForm.summary,
          body: this.postForm.body
        }
        this.$axios.post(path, payload)
          .then((response) => {
            // handle success
            this.getPosts()
            this.$toasted.success('Successed add a new post.', {
              icon: 'fingerprint'
            })
            this.postForm.title = '',
              this.postForm.summary = '',
              this.postForm.body = ''
          })
          .catch((error) => {
            // handle error
            console.log(error.response.data)
            this.$toasted.error(error.response.data.message, {
              icon: 'fingerprint'
            })
          })
      },
      onEditPost(post) {
        // 不要使用对象引用赋值： this.editPostForm = post
        // 这样是同一个 post 对象，用户在 editPostForm 中的操作会双向绑定到该 post 上， 你会看到 modal 下面的也在变
        // 如果用户修改了一些数据，但是点了 cancel，你就必须在 onResetUpdatePost() 中重新加载一次列表，不然用户会看到修改后但未提交的不对称信息
        this.editPostForm = Object.assign({}, post)
      },
      onSubmitUpdatePost() {
        this.editPostForm.errors = 0 // 重置
        // 每次提交前先移除错误，不然错误就会累加
        $('#editPostForm .form-control-feedback').remove()
        $('#editPostForm .form-group.u-has-error-v1').removeClass('u-has-error-v1')

        if (!this.editPostForm.title) {
          this.editPostForm.errors++
          this.editPostForm.titleError = 'Title is required.'
          // boostrap4 modal依赖jQuery，不兼容 vue.js 的双向绑定。所以要手动添加警示样式和错误提示
          $('#editPostFormTitle').closest('.form-group').addClass('u-has-error-v1') // Bootstrap 4
          $('#editPostFormTitle').after('<small class="form-control-feedback">' + this.editPostForm.titleError +
            '</small>')
        } else {
          this.editPostForm.titleError = null
        }

        if (!this.editPostForm.body) {
          this.editPostForm.errors++
          this.editPostForm.bodyError = 'Body is required.'
          // boostrap4 modal依赖jQuery，不兼容 vue.js 的双向绑定。所以要手动添加警示样式和错误提示
          // 给 bootstrap-markdown 编辑器内容添加警示样式，而不是添加到 #postFormBody 上
          $('#editPostForm .md-editor').closest('.form-group').addClass('u-has-error-v1') // Bootstrap 4
          $('#editPostForm .md-editor').after('<small class="form-control-feedback">' + this.editPostForm.bodyError +
            '</small>')
        } else {
          this.editPostForm.bodyError = null
        }

        if (this.editPostForm.errors > 0) {
          // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
          return false
        }

        // 先隐藏 Modal
        $('#editPostModal').modal('hide')

        const path = `/api/posts/${this.editPostForm.id}`
        const payload = {
          title: this.editPostForm.title,
          summary: this.editPostForm.summary,
          body: this.editPostForm.body
        }
        this.$axios.put(path, payload)
          .then((response) => {
            // handle success
            this.getPosts()
            this.$toasted.success('Successed update the post.', {
              icon: 'fingerprint'
            })
            this.editPostForm.title = '',
              this.editPostForm.summary = '',
              this.editPostForm.body = ''
          })
          .catch((error) => {
            // handle error
            console.log(error.response.data)
            this.$toasted.error(error.response.data.message, {
              icon: 'fingerprint'
            })
          })
      },
      onResetUpdatePost() {
        // 先移除错误
        $('#editPostForm .form-control-feedback').remove()
        $('#editPostForm .form-group.u-has-error-v1').removeClass('u-has-error-v1')
        // 再隐藏 Modal
        $('#editPostModal').modal('hide')
        // this.getPosts()
        this.$toasted.info('Cancelled, the post is not update.', {
          icon: 'fingerprint'
        })
      },
      onDeletePost(post) {
        this.$swal({
          title: "Are you sure?",
          text: "该操作将彻底删除 [ " + post.title + " ], 请慎重",
          type: "warning",
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, delete it!',
          cancelButtonText: 'No, cancel!'
        }).then((result) => {
          if (result.value) {
            const path = `/api/posts/${post.id}`
            this.$axios.delete(path)
              .then((response) => {
                // handle success
                this.$swal('Deleted', 'You successfully deleted this post', 'success')
                // this.$toasted.success('Successed delete the post.', { icon: 'fingerprint' })
                this.getPosts()
              })
              .catch((error) => {
                // handle error
                console.log(error.response.data)
                this.$toasted.error(error.response.data.message, {
                  icon: 'fingerprint'
                })
              })
          } else {
            this.$swal('Cancelled', 'The post is safe :)', 'error')
          }
        })
      }
    },
    created() {
      this.getPosts()
      // 初始化 bootstrap-markdown 插件
      $(document).ready(function () {
        $("#postFormBody, #editPostFormBody").markdown({
          autofocus: false,
          savable: false,
          iconlibrary: 'fa', // 使用Font Awesome图标
          language: 'zh'
        })
      })
    },
    // 当查询参数 page 或 per_page 变化后重新加载数据
    beforeRouteUpdate(to, from, next) {
      // 注意：要先执行 next() 不然 this.$route.query 还是之前的
      next()
      this.getPosts()
    },
    mounted() {
      // aixos 请求数据

      this.axios.get('http://127.0.0.1:5000/line').then(res => {
        console.log(res)
        var data = res.data.data
        var city = new Array()
        var money = new Array()
        
        for (var i = 0; i < data.length; i++) {
          city.push(data[i].name)
          money.push(data[i].money)
        }
        console.log(money)
        var Highcharts = require('highcharts');
        // 在 Highcharts 加载之后加载功能模块
        require('highcharts/modules/exporting')(Highcharts);
        Highcharts.chart('container', {
            title: {
              text: '一线城市平均房价'
            },
            yAxis: {
              title: {
                text: '房价'
              }
            },
            xAxis: {
              title: {
                text: '城市'
              },
              categories: city
            },
            series: [{
              name: '平均房价',
              data: money
            }]
          }

        )
      })
    },
  }
</script>

<style scoped>
  .container {
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .el-carousel__item h3 {
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

  .introduce .title {
    text-align: left;
    font-size: 24px;
  }

  .introduce {
    text-align: left;
    height: 290px;
    color: white;
    font-size: 15px;
    margin-left: 50px;
    margin-top: 50px;
  }

  .que {
    text-align: left;
    font-size: 20px;
  }

  .el-collapse-item {
    text-align: left;
    font-size: 18px;

  }

  .item-title {
    font-size: 18px;
  }

  .item-content {
    font-size: 15px;
  }

    /* 卡片 */
  .text {
    font-size: 16px;
    text-align: left;
    margin-left: 80px;

  }

  .text#item-title {
    font-size: 18px;
    text-align: left;
    margin-left: 80px;
  }

  .item {
    margin-bottom: 20px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    margin-left: -20px;
    width: 390px; 
    height: 280px;
    background-color: #eeeeee;

  }

  #container {
    max-width: 800px;
    height: 400px;
    margin: 0 auto;
    border: solid orange 1px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;

  }
</style>