import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'

import { store, key } from './services/store'

import App from './App.vue'
import Home from './pages/Home.vue'
import NotFound from './pages/NotFound.vue'
import MaterialIndex from './pages/materials/Index.vue'
import MaterialView from './pages/materials/View.vue'
import NoteView from './pages/notes/View.vue'

const routes = [
    {
        path: '/',
        component: Home,
        meta: {
            title: 'Home - Paperead'
        }
    },
    {
        path: '/materials',
        component: MaterialIndex,
        meta: {
            title: 'Materials - Paperead'
        }
    },
    {
        path: '/materials/:id',
        component: MaterialView,
        meta: {
            title: 'Loading... - Materials - Paperead'
        }
    },
    {
        path: '/materials/:id/:noteId',
        component: NoteView,
        meta: {
            title: 'Loading... - Loading... - Materials - Paperead'
        }
    },
    {
        path: '/:path*',
        component: NotFound,
        meta: {
            title: 'Not found - Paperead'
        }
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

router.beforeEach((to, from) => {
    if (to.path == from.path) {
        return true;
    }
    document.title = (to.meta.title as any).toString();
    return true;
});

const app = createApp(App);
app.use(router).use(store, key);

app.mount('#app')
