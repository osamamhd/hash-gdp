import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Loads from '../views/Loads.vue'
import Agents from '../views/Agents.vue'
import Orders from '../views/Orders.vue'
import LoadDetails from '../views/LoadDetails.vue'
import PendingOrders from '../views/PendingOrders.vue'
import DistributionReport from '../views/DistributionReport.vue'
import Summary from '../views/Summary.vue'
import CumulativeLoad from '../views/CumulativeLoad.vue'
import CumulativeReport from '../views/CumulativeReport.vue'
import RelationReport from '../views/RelationReport.vue'
const routes = [
  
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  
  
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/agents',
    name: 'Agents',
    component: Agents
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },

  {
    path: '/summary-report',
    name: 'Summary',
    component: Summary
  },

  {
    path: '/cumulative-load-report',
    name: 'CumulativeLoad',
    component: CumulativeLoad
  },

  {
    path: '/pending-orders',
    name: 'PendingOrders',
    component: PendingOrders
  },

  {
    path: '/distribution-report',
    name: 'DistributionReport',
    component: DistributionReport
  },
  {
    path: '/boat_owner_id/:boat_owner_slug/',
    name: 'CumulativeReport',
    component: CumulativeReport
  },
  {
    path: '/:load_id',
    name: 'LoadDetials',
    component: LoadDetails
  },
  {
    path: '/:boat_owner_id/:boat_owner_slug/',
    name: 'CumulativeReport',
    component: CumulativeReport
  },

  {
    path: '/loads',
    name: 'Loads',
    component: Loads
  },

  {
    path: '/relation-report',
    name: 'RelationReport',
    component: RelationReport
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
