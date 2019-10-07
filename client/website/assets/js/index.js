addBtc = document.getElementById('add-book');
seeBtc = document.getElementById('see-books');
main = document.getElementById('main');
formSending = false;
var host = 'http://82.154.129.14';

function loadAddBooksPage()
{
	main.innerHTML ='<h2>Add books</h2><div class="form"><form id="form"><div class="input"><input type="text" name="title" id="title" placeholder="Title"></div>'+
					'<label><div class="input in-file">PDF<img src="assets/img/pdf.png" width="20px"><input type="file" name="pdf" id="pdf" hidden></div></label>'+
					'<label><div class="input in-file">Image<img src="assets/img/default.gif" width="20px"><input type="file" name="img" id="img" hidden></div></label>'+
					'<div class="input"><button id="formSubmit">Add the book</button></div>'+
					'<div class="response" id="response"></div>'+'</form></div>';

	submitBtc = document.getElementById('formSubmit');
	submitBtc.addEventListener('click', submitAddBook, false);
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
					 +'<div class="link"><a href="'+host+'/read/'+data[i][2]+'" target="_blank">Link</a></div></div>';
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

function submitAddBook()
{

	if(formSending)
	{
		alert('botao bloqueado!');
		return false;
	}

	formSending = true;
	document.getElementById('formSubmit').innerHTML = '<img src="assets/img/loadingW.gif">';

	var form = document.getElementById('form');
	form.onsubmit = function() {

  		var formData = new FormData(form);

  		pdf = document.getElementById('pdf').files[0];
  		img = document.getElementById('img').files[0];
  		title = document.getElementById('title').val;

  		formData.append('file', pdf);
  		formData.append('img', img);
  		formData.append('title', title);

 		 var xhr = new XMLHttpRequest();

 		 xhr.onreadystatechange = function() {
  	  		if (this.readyState == 4 && this.status == 200) {
  	  			document.getElementById('formSubmit').innerHTML = 'Add the book';
  	  			document.getElementById('response').innerHTML = 'Book added';
  	  			formSending = false;
  	  			//loadBooksPage();		
  	  		}
  	  	};

  		xhr.open('POST', host+'/api/v1/add-book', true);
  		xhr.send(formData);

  		return false; 
	}
}


addBtc.addEventListener('click', loadAddBooksPage, false);
seeBtc.addEventListener('click', loadBooksPage, false);


loadBooksPage();