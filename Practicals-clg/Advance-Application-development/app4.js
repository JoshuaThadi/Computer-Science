//Define the module
var app = angular.module('myApp',[]);

//Define the MainController
app.controller(
    'MainController',
    function($scope){
        $scope.title = "Welcome to AngularJS Modules and Controllers";
        $scope.description= "This demonstrates how to use modules and controllers in AngularJS";
    }
);

//Define AnotherController
app.controller(
    'AnotherController', 
    function($scope){
        $scope.heading="List of items: ";
        $scope.items = ["item 1", "item 2", "item 4"];
    }
);