var display_info = function(id) {
  $.each(data, function(index, value) {
    if (id == value['id']) {
      $('#name').append(value['name']);
      $('#picture').append($('<img />').attr({
        'src': value['picture'],
        'width': 300
      }));
      $('#info').append(value['info']);
    }
  });
};

$(document).ready(function() {
  display_info(item_id)

  $(document).on("click", "#back", function() {
    window.location.href = '/search'
  })
})
