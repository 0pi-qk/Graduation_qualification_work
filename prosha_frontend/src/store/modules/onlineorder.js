import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        onlineorder: [],
        now_order: -1
    },
    getters: {
        ALL_ONLINEORDER: state => state.onlineorder,
        GET_NOW_ORDER: state => state.now_order
    },
    mutations: {
        SET_ONLINEORDER: (state, onlineorder) => state.onlineorder = onlineorder,
        NEW_ONLINEORDER: (state, onlineorder) => {
            state.onlineorder.unshift(onlineorder)
            state.now_order = onlineorder.id
        },
        UPD_ONLINEORDER: (state, new_onlineorder) => {
            const index = state.onlineorder.findIndex(t => {return t.id === Number(new_onlineorder.id)})
            if (index !== -1){
                state.onlineorder.splice(index, 1, new_onlineorder);
            }
        },
        REMOVE_ONLINEORDER: (state, id) => {
            state.onlineorder = state.onlineorder.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_ONLINEORDER({ commit, getters }) {
            commit('SET_ONLINEORDER', (await axios.get(`${variables_url.API_URL}onlineorder/${getters.GET_ID}`)).data);
        },
        async POST_ONLINEORDER({ commit }, onlineorder) {
            commit('NEW_ONLINEORDER', (await axios.post(`${variables_url.API_URL}onlineorder`, onlineorder)).data);
        },
        async PUT_ONLINEORDER({ commit }, onlineorder) {
            commit('UPD_ONLINEORDER', (await axios.put(`${variables_url.API_URL}onlineorder`, onlineorder)).data);
        },
        async DEL_ONLINEORDER({ commit }, onlineorder) {
            commit('REMOVE_ONLINEORDER', (await axios.delete(`${variables_url.API_URL}onlineorder/${onlineorder.id}`)).data);
        }
    },
}
