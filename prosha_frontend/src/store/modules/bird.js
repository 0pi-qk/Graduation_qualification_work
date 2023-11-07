import axios from "axios";

import {variables_url} from '@/URLs'

export default {
    state: {
        bird: []
    },
    getters: {
        ALL_BIRD: state => state.bird
    },
    mutations: {
        SET_BIRD: (state, bird) => state.bird = bird,
        NEW_BIRD: (state, bird) => state.bird.unshift(bird),
        UPD_BIRD: (state, new_bird) => {
            const index = state.bird.findIndex(t => {return t.id === Number(new_bird.id)})
            if (index !== -1){
                state.bird.splice(index, 1, new_bird);
            }
        },
        REMOVE_BIRD: (state, id) => {
            state.bird = state.bird.filter(t => {return t.id !== id} )
        }
    },
    actions: {
        async GET_BIRD_ID({ commit }, bird_id) {
            commit('SET_BIRD', (await axios.get(`${variables_url.API_URL}bird/${bird_id}`)).data);
        },
        async GET_BIRD({ commit, getters }, tree) {
            if (getters.GET_AUTH === 4 || tree === true){
                commit('SET_BIRD', (await axios.get(`${variables_url.API_URL}bird/tree`)).data);
            }else{
                commit('SET_BIRD', (await axios.get(`${variables_url.API_URL}bird/user/${getters.GET_ID}`)).data);
            }
        },
        async POST_BIRD({ commit }, bird) {
            commit('NEW_BIRD', (await axios.post(`${variables_url.API_URL}bird`, bird)).data);
        },
        async PUT_BIRD({ commit }, bird) {
            commit('UPD_BIRD', (await axios.put(`${variables_url.API_URL}bird`, bird)).data);
        },
        async DEL_BIRD({ commit }, bird) {
            commit('REMOVE_BIRD', (await axios.delete(`${variables_url.API_URL}bird/${bird.id}`)).data);
        }
    },
}
