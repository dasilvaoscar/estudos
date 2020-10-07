class Model {

    constructor() {
        this.title = [];
        this.desc = [];
    }

}

class Controller extends Model {
    constructor(){
        super()
    }

    getTitle() {
        return this.title;
    }

    setTitle(title) {
        this.title.push(title);
        console.log(this.title)
    }

    getDesc() {
        return this.desc;
    }

    setDesc(desc) {
        this.desc.push(desc);
        console.log(this.desc)
    }

}

class Interface extends Controller {
    constructor() {
        super();
    }

    insertCard(title, desc) {
        debugger
        let container = document.querySelector('.container')
        let card = document.createElement('div')
        let img = document.createElement('img')
        let card_body = document.createElement('div')
        let h5 = document.createElement('h5')
        let p = document.createElement('p')
        let a = document.createElement('a')
        const detail = document.createTextNode('Detalhes')
        let node_title = document.createTextNode(title)
        let node_desc = document.createTextNode(desc)

        container.appendChild(card)
        card.appendChild(img)
        card.appendChild(card_body)
        card_body.appendChild(h5)
        card_body.appendChild(p)
        card_body.appendChild(a)
        card.setAttribute('class', 'card')
        img.setAttribute('src', 'https://png.pngtree.com/png-vector/20190411/ourlarge/pngtree-vector-html-icon-png-image_925883.jpg')
        img.setAttribute('class', 'card-img-top')
        img.setAttribute('alt', '...')
        card_body.setAttribute('class', 'card-body')
        h5.setAttribute('class', 'card-title')
        h5.appendChild(node_title)
        p.setAttribute('class', 'card-text')
        p.appendChild(node_desc)
        a.setAttribute('href', '#')
        a.setAttribute('class', 'btn btn-primary')
        a.appendChild(detail)
    }

}

const ControllerList = new Controller();
const InterfaceList = new Interface();
const ModelList = new Model();

document.getElementById('novotodo').onclick = function(){
    ControllerList.setTitle(document.getElementById('title').value);
    ControllerList.setDesc(document.getElementById('desc').value);
    InterfaceList.insertCard(ControllerList.title, ControllerList.desc)
};