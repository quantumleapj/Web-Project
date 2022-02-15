console.log("lower.js 가 로드되었습니다.");

function helloworld() {
  console.log("helloworld");
}

function display_like() {
  let posts = document.getElementsByClassName("sub_body_form");
  for (i = 1; i < posts.length + 1; i++) {
    id_str = "like_" + i.toString();
    let checkbox_label = document.getElementById(id_str);
    // console.log(checkbox_label)
    let checkbox = checkbox_label.getElementsByTagName("input")[0];
    let checkbox_in = checkbox_label.getElementsByTagName("span")[0];
    // console.log(checkbox)
    checkbox.addEventListener("change", function (e) {
      // console.log(checkbox.checked, checkbox.value);
      // console.log(request) //request is not defined
      // console.log(user)
      if (checkbox.checked) {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_full.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        // console.log(csrf_token)
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        // console.log(post_id)
        post_id = parseInt(post_id.textContent);
        // console.log(post_id)
        $.ajax({
          type: "post",
          url: "like/",
          dataType: "json",
          data: {
            // 'liked':true,
            // author:'request.user',
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
            // 'author':request.user,
            // 'post':request.post
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
      } else {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_empty.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        // console.log(csrf_token)
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        // console.log(post_id)
        post_id = parseInt(post_id.textContent);
        // console.log(post_id)
        $.ajax({
          type: "post",
          url: "unlike/",
          dataType: "json",
          data: {
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
      }
    });
    checkbox_label.addEventListener("click", function () {
      like_count = "like_count" + i.toString();
      // window.location.reload()
      $("#" + like_count).load(window.location.href + "#" + like_count);
    });
  }
}

function search_like(i) {
  
  // let post_id = checkbox_label.getElementsByTagName("postid")[0];
  // // console.log(post_id)
  // post_id = parseInt(post_id.textContent);

  console.log('search_like')
  // $(document).re
  $.ajax({
    type: "get",
    url: "show_like/",
    // dataType:"json",
    data:{'post':i},
    success: function (response) {
      console.log(response);
      console.log("get success");
    },
    error: function (response) {
      console.log(response);
      console.log("get error");
    },
  });
}

display_like();

// search_like(1);
