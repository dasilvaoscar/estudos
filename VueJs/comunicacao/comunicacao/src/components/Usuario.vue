<template>
    <div class="container">
        <h1>Componente Usuário</h1>
        <p>Esse é um componente muito legal!</p>
        <p>{{ name }}</p>
        <button @click="alterarNome()">Alterar Nome</button>
        <hr>
        <div class="componentes">
            <app-usuario-info :name="name" @nomeMudou="name = $event" :reiniciarFn="reiniciarNome"/>
            <app-usuario-editar :name="name"/>
        </div>
    </div>
</template>

<script>
import AppUsuarioInfo from './UsuarioInfo'
import AppUsuarioEditar from './UsuarioEditar'

export default {
    components: { AppUsuarioInfo, AppUsuarioEditar },

    data: function() {
        return {
            name: 'Oscar'
        }
    },
    
    methods: {
        alterarNome: function() {
            this.name = this.name == 'Oscar' ? 'Oscar da Silva' : 'Oscar'
        },

        reiniciarNome: function() {
            this.name = 'Dirottéia'
        }
    }
}
</script>

<style scoped>
    .container {
        background-color: #27363b;
        color: #fff;
        padding: 10px;
    }

    .container hr {
        margin: 20px 10px;
    }

    .componentes {
        display: flex;
    }

    .componentes > * {
        margin: 10px;
    }
</style>
