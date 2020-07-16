function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//$(document).ready(function(){
  $('#upload_paper').submit(function(event){
    event.preventDefault();
    $("#progress").show();
    //alert("hii");
    var formData=new FormData($('form')[0]);
    var csrftoken = getCookie('csrftoken');

    $.ajax({

      xhr: function(){
        var xhr = new window.XMLHttpRequest();

       xhr.upload.addEventListener('progress',function(e){
          if(e.lengthComputable){
          var percent = Math.round((e.loaded/e.total)*100);
          $('#progressBar').attr('aria-valuenow',percent).css('width',percent+'%').text(percent+'%');
        }
        });
        return xhr;
      },

      'X-CSRFToken': csrftoken,
      type:'POST',
      url: '',
      data: formData,
      processData:false,
      contentType: false,
      success: function(){
        location.href = "/../success_upload/"
      },
    });

  });
//});
