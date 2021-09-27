import { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'
import { MaterialRepository } from './repository'

export interface State {
    apiUrl: string;
    materials: MaterialRepository;
}

export const key: InjectionKey<Store<State>> = Symbol()

const defaultApiUrl = "http://localhost:3649/api";

export const store = createStore<State>({
    state() {
        return {
            apiUrl: defaultApiUrl,
            materials: new MaterialRepository(defaultApiUrl),
        }
    },
    mutations: {
        setApiUrl(state, value: string) {
            state.apiUrl = value;
            state.materials = new MaterialRepository(state.apiUrl);
        }
    }
})

export function useStore() {
    return baseUseStore(key)
}