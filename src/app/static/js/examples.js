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
        let subscriber = $('#callSubscriber').val();
        let month = $('#callPMonth').val();
        let year = $('#callPYear').val();

        month = (month.length === 1) ? ('0'+month) : month;

        if (!(utils.isNumber(subscriber) && (subscriber.length > 9))) {
            utils.showWarningMessage('Invalid subscriber number!');
            return;
        }

        if ((year.length === 0) || (month.length === 0)) {
            utils.showWarningMessage('Fill all the fields!');
            return;
        }

        req.getJSONRequest(
            '/phone/'+subscriber+'/bill?period='+month+'/'+year,
            this.sendDataCallBack, null, this
        );

    };
    this.sendDataCallBack = function(data, self) {
        if (data !== 'error') {
            let $tableBody = $('#tableBody');
            $tableBody.html('');

            let content = '';
            for (const key in data) {
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
            utils.showErrorMessage('Something wrong happened. Sorry for that! :(');
        }
    };
}

$(document).ready(function(){
    ex = new Example();
    ex.init();
});