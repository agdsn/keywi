import OpenAPIClientAxios from 'openapi-client-axios';
import { Client } from '@/api/api.d';


let headers = {};
const access_token = localStorage.getItem('access_token');

if (access_token != null) {
    headers = { Authorization: `Bearer ${access_token}` };
}

function api() {
    const openapi = new OpenAPIClientAxios({
        definition: `${process.env.VUE_APP_KEYWI_API_URL}/openapi.json`,
        withServer: 'main',
        axiosConfigDefaults: {
            baseURL: process.env.VUE_APP_KEYWI_API_URL,
            headers,
        },
    }).init<Client>();

    return openapi
}

export default api();
