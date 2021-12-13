import OpenAPIClientAxios from 'openapi-client-axios';
import { Client } from '@/api/api.d';


let headers = {};
const access_token = localStorage.getItem('access_token');

if (access_token != null) {
    headers = { Authorization: `Bearer ${access_token}` };
}

function api() {
    const openapi = new OpenAPIClientAxios({
        definition: `http://localhost:6080/openapi.json`,
        withServer: 'main',
        axiosConfigDefaults: {
            headers,
        },
    }).init<Client>();

    return openapi
}

export default api();
