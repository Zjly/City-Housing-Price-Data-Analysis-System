<template>

  <div>

    <!-- Panel Header -->
    <div class="card-block g-pa-0">
      <form class="form-inline" @submit.prevent="onSubmit">
        <div class="form-group">

          <label for="exampleInputName2">省份：</label>
          <div class="col-sm-2">
            <select id="citySel" v-model="proval" @change="pr_onchange($this.options[this.options.selectedIndex].text)"
              placeholder="请选择省份" class='form-control' style="width:200px;" data-live-search="true" name='province'>
              <option value="">请选择省份</option>
              <option v-for="(item, index) in newhousedata" v-bind:key="index">{{item.province}}</option>
            </select>
          </div>
        </div>
        <div class="form-group" style="margin-left:10px">
          <label for="exampleInputEmail2">城市：</label>
          <div class="col-sm-2">
            <select class='form-control' v-model="city" style="width:200px;" size="1" data-live-search="true" id='city' name='city'>
              <option v-for="(item, index) in choosecity" v-bind:key="index">{{item}}</option>
            </select>
          </div>
        </div>
        <div>
          <button type="submit" style="margin-left:20px" class="btn btn-primary">Submit</button>
        </div>
      </form>
      <hr class="g-brd-gray-light-v4 g-my-30">
    </div>
    <div class="card-header d-flex align-items-center justify-content-between g-bg-gray-light-v5 border-0 g-mb-15">
      <div>
      </div>
      <h3 class="h6 mb-0">
        <i class="icon-media-043  g-pos-rel g-top-2 g-mr-5"></i> 新房查询结果 <small v-if="newhouse">(共
          {{ newhouse._meta.total_items }} 个, {{ newhouse._meta.total_pages }} 页)</small>
      </h3>
      <div class="dropdown g-mb-10 g-mb-0--md">
        <span class="d-block g-color-primary--hover g-cursor-pointer g-mr-minus-5 g-pa-5" data-toggle="dropdown"
          aria-haspopup="true" aria-expanded="false">
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
    <div class="card g-brd-teal rounded-0 g-mb-30">


      <div class="table-responsive">
        <table class="table table-striped u-table--v1 mb-0">
          <thead>
            <tr>
              <th>#</th>
              <th>地区</th>
              <th>楼盘名</th>
              <th>面积</th>
              <th>单价(元/㎡)	</th>
            </tr>
          </thead>

          <tbody>

            <tr v-for="(item, index) in newhousedatas" v-bind:key="index">
              <th scope="row">{{ index+1 }}</th>
              <td>{{ item[1] }}</td>
              <td>{{ item[2] }}</td>
              <td>{{ item[3] }}</td>
              <td>{{ item[4] }}</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
    <!-- End Striped Rows -->

    <!-- Pagination #04 -->
    <div v-if="newhouse">
      <pagination v-bind:cur-page="newhouse._meta.page" v-bind:per-page="newhouse._meta.per_page"
        v-bind:total-pages="newhouse._meta.total_pages">
      </pagination>
    </div>
    <!-- End Pagination #04 -->
  </div>
</template>


<script>
  import Pagination from '../Base/Pagination';

  export default {
    name: 'NewHouse',
    components: {

    },
    data() {
      return {
        proval: '',
        data: '',
        chooseprovince: '',
        newhousedata: [],
        provincedata: [],
        choosecity: [],
        housedata: [],
        province:'',
        city:'',
        newhousedatas:'',

      }
    },
    methods: {

      getMessage() {
        const path = '/api/houseaddress'
        this.$axios.get(path)
          .then((res) => {
            var data = res.data.data
            this.data = data
            var metadata = {
              province: '',
              city: []
            }
            var housedata = []
            var city = new Array()
            var province = new Array()
            var province2 = new Array()
            for (var i = 0; i < data.length; i++) {
              if (i > 0) {
                if (data[i].province != data[i - 1].province) {
                  metadata.province = data[i - 1].province
                  metadata.city = city
                  console.log(metadata.province)
                  console.log(metadata.city)
                  housedata.push({
                    province: metadata.province,
                    city: metadata.city
                  })
                  city = []
                  metadata.province = ''
                  metadata.city = []
                }
              }
              city.push(data[i].city)
              province.push(data[i].province)
              province2.push(data[i].province)
              if (i == data.length - 1) {
                metadata.province = data[i].province
                metadata.city = city
                housedata.push({
                  province: metadata.province,
                  city: metadata.city
                })
                city = []
                metadata.province = ''
                metadata.city = []
              }
            }
            console.log(housedata)
            // 合并同类项
            var tprovince = [];
            var narr = [];
            for (var i = 0; i < data.length; i++) {
              var n = tprovince.indexOf(data[i].province);
              if (n == -1) {
                tprovince.push(data[i].province);
                narr.push({
                  city: [data[i].city],
                  province: data[i].province
                });
              } else {
                narr[n].city.push(data[i].city);
              }
            }
            console.log(narr)
            this.housedata = housedata
            var newhousedata = narr
            this.newhousedata = newhousedata

            // 取省份定城市
            for (var i in newhousedata) {
              if (newhousedata[i].province == this.chooseprovince) {
                var choosecity = newhousedata[i].city
                this.choosecity = choosecity
                console.log(choosecity)
              }
            }

            function newData(data) {
              var nData = new Array();
              for (var i = 0; i < data.length; i++) {
                if (nData.indexOf(data[i]) == -1) {
                  nData.push(data[i]);
                }
              }
              return nData;
            }
            var provincedata = newData(province2)
            this.provincedata = provincedata
            this.$toasted.info('Success connect to Flask API', {
              icon: 'fingerprint'
            })
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
          })

      },
      onSubmit(e) {
        const path = `/api/newhouses/${this.proval}/${this.city}`
        const payload = {
          province: this.proval,
          city: this.city,
        }

        this.$axios.post(path, payload)
          .then((response) => {
          // handle success
          this.newhousedatas = response.data
        })
        .catch((error) => {
          // handle error
          console.error(error)
        })
       }

    },
    watch: {
      proval(val, oldval) {
        console.log(val, oldval)
        this.chooseprovince = val
        var newhousedata = this.newhousedata
        for (var i in newhousedata) {
          if (newhousedata[i].province == this.chooseprovince) {
            var choosecity = newhousedata[i].city
            this.choosecity = choosecity
            console.log(choosecity)
          }
        }
      }
    },
    created() {
      this.getMessage()
    },

  }
</script>
<style scoped>
  .bootstrap-select {
    width: 100% !important;
  }
</style>
