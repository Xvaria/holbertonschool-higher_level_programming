$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (movie) {
  $.each(movie.results, function (k, v) {
    $('li').add('<li>' + v.title + '</li>').appendTo('#list_movies');
  });
});
