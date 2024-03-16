import qs from "qs";
import api from "@/api/api";
import axios from "axios";

export default {
    async setAccessToken(access_token: string) {
        const apiClient = await api;

        const header = `Bearer ${access_token}`;
        axios.defaults.headers.common.Authorization = header;
        apiClient.defaults.headers.Authorization = header;

        const user = (await apiClient.user_getCurrent()).data

        localStorage.setItem('user', JSON.stringify(user));
        localStorage.setItem('access_token', access_token);

        window.dispatchEvent(new CustomEvent('keywi-auth-change', {}));

        return true;
    },
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

        const access_token = (await apiClient.auth_getToken(null, credentials, options)).data.access_token;

        await this.setAccessToken(access_token)

        return true;
    },
    async logout() {
        const apiClient = await api;

        localStorage.removeItem('access_token');
        localStorage.removeItem('user');
        delete axios.defaults.headers.common.Authorization;
        delete apiClient.defaults.headers.Authorization;

        window.dispatchEvent(new CustomEvent('keywi-auth-change', {}));
    },
    getOAuthUrl(returnUrl: string) {
        let newRetURL = returnUrl;

        let redirectUrl = `${process.env.VUE_APP_KEYWI_API_URL}/auth/start`;

        if (returnUrl == null) {
            newRetURL = window.location.origin;
        }

        const returnUrlEnc = encodeURIComponent(newRetURL);
        redirectUrl = redirectUrl.concat(`?return_url=${returnUrlEnc}`);

        return redirectUrl;
    },
    isLoggedIn() {
        return localStorage.getItem('access_token') != null;
    },
    async refreshUser() {
        const apiClient = await api;

        apiClient.user_getCurrent().then((response) => {
            localStorage.setItem('user', JSON.stringify(response.data));
        }).catch(() => {
            this.logout();
        });
    },
    getUser() {
        const userData = localStorage.getItem('user');

        if (userData == null) {
            return null;
        }

        return JSON.parse(userData);
    }
}
