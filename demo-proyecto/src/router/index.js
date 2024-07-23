import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../components/HelloWorld.vue';
import ListaDepartamento from '../components/ListaDepartamentos.vue';
import ListaEdificio from '../components/ListaEdificios.vue';

const routes = [
  { path: '/edificio',
  name: 'ListaEdificios',
  component: ListaEdificio },

  { path: '/departamento',
  name: 'ListaDepartamentos',
  component: ListaDepartamento },


];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
