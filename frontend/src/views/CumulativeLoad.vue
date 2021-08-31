<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2">
      <h1 class="text-xl text-green-400 font-semibold">Load Deliveries</h1>
    </div>
    <div>
      <table
        class="
          rounded-t-lg
          m-5 text-cent
          w-11/12
          mx-auto
          bg-gray-100
          text-sm text-gray-600
        "
      >
        <tr class="text-left border-b-2 border-gray-300">
          <th class="px-4 py-3">Boat Owner</th>
          <th class="px-4 py-3">Tilapia</th>
          <th class="px-4 py-3">Mackerel</th>
          <th class="px-4 py-3">Grouper</th>
          <th class="px-4 py-3 text-center">Reports</th>
        </tr>

        <tr
          class="bg-gray-100 border-b border-gray-200"
          v-for="boatowner in boatOwners"
          :key="boatowner.id"
          :boatowner="boatowner"
        >
          <td class="px-4 py-3">{{ boatowner.name }}</td>
          <td class="px-4 py-3">
            <p v-if="boatowner.tilapia_sum">
              {{ boatowner.tilapia_sum }}kg
            </p>
            <p v-else>
              0kg
            </p>
          </td>
          <td class="px-4 py-3">
            <p v-if="boatowner.mackerel_sum">
              {{ boatowner.mackerel_sum }}kg
            </p>
            <p v-else>
              0kg
            </p>
          </td>
          <td class="px-4 py-3">
            <p v-if="boatowner.grouper_sum">
              {{ boatowner.grouper_sum }}kg
            </p>
            <p v-else>
              0kg
            </p>
          </td>
          <td class="bg-green-400 text-white text-center">
            <router-link :to="boatowner.get_absolute_url">Check Report</router-link>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CumulativeLoad',

  data() {
    return {
      boatOwners: []
    }
  },

  mounted() {
    this.getcumulativeLoad()
  },

  methods: {
    getcumulativeLoad() {
      axios
        .get('/boats_owner/')
        .then(response => {
          this.boatOwners = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },


}
</script>

<style>

</style>