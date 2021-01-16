<template>
    <div class="componente">
        <h2>Alterar os Dados de Usuário</h2>
        <p>Edite as informações</p>
        <input type="text" name="" id="" v-model="name">
    </div>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            required: true,
            default: 'Anônimo' 
        },
    }
}
</script>

<style scoped>
    .componente {
        flex: 1;
        background-color: #98b99a;
        color: #fff;
    }
    input {
        width: 80%;
        height: 3rem;
        font-size: 3rem;
        text-align: center;
        margin: 1% auto 1% auto;
    }
</style>
