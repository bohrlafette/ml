angular.module("App")

.controller("MainController", function ($scope, PredictionService, $filter) {
    $scope.predictUser = {
        name: "",
        gender: 0,
        numChildren: 0,
        ownsHouse: false,   
        yearBorn: 1990,
        numCats: 0,
        numDogs: 0,
        numHorses: 0
    };

    $scope.predict = function () {
        var request = angular.copy($scope.predictUser);
        request.gender = parseInt(request.gender);
        request.ownsHouse = (request.ownsHouse) ? 1 : 0;
        PredictionService.query(
            {},
            request,
            function(success) {
                $scope.predictResult = {
                    raw: success,
                };

                for (var property in success) {
                    if (success.hasOwnProperty(property)) {
                        $scope.predictResult[property] = $filter('toPercent')(success[property]);
                    }
                }

                console.log($scope.predictResult);
            },
            function(error) {
                console.log(error);
            }
        )
    };
})

.filter('toPercent', function() {
    return function(num) {
        return Math.min(100, Math.abs(num) * 100);
    };
})

.filter('toType', function() {
    return function(num) {
        return (num < 0)? "danger" : "success";
    };
});