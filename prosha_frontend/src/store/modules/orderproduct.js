import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        orderproduct: []
    },
    getters: {
        ALL_ORDERPRODUCT: state => state.orderproduct
    },
    mutations: {
        SET_ORDERPRODUCT: (state, orderproduct) => state.orderproduct = orderproduct,
        NEW_ORDERPRODUCT: (state, orderproduct) => state.orderproduct.unshift(orderproduct),
        UPD_ORDERPRODUCT: (state, new_orderproduct) => {
            const index = state.orderproduct.findIndex(t => {return t.id === Number(new_orderproduct.id)})
            if (index !== -1){
                state.orderproduct.splice(index, 1, new_orderproduct);
            }
        },
        REMOVE_ORDERPRODUCT: (state, id) => {
            state.orderproduct = state.orderproduct.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_ORDERPRODUCT({ commit }) {
            commit('SET_ORDERPRODUCT', (await axios.get(`${variables_url.API_URL}orderproduct/${orderproduct.user}`)).data);
        },
        async POST_ORDERPRODUCT({ commit }, orderproduct) {
            commit('NEW_ORDERPRODUCT', (await axios.post(`${variables_url.API_URL}orderproduct`, orderproduct)).data);
        },
        async PUT_ORDERPRODUCT({ commit }, orderproduct) {
            commit('UPD_ORDERPRODUCT', (await axios.put(`${variables_url.API_URL}orderproduct`, orderproduct)).data);
        },
        async DEL_ORDERPRODUCT({ commit }, orderproduct) {
            commit('REMOVE_ORDERPRODUCT', (await axios.delete(`${variables_url.API_URL}orderproduct/${orderproduct.id}`)).data);
        }
    },
}
