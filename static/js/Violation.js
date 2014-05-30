
function reset_Violation(){
    $('#form_action').val('add');
    $('#Violation_id').val('');

    $('#Violation_s_date').val('');
    $('#Violation_m_date').val('');
    $('#Violation_fileNo').val('');
    $('#Violation_kootaj').val('');
    $('#Violation_cert_no').val('');
    $('#Violation_s_date_1').val('');
    $('#Violation_s_date_2').val('');
    $('#Violation_policy_1').val('');
    $('#Violation_policy_2').val('');
    $('#Violation_policy_3').val('');
    $('#Violation_policy_4').val('');
    $('#Violation_policy_5').val('');
    $('#Violation_policy_6').val('');
    $('#Violation_policy_7').val('');
    $('#Violation_policy_8').val('');
    $('#Violation_ezharname').val('');
    $('#Violation_person_type').val('');
    $('#Violation_full_name').val('');
    $('#Violation_card_no').val('');
    $('#Violation_code_no').val('');
    $('#Violation_company').val('');
    $('#Violation_ez_full_name').val('');
    $('#Violation_ez_owner').val('');
    $('#Violation_ez_agent').val('');
    $('#Violation_ez_card_no').val('');
    $('#Violation_ez_code_no').val('');
    $('#Violation_tr_full_name').val('');
    $('#Violation_tr_code_no').val('');
    $('#Violation_tr_reg_no').val('');
    $('#Violation_tr_nationality').val('');
    $('#Violation_tr_manager').val('');
    $('#Violation_tr_type').val('');
    $('#Violation_item_name').val('');
    $('#Violation_tariff_no').val('');
    $('#Violation_paid').val('');
    $('#Violation_different').val('');
    $('#Violation_fine').val('');
    $('#Violation_diff_paid').val('');
    $('#Violation_vi_type_1').val('');
    $('#Violation_vi_type_2').val('');
    $('#Violation_vi_type_3').val('');
    $('#Violation_vi_type_4').val('');
    $('#Violation_vi_type_5').val('');
    $('#Violation_vi_type_6').val('');
    $('#Violation_vi_type_7').val('');
    $('#Violation_vi_type_other').val('');
    $('#Violation_stated_tariff').val('');
    $('#Violation_stated_value').val('');
    $('#Violation_stated_weight').val('');
    $('#Violation_deducted_tariff').val('');
    $('#Violation_deducted_value').val('');
    $('#Violation_deducted_weight').val('');
    $('#Violation_law').val('');
    $('#Violation_detector').val('');
    $('#Violation_detector_other').val('');
    $('#Violation_results').val('');
    $('#Violation_commitment').val('');
    $('#Violation_receip_no').val('');
    $('#Violation_details').val('');
    $('#Violation_m_rec_date').val('');
    $('#Violation_s_rec_date').val('');
    $('#Violation_locked').val('');

}

function edit_Violation(id){
    $('#form_action').val('info');
    $('#Violation_id').val(id);
    submit_Violation();
}

function remove_Violation(id){
    $('#form_action').val('delete');
    $('#Violation_id').val(id);

    if (confirm('are you sure')){
        submit_Violation();
    }
}

