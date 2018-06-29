import Vue from 'vue';
import App from './vue/App.vue';

import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default-dark.css';

Vue.use(VueMaterial);

const app = new Vue({
    el: '#app',
    components: { App },
    template: '<App/>'
});


if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js', {scope: '/'})
      .then(reg => {
        // registration worked
        console.log('Registration succeeded. Scope is ' + reg.scope);
      }).catch(error => {
        // registration failed
        console.log('Registration failed with ' + error);
      });
  });
}
