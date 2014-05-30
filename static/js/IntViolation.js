
function reset_IntViolation(){
    $('#form_action').val('add');
    $('#IntViolation_id').val('');

    $('#IntViolation_kootaj').val('');
    $('#IntViolation_cert_no').val('');
    $('#IntViolation_s_date').val('');
    $('#IntViolation_m_date').val('');
    $('#IntViolation_int_cert_no').val('');
    $('#IntViolation_radif_marzi').val('');
    $('#IntViolation_s_entry_date').val('');
    $('#IntViolation_m_entry_date').val('');
    $('#IntViolation_karne_tir_no').val('');
    $('#IntViolation_ezhar_1').val('');
    $('#IntViolation_ezhar_2').val('');
    $('#IntViolation_ezhar_3').val('');
    $('#IntViolation_ezhar_4').val('');
    $('#IntViolation_person_type').val('');
    $('#IntViolation_full_name').val('');
    $('#IntViolation_card_no').val('');
    $('#IntViolation_code_no').val('');
    $('#IntViolation_dest_address').val('');
    $('#IntViolation_good_bame').val('');
    $('#IntViolation_net_weight').val('');
    $('#IntViolation_weight').val('');
    $('#IntViolation_input_tariff').val('');
    $('#IntViolation_good_count').val('');
    $('#IntViolation_price').val('');
    $('#IntViolation_truck_no').val('');
    $('#IntViolation_driver_name').val('');
    $('#IntViolation_chasis_no').val('');
    $('#IntViolation_trailer_no').val('');
    $('#IntViolation_tranian_truck').val('');
    $('#IntViolation_truck_address').val('');
    $('#IntViolation_truck_type').val('');
    $('#IntViolation_vi_type_1').val('');
    $('#IntViolation_vi_type_2').val('');
    $('#IntViolation_vi_type_3').val('');
    $('#IntViolation_vi_type_4').val('');
    $('#IntViolation_vi_type_5').val('');
    $('#IntViolation_vi_type_6').val('');
    $('#IntViolation_vi_type_7').val('');
    $('#IntViolation_detector').val('');
    $('#IntViolation_detector_other').val('');
    $('#IntViolation_fine_receipt_no').val('');
    $('#IntViolation_fine_price').val('');
    $('#IntViolation_final_result').val('');
    $('#IntViolation_details').val('');
    $('#IntViolation_m_rec_date').val('');
    $('#IntViolation_s_rec_date').val('');
    $('#IntViolation_locked').val('');

}

function edit_IntViolation(id){
    $('#form_action').val('info');
    $('#IntViolation_id').val(id);
    submit_IntViolation();
}

function remove_IntViolation(id){
    $('#form_action').val('delete');
    $('#IntViolation_id').val(id);

    if (confirm('are you sure')){
        submit_IntViolation();
    }
}

