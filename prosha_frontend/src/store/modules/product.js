import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        product: []
    },
    getters: {
        ALL_PRODUCT: state => state.product,
    },
    mutations: {
        SET_PRODUCT: (state, product) => state.product = product,
        NEW_PRODUCT: (state, product) => state.product.unshift(product),
        UPD_PRODUCT: (state, new_product) => {
            const index = state.product.findIndex(t => {return t.id === Number(new_product.id)})
            if (index !== -1){
                state.product.splice(index, 1, new_product);
            }
        },
        REMOVE_PRODUCT: (state, id) => {
            state.product = state.product.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_PRODUCT({ commit }) {
            commit('SET_PRODUCT', (await axios.get(`${variables_url.API_URL}product/all`)).data);
        },
        async GET_PRODUCT_ID({ commit }, id_prod) {
            commit('SET_PRODUCT', (await axios.get(`${variables_url.API_URL}product/${id_prod}`)).data);
        },
        async POST_PRODUCT({ commit }, product) {
            commit('NEW_PRODUCT', (await axios.post(`${variables_url.API_URL}product`, product)).data);
        },
        async PUT_PRODUCT({ commit }, product) {
            commit('UPD_PRODUCT', (await axios.put(`${variables_url.API_URL}product`, product)).data);
        },
        async DEL_PRODUCT({ commit }, product) {
            commit('REMOVE_PRODUCT', (await axios.delete(`${variables_url.API_URL}product/${product.id}`)).data);
        }
    },
}
