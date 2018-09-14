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
            ex.onBtnGetDataClick();
        });

        $('#btnSendCallInfo').on('click', function() {
            ex.onBtnSendDataClick();
        });
    };

    /*============================= Sending Data =============================*/
    this.onBtnSendDataClick = function() {
        let type = $('#callType').val();
        let callID = $('#callCallID').val();
        let callDate = $('#callTDate').val();
        let callTime = $('#callTTime').val();
        let source = $('#callSource').val();
        let destination = $('#callDestination').val();

        if ((callID.length === 0) || (callDate.length === 0) ||
            (callTime.length === 0)) {
            utils.showWarningMessage('Fill all the fields!');
            return;
        }

        if (type === 'start') {
            if ((source.length < 10) || (destination.length < 10)) {
                utils.showWarningMessage('Fill all the fields!');
                return;
            }
            if (!((utils.isNumber(source)) && (utils.isNumber(destination)))) {
                utils.showWarningMessage(
                    'One or more phone numbers are invalids!');
                return;
            }
        }

        let timestamp = (
            new Date(callDate).toISOString().split('T')[0] +
            'T' + callTime + ':00Z'
        );

        let jsonArgs = {
            "type"          : type,
            "call_id"       : callID,
            "timestamp"     : timestamp,
            "source"        : source,
            "destination"   : destination
        };
        req.postJSONRequest(
            '/call', jsonArgs, this.sendDataCallBack, this);
    };
    this.sendDataCallBack = function(data, jsonArgs, self) {
        if (data !== 'error') {
            utils.showSuccessMessage('Succesfully sent data! ID: '+data['id']);
        } else {
            utils.showErrorMessage('Something wrong happened. Sorry for that! :(');
        }
    };

    /*============================= Getting Data =============================*/
    this.onBtnGetDataClick = function() {
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
            this.getDataCallBack, null, this
        );

    };
    this.getDataCallBack = function(data, self) {
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