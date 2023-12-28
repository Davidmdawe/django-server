
$(document).ready(function () {
    function initializeDataTable(selector) {
        $(selector).DataTable({
            "dom": 'Bfrtip',
            "processing": true,
            "scrollCollapse": true,
            "scrollY": '70vh',
            'scrollX': true,
            "dataType": "json",
            "buttons": [
                {
                    extend: 'collection',
                    text: '☰',
                    buttons: [
                        'copy',
                        'excel',
                        'pdf'
                    ]
                }
            ],
            "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
        });
        $('.dt-buttons').css('float', 'right');
        $('.dt-buttons button').css('background-color', 'white');
        $('.dt-buttons button').css('color', 'black');
    }

    initializeDataTable('#other-vulnerable-populations');
    initializeDataTable('#reached-with-HIV-prevention-programs');
    initializeDataTable('#received-an-HIV-test');
    initializeDataTable('#initiated-oral');
    initializeDataTable('#sex-workers-wh-initiated-oral-antiretroviral-PrEP');
    initializeDataTable('#sex-workers-that-have-received-an-HIV-test');
    initializeDataTable('#sex-workers-reached-with-HIV-prevention');
    initializeDataTable('#cycle');
});