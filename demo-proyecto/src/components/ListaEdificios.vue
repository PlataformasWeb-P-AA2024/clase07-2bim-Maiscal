<template>
  <div>
    <h1>Lista de Edificio</h1>
    <center>
    <table class="mi-tabla">
      <tr>
        <th>Nombre</th>
        <th>Direccion</th>
        <th>ciudad</th>
        <th>Tipo</th>
      </tr>
      <tr v-for="t in edificio" :key="t.id">
        <td>{{ t.nombre }}</td>
        <td>{{ t.direccion }}</td>
        <td>{{ t.ciudad }}</td>
        <td>{{ t.tipo }}</td>
      </tr>
    </table>
    </center>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      edificio: []
    };
  },
  created() {
    this.fetchEdificio();
  },
  methods: {
    async fetchEdificio() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/edificio/');
        this.edificio = response.data;
      } catch (error) {
        console.error('Error obteniendo edificio:', error);
      }
    }
  }
};
</script>

<style scoped>
/* agregar ---- */
</style>
