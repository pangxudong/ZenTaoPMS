var lanhu = "https://lanhuapp.com/web/";

function goto_lanhu() {
  var username = "";
  $.ajax({
        type: "get",
        url: "/ZenTaoPMS/www/index.php?m=user&f=ajaxGetUser",
        success: function (data) {
            bbb = data.split(" ");
            for (b in bbb) {
              if (bbb[b].indexOf("value=")>-1 && bbb[b]!="value=''" && bbb[b]!="value='admin'"){
                username = bbb[b].substring("value='".length, bbb[b].length-1);
                console.log(username);
                break;
              }
            }
            if (username!="") {
                $.ajax({
                      type: "get",
                      url: "http://localhost:5000/lanhu?username=" + username,
                      success: function (data) {
                          console.log(data);
                      }
                  });
            }
        }
    });
}
