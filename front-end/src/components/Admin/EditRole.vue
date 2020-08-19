<template>
  <div>
    <h1>Edit Role</h1>
    <form @submit.prevent="onSubmit">
      <div class="form-group" v-bind:class="{'u-has-error-v1': roleForm.slugError}">
        <label for="slug">Slug</label>
        <input type="text" v-model="roleForm.slug" class="form-control" id="slug" placeholder="">
        <small class="form-control-feedback" v-show="roleForm.slugError">{{ roleForm.slugError }}</small>
      </div>
      <div class="form-group" v-bind:class="{'u-has-error-v1': roleForm.nameError}">
        <label for="name">Name</label>
        <input type="text" v-model="roleForm.name" class="form-control" id="name" placeholder="">
        <small class="form-control-feedback" v-show="roleForm.nameError">{{ roleForm.nameError }}</small>
      </div>
      <div class="form-group">
        <label for="permissions">Permissions</label>
        <div>
          <!-- Inline Checkboxes -->
          <label v-for="(perm, index) in perms" v-bind:key="index" class="form-check-inline u-check g-pl-25">
            <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" style="margin-top:289px;" type="checkbox" v-bind:id="perm.dec" v-bind:value="perm.dec" v-model="checkPerms">
            <div class="u-check-icon-checkbox-v6 g-absolute-centered--y g-left-0">
              <i class="fa" data-check-icon=""></i>
            </div>
            {{ perm.name }}
          </label>
          <!-- End Inline Checkboxes -->
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import store from '../../store'

export default {
  name: 'AddRole',  //this is the name of the component
  data () {
    return {
      sharedState: store.state,
      roleForm: {
        slug: '',
        name: '',
        permissions: [],
        errors: 0,  // 表单是否在前端验证通过，0 表示没有错误，验证通过
        slugError: null,
        nameError: null
      },
      perms: null,
      checkPerms: []
    }
  },
  methods: {
    getPerms () {
      const path = `/api/roles/perms`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          this.perms = response.data
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },
    getRole (id) {
      const path = `/api/roles/${id}`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          this.roleForm.slug = response.data.slug
          this.roleForm.name = response.data.name
          this.checkPerms = response.data.perms
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },
    onSubmit (e) {
      this.roleForm.errors = 0  // 重置

      if (!this.roleForm.slug) {
        this.roleForm.errors++
        this.roleForm.slugError = 'Slug required.'
      } else {
        this.roleForm.slugError = null
      }

      if (!this.roleForm.name) {
        this.roleForm.errors++
        this.roleForm.nameError = 'Role name required.'
      } else {
        this.roleForm.nameError = null
      }

      if (this.roleForm.errors > 0) {
        // 如果slug或name为空时，不继续往下执行，即不会通过 axios 调用后端API
        return false
      }

      const path = `/api/roles/${this.$route.params.id}`
      const payload = {
        slug: this.roleForm.slug,
        name: this.roleForm.name,
        permissions: this.checkPerms
      }
      this.$axios.put(path, payload)
        .then((response) => {
          // handle success
          this.$toasted.success('Successed modify the role.', { icon: 'fingerprint' })
          this.$router.push({name: 'AdminRoles'})
        })
        .catch((error) => {
          // handle error
          for (var field in error.response.data.message) {
            if (field == 'slug') {
              this.roleForm.slugError = error.response.data.message[field]
            } else if (field == 'name') {
              this.roleForm.nameError = error.response.data.message[field]
            } else {
              this.$toasted.error(error.response.data.message[field], { icon: 'fingerprint' })
            }
          }
        })
    }
  },
  created () {
    this.getPerms()
    const role_id = this.$route.params.id
    this.getRole(role_id)
  },
  // 当路由变化后重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    this.getPerms()
    this.getRole(to.params.id)
  }
}
</script>