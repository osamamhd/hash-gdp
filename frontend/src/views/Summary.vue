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
            Summary Report
          </h1>
        </div>
        <div class="pt-6 w-1/2">
          <table class="mx-3 text-sm text-gray-700">
            <tr class="bg-gray-100 border-2 border-gray-200 font-semibold">
              <td class="px-4 py-2 border-r-2 border-gray-200">Fish Type</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">Requested Quantity</td>
              <td class="px-4 py-2 ">Delivered Quantity</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Tilapia</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="tilapia_requested">
                  {{ tilapia_requested }}kg
                </p>
                <p v-else>0kg</p>
              </td>
              <td class="px-4 py-2 ">
                <p v-if="tilapia_delivered">
                  {{ tilapia_delivered }}kg
                </p>
                <p v-else>0kg</p>
              </td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Mackerel</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="mackerel_requested">
                  {{ mackerel_requested }}kg
                </p>
                <p v-else>0kg</p>
              </td>
              <td class="px-4 py-2 ">
                <p v-if="mackerel_delivered">
                  {{ mackerel_delivered }}kg
                </p>
                <p v-else>0kg</p>
              </td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Grouper</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="grouper_requested">
                  {{ grouper_requested }}kg
                </p>
                <p v-else>0kg</p>
              </td>
              <td class="px-4 py-2 ">
                <p v-if="grouper_delivered">
                  {{ grouper_delivered }}kg
                </p>
                <p v-else>0kg</p>
              </td>
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
import axios from 'axios'
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
export default {
  name: 'Summary', 

  data() {
    return {
      tilapia_requested: '',
      mackerel_requested: '',
      grouper_requested: '',
      
      tilapia_delivered: '',
      mackerel_delivered: '',
      grouper_delivered: '',
    }
  }, 

  methods: {
    til_req() {
      axios
        .get('/tilapia_requested/')
        .then(response => {
          this.tilapia_requested = response.data
        })
    },

    mac_req() {
      axios
        .get('/mackerel_requested/')
        .then(response => {
          this.mackerel_requested = response.data
        })
    },

    gro_req() {
      axios
        .get('/grouper_requested/')
        .then(response => {
          this.grouper_requested = response.data
        })
    },

    til_del() {
      axios
        .get('/tilapia_delivered/')
        .then(response => {
          this.tilapia_delivered = response.data
        })
    },

    mac_del() {
      axios
        .get('/mackerel_delivered/')
        .then(response => {
          this.mackerel_delivered = response.data
        })
    },

    gro_del() {
      axios
        .get('/grouper_delivered/')
        .then(response => {
          this.grouper_delivered = response.data
        })
    },

    downloadPDF() {
      html2canvas(document.querySelector("#capture")).then((canvas) => {
        var img = canvas.toDataURL("image/png");
        var doc = new jsPDF();
        doc.addImage(img, "JPEG", 0, 0, 0, 0);
        doc.save("Summay-Report.pdf");
      });
    },

    currentDate() {
      const current = new Date();
      const date = `${current.getMonth()+1}/${current.getDate()}/${current.getFullYear()}`;
      return date;
    }
  },

  mounted() {
    this.til_req()
    this.mac_req()
    this.gro_req()

    this.til_del()
    this.mac_del()
    this.gro_del()
  }
}
</script>

<style>

</style>