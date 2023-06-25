import passwordMixin from '@/mixins/password'
export default {
    name: 'submitCommandMixin',
    data() {
        return {}
    },
    mixins: [passwordMixin],
    methods: {
        getOperationType(msg) {
            if (msg.toLowerCase().split(" ").includes("password")) {
                return 'generate_password'
            } else {
                return null
            }
        },
        prepPayload(operation, msg = null) {
            if (operation === 'generate_password') {
                return this.newPasswordObj
            } else {
                return {
                    msg: msg
                }
            }
        }
    }

}