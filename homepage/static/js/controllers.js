var app = angular.module("franhpApp", ["ngSanitize", "ngResource"]);

app.controller("githubCtrl", function($scope, $http) {
	$http.get('api/github.json').
    success(function(data, status, headers, config) {
        $scope.projects = data;
    }).
    error(function(data, status, headers, config){
        $scope.projects = [];
    });
});


app.controller("lastfmCtrl", function($scope, $http) {
	$http.get('api/lastfm.json').
    success(function(data, status, headers, config) {
        $scope.songs = data;
    }).
    error(function(data, status, headers, config){
        $scope.songs = [];
    });
});


app.controller("twitterCtrl", function($scope, $http) {
	$http.get('api/twitter.json').
    success(function(data, status, headers, config) {
        $scope.tweets = data;
    }).
    error(function(data, status, headers, config){
        $scope.tweets = [];
    });
});