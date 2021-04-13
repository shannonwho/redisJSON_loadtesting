$(document).ready(function(){
    $('#get-examples').click( ()=>{getExamples()})
    $('#get-example').click( ()=>{getExample()});
    $('#get-example-names').click( ()=>{getExampleNames()});
    $('#post-example').click( ()=> {postExample()});
    $('#update-json').click( ()=> {updateJSON()});
    $('#append-json').click( ()=> {appendJSON()});
    $('#array-append-json').click( ()=> {appendArrayJSON()});

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
    let age = $('#post-example-age').val();
    let location = $('#post-example-location').val();
    let idPass = realID !== (null || '')
    let agePass = age !==0
    let locationPass = location.length < 100
    let namePass = name.length < 1000 && name !== (null || '');
    if (namePass && idPass && agePass && locationPass){
        try {
            const response = await axios({
                method: 'post',
                url: '/api/v1/redisjson',
                headers: {'Content-Type': 'application/json' },
                data: {id:realID, name:name,age:age,location:location}
            });

            $('#post-example-response-time').html(response.duration.toString());
            $('#post-example-response-body').html(JSON.stringify(response.data, null, "\t" ) );
        } catch (error) {
            console.error(error);
        }
    }
}

async function updateJSON() {
    console.log("UPDATE JSON")
    $('#update-json-response-time').html('');
    $('#update-json-response-body').html('');
    const key= $('#update-json-key').val();
    const field = $('#update-json-field').val();
    const value = $('#update-json-value').val();

    try {
        const response = await axios({
            method: 'put',
            url: '/api/v1/redisjson/update',
            headers: {'Content-Type': 'application/json' },
            data: {key:key, field:field, str:value}
        });

        $('#update-json-response-time').html(response.duration.toString());
        $('#update-json-response-body').html(JSON.stringify(response.data, null, "\t" ) );
    } catch (error) {
        console.error(error);
    }
}

async function appendJSON() {
    console.log("APPEND JSON")
    $('#append-json-response-time').html('');
    $('#append-json-response-body').html('');
    const key= $('#append-json-key').val();
    const field = $('#append-json-field').val();
    const value = $('#append-json-value').val();

    try {
        const response = await axios({
            method: 'put',
            url: '/api/v1/redisjson/append',
            headers: {'Content-Type': 'application/json' },
            data: {key:key, field:field, str:value}
        });

        $('#append-json-response-time').html(response.duration.toString());
        $('#append-json-response-body').html(JSON.stringify(response.data, null, "\t" ) );
    } catch (error) {
        console.error(error);
    }
}



async function appendArrayJSON() {
    console.log("APPEND JSON")
    $('#array-append-json-response-time').html('');
    $('#array-append-json-response-body').html('');
    const key= $('#array-append-json-key').val();
    const field = $('#array-append-json-field').val();
    const value = $('#array-append-json-value').val();

    try {
        const response = await axios({
            method: 'put',
            url: '/api/v1/redisjson/append',
            headers: {'Content-Type': 'application/json' },
            data: {key:key, field:field, arr:value}
        });

        $('#array-append-json-response-time').html(response.duration.toString());
        $('#array-append-json-response-body').html(JSON.stringify(response.data, null, "\t" ) );
    } catch (error) {
        console.error(error);
    }
}