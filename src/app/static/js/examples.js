function Example()
{
    this.init = function() {
        $('#callType').on('change', function() {
            let type = $('#callType').val();
            if (type === 'start') {
                $('#callSource').prop('disabled', false);
                $('#callDestination').prop('disabled', false);
            } else {
                $('#callSource').prop('disabled', true);
                $('#callDestination').prop('disabled', true);
                $('#callSource').val('');
                $('#callDestination').val('');
            }
        });
    };
}

$(document).ready(function(){
    ex = new Example();
    ex.init();
});