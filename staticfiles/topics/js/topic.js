function followUnfollow(topicId, action) {
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
      type: 'POST',
      url: '/quora/topics/follow_unfollow_topic/' + topicId + '/',
      data: {
          'action': action,
          csrfmiddlewaretoken: csrftoken,  // Include the CSRF token
      },
      dataType: 'json',
      success: function(data) {
          if (data.status === 'success') {
              $('#followUnfollow_' + topicId).text(data.label);
          } else {
              // Display an error message if the server response indicates failure
              alert('Error1: ' + data.message);
          }
      },
      error: function(xhr, textStatus, errorThrown) {
          alert('AJAX Error: ' + errorThrown);
      }
  });
}
