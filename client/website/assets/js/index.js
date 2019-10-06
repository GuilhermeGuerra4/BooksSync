addBtc = document.getElementById('add-book');
seeBtc = document.getElementById('see-books');
main = document.getElementById('main');
var host = 'http://192.168.1.71';

function loadAddBooksPage()
{
	main.innerHTML ='<h2>Add books</h2><div class="form"><form><div class="input"><input type="text" name="title" placeholder="Title"></div>'+
					'<label><div class="input in-file">PDF<img src="assets/img/pdf.png" width="20px"><input type="file" name="pdf" hidden></div></label>'+
					'<label><div class="input in-file">Image<img src="assets/img/default.gif" width="20px"><input type="file" name="img" hidden></div></label>'+
					'<div class="input"><button>Add the book</button></div>'+
					'<div class="response"></div>'+'</form></div>';
}

function loadBooksPage()
{
	loadLoadingPage();
	var http = new XMLHttpRequest();
	var url = host+'/api/v1/get-books';

	http.onreadystatechange = function() {
  	  if (this.readyState == 4 && this.status == 200) {
     	   var data = JSON.parse(this.responseText);
     	   html = '<h2>Books</h2><div class="books">';
     	
    	   for(i=0;i<data.length;i++)
    	   {
    	   	  html += '<div class="book" id="book-'+data[i][0]+'"><div class="img">'
					 +'<img src="'+data[i][3]+'"></div>'
					 +'<div class="title"><span>'+data[i][1]+'</span></div>'
					 +'<div class="link"><a href="'+data[i][2]+'" target="_blank">Link</a></div></div>';
    	   }

    	   if(data.length == 0){
    	   	html += '<div style="margin:20px;">Books not found!</div>'
    	   }

    	   html += '</div>';

    	   main.innerHTML = html;
    	}
	};

	http.open("GET", url, true);
	http.send();
}

function loadLoadingPage()
{
	main.innerHTML = '<div class="loading"></div>';
}

addBtc.addEventListener('click', loadAddBooksPage, false);
seeBtc.addEventListener('click', loadBooksPage, false);

loadBooksPage();