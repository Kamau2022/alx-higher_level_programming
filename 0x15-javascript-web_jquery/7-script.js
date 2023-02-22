fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
.then(function(response){
return response.json()
.then(function(data){
$('div').append(data.name)
})
}); 