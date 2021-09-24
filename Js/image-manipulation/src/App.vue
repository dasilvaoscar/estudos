<template>
  <div id="app" style="display: flex; flex-direction: column">
    <div>
      <h1>Old image</h1>
      <img :src="image">
    </div>
    <div>
      <h1>New image</h1>
      <img id="image" :src="newImage">
    </div>
    <input @change="processFile($event)" type="file">
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      image: null,
      newImage: null
    }
  },
  methods: {
    processFile(event) {
      
      // Get image and crop it
      const image = event.target.files[0]
      const reader = new FileReader()
      reader.onload = (e) => {
        const img = new Image()
        img.src = e.target.result
        img.onload = () => {
          const canvas = document.createElement('canvas')
          const ctx = canvas.getContext('2d')
          canvas.width = img.width
          canvas.height = img.height
          ctx.drawImage(img, 0, 0)
          const data = ctx.getImageData(0, 0, img.width, img.height)
          const newImage = this.crop(data)
          this.newImage = newImage
        }
      }
      reader.readAsDataURL(image)
    },
      
    crop(data) {
      const canvas = document.createElement('canvas')
      const ctx = canvas.getContext('2d')
      canvas.width = 300
      canvas.height = 300
      ctx.putImageData(data, 0, 0)
      return canvas.toDataURL()
    }  

    

  }
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
