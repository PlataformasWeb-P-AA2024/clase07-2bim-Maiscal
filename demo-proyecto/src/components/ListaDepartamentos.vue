<template>
  <div>
    <h1>Lista de Departamento</h1>
    <center>
    <table class="mi-tabla">
      <tr>
        <th>Nombre</th>
        <th>Costo</th>
        <th>nCuartos</th>
      </tr>
      <tr v-for="d in departamento" :key="d.id">
        <td>{{ d.nombre }}</td>
        <td>{{ d.costo }}</td>
        <td>{{ d.nCuartos }}</td>
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
      departamento: []
    };
  },
  created() {
    this.fetchDepartamento();
  },
  methods: {
    async fetchDepartamento() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/departamento/');
        this.departamento = response.data;
      } catch (error) {
        console.error('Error obteniendo departamento:', error);
        console.log()
      }
    }
  }
};
</script>

<style scoped>
/* agregar ---- */
</style>
