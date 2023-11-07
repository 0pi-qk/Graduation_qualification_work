import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        cart: []
    },
    getters: {
        ALL_CART: state => state.cart
    },
    mutations: {
        SET_CART: (state, cart) => state.cart = cart,
        NEW_CART: (state, cart) => state.cart.unshift(cart),
        UPD_CART: (state, new_cart) => {
            const index = state.cart.findIndex(t => {return t.id === Number(new_cart.id)})
            if (index !== -1){
                state.cart.splice(index, 1, new_cart);
            }
        },
        REMOVE_CART: (state, id) => {
            state.cart = state.cart.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_CART({ commit, getters }) {
            commit('SET_CART', (await axios.get(`${variables_url.API_URL}cart/${getters.GET_ID}`)).data);
        },
        async POST_CART({ commit }, cart) {
            commit('NEW_CART', (await axios.post(`${variables_url.API_URL}cart`, cart)).data);
        },
        async PUT_CART({ commit }, cart) {
            commit('UPD_CART', (await axios.put(`${variables_url.API_URL}cart`, cart)).data);
        },
        async DEL_CART({ commit }, cart) {
            commit('REMOVE_CART', (await axios.delete(`${variables_url.API_URL}cart/${cart.id}`)).data);
        }
    },
}
