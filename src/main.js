import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'
// Import for tailwind css
import './style.css'
// Import Toaster for custom alert
import Toaster from '@meforma/vue-toaster';

createApp(App).use(Toaster).mount('#app')
