import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        user: [],
        isAuth: 1,
        thisId: 2
    },
    getters: {
        ALL_USER: state => state.user,
        GET_AUTH: state => state.isAuth,
        GET_ID: state => state.thisId,
    },
    mutations: {
        SET_USER: (state, user) => state.user = user,
        NEW_USER: (state, user) => state.user.unshift(user),
        UPD_USER: (state, new_user) => {
            const index = state.user.findIndex(t => {return t.id === Number(new_user.id)})
            if (index !== -1){
                state.user.splice(index, 1, new_user);
            }
        },
        REMOVE_USER: (state, id) => {
            state.user = state.user.filter(t => {return t.id !== id} )
        },
        EXC_AUTH: (state) => {
            state.isAuth=0;
            state.thisId=-1
        },
        EXC_ID: (state, new_thisId) => state.thisId=new_thisId
    },
    actions: {
        async GET_USER({ commit, getters }) {
            commit('SET_USER', (await axios.get(`${variables_url.API_URL}account/${getters.GET_ID}`)).data);
        },
        async POST_USER({ commit }, user) {
            commit('NEW_USER', (await axios.post(`${variables_url.API_URL}account`, user)).data);
        },
        async PUT_USER({ commit }, user) {
            commit('UPD_USER', (await axios.put(`${variables_url.API_URL}account`, user)).data);
        },
        async DEL_USER({ commit }, user) {
            commit('REMOVE_USER', (await axios.delete(`${variables_url.API_URL}account/${user.id}`)).data);
        }
    },
}
