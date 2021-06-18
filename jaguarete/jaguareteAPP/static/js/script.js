function acercade(){		

    $.ajax({
        async : true,
        type: "GET",
        url: "./acerca",

        success: function(data) {
            //Cargamos finalmente el contenido deseado
            $('#cuerpo').fadeIn(1000).html(data);						
        },
        
        // código a ejecutar si la petición falla;
        error : function(xhr, status) {
            /// alert('Disculpe, existió un problema');
        }					
    });
}





function Btn_1(mod){
    if(mod==1){
        // window.location.href = "./accounts/login/";
        $.ajax({
            async : true,
            type: "GET",
            url: "./accounts/login/",
    
            success: function(data) {
                //Cargamos finalmente el contenido deseado
                $('#cuerpo').fadeIn(1000).html(data);						
            },
            
            // código a ejecutar si la petición falla;
            error : function(xhr, status) {
                /// alert('Disculpe, existió un problema');
            }					
        });



    }else{
        window.location.href = "./accounts/logout/";
    }
}



function Btn_2(){

    return;
}



function Btn_3(){

    return;
}


