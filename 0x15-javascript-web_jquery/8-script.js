$.ajax({
url: "https://swapi-api.alx-tools.com/api/films/?format=json",
method: "GET",
success: function(data) {
$(data.results).each(function(key, value){
$('ul').append('<li>'+value.title+'</li>');
});
}
});
  