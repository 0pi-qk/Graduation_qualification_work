import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        starproduct: []
    },
    getters: {
        ALL_STARPRODUCT: state => state.starproduct
    },
    mutations: {
        SET_STARPRODUCT: (state, starproduct) => state.starproduct = starproduct,
        NEW_STARPRODUCT: (state, starproduct) => state.starproduct.unshift(starproduct),
        UPD_STARPRODUCT: (state, new_starproduct) => {
            const index = state.starproduct.findIndex(t => {return t.id === Number(new_starproduct.id)})
            if (index !== -1){
                state.starproduct.splice(index, 1, new_starproduct);
            }
        },
        REMOVE_STARPRODUCT: (state, id) => {
            state.starproduct = state.starproduct.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_STARPRODUCT({ commit }, id) {
            commit('SET_STARPRODUCT', (await axios.get(`${variables_url.API_URL}starproduct/${id}`)).data);
        },
        async POST_STARPRODUCT({ commit }, starproduct) {
            commit('NEW_STARPRODUCT', (await axios.post(`${variables_url.API_URL}starproduct`, starproduct)).data);
        },
        async PUT_STARPRODUCT({ commit }, starproduct) {
            commit('UPD_STARPRODUCT', (await axios.put(`${variables_url.API_URL}starproduct`, starproduct)).data);
        },
        async DEL_STARPRODUCT({ commit }, starproduct) {
            commit('REMOVE_STARPRODUCT', (await axios.delete(`${variables_url.API_URL}starproduct/${starproduct.id}`)).data);
        }
    },
}
