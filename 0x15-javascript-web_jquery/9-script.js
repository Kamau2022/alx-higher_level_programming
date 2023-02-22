$.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    method: "GET",
    success: function(data) {
    $('div').append(data.hello);
    }
    });
      

      