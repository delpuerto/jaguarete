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