function submit_Violation(){
    var f_action = $('#form_action').val()
    if (f_action != 'delete' && f_action != 'info'){
        // validation
    }
    var form = $('#form_Violation');
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
                var row = parseInt($('#table_Violation tr:last td:first').html());
                row = (!row)? 1 : row + 1;
                var td ='<tr id="Violation_' + d.ret + '">' +
                        '<td>' + row + '</td>' +
                        '<td id="Violation_s_date_' + d.ret + '">' + d.full_data.s_date + '</td>' +
                        '<td id="Violation_m_date_' + d.ret + '">' + d.full_data.m_date + '</td>' +
                        '<td id="Violation_fileNo_' + d.ret + '">' + d.full_data.fileNo + '</td>' +
                        '<td id="Violation_kootaj_' + d.ret + '">' + d.full_data.kootaj + '</td>' +
                        '<td id="Violation_cert_no_' + d.ret + '">' + d.full_data.cert_no + '</td>' +
                        '<td id="Violation_s_date_1_' + d.ret + '">' + d.full_data.s_date_1 + '</td>' +
                        '<td id="Violation_s_date_2_' + d.ret + '">' + d.full_data.s_date_2 + '</td>' +
                        '<td id="Violation_policy_1_' + d.ret + '">' + d.full_data.policy_1 + '</td>' +
                        '<td id="Violation_policy_2_' + d.ret + '">' + d.full_data.policy_2 + '</td>' +
                        '<td id="Violation_policy_3_' + d.ret + '">' + d.full_data.policy_3 + '</td>' +
                        '<td id="Violation_policy_4_' + d.ret + '">' + d.full_data.policy_4 + '</td>' +
                        '<td id="Violation_policy_5_' + d.ret + '">' + d.full_data.policy_5 + '</td>' +
                        '<td id="Violation_policy_6_' + d.ret + '">' + d.full_data.policy_6 + '</td>' +
                        '<td id="Violation_policy_7_' + d.ret + '">' + d.full_data.policy_7 + '</td>' +
                        '<td id="Violation_policy_8_' + d.ret + '">' + d.full_data.policy_8 + '</td>' +
                        '<td id="Violation_ezharname_' + d.ret + '">' + d.full_data.ezharname + '</td>' +
                        '<td id="Violation_person_type_' + d.ret + '">' + d.full_data.person_type + '</td>' +
                        '<td id="Violation_full_name_' + d.ret + '">' + d.full_data.full_name + '</td>' +
                        '<td id="Violation_card_no_' + d.ret + '">' + d.full_data.card_no + '</td>' +
                        '<td id="Violation_code_no_' + d.ret + '">' + d.full_data.code_no + '</td>' +
                        '<td id="Violation_company_' + d.ret + '">' + d.full_data.company + '</td>' +
                        '<td id="Violation_ez_full_name_' + d.ret + '">' + d.full_data.ez_full_name + '</td>' +
                        '<td id="Violation_ez_owner_' + d.ret + '">' + d.full_data.ez_owner + '</td>' +
                        '<td id="Violation_ez_agent_' + d.ret + '">' + d.full_data.ez_agent + '</td>' +
                        '<td id="Violation_ez_card_no_' + d.ret + '">' + d.full_data.ez_card_no + '</td>' +
                        '<td id="Violation_ez_code_no_' + d.ret + '">' + d.full_data.ez_code_no + '</td>' +
                        '<td id="Violation_tr_full_name_' + d.ret + '">' + d.full_data.tr_full_name + '</td>' +
                        '<td id="Violation_tr_code_no_' + d.ret + '">' + d.full_data.tr_code_no + '</td>' +
                        '<td id="Violation_tr_reg_no_' + d.ret + '">' + d.full_data.tr_reg_no + '</td>' +
                        '<td id="Violation_tr_nationality_' + d.ret + '">' + d.full_data.tr_nationality + '</td>' +
                        '<td id="Violation_tr_manager_' + d.ret + '">' + d.full_data.tr_manager + '</td>' +
                        '<td id="Violation_tr_type_' + d.ret + '">' + d.full_data.tr_type + '</td>' +
                        '<td id="Violation_item_name_' + d.ret + '">' + d.full_data.item_name + '</td>' +
                        '<td id="Violation_tariff_no_' + d.ret + '">' + d.full_data.tariff_no + '</td>' +
                        '<td id="Violation_paid_' + d.ret + '">' + d.full_data.paid + '</td>' +
                        '<td id="Violation_different_' + d.ret + '">' + d.full_data.different + '</td>' +
                        '<td id="Violation_fine_' + d.ret + '">' + d.full_data.fine + '</td>' +
                        '<td id="Violation_diff_paid_' + d.ret + '">' + d.full_data.diff_paid + '</td>' +
                        '<td id="Violation_vi_type_1_' + d.ret + '">' + d.full_data.vi_type_1 + '</td>' +
                        '<td id="Violation_vi_type_2_' + d.ret + '">' + d.full_data.vi_type_2 + '</td>' +
                        '<td id="Violation_vi_type_3_' + d.ret + '">' + d.full_data.vi_type_3 + '</td>' +
                        '<td id="Violation_vi_type_4_' + d.ret + '">' + d.full_data.vi_type_4 + '</td>' +
                        '<td id="Violation_vi_type_5_' + d.ret + '">' + d.full_data.vi_type_5 + '</td>' +
                        '<td id="Violation_vi_type_6_' + d.ret + '">' + d.full_data.vi_type_6 + '</td>' +
                        '<td id="Violation_vi_type_7_' + d.ret + '">' + d.full_data.vi_type_7 + '</td>' +
                        '<td id="Violation_vi_type_other_' + d.ret + '">' + d.full_data.vi_type_other + '</td>' +
                        '<td id="Violation_stated_tariff_' + d.ret + '">' + d.full_data.stated_tariff + '</td>' +
                        '<td id="Violation_stated_value_' + d.ret + '">' + d.full_data.stated_value + '</td>' +
                        '<td id="Violation_stated_weight_' + d.ret + '">' + d.full_data.stated_weight + '</td>' +
                        '<td id="Violation_deducted_tariff_' + d.ret + '">' + d.full_data.deducted_tariff + '</td>' +
                        '<td id="Violation_deducted_value_' + d.ret + '">' + d.full_data.deducted_value + '</td>' +
                        '<td id="Violation_deducted_weight_' + d.ret + '">' + d.full_data.deducted_weight + '</td>' +
                        '<td id="Violation_law_' + d.ret + '">' + d.full_data.law + '</td>' +
                        '<td id="Violation_detector_' + d.ret + '">' + d.full_data.detector + '</td>' +
                        '<td id="Violation_detector_other_' + d.ret + '">' + d.full_data.detector_other + '</td>' +
                        '<td id="Violation_results_' + d.ret + '">' + d.full_data.results + '</td>' +
                        '<td id="Violation_commitment_' + d.ret + '">' + d.full_data.commitment + '</td>' +
                        '<td id="Violation_receip_no_' + d.ret + '">' + d.full_data.receip_no + '</td>' +
                        '<td id="Violation_details_' + d.ret + '">' + d.full_data.details + '</td>' +
                        '<td id="Violation_m_rec_date_' + d.ret + '">' + d.full_data.m_rec_date + '</td>' +
                        '<td id="Violation_s_rec_date_' + d.ret + '">' + d.full_data.s_rec_date + '</td>' +
                        '<td id="Violation_locked_' + d.ret + '">' + d.full_data.locked + '</td>' +

                        '<td>' +
                        '   <span class="btn btn-warning" onclick="edit_Violation(\'' + d.ret + '\')">Edit</span>' +
                        '   <span class="btn btn-danger" onclick="remove_Violation(\'' + d.ret + '\')">Remove</span>' +
                        '</td>' +
                        '</tr>';
                $('#table_Violation tbody').append(td);
                break;
            case 'edit':
                $('#Violation_s_date_' + d.ret).html(d.full_data.s_date);
                $('#Violation_m_date_' + d.ret).html(d.full_data.m_date);
                $('#Violation_fileNo_' + d.ret).html(d.full_data.fileNo);
                $('#Violation_kootaj_' + d.ret).html(d.full_data.kootaj);
                $('#Violation_cert_no_' + d.ret).html(d.full_data.cert_no);
                $('#Violation_s_date_1_' + d.ret).html(d.full_data.s_date_1);
                $('#Violation_s_date_2_' + d.ret).html(d.full_data.s_date_2);
                $('#Violation_policy_1_' + d.ret).html(d.full_data.policy_1);
                $('#Violation_policy_2_' + d.ret).html(d.full_data.policy_2);
                $('#Violation_policy_3_' + d.ret).html(d.full_data.policy_3);
                $('#Violation_policy_4_' + d.ret).html(d.full_data.policy_4);
                $('#Violation_policy_5_' + d.ret).html(d.full_data.policy_5);
                $('#Violation_policy_6_' + d.ret).html(d.full_data.policy_6);
                $('#Violation_policy_7_' + d.ret).html(d.full_data.policy_7);
                $('#Violation_policy_8_' + d.ret).html(d.full_data.policy_8);
                $('#Violation_ezharname_' + d.ret).html(d.full_data.ezharname);
                $('#Violation_person_type_' + d.ret).html(d.full_data.person_type);
                $('#Violation_full_name_' + d.ret).html(d.full_data.full_name);
                $('#Violation_card_no_' + d.ret).html(d.full_data.card_no);
                $('#Violation_code_no_' + d.ret).html(d.full_data.code_no);
                $('#Violation_company_' + d.ret).html(d.full_data.company);
                $('#Violation_ez_full_name_' + d.ret).html(d.full_data.ez_full_name);
                $('#Violation_ez_owner_' + d.ret).html(d.full_data.ez_owner);
                $('#Violation_ez_agent_' + d.ret).html(d.full_data.ez_agent);
                $('#Violation_ez_card_no_' + d.ret).html(d.full_data.ez_card_no);
                $('#Violation_ez_code_no_' + d.ret).html(d.full_data.ez_code_no);
                $('#Violation_tr_full_name_' + d.ret).html(d.full_data.tr_full_name);
                $('#Violation_tr_code_no_' + d.ret).html(d.full_data.tr_code_no);
                $('#Violation_tr_reg_no_' + d.ret).html(d.full_data.tr_reg_no);
                $('#Violation_tr_nationality_' + d.ret).html(d.full_data.tr_nationality);
                $('#Violation_tr_manager_' + d.ret).html(d.full_data.tr_manager);
                $('#Violation_tr_type_' + d.ret).html(d.full_data.tr_type);
                $('#Violation_item_name_' + d.ret).html(d.full_data.item_name);
                $('#Violation_tariff_no_' + d.ret).html(d.full_data.tariff_no);
                $('#Violation_paid_' + d.ret).html(d.full_data.paid);
                $('#Violation_different_' + d.ret).html(d.full_data.different);
                $('#Violation_fine_' + d.ret).html(d.full_data.fine);
                $('#Violation_diff_paid_' + d.ret).html(d.full_data.diff_paid);
                $('#Violation_vi_type_1_' + d.ret).html(d.full_data.vi_type_1);
                $('#Violation_vi_type_2_' + d.ret).html(d.full_data.vi_type_2);
                $('#Violation_vi_type_3_' + d.ret).html(d.full_data.vi_type_3);
                $('#Violation_vi_type_4_' + d.ret).html(d.full_data.vi_type_4);
                $('#Violation_vi_type_5_' + d.ret).html(d.full_data.vi_type_5);
                $('#Violation_vi_type_6_' + d.ret).html(d.full_data.vi_type_6);
                $('#Violation_vi_type_7_' + d.ret).html(d.full_data.vi_type_7);
                $('#Violation_vi_type_other_' + d.ret).html(d.full_data.vi_type_other);
                $('#Violation_stated_tariff_' + d.ret).html(d.full_data.stated_tariff);
                $('#Violation_stated_value_' + d.ret).html(d.full_data.stated_value);
                $('#Violation_stated_weight_' + d.ret).html(d.full_data.stated_weight);
                $('#Violation_deducted_tariff_' + d.ret).html(d.full_data.deducted_tariff);
                $('#Violation_deducted_value_' + d.ret).html(d.full_data.deducted_value);
                $('#Violation_deducted_weight_' + d.ret).html(d.full_data.deducted_weight);
                $('#Violation_law_' + d.ret).html(d.full_data.law);
                $('#Violation_detector_' + d.ret).html(d.full_data.detector);
                $('#Violation_detector_other_' + d.ret).html(d.full_data.detector_other);
                $('#Violation_results_' + d.ret).html(d.full_data.results);
                $('#Violation_commitment_' + d.ret).html(d.full_data.commitment);
                $('#Violation_receip_no_' + d.ret).html(d.full_data.receip_no);
                $('#Violation_details_' + d.ret).html(d.full_data.details);
                $('#Violation_m_rec_date_' + d.ret).html(d.full_data.m_rec_date);
                $('#Violation_s_rec_date_' + d.ret).html(d.full_data.s_rec_date);
                $('#Violation_locked_' + d.ret).html(d.full_data.locked);

                break;
            case 'delete':
                $('tr#Violation_' + d.ret).remove();
                var i = 1;
                $('#table_Violation tbody tr').each(function(){
                    $('td:nth-child(1)',this).html(i++);
                });
                break;
			case 'info':
                $('#form_action').val('edit');
                $('#Violation_id').val(d.ret);
				
                $('#Violation_s_date').val(d.full_data.s_date);
                $('#Violation_m_date').val(d.full_data.m_date);
                $('#Violation_fileNo').val(d.full_data.fileNo);
                $('#Violation_kootaj').val(d.full_data.kootaj);
                $('#Violation_cert_no').val(d.full_data.cert_no);
                $('#Violation_s_date_1').val(d.full_data.s_date_1);
                $('#Violation_s_date_2').val(d.full_data.s_date_2);
                $('#Violation_policy_1').val(d.full_data.policy_1);
                $('#Violation_policy_2').val(d.full_data.policy_2);
                $('#Violation_policy_3').val(d.full_data.policy_3);
                $('#Violation_policy_4').val(d.full_data.policy_4);
                $('#Violation_policy_5').val(d.full_data.policy_5);
                $('#Violation_policy_6').val(d.full_data.policy_6);
                $('#Violation_policy_7').val(d.full_data.policy_7);
                $('#Violation_policy_8').val(d.full_data.policy_8);
                $('#Violation_ezharname').val(d.full_data.ezharname);
                $('#Violation_person_type').val(d.full_data.person_type);
                $('#Violation_full_name').val(d.full_data.full_name);
                $('#Violation_card_no').val(d.full_data.card_no);
                $('#Violation_code_no').val(d.full_data.code_no);
                $('#Violation_company').val(d.full_data.company);
                $('#Violation_ez_full_name').val(d.full_data.ez_full_name);
                $('#Violation_ez_owner').val(d.full_data.ez_owner);
                $('#Violation_ez_agent').val(d.full_data.ez_agent);
                $('#Violation_ez_card_no').val(d.full_data.ez_card_no);
                $('#Violation_ez_code_no').val(d.full_data.ez_code_no);
                $('#Violation_tr_full_name').val(d.full_data.tr_full_name);
                $('#Violation_tr_code_no').val(d.full_data.tr_code_no);
                $('#Violation_tr_reg_no').val(d.full_data.tr_reg_no);
                $('#Violation_tr_nationality').val(d.full_data.tr_nationality);
                $('#Violation_tr_manager').val(d.full_data.tr_manager);
                $('#Violation_tr_type').val(d.full_data.tr_type);
                $('#Violation_item_name').val(d.full_data.item_name);
                $('#Violation_tariff_no').val(d.full_data.tariff_no);
                $('#Violation_paid').val(d.full_data.paid);
                $('#Violation_different').val(d.full_data.different);
                $('#Violation_fine').val(d.full_data.fine);
                $('#Violation_diff_paid').val(d.full_data.diff_paid);
                $('#Violation_vi_type_1').val(d.full_data.vi_type_1);
                $('#Violation_vi_type_2').val(d.full_data.vi_type_2);
                $('#Violation_vi_type_3').val(d.full_data.vi_type_3);
                $('#Violation_vi_type_4').val(d.full_data.vi_type_4);
                $('#Violation_vi_type_5').val(d.full_data.vi_type_5);
                $('#Violation_vi_type_6').val(d.full_data.vi_type_6);
                $('#Violation_vi_type_7').val(d.full_data.vi_type_7);
                $('#Violation_vi_type_other').val(d.full_data.vi_type_other);
                $('#Violation_stated_tariff').val(d.full_data.stated_tariff);
                $('#Violation_stated_value').val(d.full_data.stated_value);
                $('#Violation_stated_weight').val(d.full_data.stated_weight);
                $('#Violation_deducted_tariff').val(d.full_data.deducted_tariff);
                $('#Violation_deducted_value').val(d.full_data.deducted_value);
                $('#Violation_deducted_weight').val(d.full_data.deducted_weight);
                $('#Violation_law').val(d.full_data.law);
                $('#Violation_detector').val(d.full_data.detector);
                $('#Violation_detector_other').val(d.full_data.detector_other);
                $('#Violation_results').val(d.full_data.results);
                $('#Violation_commitment').val(d.full_data.commitment);
                $('#Violation_receip_no').val(d.full_data.receip_no);
                $('#Violation_details').val(d.full_data.details);
                $('#Violation_m_rec_date').val(d.full_data.m_rec_date);
                $('#Violation_s_rec_date').val(d.full_data.s_rec_date);
                $('#Violation_locked').val(d.full_data.locked);

                break;
        }
    }).fail(function(){
        alert('Error')
    });
    reset_Violation();
}