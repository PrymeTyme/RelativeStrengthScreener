import { createApp } from 'vue';
//import { createPinia ,setActivePinia } from 'pinia';
import pinia from './stores/store.js';
import App from './App.vue';

const app = createApp(App);
app.use(pinia)

app.mount('#app');


