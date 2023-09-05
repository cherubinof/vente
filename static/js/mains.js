$(document).ready(function(){
    $(".filtter-checkbox").on('click', function(){
        var filter_object = {};
        $(".filter-checkbox").each(function(index,ele){
            var filter_value = $(this).val();
            var filter_key = $(this).data('filter');
            console.log(filter_key,filter_value);
            filter_object[filter_key]=Array.from(document.querySelectorAll('input[data-filter='+filter_key+']:checked')).map(function(){
                return ele.value
            });
        });
        $.ajax({
            url:"{% 'filter-data' %}",
            data:filter_object,
            dataType:'json',
            success:function(res){
                $("#filteredProduct").html(res.data);
            }
        });
    });
});