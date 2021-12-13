import qs from "qs";
import api from "@/api/api";
import axios from "axios";

export default {
    async login(username: string, password: string) {
        const apiClient = await api;

        const credentials = {
            username,
            password,
        };
        const payload = qs.stringify(credentials);
        const options = {
            headers: {'content-type': 'application/x-www-form-urlencoded'},
            data: payload
        };

        apiClient.auth_login(null, undefined, options).then((rsp) => {
            const access_token = rsp.data.access_token;

            localStorage.setItem('access_token', access_token);

            const header = `Bearer ${access_token}`;
            axios.defaults.headers.common.Authorization = header;
            apiClient.defaults.headers.Authorization = header;

            apiClient.user_getCurrent().then((rsp) => {
                localStorage.setItem('user', JSON.stringify(rsp.data));
            });

            return true;
        }).catch((err) => {
            console.log(err);
            throw err;
        });
    },
    async logout() {
        const apiClient = await api;

        localStorage.removeItem('access_token');
        delete axios.defaults.headers.common.Authorization;
        delete apiClient.defaults.headers.Authorization;
    },
    isLoggedIn() {
        const loggedIn = localStorage.getItem('access_token') != null;

        console.log("Logged in:" + loggedIn)

        return loggedIn
    },
    getUser() {
        const userData = localStorage.getItem('user');

        if (userData == null) {
            return null;
        }

        return JSON.parse(userData);
    }
}