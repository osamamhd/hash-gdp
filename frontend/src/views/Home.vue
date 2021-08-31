<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2">
      <h1 class="text-xl text-green-400 font-semibold">Fishing Boats</h1>
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
          <th class="px-4 py-3">Boat Name</th>
          <th class="px-4 py-3">Fish Type</th>
          <th class="px-4 py-3">Quantity</th>
        </tr>

        <tr
          class="bg-gray-100 border-b border-gray-200"
          v-for="boat in Boats"
          :key="boat.id"
          :boat="boat"
        >
          <td class="px-4 py-3">{{ boat.id }}</td>
          <td class="px-4 py-3">{{ boat.name }}</td>
          <td class="px-4 py-3">{{ boat.fish_type }}</td>
          <td class="px-4 py-3">{{ boat.quantity }} kg</td>
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
      Boats: [],
    };
  },

  mounted() {
    this.getBoats();
  },

  methods: {
    getBoats() {
      axios
        .get("/boats/")
        .then((response) => {
          this.Boats = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
