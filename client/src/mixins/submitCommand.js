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
            }
            if (msg.toLowerCase().split(" ").includes("weather")) {
                return 'get_weather'
            }
        },
        prepPayload(operation, msg = null) {
            if (operation === 'generate_password') {
                return this.newPasswordObj
            }
            if (operation === 'get_weather') {
                return {
                    'weather_request': msg
                }
            }
        }
    }

}