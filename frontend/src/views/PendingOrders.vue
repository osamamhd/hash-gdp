<template>
  <button @click="downloadPDF" class="bg-blue-900 text-white p-1">Download PDF</button>
  <div class="border-2 w-11/12 lg:w-3/4 mx-auto">
    <div ref="content" id="capture">
      <div class="w-11/12 mx-auto pt-6">
        <div>
          <h1 class="text-2xl text-green-400 font-semibold">
            Central Fishing Agency
          </h1>
          <h1 class="text-xl text-blue-900 font-semibold">
            Pending Orders Report
          </h1>
        </div>
        <div>
          <table
            class="
              m-5
              w-3/5
              
              text-sm text-gray-700
            "
          >
            <tr class="text-left border-2">
              <th class="px-4 py-3 border-r-2">Agent Detial</th>
              <th class="px-4 py-3 border-r-2">Quantity</th>
              <th class="px-4 py-3 border-r-2">Fish Type</th>
              <th class="px-4 py-3 border-r-2">Order Date</th>
              <th class="px-4 py-3 border-r-2">Order ID</th>
            </tr>

            <tr
              v-for="orderload in orderloads"
              :key="orderload.id"
              :orderload="orderload"
              class="border-2"
            >
              <td class="px-4 py-3 border-r-2">
                <p>
                  <span class="font-semibold">Name:</span>
                  {{ orderload.order.agent.name }}
                </p>
                <p>
                  <span class="font-semibold">ID:</span>
                  {{ orderload.order.agent.agent_id }}
                </p>
              </td>
              <td class="px-4 py-3 border-r-2">{{ orderload.quantity }}</td>
              <td class="px-4 py-3 border-r-2">{{ orderload.fish_type }}</td>
              <td class="px-4 py-3 border-r-2">{{ orderload.order.ordered_at }}</td>
              <td class="px-4 py-3 border-r-2">{{ orderload.order.order_id }}</td>
              
            </tr>
          </table>
        </div>

        <div class="pt-20 pb-10 text-blue-900 font-semibold flex justify-between w-1/2">
          <h1 class="pb-3">Date: {{currentDate()}}</h1>
          <h1 class="pb-3">Reported By/Sign:</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
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
        .get("/orderloads/pending/")
        .then((response) => {
          this.orderloads = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    downloadPDF() {
      html2canvas(document.querySelector("#capture")).then((canvas) => {
        var img = canvas.toDataURL("image/png");
        var doc = new jsPDF();
        doc.addImage(img, "JPEG", 0, 0, 0, 0);
        doc.save("Pending-Orders-Report.pdf");
      });
    },

    currentDate() {
      const current = new Date();
      const date = `${current.getMonth()+1}/${current.getDate()}/${current.getFullYear()}`;
      return date;
    }
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