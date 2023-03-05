<template>
    <div class="container">
      <v-card>
        <v-card-title>
          <v-spacer />
          Hello, I'm Alfred
          <v-spacer />
        </v-card-title>
        <v-card-text>
          <v-row class="align-center justify-center">
            <v-col cols="6">
              <v-text-field
                v-model="requestMsg"
                solo dense
                placeholder="Enter Command Here"
              />
              <v-btn
                color="primary"
                small
                @click="buttonClick"
                >Submit</v-btn>
            </v-col>
          </v-row>
          <span v-if="msg !== ''">{{ msg }}</span>
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
      };
    },
    components: {},
    methods: {
      buttonClick() {
        let payload = {
          'request_msg': this.requestMsg
        }
        axios.post(PATH, payload).then((ret) => {
          if (ret.data) {
            this.msg = ret.data.return_msg
          }
        })
      }
    },
    created() {},
  };
  </script>