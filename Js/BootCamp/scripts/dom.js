let linkElement = document.createElement('a');
linkElement.setAttribute('href', 'https://github.com/OscarSilvaOfficial');

let textElement = document.createTextNode('Acessar meu GitHub');
linkElement.appendChild(textElement);

let container = document.querySelector('.container');
let div = document.createElement("div")

container.style.textAlign = 'center';
container.appendChild(div)
div.appendChild(linkElement)

let listElement = document.querySelector(".container ul")
let inputElement = document.querySelector(".container input")
let buttonElement = document.querySelector(".container #button")
let removeButton = document.querySelector(".container ul li .btn btn-primary")

let todos = [
    
];

function renderList() {

    listElement.innerHTML = ''

    for (todo of todos) {
        
        let todoElement = document.createElement('li');
        let todoText = document.createTextNode(todo);
        
        todoElement.appendChild(todoText);
        listElement.appendChild(todoElement);

    }
}

function addList() {
    let textInput = inputElement.value

    todos.push(textInput);
    inputElement.value = '';

    renderList()
}

buttonElement.onclick = addList;
