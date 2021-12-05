import OpenAPIClientAxios from 'openapi-client-axios';
import { Client } from '@/api/api.d';


export default function api() {
    const openapi = new OpenAPIClientAxios({
        definition: `http://localhost:6080/openapi.json`,
        withServer: 'main',
        /* axiosConfigDefaults: {
            headers,
        },*/
    }).init<Client>();

    return openapi
}
