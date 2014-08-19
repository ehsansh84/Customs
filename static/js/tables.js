

var table_show = {
    info:{
        page:1,
        pageNow:0
    },
    set_inputs:function(){
        var values = getUrlData();
        var fields = values['fields'].split('|');

        var form = $('#table_search_form');

        for(var field in fields)
        {
            field = fields[field];
            $('.field[data-action="'+field+'"]',form).attr('checked','checked');

            var label = $('.search_field[data-name="'+field+'"]').data('label');

            $('#main_table thead th[data-action="'+field+'"]').html(label);
        }

        var fieldSearch = values['fieldSearch'];

        if(fieldSearch != undefined)
        {
            fieldSearch = fieldSearch.split('|');

            for(var value in fieldSearch)
            {
                value = fieldSearch[value];
                if(values[value] == undefined) continue;
                $('.search[data-action="'+value+'"]',form).val(values[value]);
            }
        }



        table_show.info.pageNow = parseInt(values['page']);
        var perPage = parseInt(values['perPage']);
        $('input[name="perPage"]',form).val(perPage);
        $('input[name="order"]',form).val(values['order']);
        $('input[name="sort"]',form).val(values['sort']);

        $('th[data-action="'+values['sort']+'"]').attr('data-order',values['order']).append('<i class="fa"></i>');
        if(values['order'] == 'asc')
            $('th[data-action="'+values['sort']+'"] .fa').addClass('fa-caret-down');
        else
            $('th[data-action="'+values['sort']+'"] .fa').addClass('fa-caret-up');

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

    if(!form_validate.validate(form)) {
        e.preventDefault();
        return false;
    }

    var fields = form.data('fields');
    if(fields != "")
    {
        fields = fields.slice(0,-1);
    }
    var fieldSearch = '' ;

    $('.field[data-action]:checked',form).each(function(){
        if(fields != '') fields += '|' ;
        fields += $.trim($(this).data('action'));
    });

    $('.search',form).each(function(){
        var val = $(this).val();
        if($.trim(val) != '')
        {
            var name = $.trim($(this).data('action')) ;
            $(this).attr('name',name);
            if(fieldSearch != '') fieldSearch += '|' ;
            fieldSearch +=  name;
        }
    });

    $('input[name="fields"]',form).val(fields);

    if(table_show.info.page != 0)
        $('input[name="page"]',form).val(table_show.info.page);

    if(fieldSearch != '')
    {
        $('input[data-action="fieldSearch"]',form).val(fieldSearch).attr('name','fieldSearch');
    }
});


/// more in page
$(document).on('click','.edit_object_request',function(e)
{
    e.preventDefault();
    var action = $(this).data('action');
    $('form#edit_request_form #action_no').val(action);
    $('form#edit_request_form #text').val('');
    $('#edit_request_modal').modal('show');
});

$(document).on('click','.edit_request_form_submit',function(e)
{
    e.preventDefault();
    $('form#edit_request_form').submit();
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