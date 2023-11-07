import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        article: []
    },
    getters: {
        ALL_ARTICLE: state => state.article
    },
    mutations: {
        SET_ARTICLE: (state, article) => state.article = article,
        NEW_ARTICLE: (state, article) => state.article.unshift(article),
        UPD_ARTICLE: (state, new_article) => {
            const index = state.article.findIndex(t => {return t.id === Number(new_article.id)})
            if (index !== -1){
                state.article.splice(index, 1, new_article);
            }
        },
        REMOVE_ARTICLE: (state, id) => {
            state.article = state.article.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_ARTICLE({ commit }) {
            commit('SET_ARTICLE', (await axios.get(`${variables_url.API_URL}article/all`)).data);
        },
        async GET_ARTICLE_ID({ commit }, id) {
            commit('SET_ARTICLE', (await axios.get(`${variables_url.API_URL}article/${id}`)).data);
        },
        async POST_ARTICLE({ commit }, article) {
            commit('NEW_ARTICLE', (await axios.post(`${variables_url.API_URL}article`, article)).data);
        },
        async PUT_ARTICLE({ commit }, article) {
            commit('UPD_ARTICLE', (await axios.put(`${variables_url.API_URL}article`, article)).data);
        },
        async DEL_ARTICLE({ commit }, article) {
            commit('REMOVE_ARTICLE', (await axios.delete(`${variables_url.API_URL}article/${article.id}`)).data);
        }
    },
}
