addEventListener("DOMContentLoaded", function () {
    let $ = (x) => document.querySelector(x);

    $('#shorten_button').onclick = function () {
        let url = $('#input_url').value;

        fetch('/shorten', {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify({
                'url': url
            })
        }).then(response => response.json())
          .then(result => {
              if (result['ok']) {
                  let shorten_url = result['url'];
        
                  $('#output_url').value = shorten_url;
                  $('#output_url').select();
        
                  if ($('#clipboard').checked) {
                      document.execCommand('copy');
                  }
              } else {
                  alert(result['reason']);
              }
          })
    }
});
