<template>
  <v-app class="appBody">
    <v-app-bar
      app
      class="topToolBar"
      elevation="2"
    >
      <v-img
        alt="Alfred"
        class="shrink mt-1 hidden-sm-and-down buttonPointer"
        contain
        min-width="50"
        @click="routeChange('')"
        src="../public/butler-silhouette.png"
        width="50"/>

      <v-spacer />

      <v-badge
          pill
          overlap
          floating
          left
          content="Coming Soon"
          color="red"
      >
        <v-btn
            disabled
            icon small
            color="white"
            title="Resize / Format Images"
            @click="routeChange('imitari')"
        >
          <v-icon small color="white">fa-solid fa-image</v-icon>
        </v-btn>
      </v-badge>

      <!-- Future project to enable reminders -->
      <!-- <v-btn
        small
        icon
        ><v-icon small>fa-solid fa-bell</v-icon></v-btn> -->
    
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
  methods: {
    routeChange(page) {
      this.$router.push('/' + page)
    }
  }
};
</script>

<style lang="scss">
// Import main / global style for Alfred
@import 'assets/css/custom';
</style>
