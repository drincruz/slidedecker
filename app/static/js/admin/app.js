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

    // New slide placeholder
    $scope.newSlide = {};

    // Message div class toggle
    $scope.msgClass = 'success';

    // Message div show toggle
    $scope.msgShow = false;
    
    // Message div text
    $scope.msgText = '';

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
        $http({
            method: 'POST',
            url: SAVE_SLIDE_ENDPOINT,
            data: { 
                'slide_id': slide.id,
                'title': slide.title,
                'bg_image': slide.bg_image,
                'bg_color': slide.bg_color,
                'text': slide.text
            },
            headers: {'Content-Type': 'application/json'}
        })
        .success(function(data, status, headers, config) {
            if (data) {
                $scope.slides.push(data.slide_data);
                $scope.msgClass = data.status;
                $scope.msgText = data.message
                $scope.msgShow = true;
            }
        })
        .error(function(data, status, headers, config) {
            console.log("[ERROR] " + data);
        });
    };

    /**
     * Delete a slide
     *
     */
    $scope.deleteSlide = function(slide_id, slide_index) {
        var DEL_SLIDE_ENDPOINT = '/admin/slide/delete';
        $http({
            method: 'POST',
            url: DEL_SLIDE_ENDPOINT,
            data: { 
                'slide_id': slide_id,
            },
            headers: {'Content-Type': 'application/json'}
        })
        .success(function(data, status, headers, config) {
            if (data) {
                if ("success" === data.message) {
                    // Delete the slide from the JS array
                    $scope.slides.splice(slide_index, 1);
                }
                $scope.msgClass = data.status;
                $scope.msgText = data.message;
                $scope.msgShow = true;
            }
        })
        .error(function(data, status, headers, config) {
            console.log("[ERROR] " + data);
        });
    };
}]);
