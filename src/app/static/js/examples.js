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

        $('#btnGetBill').on('click', function() {
            ex.onBtnSendDataClick();
        });
    };

    this.onBtnSendDataClick = function() {
        req.getJSONRequest(
            '/phone/99988526423/bill?period=12/2017',
            this.sendDataCallBack, null, this
        );
    };
    this.sendDataCallBack = function(data, self) {
        if (data !== 'error') {
            let $tableBody = $('#tableBody');
            $tableBody.html('');

            let content = '';
            for (const key in data) {
                console.log(data[key]);

                content +=
                    '<tr>' +
                        '<td>' + data[key]['destination'] + '</td>' +
                        '<td>' + data[key]['call_start_date'] + '</td>' +
                        '<td>' + data[key]['call_start_time'] + '</td>' +
                        '<td>' + data[key]['duration'] + '</td>' +
                        '<td>' + data[key]['call_price'].replace('.', ',') + '</td>' +
                    '</tr>';
            }
            $tableBody.append(content);
        } else {
            // ToDo
        }
    };
}

$(document).ready(function(){
    ex = new Example();
    ex.init();
});