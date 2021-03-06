

var table_show = {
    info:{
        page:1,
        pageNow:0
    },
    set_inputs:function(){
        var values = getUrlData();

        var form = $('#table_search_form');

        table_show.info.pageNow = 1;
        var perPage = 10;

        if(values != false)
        {
            table_show.info.pageNow = parseInt(values['page']);
            var perPage = parseInt(values['perPage']);
        }


        $('input[name="perPage"]',form).val(perPage);

        var count = parseInt($('.pagination').data('count'));

        if(count < perPage + 1)
        {
            $('.pagination').remove();
        }
        else
        {
            try{
                $('.pagination').pagination({
                count:count,
                className:'table_paginator',
                perPage:perPage});

                if(table_show.info.pageNow != 1)
                {
                    $('.pagination').pagination({
                    action:'update',
                    className:'table_paginator',
                    page:table_show.info.pageNow});
                }
            }
            catch (err)
            {
                alert(err);
            }
        }

    }
};

$(document).on('click','.table_paginator',function(e){
    e.preventDefault();

    if($(this).parent().hasClass('disabled')) return false;
    if($(this).parent().hasClass('active')) return false;

    table_show.info.page = $(this).data('action');
    $('#table_search_form').submit();
});

$(document).on('click','.sortable',function(e){
    e.preventDefault();
    var sort = $(this).data('action');

    var form = $('#table_search_form');

    $('input[name="sort"]',form).val(sort);
    var order = ($(this).data('order') == 'desc')? 'asc' : ($(this).data('order') == undefined)? 'asc' : 'desc' ;
    $('input[name="order"]',form).val(order);

    form.submit();
});

$(document).on('submit','#table_search_form',function(e){

    var form = $(this);

    if(table_show.info.page != 0)
        $('input[name="page"]',form).val(table_show.info.page);


});


$(document).on('click','.open_request_modal',function(e){
    e.preventDefault();

    var action = $(this).data('action');

    $('#myModalLabel').html((action == 1)? "تایید درخواست" : "رد درخواست");

    $('#request_form #action_no').val(action);
    $('#request_form #action_num').val($(this).parents('tr').data('action'));

    $('#request_modal').modal('show');

});





////plugins

jQuery.fn.pagination = function (options) {

    var element = this;

    var pages = 0, start = 0, end = 0, active = 0
        , count = 0, perPage = 0, page = 0, className = 'paginationClick';

    var settings = $.extend({
        count: 0,
        perPage: 0,
        className: 'paginationClick',
        action:'create',
        page:1
    }, options);

    if(settings.action == 'update') {
        count = parseInt(element.data('count'));
        perPage = parseInt(element.data('perPage'));
        pages = parseInt(element.data('pages'));
        start = parseInt(element.data('start'));
        end = parseInt(element.data('end'));
        active = parseInt(element.data('active'));
        className = element.data('className');
        page = parseInt(settings.page);

        var rebuild = false;

        if(page > end)
        {
            do{
                start = end + 1 ;
                end = start + (5 - 1) ;
            }while(page > end);
            if(end > pages) end = pages ;
            rebuild = true;

        }else{
            if(start > page)
            {
                do{
                    end = start - 1 ;
                    start = end - (5 - 1) ;
                }while(page < start);
                if(start <= 0) start = 1 ;
                rebuild = true;
            }

        }

        if(rebuild)
        {
            this.html(_.template($('#pagination').html(), {
                pages: pages,
                start: start,
                end: end,
                active: page,
                className: className
            }));
        }
        else{
            if(active != page)
            {
                $('li.prev a',element).attr('data-action',(page == 1)? 1 : page - 1);
                $('li.next a',element).attr('data-action',(page == pages)? pages : page + 1);

                $('li.disabled',element).removeClass('disabled');
                $('li.active',element).removeClass('active');
                $('a',element).addClass(className);
                $('a:not(.number)[data-action="'+page+'"]',element).removeClass('className').parent().addClass('disabled');
                $('a.number[data-action="'+page+'"]',element).removeClass('className').parent().addClass('active');

            }
        }

        active = page;
    }
    else {


        if (settings.count != 0 && settings.perPage != 0) {
            className = settings.className;
            try{
                count = parseInt(settings.count);
                perPage = parseInt(settings.perPage);

                element.data({'count' : count, 'perPage' : perPage});
                pages = Math.ceil(count / perPage);
                start = 1 ;
                end = (pages > 5)? 5 : pages ;
                active = parseInt(settings.page) ;
                this.html(_.template($('#pagination').html(), {
                    pages: pages,
                    start: start,
                    end: end,
                    active: active,
                    className:className
                }));
            }
            catch (err)
            {
                alert(err);
            }
        }
    }



    this.data({count: count, perPage: perPage, pages: pages, start: start, end: end, active: active, className: className});

};