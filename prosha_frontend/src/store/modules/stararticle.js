import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        stararticle: []
    },
    getters: {
        ALL_STARARTICLE: state => state.stararticle
    },
    mutations: {
        SET_STARARTICLE: (state, stararticle) => state.stararticle = stararticle,
        NEW_STARARTICLE: (state, stararticle) => state.stararticle.unshift(stararticle),
        UPD_STARARTICLE: (state, new_stararticle) => {
            const index = state.stararticle.findIndex(t => {return t.id === Number(new_stararticle.id)})
            if (index !== -1){
                state.stararticle.splice(index, 1, new_stararticle);
            }
        },
        REMOVE_STARARTICLE: (state, id) => {
            state.stararticle = state.stararticle.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_STARARTICLE({ commit }, id) {
            commit('SET_STARARTICLE', (await axios.get(`${variables_url.API_URL}stararticle/${id}`)).data);
        },
        async POST_STARARTICLE({ commit }, stararticle) {
            commit('NEW_STARARTICLE', (await axios.post(`${variables_url.API_URL}stararticle`, stararticle)).data);
        },
        async PUT_STARARTICLE({ commit }, stararticle) {
            commit('UPD_STARARTICLE', (await axios.put(`${variables_url.API_URL}stararticle`, stararticle)).data);
        },
        async DEL_STARARTICLE({ commit }, stararticle) {
            commit('REMOVE_STARARTICLE', (await axios.delete(`${variables_url.API_URL}stararticle/${stararticle.id}`)).data);
        }
    },
}
