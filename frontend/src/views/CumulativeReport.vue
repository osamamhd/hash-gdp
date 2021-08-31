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
            Cumulative Load Report
          </h1>
        </div>
        <div class="pt-6 w-2/3">
          <div class="flex text-xl font-semibold pb-3">
            <p class="text-blue-900">Boat Owner:</p>
            <p class="text-green-400">{{ boatowner.name }}</p>
          </div>
          <table class="mx-3 text-sm text-gray-700">
            <tr class="bg-gray-100 border-2 border-gray-200 font-semibold">
              <td class="px-4 py-2 border-r-2 border-gray-200">Fish Type</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">Cumulative Quantity</td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Tilapia</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="boatowner.tilapia_sum">
                  {{ boatowner.tilapia_sum }}kg
                </p>
                <p v-else>0kg</p>
              </td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Mackerel</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="boatowner.mackerel_sum">
                  {{ boatowner.mackerel_sum }}kg
                </p>
                <p v-else>0kg</p>
              </td>
            </tr>

            <tr class="bg-gray-100 border-2 border-gray-200">
              <td class="px-4 py-2 border-r-2 border-gray-200">Grouper</td>
              <td class="px-4 py-2 border-r-2 border-gray-200">
                <p v-if="boatowner.grouper_sum">
                  {{ boatowner.grouper_sum }}kg
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
import axios from 'axios';
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
export default {
  name: 'CumulativeReport',

  data() {
    return { 
      boatowner: {
        boats: []
      }
    }
  }, 

  mounted() {
    this.getBoatOwner()
  },

  methods: {
    getBoatOwner() {
      const boat_owner_id = this.$route.params.boat_owner_id
      const boat_owner_slug = this.$route.params.boat_owner_slug;
      axios
        .get(`/boats_owner/${boat_owner_id}/${boat_owner_slug}/`)
        .then((response) => {
          this.boatowner = response.data;
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
        doc.save("Cumulative-Report.pdf");
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

<style>

</style>