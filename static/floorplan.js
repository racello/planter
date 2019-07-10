//display items in table
var display_table = function(wishlist, data) {
  $.each(wishlist, function(index, value) {
    var row = $('<tr></tr>');

    var icon = '<img class="icon" width="100" src="' + value['pic'] + '" />';
    var icon_cell = $('<td>' + icon + '</td>')

    var name_cell = $('<td>' + value['name'] + '</td>')

    var sun_cell;
    var sun;
    $.each(data, function(i, v){
      if (value['id'] == v['id']) {
        sun = v['sun']
      }
    })
    sun_cell = $('<td id=' + value['id'] + '>' + sun + '</td>')

    var location_cell = $('<td class="location" style="color: #eb7f65"> unhappy </td>')

    row.append(icon_cell)
        .append(name_cell)
        .append(sun_cell)
        .append(location_cell);
    $('#table > tbody:last-child').append(row);
  })
}

//check current position of plant in room
//return how much sunlight they receive from that position
var check_position = function(plant_position, windows){
  var shortest_dist = Number.POSITIVE_INFINITY;
  var plant_left = plant_position['left']
  var plant_top = plant_position['top']
  $.each(windows, function(index, value) {
    var window_left = value['position']['left']
    var window_top = value['position']['top']
    var delta_x = plant_left - window_left
    var delta_y = plant_top - window_top
    var dist = Math.sqrt(delta_x*delta_x + delta_y*delta_y)
    shortest_dist = Math.min(shortest_dist, dist)
  })
  var returnvalue;
  if (shortest_dist < 100) {
    returnvalue = "high"
  }
  else if (shortest_dist >= 100 && shortest_dist < 200) {
    returnvalue = "medium"
  }
  else {
    returnvalue = "low"
  }
  return returnvalue;
}

//check if current position of plant matches actual needs
var check_sun_happiness = function(id, current_sun) {
  //go through each tr
  $('#table tr').each(function(index, value) {
    if (index != 0) {
      var sun_cell_val;
      //go through each td
      $(this).find('td').each(function() {
        if ($(this).attr('id') == id) {
          sun_cell_val = $(this).html();
          if (sun_cell_val == current_sun) {
            $(this).siblings('.location').html("healthy!")
            $(this).siblings('.location').css("color", "#a3b995")
          }
          else {
            $(this).siblings('.location').html("unhappy")
            $(this).siblings('.location').css("color", "#eb7f65")
          }
        }
      })
    }
  })
}

var check_all_sun = function() {
  var result = [];
  var bool = false;
  $('#table tr').each(function(index, value) {
    if (index != 0) {
      var status = $(this).find('.location').html().replace(/\s/g,'')
      result.push(status)
    }
  })
  if (result.indexOf('unhappy') == -1) {
    bool = true;
  }
  return bool
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
      //console.log(JSON.stringify(result))
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
var add_window = function(w) {
  var data_to_save = {"w": w}
  $.ajax({
    type: "POST",
    url: "add_window",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      windows = result["windows"]
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

//check input values for room dimensions
var enter = function() {
  if ($('#width').val() == '') {
    alert('Enter a number!');
    $('#width').focus();
  }
  else if ( $.isNumeric( $('#width').val() ) == false) {
    alert('Please enter an integer value.');
    $('#width').val('');
    $('#width').focus();
  }
  else if ($('#height').val() == '') {
    alert('Enter a number!');
    $('#height').focus();
  }
  else if ( $.isNumeric( $('#height').val() ) == false) {
    alert('Please enter an integer value.');
    $('#height').val('');
    $('#height').focus();
  }
  else {
    var width = $('#width').val() * 40
    var height = $('#height').val() * 40
    $('#room').width(width)
    $('#room').height(height)
  }
}

$(document).ready(function() {
  display_table(wishlist, data);

  //manually enter room dimensions
  $('#submit').click(function() {
    enter();
  })
  $('#width').keypress(function(e) {
    if (e.which == 13) {
      enter();
      return false;
    }
  })
  $('#height').keypress(function(e) {
    if (e.which == 13) {
      enter();
      return false;
    }
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

  //double click a window to delete it
  $('.window').dblclick(function() {

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
      var dragposition = ui.offset;

      if (dragging.hasClass('window')) {
        var w = {
          id: id,
          position: dragposition
        }
        add_window(w);
      }
      else { //plant
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
        }
        put_in_room(plant);

        //get current sun level of dragged plant
        var current_sun = check_position(dragposition, windows)
        //assess if current sun level is healthy for plant
        check_sun_happiness(wish_id, current_sun)
        if (check_all_sun() == true) {
          $('#happy').addClass('show')
        }
        else {
          $('#happy').removeClass('show')
        }
      }
    }
  })
  $('.icon').draggable({
    revert: "invalid",
    cursor: "move"
  })
})
