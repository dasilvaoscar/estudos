const app = new Vue({
    el: '#app',
    template:
    `<div class="container">
        <h1>Comentários</h1>
        <hr/>

        <div class='form-todo form group'>
          <p>
            <input type='text' placeholder='Nome' name='author' class='form-control'
             v-model='name'/>
          </p>
          <p>
            <textarea name="message" placeholder="Comentário" class="form-control"
            v-model='message' cols="30" rows="10"></textarea>
          </p>
          <a v-on:click='addComment' name="" id="" class="btn btn-primary" href="#" role="button">Enviar</a>
        </div>  

        <div class="list-group" style="margin-top: 2rem; margin-bottom: 2rem">
          <div class="list-group-item" v-for="comment in comments">
            <span class="comment__author">Autor: <strong>{{comment.name}}</strong></span>
                <p>{{comment.message}}</p><hr/>
                <div>
                
                  <a href="#" title="Excluir">
                    <i class="fa fa-trash" aria-hidden="true" style='color:red; font-size: 1.5rem;'></i>
                  </a>
                </div>
          </div>
        </div>
      </div>
      `,
      data(){
        return{
          comments: [
            
          ],
          name: '',
          message: '',
        }
      },
      methods:{
        addComment(){
          if(this.name.trim() === '' || this.message.trim() === '') {
            if(this.name.trim() === '' && this.message.trim() === ''){
              return alert('Os campos estão vazios.')
            }
            else if (this.message.trim() === '') {
              return alert('Comentário não foi preenchido.')
              
            }
            else if (this.name.trim() === '' || this.message.trim() === '') {
              return alert('Nome não foi preenchido.')
            }
          }

          this.comments.push({
            name: this.name,
            message: this.message
          });

          this.name = '',
          this.message = ''

        }
      }
})

