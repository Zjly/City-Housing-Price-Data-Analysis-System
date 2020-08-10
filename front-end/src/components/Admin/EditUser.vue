<template>
  <div>
    <h1>Edit User</h1>
    <hr class="g-brd-gray-light-v4 g-mx-minus-30">

    <form @submit.prevent="onSubmit">
      <div v-if="user" class="form-group">
        <h4 class="h6 g-font-weight-700 g-mb-20">Username</h4>
        <input id="username" v-bind:value="user.username" class="form-control form-control-md rounded-0" type="text" disabled="">
      </div>

      <hr class="g-brd-gray-light-v4 g-mx-minus-30">
      <div class="form-group">
        <h4 class="h6 g-font-weight-700 g-mb-20">Confirm</h4>
        <!-- Toggles Views -->
        <div class="d-block my-3">
        <div class="custom-control custom-radio">
            <input id="confirmed" name="confirmed" type="checkbox" class="custom-control-input" v-model="checked">
            <label class="custom-control-label" for="confirmed">邮箱认证</label>
        </div>
        </div>

        <!-- End Toggles Views -->
      </div>

      <hr class="g-brd-gray-light-v4 g-mx-minus-30">
      <div class="form-group">
        <h4 class="h6 g-font-weight-700 g-mb-20">Role</h4>
        <div>
          <!-- Inline Radios -->
          <label v-for="(role, index) in roles.items" v-bind:key="index" class="form-check-inline u-check g-pl-25 ml-0 g-mr-25">
            <input style="margin-top:365px;" class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="role_id" type="radio" v-bind:id="role.id" v-bind:value="role.id" v-model="picked">
            <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
              <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
            </div>
            {{ role.name }}
          </label>
          <!-- End Inline Radios -->
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>


export default {
  name: 'EditUser',  //this is the name of the component
  data () {
    return {
      user: null,
      roles: '',
      checked: false,
      picked: null
    }
  },
  methods: {
    getUser (id) {
      const path = `/api/users/${id}`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          this.user = response.data
          this.checked = this.user.confirmed
          this.picked = this.user.role_id
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },
    getRoles () {
      let page = 1
      let per_page = 5
      if (typeof this.$route.query.page != 'undefined') {
        page = this.$route.query.page
      }

      if (typeof this.$route.query.per_page != 'undefined') {
        per_page = this.$route.query.per_page
      }

      const path = `/api/roles/?page=${page}&per_page=${per_page}`
      this.$axios.get(path)
        .then((response) => {
          // handle success
          this.roles = response.data
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
    },
    onSubmit (e) {
      const path = `/api/users/${this.$route.params.id}`
      const payload = {
        confirmed: this.checked,
        role_id: this.picked
      }

      this.$axios.put(path, payload)
        .then((response) => {
          // handle success
          this.$toasted.success('Successed modify the user.', { icon: 'fingerprint' })
          this.$router.push({name: 'AdminUsers'})
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
    const user_id = this.$route.params.id
    this.getUser(user_id)
    this.getRoles()
  },
}
</script>