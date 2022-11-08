import { createApp } from 'vue';
//import { createPinia ,setActivePinia } from 'pinia';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {library} from '@fortawesome/fontawesome-svg-core';
import{fas} from '@fortawesome/free-solid-svg-icons';
//import{fas} from '@fortawesome/free-regular-svg-icons'
import pinia from './stores/store.js';
import App from './App.vue';

library.add(fas);

const app = createApp(App).component('fa',FontAwesomeIcon);
app.use(pinia)

app.mount('#app');


