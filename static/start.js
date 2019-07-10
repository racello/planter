var save_desired = function(name) {
  var data_to_save = {"name": name}
  $.ajax({
    type: "POST",
    url: "get_desired",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      //console.log(JSON.stringify(result))
    },
    error: function(request, status, error){
      console.log("Error")
      console.log(request)
      console.log(status)
      console.log(error)
    }
  })
}

$(document).ready(function() {
  //hit "i want this many"
  $('#confirm').click(function() {
    if ($('#desired').val() == '' ) {
      alert('Enter a number!');
      $('#desired').focus();
    }
    else if ( $.isNumeric( $('#desired').val() ) == false) {
      alert('Please enter an integer value.');
      $('#desired').val('');
      $('#desired').focus();
    }
    else {
      save_desired($('#desired').val())
      window.location.href = 'search';
    }
  })

  //hit enter in textarea
  $('#desired').keypress(function(e) {
    if (e.which == 13) {
      if ($('#desired').val() == '' ) {
        alert('Enter a number!');
        $('#desired').focus();
      }
      else if ( $.isNumeric( $('#desired').val() ) == false) {
        alert('Please enter an integer value.');
        $('#desired').val('')
        $('#desired').focus();
      }
      else {
        save_desired($('#desired').val())
        window.location.href = 'search';
      }
      return false;
    }
  })
})
