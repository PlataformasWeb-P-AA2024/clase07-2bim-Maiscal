<template>

<div id="app1">
  <nav>

      [<span><router-link to="/edificio">Edificio</router-link></span>]
      [<span><router-link to="/departamento">Departamento</router-link></span>]

  </nav>
  <router-view></router-view>
</div>

</template>

<script>


export default {
  name: 'App'

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
