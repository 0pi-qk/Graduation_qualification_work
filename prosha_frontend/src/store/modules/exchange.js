import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        exchange: []
    },
    getters: {
        ALL_EXCHANGE: state => state.exchange
    },
    mutations: {
        SET_EXCHANGE: (state, exchange) => state.exchange = exchange,
        NEW_EXCHANGE: (state, exchange) => state.exchange.unshift(exchange),
        UPD_EXCHANGE: (state, new_exchange) => {
            const index = state.exchange.findIndex(t => {return t.id === Number(new_exchange.id)})
            if (index !== -1){
                state.exchange.splice(index, 1, new_exchange);
            }
        },
        REMOVE_EXCHANGE: (state, id) => {
            state.exchange = state.exchange.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_EXCHANGE({ commit }) {
            commit('SET_EXCHANGE', (await axios.get(`${variables_url.API_URL}exchange`)).data);
        },
        async POST_EXCHANGE({ commit }, exchange) {
            commit('NEW_EXCHANGE', (await axios.post(`${variables_url.API_URL}exchange`, exchange)).data);
        },
        async PUT_EXCHANGE({ commit }, exchange) {
            commit('UPD_EXCHANGE', (await axios.put(`${variables_url.API_URL}exchange`, exchange)).data);
        },
        async DEL_EXCHANGE({ commit }, exchange) {
            commit('REMOVE_EXCHANGE', (await axios.delete(`${variables_url.API_URL}exchange/${exchange.id}`)).data);
        }
    },
}
