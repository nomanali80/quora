
$(document).ready(function () {
  // Handle form submission using AJAX
  $('form.ajax-form').submit(function (event) {
    console.log('Form submitted');
    event.preventDefault();
    var form = $(this);
    console.log(form);
    $.ajax({
      type: form.attr('method'),
      url: form.attr('action'),
      data: form.serialize(),
      headers: { 'X-Requested-With': 'XMLHttpRequest' },
      success: function (data) {
        // Update the answers section with the newly submitted answer
        var answersContainer = form.closest('.list-group-item').find('.existing-answers');
        answersContainer.html(data);
        form.find('input[type="text"]').val('');
      }
    });
  });
});

function likeDislikeQuestion(questionId, like_dislike, action) {
// Get the CSRF token from the page
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$.ajax({
    type: 'POST',
    url: '/quora/questions/like_dislike_question/' + questionId + '/',
    data: {
        'action': action,
        'like_dislike': like_dislike,
        csrfmiddlewaretoken: csrftoken,  // Include the CSRF token
    },
    dataType: 'json',
    success: function(data) {
        if (data.status === 'success') {
            // Update the like and dislike counts on the UI
            $('#likeCount_' + questionId).text(data.like_count);
            $('#dislikeCount_' + questionId).text(data.dislike_count);
            if (like_dislike == "like") {
              var likeButton = $('#likeCount_' + questionId).parent(); // parent of the span is the button
              var dislikeButton = $('#dislikeCount_' + questionId).parent(); // parent of the span is the button
              
              if (data.liked) {
                likeButton.addClass('btn-success');
                dislikeButton.removeClass('btn-danger');
              } else {
                likeButton.removeClass('btn-success');
              }
            } else {
              var dislikeButton = $('#dislikeCount_' + questionId).parent(); // parent of the span is the button
              var likeButton = $('#likeCount_' + questionId).parent();

              if (data.disliked) {
                dislikeButton.addClass('btn-danger');
                likeButton.removeClass('btn-success');
              } else {
                dislikeButton.removeClass('btn-danger');
              }
            }
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

function likeDislikeAnswer(answerId, like_dislike, action) {
    // Get the CSRF token from the page
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    // Make the POST request with CSRF token
    $.ajax({
        type: 'POST',
        url: '/quora/answers/like_dislike_answer/' + answerId + '/',
        data: {
            'action': action,
            'like_dislike': like_dislike,
            csrfmiddlewaretoken: csrftoken,  // Include the CSRF token
        },
        dataType: 'json',
        success: function(data) {
            if (data.status === 'success') {
                // Update the like and dislike counts on the UI
                $('#likeCountAns_' + answerId).text(data.like_count);
                $('#dislikeCountAns_' + answerId).text(data.dislike_count);

                if (like_dislike == "like") {
              var likeButton = $('#likeCountAns_' + answerId).parent(); // parent of the span is the button
              var dislikeButton = $('#dislikeCountAns_' + answerId).parent(); // parent of the span is the button
              if (data.liked) {
                likeButton.addClass('btn-success');
                dislikeButton.removeClass('btn-danger');
              } else {
                likeButton.removeClass('btn-success');
              }
            } else {
              var dislikeButton = $('#dislikeCountAns_' + answerId).parent(); // parent of the span is the button
              var likeButton = $('#likeCountAns_' + answerId).parent();

              if (data.disliked) {
                dislikeButton.addClass('btn-danger');
                likeButton.removeClass('btn-success');
              } else {
                dislikeButton.removeClass('btn-danger');
              }
            }
            } else {
                // Display an error message if the server response indicates failure
                alert('Error1: ' + data.message);
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            // Handle AJAX errors, e.g., show a generic error message
            alert('AJAX Error: ' + errorThrown);
        }
    });
}
