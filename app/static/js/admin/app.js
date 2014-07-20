var myApp = angular.module('myApp', []);

myApp.controller('MainCtrl', ['$scope', '$http', function($scope, $http) {
    /**
     * Do any loading on document ready
     *
     */
    angular.element(document).ready(function() {
        $scope.loadSlides();
    });

    // Slides
    $scope.slides = [];

    /**
     * Load any saved slides, if any
     *
     */
    $scope.loadSlides = function() {
        var GET_SLIDES_ENDPOINT = '/admin/get/slides';
        $http({
            method: 'GET',
            url: GET_SLIDES_ENDPOINT
        })
        .success(function(data, status, headers, config) {
            if (data) {
                console.log(data);
                $scope.slides = data.slides;
            }
        })
        .error(function(data, status, headers, config) {
            console.log("[ERROR] " + data);
        });
    };
}]);
