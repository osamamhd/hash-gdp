<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2 border-gray-300">
      <h1 class="text-xl text-green-400 font-semibold">Orders</h1>
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
        <tr class="text-left borderload-b-2 borderload-gray-300">
          <th class="px-4 py-3">Agent Detial</th>
          <th class="px-4 py-3">Quantity</th>
          <th class="px-4 py-3">Fish Type</th>
          <th class="px-4 py-3">Order Date</th>
          <th class="px-4 py-3">Order ID</th>
          <th class="px-4 py-3 text-center">Status</th>
        </tr>

        <tr
          class="bg-gray-100 borderload-b borderload-gray-200"
          v-for="orderload in orderloads"
          :key="orderload.id"
          :orderload="orderload"
        >
          <td class="px-4 py-3">
            <p>
              <span class="font-semibold">Name:</span>
              {{ orderload.order.agent.name }}
            </p>
            <p>
              <span class="font-semibold">ID:</span>
              {{ orderload.order.agent.agent_id }}
            </p>
          </td>
          <td class="px-4 py-3">{{ orderload.quantity }}</td>
          <td class="px-4 py-3">{{ orderload.fish_type }}</td>
          <td class="px-4 py-3">{{ orderload.order.ordered_at }}</td>
          <td class="px-4 py-3">{{ orderload.order.order_id }}</td>
          <td class="px-4 py-3 text-center" >
            <p v-if="orderload.pending" :id="orderload.pending">Pending</p>
            <p v-else :id="orderload.pending">Done</p>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "orderloads",

  data() {
    return {
      orderloads: [],
    };
  },

  methods: {
    getorderloads() {
      axios
        .get("/orderloads/")
        .then((response) => {
          this.orderloads = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getorderloads();
  },
};
</script>

<style>
#true {
  background-color: rgb(216, 85, 111);
  color: aliceblue;

}

#false {
  background-color: rgb(70, 243, 186);
}
</style>