function submit_IntViolation(){
    var f_action = $('#form_action').val()
    if (f_action != 'delete' && f_action != 'info'){
        // validation
    }
    var form = $('#form_IntViolation');
    $.ajax({
        url: '',
        type: 'POST',
        data: form.serialize(),
        cache: false
    }).done(function(responce){
        var d = JSON.parse(responce);
        if (d.ret == 'error' || d.action == 'error'){
            alert('Can not complete action. ' + d.ret);
            return;
        }
        switch (d.action){
            case 'add':
                var row = parseInt($('#table_IntViolation tr:last td:first').html());
                row = (!row)? 1 : row + 1;
                var td ='<tr id="IntViolation_' + d.ret + '">' +
                        '<td>' + row + '</td>' +
                        '<td id="IntViolation_kootaj_' + d.ret + '">' + d.full_data.kootaj + '</td>' +
                        '<td id="IntViolation_cert_no_' + d.ret + '">' + d.full_data.cert_no + '</td>' +
                        '<td id="IntViolation_s_date_' + d.ret + '">' + d.full_data.s_date + '</td>' +
                        '<td id="IntViolation_m_date_' + d.ret + '">' + d.full_data.m_date + '</td>' +
                        '<td id="IntViolation_int_cert_no_' + d.ret + '">' + d.full_data.int_cert_no + '</td>' +
                        '<td id="IntViolation_radif_marzi_' + d.ret + '">' + d.full_data.radif_marzi + '</td>' +
                        '<td id="IntViolation_s_entry_date_' + d.ret + '">' + d.full_data.s_entry_date + '</td>' +
                        '<td id="IntViolation_m_entry_date_' + d.ret + '">' + d.full_data.m_entry_date + '</td>' +
                        '<td id="IntViolation_karne_tir_no_' + d.ret + '">' + d.full_data.karne_tir_no + '</td>' +
                        '<td id="IntViolation_ezhar_1_' + d.ret + '">' + d.full_data.ezhar_1 + '</td>' +
                        '<td id="IntViolation_ezhar_2_' + d.ret + '">' + d.full_data.ezhar_2 + '</td>' +
                        '<td id="IntViolation_ezhar_3_' + d.ret + '">' + d.full_data.ezhar_3 + '</td>' +
                        '<td id="IntViolation_ezhar_4_' + d.ret + '">' + d.full_data.ezhar_4 + '</td>' +
                        '<td id="IntViolation_person_type_' + d.ret + '">' + d.full_data.person_type + '</td>' +
                        '<td id="IntViolation_full_name_' + d.ret + '">' + d.full_data.full_name + '</td>' +
                        '<td id="IntViolation_card_no_' + d.ret + '">' + d.full_data.card_no + '</td>' +
                        '<td id="IntViolation_code_no_' + d.ret + '">' + d.full_data.code_no + '</td>' +
                        '<td id="IntViolation_dest_address_' + d.ret + '">' + d.full_data.dest_address + '</td>' +
                        '<td id="IntViolation_good_bame_' + d.ret + '">' + d.full_data.good_bame + '</td>' +
                        '<td id="IntViolation_net_weight_' + d.ret + '">' + d.full_data.net_weight + '</td>' +
                        '<td id="IntViolation_weight_' + d.ret + '">' + d.full_data.weight + '</td>' +
                        '<td id="IntViolation_input_tariff_' + d.ret + '">' + d.full_data.input_tariff + '</td>' +
                        '<td id="IntViolation_good_count_' + d.ret + '">' + d.full_data.good_count + '</td>' +
                        '<td id="IntViolation_price_' + d.ret + '">' + d.full_data.price + '</td>' +
                        '<td id="IntViolation_truck_no_' + d.ret + '">' + d.full_data.truck_no + '</td>' +
                        '<td id="IntViolation_driver_name_' + d.ret + '">' + d.full_data.driver_name + '</td>' +
                        '<td id="IntViolation_chasis_no_' + d.ret + '">' + d.full_data.chasis_no + '</td>' +
                        '<td id="IntViolation_trailer_no_' + d.ret + '">' + d.full_data.trailer_no + '</td>' +
                        '<td id="IntViolation_tranian_truck_' + d.ret + '">' + d.full_data.tranian_truck + '</td>' +
                        '<td id="IntViolation_truck_address_' + d.ret + '">' + d.full_data.truck_address + '</td>' +
                        '<td id="IntViolation_truck_type_' + d.ret + '">' + d.full_data.truck_type + '</td>' +
                        '<td id="IntViolation_vi_type_1_' + d.ret + '">' + d.full_data.vi_type_1 + '</td>' +
                        '<td id="IntViolation_vi_type_2_' + d.ret + '">' + d.full_data.vi_type_2 + '</td>' +
                        '<td id="IntViolation_vi_type_3_' + d.ret + '">' + d.full_data.vi_type_3 + '</td>' +
                        '<td id="IntViolation_vi_type_4_' + d.ret + '">' + d.full_data.vi_type_4 + '</td>' +
                        '<td id="IntViolation_vi_type_5_' + d.ret + '">' + d.full_data.vi_type_5 + '</td>' +
                        '<td id="IntViolation_vi_type_6_' + d.ret + '">' + d.full_data.vi_type_6 + '</td>' +
                        '<td id="IntViolation_vi_type_7_' + d.ret + '">' + d.full_data.vi_type_7 + '</td>' +
                        '<td id="IntViolation_detector_' + d.ret + '">' + d.full_data.detector + '</td>' +
                        '<td id="IntViolation_detector_other_' + d.ret + '">' + d.full_data.detector_other + '</td>' +
                        '<td id="IntViolation_fine_receipt_no_' + d.ret + '">' + d.full_data.fine_receipt_no + '</td>' +
                        '<td id="IntViolation_fine_price_' + d.ret + '">' + d.full_data.fine_price + '</td>' +
                        '<td id="IntViolation_final_result_' + d.ret + '">' + d.full_data.final_result + '</td>' +
                        '<td id="IntViolation_details_' + d.ret + '">' + d.full_data.details + '</td>' +
                        '<td id="IntViolation_m_rec_date_' + d.ret + '">' + d.full_data.m_rec_date + '</td>' +
                        '<td id="IntViolation_s_rec_date_' + d.ret + '">' + d.full_data.s_rec_date + '</td>' +
                        '<td id="IntViolation_locked_' + d.ret + '">' + d.full_data.locked + '</td>' +

                        '<td>' +
                        '   <span class="btn btn-warning" onclick="edit_IntViolation(\'' + d.ret + '\')">Edit</span>' +
                        '   <span class="btn btn-danger" onclick="remove_IntViolation(\'' + d.ret + '\')">Remove</span>' +
                        '</td>' +
                        '</tr>';
                $('#table_IntViolation tbody').append(td);
                break;
            case 'edit':
                $('#IntViolation_kootaj_' + d.ret).html(d.full_data.kootaj);
                $('#IntViolation_cert_no_' + d.ret).html(d.full_data.cert_no);
                $('#IntViolation_s_date_' + d.ret).html(d.full_data.s_date);
                $('#IntViolation_m_date_' + d.ret).html(d.full_data.m_date);
                $('#IntViolation_int_cert_no_' + d.ret).html(d.full_data.int_cert_no);
                $('#IntViolation_radif_marzi_' + d.ret).html(d.full_data.radif_marzi);
                $('#IntViolation_s_entry_date_' + d.ret).html(d.full_data.s_entry_date);
                $('#IntViolation_m_entry_date_' + d.ret).html(d.full_data.m_entry_date);
                $('#IntViolation_karne_tir_no_' + d.ret).html(d.full_data.karne_tir_no);
                $('#IntViolation_ezhar_1_' + d.ret).html(d.full_data.ezhar_1);
                $('#IntViolation_ezhar_2_' + d.ret).html(d.full_data.ezhar_2);
                $('#IntViolation_ezhar_3_' + d.ret).html(d.full_data.ezhar_3);
                $('#IntViolation_ezhar_4_' + d.ret).html(d.full_data.ezhar_4);
                $('#IntViolation_person_type_' + d.ret).html(d.full_data.person_type);
                $('#IntViolation_full_name_' + d.ret).html(d.full_data.full_name);
                $('#IntViolation_card_no_' + d.ret).html(d.full_data.card_no);
                $('#IntViolation_code_no_' + d.ret).html(d.full_data.code_no);
                $('#IntViolation_dest_address_' + d.ret).html(d.full_data.dest_address);
                $('#IntViolation_good_bame_' + d.ret).html(d.full_data.good_bame);
                $('#IntViolation_net_weight_' + d.ret).html(d.full_data.net_weight);
                $('#IntViolation_weight_' + d.ret).html(d.full_data.weight);
                $('#IntViolation_input_tariff_' + d.ret).html(d.full_data.input_tariff);
                $('#IntViolation_good_count_' + d.ret).html(d.full_data.good_count);
                $('#IntViolation_price_' + d.ret).html(d.full_data.price);
                $('#IntViolation_truck_no_' + d.ret).html(d.full_data.truck_no);
                $('#IntViolation_driver_name_' + d.ret).html(d.full_data.driver_name);
                $('#IntViolation_chasis_no_' + d.ret).html(d.full_data.chasis_no);
                $('#IntViolation_trailer_no_' + d.ret).html(d.full_data.trailer_no);
                $('#IntViolation_tranian_truck_' + d.ret).html(d.full_data.tranian_truck);
                $('#IntViolation_truck_address_' + d.ret).html(d.full_data.truck_address);
                $('#IntViolation_truck_type_' + d.ret).html(d.full_data.truck_type);
                $('#IntViolation_vi_type_1_' + d.ret).html(d.full_data.vi_type_1);
                $('#IntViolation_vi_type_2_' + d.ret).html(d.full_data.vi_type_2);
                $('#IntViolation_vi_type_3_' + d.ret).html(d.full_data.vi_type_3);
                $('#IntViolation_vi_type_4_' + d.ret).html(d.full_data.vi_type_4);
                $('#IntViolation_vi_type_5_' + d.ret).html(d.full_data.vi_type_5);
                $('#IntViolation_vi_type_6_' + d.ret).html(d.full_data.vi_type_6);
                $('#IntViolation_vi_type_7_' + d.ret).html(d.full_data.vi_type_7);
                $('#IntViolation_detector_' + d.ret).html(d.full_data.detector);
                $('#IntViolation_detector_other_' + d.ret).html(d.full_data.detector_other);
                $('#IntViolation_fine_receipt_no_' + d.ret).html(d.full_data.fine_receipt_no);
                $('#IntViolation_fine_price_' + d.ret).html(d.full_data.fine_price);
                $('#IntViolation_final_result_' + d.ret).html(d.full_data.final_result);
                $('#IntViolation_details_' + d.ret).html(d.full_data.details);
                $('#IntViolation_m_rec_date_' + d.ret).html(d.full_data.m_rec_date);
                $('#IntViolation_s_rec_date_' + d.ret).html(d.full_data.s_rec_date);
                $('#IntViolation_locked_' + d.ret).html(d.full_data.locked);

                break;
            case 'delete':
                $('tr#IntViolation_' + d.ret).remove();
                var i = 1;
                $('#table_IntViolation tbody tr').each(function(){
                    $('td:nth-child(1)',this).html(i++);
                });
                break;
			case 'info':
                $('#form_action').val('edit');
                $('#IntViolation_id').val(d.ret);
				
                $('#IntViolation_kootaj').val(d.full_data.kootaj);
                $('#IntViolation_cert_no').val(d.full_data.cert_no);
                $('#IntViolation_s_date').val(d.full_data.s_date);
                $('#IntViolation_m_date').val(d.full_data.m_date);
                $('#IntViolation_int_cert_no').val(d.full_data.int_cert_no);
                $('#IntViolation_radif_marzi').val(d.full_data.radif_marzi);
                $('#IntViolation_s_entry_date').val(d.full_data.s_entry_date);
                $('#IntViolation_m_entry_date').val(d.full_data.m_entry_date);
                $('#IntViolation_karne_tir_no').val(d.full_data.karne_tir_no);
                $('#IntViolation_ezhar_1').val(d.full_data.ezhar_1);
                $('#IntViolation_ezhar_2').val(d.full_data.ezhar_2);
                $('#IntViolation_ezhar_3').val(d.full_data.ezhar_3);
                $('#IntViolation_ezhar_4').val(d.full_data.ezhar_4);
                $('#IntViolation_person_type').val(d.full_data.person_type);
                $('#IntViolation_full_name').val(d.full_data.full_name);
                $('#IntViolation_card_no').val(d.full_data.card_no);
                $('#IntViolation_code_no').val(d.full_data.code_no);
                $('#IntViolation_dest_address').val(d.full_data.dest_address);
                $('#IntViolation_good_bame').val(d.full_data.good_bame);
                $('#IntViolation_net_weight').val(d.full_data.net_weight);
                $('#IntViolation_weight').val(d.full_data.weight);
                $('#IntViolation_input_tariff').val(d.full_data.input_tariff);
                $('#IntViolation_good_count').val(d.full_data.good_count);
                $('#IntViolation_price').val(d.full_data.price);
                $('#IntViolation_truck_no').val(d.full_data.truck_no);
                $('#IntViolation_driver_name').val(d.full_data.driver_name);
                $('#IntViolation_chasis_no').val(d.full_data.chasis_no);
                $('#IntViolation_trailer_no').val(d.full_data.trailer_no);
                $('#IntViolation_tranian_truck').val(d.full_data.tranian_truck);
                $('#IntViolation_truck_address').val(d.full_data.truck_address);
                $('#IntViolation_truck_type').val(d.full_data.truck_type);
                $('#IntViolation_vi_type_1').val(d.full_data.vi_type_1);
                $('#IntViolation_vi_type_2').val(d.full_data.vi_type_2);
                $('#IntViolation_vi_type_3').val(d.full_data.vi_type_3);
                $('#IntViolation_vi_type_4').val(d.full_data.vi_type_4);
                $('#IntViolation_vi_type_5').val(d.full_data.vi_type_5);
                $('#IntViolation_vi_type_6').val(d.full_data.vi_type_6);
                $('#IntViolation_vi_type_7').val(d.full_data.vi_type_7);
                $('#IntViolation_detector').val(d.full_data.detector);
                $('#IntViolation_detector_other').val(d.full_data.detector_other);
                $('#IntViolation_fine_receipt_no').val(d.full_data.fine_receipt_no);
                $('#IntViolation_fine_price').val(d.full_data.fine_price);
                $('#IntViolation_final_result').val(d.full_data.final_result);
                $('#IntViolation_details').val(d.full_data.details);
                $('#IntViolation_m_rec_date').val(d.full_data.m_rec_date);
                $('#IntViolation_s_rec_date').val(d.full_data.s_rec_date);
                $('#IntViolation_locked').val(d.full_data.locked);

                break;
        }
    }).fail(function(){
        alert('Error')
    });
    reset_IntViolation();
}