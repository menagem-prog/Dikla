// Service Worker – מאפשר פתיחה גם ללא אינטרנט אחרי ביקור ראשון
const CACHE = 'dikla-bday-v1';
const FILES = ['index.html', 'manifest.json', 'timeline-data.json', 'stations-data.json'];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.addAll(FILES);
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function (e) {
  if (e.request.url.indexOf(self.location.origin) !== 0) return;
  e.respondWith(
    fetch(e.request).catch(function () {
      return caches.match(e.request);
    })
  );
});
