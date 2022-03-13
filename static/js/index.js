$( document ).ready( readyFunction );

function readyFunction() {
    $( "#menu-toggle" ).click( () => {
        $( "#menu" ).toggle();
    })
}