var check_wishlist = function(id) {
  var returnvalue = false;
  $.each(wishlist, function(index, value){
    if (id == value['id']) {
      returnvalue = true;
    }
  })
  return returnvalue;
}

var display_items = function(data, filter) {
  $('#items').empty();
  $('#items').append($('<div class="row"></div>'));

  $.each(data, function(index, value) {
    var link = value['picture'];
    var id = value['id'];
    var name = value['name'];
    var toInsert = '<div class="column"><div class="content"><img src=' + link + ' style="width: 100%;"><h4 id=' + id + '>' + name + '</h4><button class="add_btn" id=' + id + '> add to wishlist </button><button class="delete"> remove </button></div></div>';

    if (filter == "") { //show all
      $('.row').append($(toInsert));
    }
    else { //if category == filter then append to row
      if (value['category'] == filter) {
        $('.row').append($(toInsert));
      }
    }
    if (check_wishlist(id)) {
      $("#" + id + ".add_btn").html('added!');
      $("#" + id + ".add_btn").addClass('active');
      $("#" + id + ".add_btn").siblings('.delete').addClass('show');
    }
    else if (!check_wishlist(id)){
      $("#" + id + ".add_btn").removeClass('active');
      $("#" + id + ".add_btn").html('add to wishlist');
      $("#" + id + ".add_btn").siblings('.delete').removeClass('show');
    }
  })
}

var add_to_wishlist = function(new_item) {
  var data_to_save = {"new_item": new_item}
  var total;
  $.ajax({
    type: "POST",
    url: "add_item",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data_to_save),
    success: function(result) {
      var all_data = result["wishlist"]
      wishlist = all_data
      console.log(JSON.stringify(result))

      total = result['total']
      $('#totally').text(total)
      if (desired == total) {
        $('#next').addClass('show')
      }
    },
    error: function(request, status, error) {
      console.log("Error")
      console.log(request)
      console.log(status)
      console.log(error)
    }
  });
}

var delete_wishlist = function(id) {
  var item_to_remove = {"id": id}
  $.ajax({
    type: "DELETE",
    url: "delete_wishlist",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(item_to_remove),
    success: function(result) {
      wishlist = result['wishlist']
      total = result['total']
      $('#totally').text(total)
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
  display_items(data, "");

  $('#totally').html(total);

  $(document).on("click", "#filter", function() {
    var search_for = $(this).text()
    if (search_for == "show all") {
      search_for = ""
    }
    console.log(search_for)
    display_items(data, search_for)
  })

  //go to my plan(ts)
  $(document).on("click", "#next", function() {
    window.location.href = '/floorplan'
  })

  //click on image to get more information
  $(document).on("click", "img", function() {
    var id = 0
    var imglink = $(this).attr("src");
    $.each(data, function(index, value) {
      if (imglink == value['picture']) {
        id = value['id'];
      }
    })
    window.location.href = 'item/' + id;
  })

  //selected filter button shows active class
  $('#filters > button').not($('.active')).click(function(){
    $('#filters > button').removeClass('active');
    $(this).addClass('active');
  })

  //add to wishlist from gallery view
  $(document).on("click", ".add_btn", function() {
    //update button view to show users it worked
    $(this).html('added!');
    $(this).addClass('active');
    //only show delete button if item has been added
    $(this).siblings('.delete').addClass('show');

    //add to wishlist array
    var plant_id = $(this).siblings('h4').attr('id');
    var plant_name = $(this).siblings('h4').html();
    var photo = $(this).siblings('img').attr("src");
    var item = {
      id: plant_id,
      name: plant_name,
      pic: photo
    };
    add_to_wishlist(item);
  })

  //remove from wishlist from gallery view
  $(document).on("click", ".delete", function() {
    delete_id = $(this).siblings('h4').attr('id');
    delete_wishlist(delete_id);
    //reset add button
    $(this).siblings('.add_btn').removeClass('active');
    $(this).siblings('.add_btn').html('add to wishlist');
    //rehide delete button
    $(this).removeClass('show');
  })
})
