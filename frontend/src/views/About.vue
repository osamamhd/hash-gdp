<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2 ">
      <h1 class="text-xl text-green-400 font-semibold">
        Reports
      </h1>
    </div>

    <div class="m-5 w-11/12 mx-auto">
      <div class="flex justify-between">
        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/loads">Load Reports</router-link>
        </div>

        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/pending-orders">Pending Orders Report</router-link>
        </div>

        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/distribution-report">Distribution Reports</router-link>
        </div>

        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/cumulative-load-report">Cumulative Load Report</router-link>
        </div>

        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/summary-report">Summary Report</router-link>
        </div>

        <div class="rounded bg-blue-900 text-white py-2 px-5 mx-2">
          <router-link to="/relation-report">Relation Report</router-link>
        </div>

      </div>
    </div>
    
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>