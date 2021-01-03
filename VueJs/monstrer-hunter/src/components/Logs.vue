<template>
  <div>
    <b-card id="main-logs" v-for="stage of getStages()" :key="stage.id" v-show="stage.damageOnPlayer != 0">

      <div class="avatar">
        <b-avatar class="avatar-icon" variant="" src="https://i.pinimg.com/originals/65/a2/17/65a2173428889205e3dd25d46c662b10.png"></b-avatar>
      </div>
      <div class="comment">
        <div class="mb-2" v-if="stage.damageOnPlayer != 0">
          <b-avatar class="hit" variant="danger" :text="stage.damageOnPlayer.toString()"></b-avatar> 
        </div>
      </div>

      <div class="comment">
        <div class="mb-2" v-if="stage.damageOnMonster != 0">
          <b-avatar class="hit" variant="danger" :text="stage.damageOnMonster.toString()"></b-avatar>
        </div>
      </div>
      <div class="avatar">
        <b-avatar class="avatar-icon" variant="" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cd8194ce-75b8-4b12-b51e-20d230a3cf9a/dduhe8j-537a20fd-30c1-46dd-bd99-90739d5da190.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvY2Q4MTk0Y2UtNzViOC00YjEyLWI1MWUtMjBkMjMwYTNjZjlhXC9kZHVoZThqLTUzN2EyMGZkLTMwYzEtNDZkZC1iZDk5LTkwNzM5ZDVkYTE5MC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.HNYb-WPmHWE3g9_9X4W6ppUQS5-lvVCQ19NZKnPJZoA"></b-avatar>
      </div> 

    </b-card>
  </div>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator';

@Component({
  methods: {
    getStages: function () {
      return this.$store.getters.stage
    }
  }
})

export default class Logs extends Vue {}
</script>

<style>
.hit {
  width: 30%;
  height: 80px !important;
  font-size: 2rem;
}

.card-body {
    display: flex !important;
}

.comment {
  width: 100%;
  margin: auto auto auto 5%;
  text-align: center;
}

.avatar {
  width: 75%;  
}

.avatar-icon {
  width: 100% ; 
  height: 100%;
}

#main-logs {
  margin: 2rem auto 2rem auto
}
</style>