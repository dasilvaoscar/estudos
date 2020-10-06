axios.get('https://api.github.com/users/OscarSilvaOfficial')
    .then(function(response){
        console.log(response.config.url);
    })
    .catch(function(error){
        console.warn(error);
    });