<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-img
        alt="Alfred"
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="50"
        @click="routeChange('')"
        src="../public/butler-black.png"
        width="50"
        style="cursor: pointer;"
          />

      <v-spacer />

      <v-btn
        small
        icon
        title="Resize / Format Images"
        @click="routeChange('imitari')"
        ><v-icon small>fa-solid fa-image</v-icon></v-btn>

      <v-btn
        small
        icon
        ><v-icon small>fa-solid fa-bell</v-icon></v-btn>
    
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
