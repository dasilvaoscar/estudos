let ul = document.createElement("ul")
let container = document.querySelector(".container");
let input = document.querySelector(".container input");
let button = document.querySelector(".container #button");
let removeButton = document.querySelector(".container ul li .btn btn-primary");
let h1 = document.createElement("h1")

h1.innerHTML = '<kbd>Oscar-estudos<span style="color: #35ae35">~$</span></kbd> Aprendi em JS'
container.insertBefore(ul, input)
container.insertBefore(h1, ul)
let todos = JSON.parse(localStorage.getItem('list_todos')) || [];

function renderList() {

    ul.innerHTML = ''

    for (todo of todos) {
        
        let li = document.createElement('li');
        let todoText = document.createTextNode(todo);
        let linkRemove = document.createElement('a');
        let linkUpdate = document.createElement('a')
        let ind = todos.indexOf(todo);

        li.appendChild(todoText);
        li.setAttribute('class', 'list-group-item');
        li.appendChild(linkRemove);    
        li.appendChild(linkUpdate);
        
        ul.appendChild(li);
        linkRemove.setAttribute('href', '#');
        linkRemove.setAttribute('onclick', 'delList(' + ind + ')');
        linkRemove.setAttribute('class', 'fa fa-trash');
        linkUpdate.setAttribute('href', '#');
        linkUpdate.setAttribute('onclick', 'updateList(' + ind + ')');
        linkUpdate.setAttribute('class', 'fa fa-edit');
        linkUpdate.style.marginLeft = '.5em';
        linkRemove.style.color = 'red';
        linkRemove.style.marginLeft = '.5em';
        li.style.marginBottom = '.5em';
        
        
    }
}

function addList() {
    let textInput = input.value;

    if(textInput == ''){
        alert('Não insira objetos nulos');
    }
    else{
        todos.push(textInput);
        input.value = '';
        renderList();
        saveToCache();
        
    }
}

function updateList(ind){
    let resp = window.prompt("Deseja alterar? " + todos[ind]);
    todos[ind] = resp;
    renderList();
    saveToCache();
}

function delList(ind){
    todos.splice(ind, 1);
    renderList();
    saveToCache();
}

function git () {

    let linkElement = document.createElement('a');
    let git = document.createElement('i');
    let container = document.querySelector('.container');
    let div = document.createElement("div");

    linkElement.setAttribute('href', 'https://github.com/OscarSilvaOfficial');
    linkElement.appendChild(git);
    linkElement.setAttribute('target', '_blank');
    container.style.textAlign = 'center';
    container.appendChild(div);
    git.style.fontSize = '2em';
    git.style.color = 'black';
    git.setAttribute('class', 'fa fa-github');
    div.appendChild(linkElement);

    renderList();

}

function saveToCache() {
    localStorage.setItem('list_todos', JSON.stringify(todos));
}

git();
button.onclick = addList;
