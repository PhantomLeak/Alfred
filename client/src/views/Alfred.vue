<template>
    <div class="container">
      <v-card :loading="loading" height="80vh" class="d-flex flex-column">
        <v-card-text style="overflow-y: scroll;">
          <v-container>
            <v-row>
              <v-col>
                <div v-for="(item, index) in chat" :key="index" 
                    :class="['d-flex flex-row align-center my-2', isMessageFromUser(item.from) ? 'justify-end': null]">
                  <span v-if="isMessageFromUser(item.from)" class="blue--text mr-3">{{ item.msg }}</span>
                  <v-avatar :color="isMessageFromUser(item.from) ? 'indigo': 'red'" size="36">
                    <span class="white--text">{{ item.from[0] }}</span>
                  </v-avatar>
                  <span v-if="!isMessageFromUser(item.from)" class="blue--text ml-3">{{ item.msg }}</span>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-spacer />
        <v-card-actions>
          <v-row no-gutters>
            <v-col>
              <div class="d-flex flex-row align-center">
                <v-avatar @click="changeUserName()" 
                  color="indigo" size="36">
                  <span class="white--text">{{ userName[0] }}</span>
                </v-avatar>
                <v-text-field v-model="msg" placeholder="Type Something" @keypress.enter="submitCommand"></v-text-field>
                <v-btn icon class="ml-4" @click="submitCommand"><v-icon>mdi-send</v-icon></v-btn>
              </div>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>

      <!-- Change Username dialog-->
      <v-dialog
        v-model="changeUserNameModal"
        @click:outsize="changeUserNameModal = false"
        width="500"
        >
        <v-card>
          <v-card-title>Change your display name</v-card-title>
          <v-card-text>
            <v-text-field
              v-model="userName"
              />
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn
              @click="setNewUserName"
              color="red"
              small
              >Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const PATH = 'http://localhost:5000/'
  export default {
    name: 'Alfred-vue',
    data() {
      return {
        msg: null,
        loading: false,
        chat: [],
        userName: 'user',
        prevUserName: null,  
        changeUserNameModal: false
      };
    },
    components: {
    },
    methods: {
      submitCommand() {
        this.loading = true
        this.writeUserRequest()
        let payload = {
          'request_msg': this.msg
        }
        axios.post(PATH, payload).then((ret) => {
          if (ret.data) {
            this.msg = null
            this.addReply(ret.data.return_msg)
          }
        })
        this.loading = false
      },
      clearInfo() {
        this.msg = null
        this.requestMsg = ''
      },
      async getGreeting() {
        axios.get(PATH).then((ret) => {
          if (ret.data) {
            this.addReply(ret.data.greeting_msg)  
          }
        })
      },
      writeUserRequest: function(){
        this.chat.push({from: this.userName, msg: this.msg})
      },
      addReply(msg){
        this.chat.push({
          from: "Alfred",
          msg: msg
        })
      },
      isMessageFromUser(from) {
        if (from === this.userName || from === this.prevUserName) {
          return true
        } else {
          return false
        }
      },
      changeUserName() {
        this.prevUserName = this.userName
        this.changeUserNameModal = true
      },
      setNewUserName() {
        this.chat.forEach(m => {
          if (m.from !== 'Alfred') {
            m.from = this.userName
          }
        })
        this.changeUserNameModal = false
      }
    },
    created() {},
    async mounted() {
      this.loading = true
      await this.getGreeting()
      this.loading = false
    }
  };
  </script>
<style scoped lang="scss">
</style>