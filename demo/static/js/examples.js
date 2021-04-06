$(document).ready(function(){
    $('#get-examples').click( ()=>{getExamples()})
    $('#get-example').click( ()=>{getExample()});
    $('#get-example-names').click( ()=>{getExampleNames()});
    // $('#post-example').click( ()=>{postExample()});
    $('#post-example').click( ()=> {postExample()});

});

//get a list of keys based on the key pattern (similar to SCAN)
async function getExamples() {
    $('#get-examples-response-time').html('');
    $('#get-examples-response-body').html('');
    const patterns= $('#get-examples-pattern').val();

    try {
    const response = await axios.get('/api/v1/keys?pattern='+patterns);
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
    const response = await axios.get('/api/v1/doc/' +  id );
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
    const response = await axios.get('/api/v1/subdoc/'+ id + '/' + field);
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
                url: '/api/v1/redisjson',
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