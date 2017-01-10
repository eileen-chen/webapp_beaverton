$(document).ready(function(){
    $( "#id_birthday" ).datepicker()


    form_num = 0;
    $("#add-contact-row #add_contact").click(function() {
       console.log('aa');
       form_num ++;
       appendElement = $('#add-contact-row').append("<div class='form-group'><div class='form-inline'><div class='form-group' id='remove-contact-row'><label for='id_form-" + form_num + "-name'>緊急聯絡人姓名: </label><input class='form-control contact-input' id='id_form-" + form_num + "-name' maxlength='30' name='form-" + form_num + "-name' type='text'></div><div class='form-group contact-label'><label for='id_form-" + form_num + "-phone'>緊急聯絡人電話: </label><input class='form-control contact-input' id='id_form-" + form_num + "-phone' maxlength='30' name='form-" + form_num + "-phone' type='text'></div><a href='#' id='remove_contact' class='remove_contact'>刪除</a></div></div>")

      appendElement.children().each(function(){
        //  console.log($(this).find('#remove_contact'));
        $(this).find('#remove_contact').click(function() {
            $(this).parent().parent().remove();
        });
      });


      $('#form_num').val(form_num + 1); 
    });


    $('.link-formset').formset({
        addText: '新增緊急聯絡人',
        deleteText: '刪除'
    });
    // $("#remove-contact-row #remove_contact").click(function() {
    //     $(this).parent().parent().remove();
    // });
   
});

