<template>
    <div class="container">
      <v-card :loading="loading" height="80vh">
        <v-card-title>
          <v-spacer />
          <h2>{{ greeting }}</h2>
          <v-spacer />
        </v-card-title>
        <v-card-text>
          <v-form ref="postCommand" @submit.prevent="submitCommand">
            <v-row class="align-center justify-center">
              <v-col cols="8">
                <v-text-field
                  v-model="requestMsg"
                  solo dense
                  placeholder="Enter Your Request Here..."
                />
                <v-btn
                  color="primary"
                  small
                  @click="submitCommand"
                  >Submit</v-btn>
                
                <v-btn
                  v-if="msg !== ''"
                  color="red"
                  small
                  class="ml-4"
                  @click="clearInfo"
                  >Clear</v-btn>
              </v-col>
            </v-row>
          </v-form>
          <v-sheet v-if="msg !== ''" class="mt-10">
            <v-card-text>
              <v-row class="align-center justify-center">
                <v-col cols="6">
                  <span class="blue--text">{{ msg }}</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-sheet>
        </v-card-text>
      </v-card>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const PATH = 'http://localhost:5000/'
  export default {
    name: 'Alfred-vue',
    data() {
      return {
        requestMsg: '',
        msg: '',
        loading: false,
        greeting: '',
      };
    },
    components: {},
    methods: {
      submitCommand() {
        this.loading = true

        let payload = {
          'request_msg': this.requestMsg
        }
        axios.post(PATH, payload).then((ret) => {
          if (ret.data) {
            this.msg = ret.data.return_msg
            this.requestMsg = ''
          }

          this.loading = false
        })
      },
      clearInfo() {
        this.msg = ''
        this.requestMsg = ''
      },
      async getGreeting() {
        axios.get(PATH).then((ret) => {
          if (ret.data) {
            this.greeting = ret.data.greeting_msg
          }
        })
      },
    },
    created() {},
    async mounted() {
      this.loading = true
      await this.getGreeting()
      this.loading = false
    }
  };
  </script>