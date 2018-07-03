var CACHE_NAME = 'jcdin-cache-v1';
var urlsToCache = [
  '/',
  '/static/app.js',
  '/static/vendors.js',
  '//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons'
];

self.addEventListener('install', function(event) {
    console.log("Service Worker installed");
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(cache => {
          return cache.addAll(urlsToCache);
        })
        // }).then(() => {
        //   // notify user on offline ready
        // }).catch(() => {
        //   // something went wrong on caching
        // })
    );
});

self.addEventListener('activate', function(event) {
    console.log("Service Worker activated");
    event.waitUntil(clients.claim());
});


self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        var fetchRequest = event.request.clone();
        return fetch(fetchRequest)
          .then(response => {
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            var responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });

            return response;
          });
      })
  );
});
