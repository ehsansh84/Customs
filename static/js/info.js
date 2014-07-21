//borrow page
$(document).on('click','.user_info_link',function(e){
    e.preventDefault();
    userInfoCall();
});

$(document).on('keydown','.user_info_input',function(e){
    if(e.keyCode == 13){
        e.preventDefault();
        userInfoCall();
    }
});

var loader = {
    start:function(){
        $('body').append('<loader></loader>');
    },
    stop:function(){
        $('body>loader').remove();
    }
}

function userInfoCall(){

    var element = $('.user_info_input');
    var form = element.parents('form') ;
    form_validate.cleanForm(form)

    var val = element.val();
    if($.trim(val) == '')
    {
        form_validate.add_error(element,'ورودی نمی تواند خالی باشد');
        return false;
    }

    if(!form_validate.method.numberCheck(val))
    {
        element.val('');
        form_validate.add_error(element,'ورودی باید عددی باشد');
        return false;
    }

    loader.start();
    $.ajax({
        url:$('.user_info_link').attr('href'),
        cache:false,
        data:{id:val},
        type:'post'
    }).done(function(response){
        loader.stop();
        if(response == '-2')
        {
            form_validate.add_error(element,'آیدی وارد شده اشتباه است');
            return false;
        }

        var user = JSON.parse(response);

        $('input#name',form).val(user.name);
        $('input#family',form).val(user.family);
        $('input#district',form).val(user.district);
        $('input#username',form).val(user.username);
        $('input#password',form).val(user.password);


    }).error(function (xhr, ajaxOptions, thrownError){
        loader.stop();
        console.log('error in call ajax request', xhr.response);
        form_validate.add_error(element,'ارتباط برقرار نشد');
    });
}





$(document).on('click','.shape_info_link',function(e){
    e.preventDefault();
    shapeInfoCall();
});

$(document).on('keydown','.shape_info_input',function(e){
    if(e.keyCode == 13){
        e.preventDefault();
        shapeInfoCall();
    }
});

function shapeInfoCall(){
    var element = $('.shape_info_input');
    var form = element.parents('form') ;
    form_validate.cleanForm(form)

    var val = element.val();
    if($.trim(val) == '')
    {
        form_validate.add_error(element,'ورودی نمی تواند خالی باشد');
        return false;
    }

    if(!form_validate.method.numberCheck(val))
    {
        element.val('');
        form_validate.add_error(element,'ورودی باید عددی باشد');
        return false;
    }
    loader.start();
    $.ajax({
        url:$('.shape_info_link').attr('href'),
        cache:false,
        data:{id:val},
        type:'post'
    }).done(function(response){
        loader.stop();
        if(response == '-2')
        {
            alert('آیدی وارد شده اشتباه است');
            return false;
        }

        var shape = JSON.parse(response);

        $('#explain',form).val(shape.explain);


    }).error(function (xhr, ajaxOptions, thrownError){
        loader.stop();
        console.log('error in call ajax request', xhr.response);
        alert('ارتباط برقرار نشد');
    });
}


//table Ajax page
$(document).on('click','.shape_record_link',function(e){

    try{
        e.preventDefault();
        var val = $(this).data('action');

        loader.start();
        $.ajax({
            url:$('input[name="shape_record_address"]').val(),
            cache:false,
            data:{id:val},
            type:'post'
        }).done(function(response){
            loader.stop();
            if(response == '-2')
            {
                alert('آیدی وارد شده اشتباه است');
                return false;
            }

            $('#shape_record_modal .modal-body').html(response);
            $('#shape_record_modal').modal('show');

        }).error(function (xhr, ajaxOptions, thrownError){
            loader.stop();
            console.log('error in call ajax request', xhr.response);
            alert('ارتباط برقرار نشد');
        });
    }
    catch (err)
    {
        alert(err);
    }
});