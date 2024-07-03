
$(document).ready(function () {
  $('#formularioRegistro').submit(function (e) {
    e.preventDefault();

    // Obtener los valores de los campos del formulario
    var nombres = $('#nombres').val();
    var apellido = $('#apellido').val();
    var correo = $('#correo').val();
    var password = $('#password').val();

    // VALIDACION QUE LOS CAMPOS DEL REGISTRO NO ESTEN VACIOS
    if (nombres.trim() === '' || apellido.trim() === '' || correo.trim() === '' || password.trim() === '') {
      alert("Por favor, complete todos los campos.");
      return; // Detener el envío del formulario si hay campos vacíos
    }

    // Crear el objeto de usuario
    var usuario = {
      nombres: nombres,
      apellido: apellido,
      correo: correo,
      password: password
    };

    // Guardar el usuario en localStorage
    localStorage.setItem('usuario', JSON.stringify(usuario));

    // Limpiar los campos del formulario
    $('#nombres').val('');
    $('#apellido').val('');
    $('#correo').val('');
    $('#password').val('');

    window.location.href = "{% url 'login' %}";
  });


  $('#login-button').click(function () {
    var username = $('#username').val();
    var password = $('#password').val();

    // Recuperar el usuario de localStorage
    var usuarioGuardado = JSON.parse(localStorage.getItem('usuario'));

    if (usuarioGuardado && usuarioGuardado.correo === username && usuarioGuardado.password === password) {
      alert("Inicio de sesión exitoso!");
      window.location.href = "{% url 'ventanaPago' %}";
    } else {
      alert("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.");
    }
  });

});

$(document).ready(function () {
  // Array para almacenar los productos en el carrito
  var carrito = [];

  // Función para actualizar el carrito
  function actualizarCarrito() {
    $('#product-image').attr('src', '#');
    $('#product-name').text(' ');
    $('#product-price').text(' ');
    var ultimoProducto = carrito[carrito.length - 1];
    if (ultimoProducto) {
      $('#product-image').attr('src', ultimoProducto.imagen);
      $('#product-name').text(ultimoProducto.nombre);
      $('#product-price').text(ultimoProducto.precio);
    }
  }

  // Cuando se hace clic en "Agregar Carrito"
  $('#cart-button').click(function () {
    var producto = {
      nombre: $('.tituloproU').text(),
      precio: $('.costepro').text(),
      imagen: $('#prodimage').attr('src')
    };
    console.log(producto)

    // Agregar el producto al carrito
    carrito.push(producto);

    // Actualizar el carrito
    actualizarCarrito();

    // Abrir el offcanvas
    var offcanvasElement = document.getElementById('offcanvasRight');
    var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement);
    console.log(producto.nombre)
    bsOffcanvas.show();
  });

  $('#btnpagodirecto').click(function () {

    window.location.href = "{% url 'ventanaPago' %}";

  });

  $('#pagarcarrito').click(function () {

    window.location.href = "{% url 'ventanaPago' %}";

  });
  $(document).ready(function () {
  $('#btnapi').click(function () {

    window.location.href = 'quepjeres.html';

  });
})

$(document).ready(function () {
 //https://dragonball-api.com/api/characters/1
//CREAR FUNCION PARA RECOJER DATOS DE LA API, Y MODIFICAR EL NUMERO PARA CAMBIAR PERSONAJE


});
});










  







