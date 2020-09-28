var SweetAlert2Demo = function() {

    //== Demos
    var initDemos = function() {
        //== Sweetalert Demo 1
        $('#alert_demo_1').click(function(e) {
            swal('Good job!', {
                buttons: {        			
                    confirm: {
                        className : 'btn btn-success'
                    }
                },
            });
        });

        //== Sweetalert Demo 2
        $('#alert_demo_2').click(function(e) {
            swal("Here's the title!", "...and here's the text!", {
                buttons: {        			
                    confirm: {
                        className : 'btn btn-success'
                    }
                },
            });
        });

        //== Sweetalert Demo 3
        $('.fa-trash').click(function(e) {
            
            swal("Regístro removido", {
                icon : "success",
                buttons: {   

                    Ok: {
                        visible: true,
                        className: 'btn btn-success',
                        
                    },    			

                },
                
            },).then(function(isConfirm){jQuery("#send-delete").submit();});
            
            
        });

        $('#alert_demo_3_2').click(function(e) {
            swal("Good job!", "You clicked the button!", {
                icon : "error",
                buttons: {        			
                    confirm: {
                        className : 'btn btn-danger'
                    }
                },
            });
        });

        $('#alert_demo_3_3').click(function(e) {
            swal("Good job!", "You clicked the button!", {
                icon : "success",
                buttons: {        			
                    confirm: {
                        className : 'btn btn-success'
                    }
                },
            });
        });

        $('#alert_demo_3_4').click(function(e) {
            swal("Good job!", "You clicked the button!", {
                icon : "info",
                buttons: {        			
                    confirm: {
                        className : 'btn btn-info'
                    }
                },
            });
        });

        //== Sweetalert Demo 4
        $('#alert_demo_4').click(function(e) {
            swal({
                title: "Good job!",
                text: "You clicked the button!",
                icon: "success",
                buttons: {
                    confirm: {
                        text: "Confirm Me",
                        value: true,
                        visible: true,
                        className: "btn btn-success",
                        closeModal: true
                    }
                }
            });
        });

        $('').click(function(e){
            swal({
                title: 'Input Something',
                html: '<br><button class="btn btn-success" type="submit" form="send-delete"></button>',
                content: {
                    element: "button",
                    attributes: {
                        placeholder: "Input Something",
                        type: "submit",
                        className: "btn btn-success"
                    },
                },
                buttons: {
           
                    confirm: {
                        className : 'btn btn-success'
                    }
                },
            }).then(
            function() {
                swal("", "You entered : " + $('#input-field').val(), "success");
            }
            );
        });

        $('#alert_demo_6').click(function(e) {
            swal("This modal will disappear soon!", {
                buttons: false,
                timer: 3000,
            });
        });

        $('#alert_demo_7').click(function(e) {
            swal({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                type: 'warning',
                buttons:{
                    confirm: {
                        text : 'Yes, delete it!',
                        className : 'btn btn-success'
                    },
                    cancel: {
                        visible: true,
                        className: 'btn btn-danger'
                    }
                }
            }).then((Delete) => {
                if (Delete) {
                    swal({
                        title: 'Deleted!',
                        text: 'Your file has been deleted.',
                        type: 'success',
                        buttons : {
                            confirm: {
                                className : 'btn btn-success'
                            }
                        }
                    });
                } else {
                    swal.close();
                }
            });
        });

        $('#alert_demo_8').click(function(e) {
            swal({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                type: 'warning',
                buttons:{
                    cancel: {
                        visible: true,
                        text : 'No, cancel!',
                        className: 'btn btn-danger'
                    },        			
                    confirm: {
                        text : 'Yes, delete it!',
                        className : 'btn btn-success'
                    }
                }
            }).then((willDelete) => {
                if (willDelete) {
                    swal("Poof! Your imaginary file has been deleted!", {
                        icon: "success",
                        buttons : {
                            confirm : {
                                className: 'btn btn-success'
                            }
                        }
                    });
                } else {
                    swal("Your imaginary file is safe!", {
                        buttons : {
                            confirm : {
                                className: 'btn btn-success'
                            }
                        }
                    });
                }
            });
        })

    };

    
    
    return {
        //== Init
        init: function() {
            initDemos();
        },
    };
}();

//== Class Initialization
jQuery(document).ready(function() {
    SweetAlert2Demo.init();
});





















