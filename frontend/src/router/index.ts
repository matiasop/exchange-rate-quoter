import { createRouter, createWebHistory } from "vue-router";
import QuoterView from "@/views/QuoterView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "quoter",
      component: QuoterView,
    },
  ],
});

export default router;
