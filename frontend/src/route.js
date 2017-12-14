angular.module("App")

.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
        templateUrl: 'main/main.html',
        controller: 'MainController',
    })
    .otherwise({ redirectTo: "/" });
});