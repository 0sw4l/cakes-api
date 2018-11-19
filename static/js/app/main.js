var app = app || {};

app.source = $("#document-template").html();

app.hideDomElement = function (selector) {
    $(selector).addClass('hidden');
};

app.showDomElement = function (selector) {
    $(selector).removeClass('hidden');
}
app.mainView = Backbone.View.extend({
    el: '#app',

    events: {
        'click .buy': 'showAlertBuy',
        'submit #client_form': 'sendDataClient',
        'click .delete': 'removeProduct',
        'click #enviar_pedido': 'confirmar'
    },

    initialize: function () {
        if (localStorage.getItem('client_id') && localStorage.getItem('pedido_id')) {
            app.showDomElement('#shop, .pedido');
            app.hideDomElement('#customer_data');
            this.loadData();
        }

    },

    sendDataClient: function (e) {
        e.preventDefault();
        $.ajax({
            url: '/api/app/enviar-cliente/',
            method: 'POST',
            data: {
                cedula: $('#cc').val(),
                nombre: $('#name').val(),
                telefono: $('#phone').val(),
                correo: $('#mail').val(),
                direccion: $('#address').val()
            },
            success: function (data) {
                localStorage.setItem('client_id', data.id);
                app.showDomElement('#shop, .pedido');
                app.hideDomElement('#customer_data');
                swal("Excelente", "datos del cliente enviados!", "success");

                $.post("/api/app/viewsets/pedidos/", {cliente_id: data.id}, function (data, status) {
                    localStorage.setItem('pedido_id', data.id);
                });
            }
        });

    },

    showAlertBuy: function (e) {
        var id = $(e.currentTarget).attr('data-id-product');
        var name = $(e.currentTarget).attr('data-name-product');
        var price = $(e.currentTarget).attr('data-price-product');
        var self = this;
        swal({
            title: "Comprar " + name + "",
            text: "Desea comprar el producto " + name + " X $" + price + " C/U",
            type: "input",
            showCancelButton: true,
            closeOnConfirm: false,
            inputPlaceholder: "Ejemplo: 5"
        }, function (inputValue) {
            var q = parseInt(inputValue);
            if (isNaN(q)) {
                swal.showInputError("Error, solo puedes ingresar numeros!");
                return false
            } else {
                if (q <= 0)
                    swal.showInputError("Error, solo puedes ingresar numeros positivos!");
                else
                    self.sendItemShop(id, q);
            }

        });
    },

    sendItemShop: function (id, cantidad) {
        var last_pedido = localStorage.getItem('pedido_id');
        $.post("/api/app/viewsets/pedidos/" + last_pedido + "/add_product/", {
            product_id: id,
            cantidad: cantidad
        }, function (data, status) {
            swal("Excelente", "producto agregado con exito!", "success")
        });
    },


    loadData: function () {
        $.getJSON('/api/app/viewsets/pedidos/'+localStorage.getItem('pedido_id')+'/items/', function( data ) {
            var template = Handlebars.compile(app.source);
            var html = template(data.productos);
            if (data.productos.length === 0)
                app.hideDomElement('#enviar_pedido');
            else
                app.showDomElement('#enviar_pedido');
            $('#DocumentResults').html(html);
            $('#total_pedido').text('$ '+data.total);
        });
    },

    removeProduct: function (e) {
         var producto = $(e.currentTarget).attr('data-id-producto');
         var pedido = $(e.currentTarget).attr('data-id-pedido');
         var self = this;
         $.post("/api/app/viewsets/pedidos/" + pedido + "/remove_product/", {
            product_id: producto
        }, function (data, status) {
             self.loadData();
        });
    },

    confirmar: function (e) {
        var last_pedido = localStorage.getItem('pedido_id');
        $.post("/api/app/viewsets/pedidos/" + last_pedido + "/send/", {}, function (data, status) {
            swal("Excelente", "el pedido fue confirmado con exito", "success");
            localStorage.clear();
            window.location.href = '/';
        });
    }


});
