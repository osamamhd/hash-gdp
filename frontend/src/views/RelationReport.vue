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
        Relation Report
      </h1>
    </div>
    <div>
      <table
        class="
          rounded-t-lg
          m-5
          w-1/2
          bg-gray-100
          text-sm text-gray-600
        "
      >
        <tr class="text-left border-b-2 border-gray-300">
          <th class="px-4 py-3">Delivery Date</th>
          <th class="px-4 py-3">Fish Type</th>
          <th class="px-4 py-3">Quantity</th>
        </tr>

        <tr
          class="bg-gray-100 border-b border-gray-200"
          v-for="load in Loads"
          :key="load.id"
          :load="load"
        >
          
          <td class="px-4 py-3">{{ load.format_delivery_date }}</td>
          <td class="px-4 py-3">{{ load.boat.fish_type }}</td>
          <td class="px-4 py-3">{{ load.boat.quantity }}</td>
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
import axios from 'axios';
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
export default {
  name: 'CumulativeReport',

  data() {
    return { 
      Loads:[]
    }
  }, 

  mounted() {
    this.getLoads()
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

    downloadPDF() {
      html2canvas(document.querySelector("#capture")).then((canvas) => {
        var img = canvas.toDataURL("image/png");
        var doc = new jsPDF();
        doc.addImage(img, "JPEG", 0, 0, 0, 0);
        doc.save("Relation-Report.pdf");
      });
    },

    currentDate() {
      const current = new Date();
      const date = `${current.getMonth()+1}/${current.getDate()}/${current.getFullYear()}`;
      return date;
    }
  }

}
</script>
