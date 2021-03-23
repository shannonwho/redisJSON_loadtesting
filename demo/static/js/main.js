$(document).ready(function() {
    //for nav
	$('#'+location.pathname.split('/')[1] +'-nav').addClass('active')
	//trigger response time to axios requests
	addResponseTimeDataToAxios();
})

//function to add response time to axios requests
function addResponseTimeDataToAxios(){
    axios.interceptors.request.use(
        function (config) {
            config.metadata = { startTime: new Date()}
            return config;
        },
        function (error) {
            return Promise.reject(error);
        }
     );

    axios.interceptors.response.use(
        function (response) {
            response.config.metadata.endTime = new Date()
            response.duration = response.config.metadata.endTime - response.config.metadata.startTime
            return response;
        },
        function (error) {
            error.config.metadata.endTime = new Date();
            error.duration = error.config.metadata.endTime - error.config.metadata.startTime;
            return Promise.reject(error);
         }
    );
}