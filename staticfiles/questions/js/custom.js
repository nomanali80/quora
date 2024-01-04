$(document).ready(function() {
  initilizeSelect2();

  $('form.ajax-form').submit(function(event) {
      console.log('Form submitted');
      event.preventDefault();
      var form = $(this);
      console.log(form);
      $.ajax({
          type: form.attr('method'),
          url: form.attr('action'),
          data: form.serialize(),
          headers: {
              'X-Requested-With': 'XMLHttpRequest'
          },
          success: function(data) {
              var answersContainer = form.closest('.list-group-item').find('.existing-answers');
              answersContainer.html(data);
              form.find('input[type="text"]').val('');
              alert('Answer submitted successfully:');
          }
      });
  });
});

function initilizeSelect2() {
    var urlParams = new URLSearchParams(window.location.search);
    var selectedTopics = urlParams.getAll('topics');

    $('#topics').val(selectedTopics);
    $('#topics').select2({
        placeholder: 'Select topics',
        allowClear: true,  // Enable clearing the selected options
        width: '100%',      // Set the width to 50%
    });
}


function likeDislikeQuestion(questionId, like_dislike, action) {
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
      type: 'POST',
      url: '/quora/questions/like_dislike_question/' + questionId + '/',
      data: {
          'action': action,
          'like_dislike': like_dislike,
          csrfmiddlewaretoken: csrftoken,
      },
      dataType: 'json',
      success: function(data) {
          if (data.status === 'success') {
              $('#likeCount_' + questionId).text(data.like_count);
              $('#dislikeCount_' + questionId).text(data.dislike_count);
              if (like_dislike == "like") {
                  var likeButton = $('#likeCount_' + questionId).parent();
                  var dislikeButton = $('#dislikeCount_' + questionId).parent();

                  if (data.liked) {
                      likeButton.addClass('btn-success');
                      dislikeButton.removeClass('btn-danger');
                  } else {
                      likeButton.removeClass('btn-success');
                  }
              } else {
                  var dislikeButton = $('#dislikeCount_' + questionId).parent();
                  var likeButton = $('#likeCount_' + questionId).parent();

                  if (data.disliked) {
                      dislikeButton.addClass('btn-danger');
                      likeButton.removeClass('btn-success');
                  } else {
                      dislikeButton.removeClass('btn-danger');
                  }
              }
          } else {
              alert('Error: ' + 'error while processing');
          }
      },
      error: function(xhr, textStatus, errorThrown) {
          alert('AJAX Error: ' + errorThrown);
      }
  });
}

function likeDislikeAnswer(answerId, like_dislike, action) {
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
      type: 'POST',
      url: '/quora/answers/like_dislike_answer/' + answerId + '/',
      data: {
          'action': action,
          'like_dislike': like_dislike,
          csrfmiddlewaretoken: csrftoken,
      },
      dataType: 'json',
      success: function(data) {
          if (data.status === 'success') {
              $('#likeCountAns_' + answerId).text(data.like_count);
              $('#dislikeCountAns_' + answerId).text(data.dislike_count);

              if (like_dislike == "like") {
                  var likeButton = $('#likeCountAns_' + answerId).parent();
                  var dislikeButton = $('#dislikeCountAns_' + answerId).parent();
                  if (data.liked) {
                      likeButton.addClass('btn-success');
                      dislikeButton.removeClass('btn-danger');
                  } else {
                      likeButton.removeClass('btn-success');
                  }
              } else {
                  var dislikeButton = $('#dislikeCountAns_' + answerId).parent();
                  var likeButton = $('#likeCountAns_' + answerId).parent();

                  if (data.disliked) {
                      dislikeButton.addClass('btn-danger');
                      likeButton.removeClass('btn-success');
                  } else {
                      dislikeButton.removeClass('btn-danger');
                  }
              }
          } else {
              alert('Error1: ' + 'error while processing');
          }
      },
      error: function(xhr, textStatus, errorThrown) {
          alert('AJAX Error: ' + errorThrown);
      }
  });
}
