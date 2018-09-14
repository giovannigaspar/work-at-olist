/*
    This is my standard javascript "Class" used for default HTTP Requests
    like GET, POST, PUT & DELETE.
*/

function Requests() {
    this.getJSONRequest = function(reqURL, callback, args=null, self=null) {
        let params = '';
        if (args !== null) {
            params = '?' + this.filterParams(args);
        }

        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: reqURL + params,
            cache: false,
            success: function(result) {
                callback(JSON.parse(JSON.stringify(result)), self);
            },
            error: function() {
                callback('error', self);
            }
        });
    }

    this.postJSONRequest = function(reqURL, jsonArgs, callback=null, self=null) {
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: reqURL,
            cache: false,
            data: JSON.stringify(jsonArgs),
            success: function(result) {
                if (callback !== null)
                    callback(JSON.parse(JSON.stringify(result)), jsonArgs, self);
            },
            error: function() {
                if (callback !== null)
                    callback('error', null, self);
            }
        });
    }

    this.putJSONRequest = function(reqURl, args, jsonArgs, callback=null, self=null) {
        let params = '';
        if (args !== null) {
            params = '?' + this.filterParams(args);
        }

        $.ajax({
            type: 'PUT',
            contentType: 'application/json',
            url: reqURl + params,
            cache: false,
            data: JSON.stringify(jsonArgs),
            success: function(result) {
                if (callback !== null)
                    callback(JSON.parse(JSON.stringify(result)), jsonArgs, self);
            },
            error: function() {
                if (callback !== null)
                    callback('error', null, self);
            }
        });
    }

    this.deleteRequest = function(reqURL, args, callback=null, self=null) {
        let params = ((args !== null) ? '?' + this.filterParams(args) : "");
        $.ajax({
            type: 'DELETE',
            url: reqURL + params,
            cache: false,
            success: function(result) {
                if (callback !== null)
                    callback(JSON.parse(JSON.stringify(result)), self);
            },
            error: function() {
                if (callback !== null)
                    callback('error', self);
            }
        });
    }

    this.filterParams = function(args) {
        return 'filter=' + args;
    }

    this.parseNull = function(value) {
        return (value == null ? "" : value);
    }
}

req = new Requests();
