<template>
  <div>
    <input v-model="nombre"/>
    <br>
    Hola, mi nombre es {{nombre}}
  </div>
</template>

<script>
export default {
  name: 'ExampleComponent',
  data: function () {
    return {
      nombre: 'Juan'
    }
  }
}
</script>
