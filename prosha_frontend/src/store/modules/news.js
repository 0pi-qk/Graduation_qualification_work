import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        news: []
    },
    getters: {
        ALL_NEWS: state => state.news
    },
    mutations: {
        SET_NEWS: (state, news) => state.news = news,
        NEW_NEWS: (state, news) => state.news.unshift(news),
        UPD_NEWS: (state, new_news) => {
            const index = state.news.findIndex(t => {return t.id === Number(new_news.id)})
            if (index !== -1){
                state.news.splice(index, 1, new_news);
            }
        },
        REMOVE_NEWS: (state, id) => {
            state.news = state.news.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_NEWS({ commit }) {
            commit('SET_NEWS', (await axios.get(`${variables_url.API_URL}news/all`)).data);
        },
        async GET_NEWS_ID({ commit }, id) {
            commit('SET_NEWS', (await axios.get(`${variables_url.API_URL}news/${id}`)).data);
        },
        async POST_NEWS({ commit }, news) {
            commit('NEW_NEWS', (await axios.post(`${variables_url.API_URL}news`, news)).data);
        },
        async PUT_NEWS({ commit }, news) {
            commit('UPD_NEWS', (await axios.put(`${variables_url.API_URL}news`, news)).data);
        },
        async DEL_NEWS({ commit }, news) {
            commit('REMOVE_NEWS', (await axios.delete(`${variables_url.API_URL}news/${news.id}`)).data);
        }
    },
}
