var productListApiUrl='http://127.0.0.1:5000/getProducts'
var productModal = $("#productModal");
    $(function () {

        //JSON data by API call
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, product) {
                    table += '<tr data-id="'+ product.product_id +'" data-name="'+ product.name +'" data-unit="'+ product.uom_id +'" data-price="'+ product.price_per_unit +'">' +
                        '<td>'+ product.name +'</td>'+
                        '<td>'+ product.uom_name +'</td>'+
                        '<td>'+ product.price_per_unit +'</td>'+
                        '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });
// window.onload = function () {
//     // Get the <tbody> of the table
//     const tableBody = document.querySelector("tbody");
  
//     // Fetch data from the API
//     fetch("http://127.0.0.1:5000/getProducts")
//       .then(response => response.json())
//       .then(products => {
//         // Clear the table before adding new data
//         tableBody.innerHTML = "";
  
//         // Go through each product and create a row
//         products.forEach(product => {
//           const row = document.createElement("tr");
  
//           row.innerHTML = `
//             <td>${product.name}</td>
//             <td>${product.uom_name}</td>
//             <td>₹${product.price_per_unit}</td>
//             <td><button class="action-btn">Delete</button></td>
//           `;
  
//           tableBody.appendChild(row);
//         });
//       })
//       .catch(error => {
//         console.log("Error loading products:", error);
//         tableBody.innerHTML = `<tr><td colspan="4">Failed to load products</td></tr>`;
//       });
//   };
  