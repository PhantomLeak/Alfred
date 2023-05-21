<template>
    <div class="container">
      <v-card :loading="loading" height="80vh" class="d-flex flex-column" elevation-2>
        <v-card-text style="overflow-y: auto; display: flex; flex-direction: column-reverse;">
          <v-container>
            <v-row align="end">
              <v-col>
                <div v-for="(item, index) in chat" :key="index" style="text-overflow: clip;"
                    :class="['d-flex flex-row align-center my-2', isMessageFromUser(item.from) ? 'justify-end': null]">
                  <span v-if="isMessageFromUser(item.from)" class="blue--text mr-3" v-html="item.msg" />
                  <v-avatar 
                    :title="item.from"
                    :color="isMessageFromUser(item.from) ? displayColor : '#217596'" size="36">
                    <span class="white--text">{{ item.from[0] }}</span>
                  </v-avatar>
                  <span v-if="!isMessageFromUser(item.from)" class="blue--text ml-3" v-html="item.msg" />
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-spacer />
        <v-card-actions>
          <v-row no-gutters fixed>
            <v-col>
              <div class="d-flex flex-row align-center">
                <v-avatar @click="changeUserName()" class="buttonPointer"
                  :color="displayColor" size="36" title="Change Display Name">
                  <span class="white--text">{{ userName[0] }}</span>
                </v-avatar>
                <v-text-field v-model="msg" class="ml-3" placeholder="Type Something" @keypress.enter="submitCommand" />
                <v-btn icon class="ml-4" @click="submitCommand" title="Send Message"><v-icon>mdi-send</v-icon></v-btn>
              </div>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>

      <!-- Change Username dialog-->
      <v-dialog
        v-model="changeUserNameModal"
        @click:outsize="setNewUserName()"
        width="500"
        >
        <v-card>
          <v-card-title>
            <span>{{ userNameModalView === 'nameChange' ? 'Change your display name' : 'Change your display color' }}</span>
        
            <v-btn
              v-if="userNameModalView === 'nameChange'"
              small
              icon
              title="Change color"
              @click="userNameModalView = 'colorChange'"
              ><v-icon small>fa fa-palette</v-icon></v-btn>
                        
            <v-spacer />
            <v-btn
              x-small
              icon
              class="mt-n10 mr-n5"
              @click="changeUserNameModal = false"
              ><v-icon x-small>fa fa-times</v-icon></v-btn>
          </v-card-title>
          <v-card-text>
            <v-row class="align-center justify-center">
              <v-col cols="12">
                <v-text-field
                  v-if="userNameModalView === 'nameChange'"
                  v-model="userName"
                  />
                
                <v-color-picker 
                  v-if="userNameModalView === 'colorChange'"
                  class="ml-16"
                  v-model="displayColor"
                />
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="userNameModalView === 'colorChange'"
              small
              title="Back"
              color="info"
              @click="userNameModalView = 'nameChange'"
              >back</v-btn>
            <v-spacer />
            <v-btn
              @click="setNewUserName()"
              color="primary"
              small
              >Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const PATH = 'http://localhost:5000/'
  const PAGE_STORAGE_KEY = 'alfred'
  export default {
    name: 'Alfred-vue',
    data() {
      return {
        msg: null,
        loading: false,
        chat: [],
        userName: 'user',
        displayColor: '#4B0082',
        prevUserNames: [],
        prevRequest: '',
        performSameActionIndicators: [
          'tell me another one',
          'tell me another',
          'again'
        ],
        changeUserNameModal: false,
        userNameModalView: 'nameChange',
      };
    },
    components: {
    },
    methods: {
      submitCommand() {
        this.loading = true
        this.writeUserRequest()
        if (this.performSameActionIndicators.includes(this.msg)) {
          this.msg = this.prevRequest
        } else {
          this.prevRequest = this.msg
        }

        let payload = {
          'request_msg': this.msg
        }
        axios.post(PATH, payload).then((ret) => {
          if (ret.data) {
            this.msg = null
            this.addReply(ret.data.return_msg)
          }

          this.loading = false
        })
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
        if (from === this.userName || this.prevUserNames.includes(from)) {
          return true
        } else {
          return false
        }
      },
      changeUserName() {
        this.prevUserNames.push(this.userName)
        this.changeUserNameModal = true
      },
      setNewUserName() {
        this.chat.forEach(m => {
          if (m.from !== 'Alfred') {
            m.from = this.userName  // Update all records from previous messages with proper display name
          }
        })
        this.saveItemsToLocalStorage()
        this.changeUserNameModal = false
        this.userNameModalView = 'nameChange'
      },
      saveItemsToLocalStorage() {
        let settings = JSON.parse(localStorage.getItem(PAGE_STORAGE_KEY))
        if (settings) {
          settings.userName = this.userName
          settings.prevUserNames = this.prevUserNames
          settings.displayColor = this.displayColor
        }
        else {
          settings = {
            userName: this.userName,
            prevUserNames: this.prevUserNames,
            displayColor: this.displayColor
          }
        }

        localStorage.setItem(PAGE_STORAGE_KEY, JSON.stringify(settings))
      }
    },
    created() {},
    async mounted() {
      this.loading = true

      let settings = JSON.parse(localStorage.getItem(PAGE_STORAGE_KEY))
      if (settings) {
        if (settings.userName && settings.userName !== undefined) {
          this.userName = settings.userName
        }
        if (settings.prevUserNames && settings.prevUserNames !== []) {
          this.prevUserNames = settings.prevUserNames
        }
        if (settings.displayColor && settings.displayColor !== undefined) {
          this.displayColor = settings.displayColor
        }
      }

      await this.getGreeting()
      this.loading = false
    }
  };
  </script>
<style scoped lang="scss">
</style>