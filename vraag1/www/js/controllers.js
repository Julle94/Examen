angular.module('vraag1.controllers', ['ionic'])

.controller('QuoteCtrl', function($scope, $ionicModal) {
  $scope.quotes = [];
  $scope.authors = [];

  $ionicModal.formTemplateUrl('templates/quotes.html', function(modal){
  $scope.taskModal = modal;
  }, {
    scope: $scope
  });

  $scope.quotes = Quotes.all();

  $scope.selectAuthor = function(author) {
    $scope.activeauthor = author;
  }
});
