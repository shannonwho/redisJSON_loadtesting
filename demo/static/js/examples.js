$(document).ready(function(){
    $('#get-examples').click( ()=>{getExamples()})
    $('#get-example').click( ()=>{getExample()});
    $('#get-example-names').click( ()=>{getExampleNames()});
    // $('#post-example').click( ()=>{postExample()});
    $('#post-example').click( ()=> {postExample()});

});

async function getExamples() {
    $('#get-examples-response-time').html('');
    $('#get-examples-response-body').html('');
    const id= $('#get-examples-id').val();
    try {
    const response = await axios.get('/api/v1/keys');
    $('#get-examples-response-time').html(response.duration.toString());
    $('#get-examples-response-body').html( JSON.stringify( response.data, null, "\t" ) );
    }
    catch(error){
    console.error(error);
    }
}

async function getExample() {
    $('#get-example-response-time').html('');
    $('#get-example-response-body').html('');
    const id= $('#get-example-id').val();
    try {
    const response = await axios.get('/api/v1/examples/' +  id );
    $('#get-example-response-time').html(response.duration.toString());
    $('#get-example-response-body').html( JSON.stringify( response.data, null, "\t" ) );
    }
    catch(error){
    console.error(error);
    }
}


async function getExampleNames() {
    $('#get-example-names-response-time').html('');
    $('#get-example-names-response-body').html('');
    const id= $('#get-example-name').val();
    const field = $('#get-example-field').val();
    try {
    const response = await axios.get('/api/v1/examples/'+ id + '/' + field);
    $('#get-example-names-response-time').html(response.duration.toString());
    $('#get-example-names-response-body').html( JSON.stringify( response.data, null, "\t" ) );
    }
    catch(error){
    console.error(error);
    }
}
async function postExample() {
    console.log("POST EXAMPLE!")
    $('#add-example-response-time').html('');
    $('#add-example-response-body').html('');
    $('#post-example-name-error').removeClass('visible');
    $('#post-example-location-error').removeClass('visible');
    $('#post-example-name-error').addClass('invisible');
    $('#post-example-location-error').addClass('invisible');
    let realID = $('#post-example-id').val();
    let name = $('#post-example-name').val();
    let location = $('#post-example-location').val();
    let idPass = realID !== (null || '')
    let namePass = name.length < 1000 && name !== (null || '');
    if (namePass && idPass){
        try {
            const response = await axios({
                method: 'post',
                url: '/api/v1/examples',
                headers: {'Content-Type': 'application/json' },
                data: {id:realID, name:name}
            });

            $('#post-example-response-time').html(response.duration.toString());
            $('#post-example-response-body').html(JSON.stringify(response.data, null, "\t" ) );
        } catch (error) {
            console.error(error);
        }
    }
}


// async function postExample() {
//     $('#put-product-sql-code').html('')
//     $('#put-product-response-time').html('');
//     $('#put-product-response-body').html('');
//   const newQuantity = parseInt($('#put-product-quantity').val(), 10)
//   if(newQuantity !== '' && Number.isInteger(newQuantity) ){
//       try {
//         const response = await axios({
//           method: 'put',
//           url: '/api/products/' + $('#put-product-code').val() + '?show_sql=1',
//           headers: {'Content-Type': 'application/json' },
//           data: {name: $('#put-product-name').val(),quantity: newQuantity}
//         });
//         $('#put-product-quantity-error').removeClass('visible');
//         $('#put-product-quantity-error').addClass('invisible');
//         $('#put-product-sql-code').html(response.headers['sql-statement'])
//         $('#put-product-response-time').html(response.duration.toString());
//         $('#put-product-response-body').html( JSON.stringify( response.data, null, "\t" ) );
//       } catch (error) {
//         console.error(error);
//       }
//   }
//   else{
//      $('#put-product-quantity-error').removeClass('invisible');
//      $('#put-product-quantity-error').addClass('visible');
//   }
// }