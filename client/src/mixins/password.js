export default {
    name: 'passwordMixin',
    data() {
        return {
            passwordTypeOptions: [
                {name: 'Alphanumeric', code: 'alphanumeric'},
                {name: 'Letters Only', code: 'letters'}
            ],
            newPasswordObj: {
                'passlen': 16,
                'useSpecialCharacters': true,
                'selectedPasswordType': 'alphanumeric'
            },
            hasPasswordDetails: false
        }
    },
    methods: {
        passwordContainsLen(password) {
            return /\d/.test(password);
        },
        extractPasswordLen(password) {
            return password.match(/\d+/)[0]
        },
        prepPasswordObject(password) {
            if (this.passwordContainsLen(password)) {
                this.newPasswordObj.passLen = this.extractPasswordLen(password)
            }
            return this.newPasswordObj
        },
        clearPasswordData() {
            this.newPasswordObj = {
                'passlen': 16,
                'useSpecialCharacters': true,
                'selectedPasswordType': 'alphanumeric'
            }
        }
    }

}