<template lang="html">
  <div class="page-container">
    <md-app md-waterfall md-mode="overlap">
      <md-app-toolbar class="md-primary md-large">
        <div class="md-toolbar-row">
          <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
            <md-icon>menu</md-icon>
          </md-button>

          <span class="md-title">Welcome</span>
        </div>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>account_balance</md-icon>
            <span class="md-list-item-text">Home</span>
          </md-list-item>

          <md-list-item>
            <md-icon>face</md-icon>
            <span class="md-list-item-text">Me</span>
          </md-list-item>

          <md-list-item>
            <md-icon>timeline</md-icon>
            <span class="md-list-item-text">Works</span>
          </md-list-item>

          <md-list-item>
            <md-icon>contact_support</md-icon>
            <span class="md-list-item-text">Contact</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>
      <md-app-content></md-app-content>
    </md-app>
  </div>
</template>

<script>

export default {
  name: 'Overlap',
  data: () => ({
    menuVisible: false
  })
}
</script>

<style lang="css" scoped="true">
.md-app {
  min-height: 100vh;
}
.md-app {
  max-height: 400px;
  border: 1px solid rgba(#000, .12);
}
.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>
