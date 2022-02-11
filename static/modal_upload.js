console.log('modal_upload.js 가 로드되었습니다.')

const modal = document.getElementById("id_modal_upload");
const buttonAddFeed = document.getElementById("id_upload_button");
buttonAddFeed.addEventListener("click", e => {
    console.log('buttonAddFeed')
    modal.style.display = "flex";
    modal.style.top = window.pageYOffset + 'px'; // top을 이용해 시작 y위치를 바꿔줌
    document.body.style.overflowY = "hidden"; // 스크롤 없애기
});

function CloseModal() {
  console.log('닫기 버튼 온클릭 함수 실행')
  modal.style.display='none';
  document.body.style.overflowY = "visible";
}
console.log(modal)
// modal.style.top = window.pageYOffset + 'px'; 
// modal.style.display='hidden';

function testfunc(){
  
  var form1=new FormData($("#form_upload")[0])
  var form2=new FormData($("#form_upload"))
  console.log(form1);
  console.log(form2)
  console.log(FormData)
  alert("error");
}

$(function(){
  $('#upload').on("click",function () {

      // var form1 = $("#form_upload").serialize();
      var form1=new FormData($("#form_upload")[0])
      console.log(form1);
      $.ajax({
          type: "post",
          url: "upload",
          data: form1,
          dataType:FormData,
          cache:false,
          contentType:false,
          processData:false,
          success: function (data) {
            console.log(request)  
            alert("success");
            console.log(data);
          },
          error: function (request, status, error) {
              console.log("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
              alert("error");
          }
      });
      console.log('ajax함수끝')
  });
});