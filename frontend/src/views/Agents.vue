<template>
  <div class="w-11/12 lg:w-3/4 mx-auto pt-6">
    <div class="border-b-2 ">
      <h1 class="text-xl text-green-400 font-semibold">
        Agents
      </h1>
    </div>
    <div>
      <table class="rounded-t-lg m-5 w-11/12 mx-auto bg-gray-100 text-sm text-gray-600">
        <tr class="text-left border-b-2 border-gray-300">
          <th class="px-4 py-3">ID</th>
          <th class="px-4 py-3">Agent Name</th>
          <th class="px-4 py-3">Joining date</th>
          <th class="px-4 py-3">Agent ID</th>
        </tr>
        
        <tr class="bg-gray-100 border-b border-gray-200"
          v-for="agent in agents" 
          :key="agent.id" 
          :agent="agent">
          <td class="px-4 py-3">{{ agent.id }}</td>
          <td class="px-4 py-3">{{ agent.name }}</td>
          <td class="px-4 py-3">{{ agent.join_date }}</td>
          <td class="px-4 py-3">{{ agent.agent_id }}</td>
        </tr> 
     
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Agents',

  data() {
    return {
      agents: []
    }
  }, 

  methods: {
    getAgents() {
      axios
        .get('/agents/')
        .then(response => {
          this.agents = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

  mounted() {
    this.getAgents()
  }

}
</script>

<style>

</style>