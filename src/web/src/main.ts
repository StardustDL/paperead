import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'

import { store, key } from './services/store'

import App from './App.vue'
import Home from './pages/Home.vue'
import MaterialIndex from './pages/materials/Index.vue'
import MaterialView from './pages/materials/View.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/materials', component: MaterialIndex },
    { path: '/materials/:id', component: MaterialView },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

const app = createApp(App);
app.use(router).use(store, key);

app.mount('#app')
