import { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'
import { Api } from './api';
import { MaterialRepository } from './repository'

export interface State {
    api: Api;
    readerMode: boolean;
}

export const key: InjectionKey<Store<State>> = Symbol()

const defaultApiUrl = import.meta.env.DEV ? "http://localhost:3649/api" : "/api";

export const store = createStore<State>({
    state() {
        return {
            api: new Api(defaultApiUrl),
            readerMode: false,
        }
    },
    mutations: {
        setApiUrl(state, value: string) {
            state.api = new Api(value);
        },
        setReaderMode(state, value: boolean) {
            state.readerMode = value;
        }
    }
})

export function useStore() {
    return baseUseStore(key)
}