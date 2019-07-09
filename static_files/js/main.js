$(document).ready(function () {
    var table = {
        buildings: null,
        apartments: null,
        rooms: null,
        furnishings: null,
    };
    table['rooms'] = $('.flat-table').DataTable({
        searching: true,
        ajax: '/api/rooms/',
        dataSrc: function (d) {
            return {data: d}
        },
        columns: [
            {data: 'apartment'},
            {data: 'name'},
            {
                data: "id",
                responsivePriority: -1,
                render: function (a, t, e, n) {
                    return `<button data-type="rooms" data-id="${a}" class="action-button edit" href="javascript:">Edit</button> 
                        <button data-type="rooms" data-id="${a}" class="action-button delete" href="javascript:">Delete</button>`
                }
            }
        ],
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
});