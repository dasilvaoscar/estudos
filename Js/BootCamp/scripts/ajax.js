let ajax = new XMLHttpRequest;

ajax.open('GET', 'https://api.github.com/users/OscarSilvaOfficial');
ajax.send();

ajax.onreadystatechange = () => {
    if (ajax.readyState === 4){
        console.log(JSON.parse(ajax.responseText));
    }
}