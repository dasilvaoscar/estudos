const app3 = new Vue({
  el: '#app-3',
  data: {
    seen: false
  },
})

const see_or_not = () => {
  if(app3.seen == true){
    app3.seen = false
  } 
  else{
    app3.seen = true
  }
}