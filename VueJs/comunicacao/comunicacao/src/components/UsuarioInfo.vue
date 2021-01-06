<template>
    <div class="componente">
        <h2>As Informações de Usuário</h2>
        <p>Nome: <strong v-once>{{ name }}</strong></p>
        <button @click="setNomeAleatorio">Reiniciar Nome</button>
        <button @click="reiniciarFn()">Reiniciar Nome (Callbacks)</button>
    </div>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            required: true,
            default: 'Anônimo',
        }, 

        reiniciarFn: Function
    },

    methods: {
        setNomeAleatorio: function() {
            this.$emit('nomeMudou', this.name == 'Oscar' ? 'Osilvinha':'Oscar')
        }
    },
}
</script>

<style scoped>
    .componente {
        flex: 1;
        background-color: #ec485f;
        color: #fff;
    }
</style>
