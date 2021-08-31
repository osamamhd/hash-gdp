<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2">
      <h1 class="text-xl text-green-400 font-semibold">Load Deliveries</h1>
    </div>
    <div>
      <table
        class="
          rounded-t-lg
          m-5
          w-11/12
          mx-auto
          bg-gray-100
          text-sm text-gray-600
        "
      >
        <tr class="text-left border-b-2 border-gray-300">
          <th class="px-4 py-3">ID</th>
          <th class="px-4 py-3">Boat Details</th>
          <th class="px-4 py-3">Delivery Date</th>
          <th class="px-4 py-3">Expiration Date</th>
          <th class="px-4 py-3">Batch No</th>
          <th class="px-4 py-3 text-center">Reports</th>
        </tr>

        <tr
          class="bg-gray-100 border-b border-gray-200"
          v-for="load in Loads"
          :key="load.id"
          :load="load"
        >
          <td class="px-4 py-3">{{ load.id }}</td>
          <td class="px-4 py-3">
            <p>
              Name:
              <span class="font-semibold">
                {{ load.boat.name }}
              </span>
            </p>
            <p>
              Fish Type:
              <span class="font-semibold">
                {{ load.boat.fish_type }}
              </span>
            </p>
            <p>
              Quantity:
              <span class="font-semibold"> {{ load.boat.quantity }} kg </span>
            </p>
          </td>
          <td class="px-4 py-3">{{ load.format_delivery_date }}</td>
          <td class="px-4 py-3">{{ load.expiration_date }}</td>
          <td class="px-4 py-3">{{ load.batch_no }}</td>
          <td class="bg-green-400 text-white text-center">
            <router-link :to="load.get_absolute_url">Check Report</router-link>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",

  data() {
    return {
      Loads: [],
    };
  },

  mounted() {
    this.getLoads();
  },

  methods: {
    getLoads() {
      axios
        .get("/loads/")
        .then((response) => {
          this.Loads = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
