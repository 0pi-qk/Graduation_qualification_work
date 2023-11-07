import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        starnews: []
    },
    getters: {
        ALL_STARNEWS: state => state.starnews
    },
    mutations: {
        SET_STARNEWS: (state, starnews) => state.starnews = starnews,
        NEW_STARNEWS: (state, starnews) => state.starnews.unshift(starnews),
        UPD_STARNEWS: (state, new_starnews) => {
            const index = state.starnews.findIndex(t => {return t.id === Number(new_starnews.id)})
            if (index !== -1){
                state.starnews.splice(index, 1, new_starnews);
            }
        },
        REMOVE_STARNEWS: (state, id) => {
            state.starnews = state.starnews.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_STARNEWS({ commit }, id) {
            commit('SET_STARNEWS', (await axios.get(`${variables_url.API_URL}starnews/${id}`)).data);
        },
        async POST_STARNEWS({ commit }, starnews) {
            commit('NEW_STARNEWS', (await axios.post(`${variables_url.API_URL}starnews`, starnews)).data);
        },
        async PUT_STARNEWS({ commit }, starnews) {
            commit('UPD_STARNEWS', (await axios.put(`${variables_url.API_URL}starnews`, starnews)).data);
        },
        async DEL_STARNEWS({ commit }, starnews) {
            commit('REMOVE_STARNEWS', (await axios.delete(`${variables_url.API_URL}starnews/${starnews.id}`)).data);
        }
    },
}
