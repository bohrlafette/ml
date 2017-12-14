angular.module("App")

.factory("PredictionService", function($resource) {
  return $resource('/api/predict', {}, {
    query: {method: 'post', isArray: false}
  });
});