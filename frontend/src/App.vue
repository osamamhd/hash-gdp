<template>
<div>
  <div id="nav" class="bg-gray-100 shadow">
    <div class="w-11/12 lg:3/4 mx-auto pt-1 flex justify-between">

      <div>
        <h1 class="text-3xl text-blue-900 font-black">
          C.F.A
        </h1>
      </div>

      <div class="py-2">
        <router-link to="/">Boats</router-link> |
        <router-link to="/loads">Loads</router-link> |
        <router-link to="/agents">Agents</router-link> |
        <router-link to="/orders">Orders</router-link> |
        <router-link to="/about">Reports</router-link>
      </div>
    </div>

    
    
  </div>

  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2 ">
      <h1 class="text-xl text-green-400 font-semibold">
        Inventories
      </h1>
    </div>
    <div class="rounded-lg m-5 w-11/12 mx-auto bg-gray-100 text-gray-600">
      <div class="py-2 px-4 flex justify-between">
        <p>
          <span class="text-green-500 font-semibold">Tilapia:</span>
          {{tilapia}}kg
        </p>
        <p>
          <span class="text-green-500 font-semibold">Mackerel:</span>
          {{mackerel}}kg
        </p>
        <p>
          <span class="text-green-500 font-semibold">Grouper:</span>
          {{grouper}}kg
        </p>
      </div>
      
    </div>
  </div>
</div>
  <router-view/>
</template>

<script>
import axios from 'axios'
export default {

  data() {
    return {
      tilapia: Number,
      mackerel: Number,
      grouper: Number,
    }
  },

  methods: {
    tilapiaQuantity() {
      axios
        .get('/tilapia_quantity/')
        .then(res => {
          this.tilapia = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    mackerelQuantity() {
      axios
        .get('/mackerel_quantity/')
        .then(res => {
          this.mackerel = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    grouperQuantity() {
      axios
        .get('/grouper_quantity/')
        .then(res => {
          this.grouper = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },

  mounted() {
    this.tilapiaQuantity()
    this.mackerelQuantity()
    this.grouperQuantity()
  }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav a {
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
