const uuid = require('uuid')

class Todo {
    constructor({ text, when }) {
        this.text = text
        this.when = when
        this.status = ''
        this.id = uuid.v4()
    }
}