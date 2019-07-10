function format(d) {
    return '<table style="padding-left:50px;">' +
        '<tr>' +
        '<td>Total Price:</td>' +
        '<td>' + d.total_price + ' ₺</td>' +
        '</tr>' +
        '</table>';
}

$(document).ready(function () {
    var table = {
        buildings: null,
        apartments: null,
        rooms: null,
        furnishings: null,
    };
    table['buildings'] = $('#building-table').DataTable({
        searching: true,
        ajax: '/api/buildings/',
        dataSrc: function (d) {
            return {data: d}
        },
        columns: [
            {
                className: 'details-control',
                orderable: false,
                data: null,
                defaultContent: ''
            },
            {data: 'name'},
            {data: 'no'},
            {data: 'address'},
            {
                data: "id",
                orderable: false,
                responsivePriority: -1,
                render: function (a, t, e, n) {
                    return `<a data-type="buildings" data-id="${a}" class="action-button edit" href="/buildings/edit/${a}">Edit</a> 
                        <a data-type="buildings" data-id="${a}" class="action-button delete" href="javascript:">Delete</a>`
                }
            }
        ],
        order: [[1, 'asc']]
    });
    table['apartments'] = $('#apartment-table').DataTable({
        searching: true,
        ajax: '/api/apartments/',
        dataSrc: function (d) {
            return {data: d}
        },
        columns: [
            {
                className: 'details-control',
                orderable: false,
                data: null,
                defaultContent: ''
            },
            {data: 'building'},
            {data: 'apartment_no'},
            {data: 'floor'},
            {data: 'square_meter'},
            {
                data: "id",
                orderable: false,
                responsivePriority: -1,
                render: function (a, t, e, n) {
                    return `<a data-type="apartments" data-id="${a}" class="action-button edit" href="/apartments/edit/${a}">Edit</a> 
                        <a data-type="apartments" data-id="${a}" class="action-button delete" href="javascript:">Delete</a>`
                }
            }
        ],
        order: [[1, 'asc']]
    });
    table['rooms'] = $('#room-table').DataTable({
        searching: true,
        ajax: '/api/rooms/',
        dataSrc: function (d) {
            return {data: d}
        },
        columns: [
            {
                className: 'details-control',
                orderable: false,
                data: null,
                defaultContent: ''
            },
            {data: 'apartment'},
            {data: 'name'},
            {
                data: "id",
                orderable: false,
                responsivePriority: -1,
                render: function (a, t, e, n) {
                    return `<a data-type="rooms" data-id="${a}" class="action-button edit" href="/rooms/edit/${a}">Edit</a>
                        <a data-type="rooms" data-id="${a}" class="action-button delete" href="javascript:">Delete</a>`
                }
            }
        ],
        order: [[1, 'asc']]
    });
    table['furnishings'] = $('#furniture-table').DataTable({
        searching: true,
        ajax: '/api/furnishings/',
        dataSrc: function (d) {
            return {data: d}
        },
        columns: [
            {data: 'room'},
            {data: 'name'},
            {data: 'price'},
            {
                data: "id",
                orderable: false,
                responsivePriority: -1,
                render: function (a, t, e, n) {
                    return `<a data-type="furnishings" data-id="${a}" class="action-button edit" href="/furnishings/edit/${a}">Edit</a>
                        <a data-type="furnishings" data-id="${a}" class="action-button delete" href="javascript:">Delete</a>`
                }
            }
        ],
        order: [[1, 'asc']]
    });
    $(document).on('click', '.delete', function () {
        var id = $(this).data('id');
        var type = $(this).data('type');
        $.ajax({
            url: `/api/${type}/${id}`,
            method: 'DELETE',
            success: function () {
                table[type].ajax.reload();
                alert('Delete Successful!')
            }
        })
    });
    $('.flat-table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var type = $(this).closest('table').data('type');
        var row = table[type].row(tr);

        if (row.child.isShown()) {
            row.child.hide();
            tr.removeClass('shown');
        } else {
            row.child(format(row.data())).show();
            tr.addClass('shown');
        }
    });
});