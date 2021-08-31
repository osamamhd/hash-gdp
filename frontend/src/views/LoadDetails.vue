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
            Load Delivery Report
          </h1>
        </div>
        <div class="pt-6">
          <h1 class="text-green-500 font-semibold pb-3">Boat Details</h1>
          <table class="mx-3 text-sm text-gray-700">
            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Name</td>
              <td class="px-4 py-2 w-4/5">{{ load.boat.name }}</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Fish Type</td>
              <td class="px-4 py-2 w-4/5">{{ load.boat.fish_type }}</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Quantity</td>
              <td class="px-4 py-2 w-4/5">{{ load.boat.quantity }}kg</td>
            </tr>
          </table>
        </div>

        <div class="pt-6">
          <h1 class="text-green-500 font-semibold pb-3">Load Description</h1>
          <table class="mx-3 text-sm text-gray-700">
            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Batch No</td>
              <td class="px-4 py-2 w-4/5">{{ load.batch_no }}</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Delivery Date</td>
              <td class="px-4 py-2 w-4/5">{{ load.format_delivery_date }}</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Expiration Date</td>
              <td class="px-4 py-2 w-4/5">{{ load.expiration_date }}</td>
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
  name: "LoadDetails",

  data() {
    return {
      load: {
        boat: [],
      },
    };
  },

  methods: {
    getLoad() {
      const load_id = this.$route.params.load_id;
      axios
        .get(`/loads/${load_id}/`)
        .then((response) => {
          this.load = response.data;
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
        doc.save("Load-Report.pdf");
      });
    },

    currentDate() {
      const current = new Date();
      const date = `${current.getMonth()+1}/${current.getDate()}/${current.getFullYear()}`;
      return date;
    }
  },

  mounted() {
    this.getLoad();
  },
};
</script>

<style>
</style>