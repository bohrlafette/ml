angular.module("App")

.controller("MainController", function ($scope, PredictionService) {
    $scope.predictUser = {
        name: "",
        gender: "0",
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
                console.log(success);
                $scope.predictResult = success;
            },
            function(error) {
                console.log(error);
            }
        )
    };
});