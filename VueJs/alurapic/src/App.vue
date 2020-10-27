<template>

  <main>
    <h1 class='title-header'>{{title}}</h1>
    <ul>
      <li v-for="foto of fotos">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{foto.titulo}}</h5>
            <img :src="foto.url" :alt="foto.title" :width="largura" :height="altura">
            <p class="card-text">ID: {{ foto._id }}</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </li>
    </ul>
  </main>
  
</template>

<script>

export default {
  data() {
    return {
      title: 'RepoPic',
      largura: 190,
      largura: 140,
      fotos: [],
    }
  },

  created() {

    let promise = this.$http.get('http://localhost:3000/v1/fotos')
    promise
    .then(res => res.json())
    .then(fotos => this.fotos = fotos)
    .then(t => console.log(this.fotos))

  }
}

</script>

<style>

  .title-header {
    text-align: center;
  }

  .card {
    width: 18rem;
  }

  li {
    list-style-type: none;
  }

</style>
