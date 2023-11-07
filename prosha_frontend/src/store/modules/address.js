import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        address: []
    },
    getters: {
        ALL_ADDRESS: state => state.address
    },
    mutations: {
        SET_ADDRESS: (state, address) => state.address = address,
        NEW_ADDRESS: (state, address) => state.address.unshift(address),
        UPD_ADDRESS: (state, new_address) => {
            const index = state.address.findIndex(t => {return t.id === Number(new_address.id)})
            if (index !== -1){
                state.address.splice(index, 1, new_address);
            }
        },
        REMOVE_ADDRESS: (state, id) => {
            state.address = state.address.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_ADDRESS({ commit }, address) {
            commit('SET_ADDRESS', (await axios.get(`${variables_url.API_URL}address/${address.user}`)).data);
        },
        async POST_ADDRESS({ commit }, address) {
            commit('NEW_ADDRESS', (await axios.post(`${variables_url.API_URL}address`, address)).data);
        },
        async PUT_ADDRESS({ commit }, address) {
            commit('UPD_ADDRESS', (await axios.put(`${variables_url.API_URL}address`, address)).data);
        },
        async DEL_ADDRESS({ commit }, address) {
            commit('REMOVE_ADDRESS', (await axios.delete(`${variables_url.API_URL}address/${address.id}`)).data);
        }
    },
}
