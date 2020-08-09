<template>
  <div>
    <!-- Panel Header -->
    <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
      <h3 class="h6 mb-0">
        <i class="icon-people g-pos-rel g-top-1 g-mr-5"></i> 博客列表 <small v-if="posts">(共 {{ posts._meta.total_items }} 个, {{ posts._meta.total_pages }} 页)</small>
      </h3>
      <div class="dropdown g-mb-10 g-mb-0--md">
        <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-options-vertical g-pos-rel g-top-1"></i>
        </span>
        <div class="dropdown-menu dropdown-menu-right rounded-0 g-mt-10">
          <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 1 }}" class="dropdown-item g-px-10">
            <i class="icon-plus g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 1 个
          </router-link>
          <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 5 }}" class="dropdown-item g-px-10">
            <i class="icon-layers g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 5 个
          </router-link>
          <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 10 }}" class="dropdown-item g-px-10">
            <i class="icon-wallet g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 10 个
          </router-link>
          
          <div class="dropdown-divider"></div>

          <router-link v-bind:to="{ path: $route.path, query: { page: 1, per_page: 20 }}" class="dropdown-item g-px-10">
            <i class="icon-fire g-font-size-12 g-color-gray-dark-v5 g-mr-5"></i> 每页 20 个
          </router-link>
          
        </div>
      </div>
    </div>
    <!-- End Panel Header -->

    <!-- Striped Rows -->
    <div v-if="posts" class="card g-brd-teal rounded-0 g-mb-30">
      
      <div class="table-responsive">
        <table class="table table-striped u-table--v1 mb-0">
          <thead>
            <tr>
              <th>#</th>
              <th>Title</th>
              <th class="hidden-sm">Time</th>
              <th>Author</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>

            <tr v-for="(post, index) in posts.items" v-bind:key="index">
              <th scope="row">{{ index+1 }}</th>
              <td>
                <router-link v-bind:to="{ name: 'PostDetail', params: { id: post.id } }" class="g-text-underline--none--hover">{{ post.title }}</router-link>
              </td>
              <td class="hidden-sm">
                <span class="g-color-gray-dark-v4 g-font-size-12">{{ $moment(post.timestamp).format('YYYY年MM月DD日 HH:mm:ss') }}</span>
              </td>
              <td>
                <router-link v-bind:to="{ path: `/user/${post.author.id}` }" class="g-text-underline--none--hover">{{ post.author.name || post.author.username }}</router-link>
              </td>
              <td>
                <button v-on:click="onDeletePost(post)" class="btn btn-xs u-btn-outline-red">删除</button>
              </td>
            </tr>
          
          </tbody>
        </table>
      </div>
    </div>
    <!-- End Striped Rows -->

    <!-- Pagination #04 -->
    <div v-if="posts">
      <pagination
        v-bind:cur-page="posts._meta.page"
        v-bind:per-page="posts._meta.per_page"
        v-bind:total-pages="posts._meta.total_pages">
      </pagination>
    </div>
    <!-- End Pagination #04 -->
  </div>
</template>

<script>
import Pagination from '../Base/Pagination'

export default {
  name: 'Posts',  //this is the name of the component
  components: {
    Pagination
  },
  data () {
    return {
      posts: ''
    }
  },
  methods: {
    getPosts () {
      let page = 1
      let per_page = 10
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
          console.error(error)
        })
    },
    onDeletePost (post) {
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
        if(result.value) {
          const path = `/api/posts/${post.id}`
          this.$axios.delete(path)
            .then((response) => {
              // handle success
              this.$swal('Deleted', 'You successfully deleted this post', 'success')
              this.getPosts()
            })
            .catch((error) => {
              // handle error
              console.log(error.response.data)
              this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
            })
        } else {
          this.$swal('Cancelled', 'The post is safe :)', 'error')
        }
      })
    }
  },
  created () {
    this.getPosts()
  },
  // 当路由变化后(比如变更查询参数 page 和 per_page)重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    this.getPosts()
  }
}
</script>