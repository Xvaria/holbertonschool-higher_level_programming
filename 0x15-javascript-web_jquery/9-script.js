$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(trad) {
  $('#hello').text(trad.hello);
});
