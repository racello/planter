//display wishlist items
var display_wishlist = function(wishlist) {
  $('#plants').empty();
  $.each(wishlist, function(index, value) {
    $('#plants').append($('<img />').attr({
      'class': 'icon',
      'src': value['pic'],
      'width': 100
    }));
  })
};

var display_table = function(wishlist) {
  $.each(wishlist, function(index, value) {
    var row = $('<tr id=' + index + '></tr>');
    var name_cell = $('<td>' + value['name'] + '</td>')
    var sun_cell = 1;
    row.append(name_cell)
        .append(sun_cell);
    $('#table > tbody:last-child').append(row);
  })
}

//display room list items (shopping list)
var display_roomlist = function(room) {
  $('#room_list').empty();
  var shop_id = 0;

  $.each(room, function(index, value) {
    shop_id++;
    $('#room_list').append($('<div id=' + shop_id + '></div>'));
    $('#' + shop_id).append($('<img />').attr({
        'class': 'buy',
        'src': value['pic'],
        'width': 100
      }),
      value['name'],
      );
  })
}
//print
function printDiv(divName) {
  display_roomlist(room);
   var printContents = document.getElementById(divName).innerHTML;
   var originalContents = document.body.innerHTML;
   document.body.innerHTML = printContents;
   window.print();
   document.body.innerHTML = originalContents;
};

//display room layout
var load_room = function(room) {
  $('#room').empty();

  $.each(room, function(index, value) {
    $('#room').append($('<img />').attr({
      'class': 'icon',
      'src': value['pic'],
      'width': 100,
    }))
    $('.in_room').position(value['position'])
  })
}

//display plants in room layout
var put_in_room = function(plant) {
  var data_to_save = {"plant": plant}
  $.ajax({
    type: "POST",
    url: "add_to_room",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      var all_data = result["room"]
      room = all_data
      console.log(JSON.stringify(result))

      //load_room(room)
    },
    error: function(request, status, error) {
      console.log("Error")
      console.log(request)
      console.log(status)
      console.log(error)
    }
  })
};

//make windows display in room
var add_window = function(id) {
  var data_to_save = {"id": id}
  $.ajax({
    type: "POST",
    url: "add_window",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      var all_data = result["room"]
      room = all_data
      //console.log(JSON.stringify(result))
    },
    error: function(request, status, error) {
      console.log("Error")
      console.log(request)
      console.log(status)
      console.log(error)
    }
  })
}

//putting item back in wishlist section deletes it from room
var delete_from_room = function(id) {
  var item_to_remove = {"id": id}
  $.ajax({
    type: "DELETE",
    url: "delete_room",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(item_to_remove),
    success: function(result) {
      var all_data = result["room"]
      data = all_data
      console.log(JSON.stringify(result))
    },
    error: function(request, status, error) {
      console.log("Error")
      console.log(request)
      console.log(status)
      console.log(error)
    }
  })
}

$(document).ready(function() {
  display_wishlist(wishlist);
  display_table(wishlist);

  $('#shop').click(function() {
    console.log('click')
    display_roomlist(room);
  })

  //click button to make windows
  var window_id = 0;
  $('.window_btn').click(function() {
    window_id++;
    if ($(this).text() == "horizontal window") {
      $('#room').append('<div class="window Hwindow ui-draggable ui-draggable-handle" id=' + window_id + '></div>')
      $('.window').draggable({
        revert: "invalid",
        cursor: "move"
      })    }
    else {
      $('#room').append('<div class="window Vwindow ui-draggable ui-draggable-handle" id=' + window_id + '></div>')
      $('.window').draggable({
        revert: "invalid",
        cursor: "move"
      })
    }
  })

  //put plants back in wishlist
  $('#wish').droppable({
    accept: '.icon',
    drop: function(event, ui) {
      var dragging = ui.draggable;
      var pic = dragging.attr('src');
      var target = $('#wish');

      var id;
      $.each(room, function(index, value){
        if (value['pic'] == pic) {
          id = value['id']
        }
      })
      delete_from_room(id);
    }
  })

  //drag and drop windows and plants
  $('#room').droppable({
    accept: '.window, .icon',
    drop: function(event, ui) {
      var dragging = ui.draggable;
      var id = dragging.attr('id');
      var pic = dragging.attr('src');
      var target = $('#room');
      var dragposition = ui.position;

      if (dragging.hasClass('window')) {
        add_window(id);
      }
      else {
        var name;
        var wish_id;
        $.each(wishlist, function(index, value){
          if (value['pic'] == pic) {
            name = value['name']
            wish_id = value['id']
          }
        })
        var plant = {
          name: name,
          pic: pic,
          id: wish_id
          //position: dragposition
        }
        put_in_room(plant);
      }
    }
  })
  $('.icon').draggable({
    revert: "invalid",
    cursor: "move"
  })

  //display square footage of room
  $('#room').resize(function() {
    var w = $('#room').width()
    var h = $('#room').height()
    console.log(w)
    console.log(h)
  })
})
