function Utils()
{
    //================================ MODALS ================================//
    this.showErrorMessage = function(message='') {
        let html = `
            <div id="errorModal" class="modal fade" tabindex="-1" role="dialog"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-custom" role="document">
                    <div class="card text-white bg-danger mb-3">
                        <div class="card-header">Ops</div>
                        <div class="card-body">
                            <p id="errorMessage"class="card-text">`+message+`</p>
                        </div>
                        </div>
                    </div>
                </div>
            </div>`;

        $('body').append(html);
        $("#errorModal").modal();
        $("#errorModal").modal('show');
        $('#errorModal').on('hidden.bs.modal', function (e) {
            $(this).remove();
        });
    }

    this.showWarningMessage = function(message='') {
        let html = `
            <div id="warningModal" class="modal fade" tabindex="-1" role="dialog"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-custom" role="document">
                    <div class="card text-white bg-dark mb-3">
                        <div class="card-header">Attention</div>
                        <div class="card-body">
                        <p id="warningMessage"class="card-text">`+message+`</p>
                        </div>
                    </div>
                </div>
                </div>
            </div>`;

        $('body').append(html);
        $("#warningModal").modal();
        $("#warningModal").modal('show');
        $('#warningModal').on('hidden.bs.modal', function (e) {
            $(this).remove();
        });
    }

    this.showSuccessMessage = function(message=''){
        let html = `
            <div id="successModal" class="modal fade" tabindex="-1"
                    role="dialog" aria-hidden="true">
                <div class="modal-dialog modal-dialog-custom" role="document">
                    <div class="card text-white bg-success mb-3">
                        <div class="card-header">Success</div>
                        <div class="card-body">
                        <p id="successMessage"class="card-text">`+message+`</p>
                        </div>
                    </div>
                </div>
                </div>
            </div>`;

        $('body').append(html);
        $("#successModal").modal();
        $("#successModal").modal('show');
        $('#successModal').on('hidden.bs.modal', function (e) {
            $(this).remove();
        });
    }

    this.isNumber = function(str) {
        let isNumber = /^\d+$/.test(str);
        return isNumber;
    }
}

$(document).ready(function(){
    utils = new Utils();
    utils.init();
});