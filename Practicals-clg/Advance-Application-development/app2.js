// write a program to perform validation of a form using angular JS

var app = angular.module('myApp', []);

app.controller('FormController', function($scope) {
    $scope.user = {};
    $scope.submitted = false;

    $scope.submitForm = function() {
        if ($scope.userForm.$valid) {
            $scope.submitted = true;
        }
    };
});
