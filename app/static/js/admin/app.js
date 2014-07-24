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

    /**
     * Save a slide
     *
     */
    $scope.saveSlide = function(slide) {
        var SAVE_SLIDE_ENDPOINT = '/admin/slide/edit';
        console.log("[DEBUG] getting here?");
        console.log(slide);
        $http({
            method: 'POST',
            url: SAVE_SLIDE_ENDPOINT,
            data: JSON.stringify({ 
                'slide_id': slide.id
            }),
            headers: {'Content-Type': 'application/json'}
            
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
