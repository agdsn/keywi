import OpenAPIClientAxios from 'openapi-client-axios';
import {Client} from '@/api/api.d';
import qs from "qs";

// Der Code ist Spaghetti af, aber ich bin erstmal ich habe verschiedene Sachen probiert und bin froh, dass es grad überhaupt läuft
// Kannst gerne etwas hübscher machen wenn du Lust hast
export default async function api() {
    const openapi = await new OpenAPIClientAxios({
        definition: `http://localhost:6080/openapi.json`,
        withServer: 'main',
        /* axiosConfigDefaults: {
            headers,
        },*/
    }).init<Client>();

    const credentials = {
        username: "test",
        password: "abc"
    };
    const payload = qs.stringify(credentials);
    const options = {
        headers: {'content-type': 'application/x-www-form-urlencoded'},
        data: payload
    };

    // Operationen werden dynamisch geladen, eslint kommt damit nicht so gut klar
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    const response = await openapi.auth_login(undefined, undefined, options);
    const accessToken = response.data.access_token;
    const config = {
        headers: {
            "Authorization": "Bearer " + accessToken
        }
    };

    // das Überschreiben der axiosConfigDefaults mit dem schon vorhandenen Objekt hat nicht funktioniert
    // Das geht sicher irgendwie, weiß aber grad nicht wie
    const api = new OpenAPIClientAxios({
        definition: `http://localhost:6080/openapi.json`,
        withServer: 'main',
        axiosConfigDefaults: config
    }).init<Client>();
    return api;
}