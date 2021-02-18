$(document).ready(function(){
    $("#searchbutton").click(function (){
        search_query=$('#searchbox').val();
        console.log('sucess!');
        // $.get(`/search/${search_query}`);
        window.location.replace(`/search/${search_query}`);
    });
    $("#homebutton").click(function (){
        window.location.replace('/')
    })
  
  }); 