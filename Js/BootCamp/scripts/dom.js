let ul = document.querySelector(".container ul");
let input = document.querySelector(".container input");
let button = document.querySelector(".container #button");
let removeButton = document.querySelector(".container ul li .btn btn-primary");

let todos = [
    
];

function renderList() {

    ul.innerHTML = ''

    for (todo of todos) {
        
        let li = document.createElement('li');
        let todoText = document.createTextNode(todo);
        let linkRemove = document.createElement('a');
        let removeText = document.createTextNode('Remover');
        let ind = todos.indexOf(todo);

        li.appendChild(todoText);
        li.setAttribute('class', 'list-group-item');
        li.style.marginBottom = '.5em';
        ul.appendChild(li);
        linkRemove.setAttribute('href', '#');
        linkRemove.setAttribute('onclick', 'delList(' + ind + ')');
        linkRemove.appendChild(removeText);
        linkRemove.style.marginLeft = '.5em';
        li.appendChild(linkRemove);     

    }
}

function addList() {
    let textInput = input.value;

    todos.push(textInput);
    input.value = '';
    renderList();
}

function delList(ind){
    todos.splice(ind, 1);
    renderList();
}

function git () {

    let linkElement = document.createElement('a');
    let git = document.createElement('i');
    let container = document.querySelector('.container');
    let div = document.createElement("div")

    linkElement.setAttribute('href', 'https://github.com/OscarSilvaOfficial');
    linkElement.appendChild(git);
    linkElement.setAttribute('target', '_blank');
    container.style.textAlign = 'center';
    container.appendChild(div);
    git.style.fontSize = '2em';
    git.style.color = 'black';
    git.setAttribute('class', 'fa fa-github');
    div.appendChild(linkElement);

}

git();
button.onclick = addList;
