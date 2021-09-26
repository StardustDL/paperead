import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import App from './App.vue'
import Home from './pages/Home.vue'
import MaterialIndex from './pages/materials/Index.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/materials', component: MaterialIndex },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
})

const app = createApp(App);
app.use(router);

app.mount('#app')
