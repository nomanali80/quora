function followUnfollow(topicId, action) {
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
      type: 'POST',
      url: '/quora/topics/follow_unfollow_topic/' + topicId + '/',
      data: {
          'action': action,
          csrfmiddlewaretoken: csrftoken,
      },
      dataType: 'json',
      success: function(data) {
          if (data.status === 'success') {
              $('#followUnfollow_' + topicId).text(data.label);
              $('#followedCount_' + topicId).text('Followed by: ' + data.followed_count)
          } else {
              alert('Error1: ' + 'error while performing');
          }
      },
      error: function(xhr, textStatus, errorThrown) {
          alert('AJAX Error: ' + errorThrown);
      }
  });
}
