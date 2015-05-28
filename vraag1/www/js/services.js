angular.module('vraag1.services', [])

.factory('Quotes', function() {
  return {
    all: function() {
      var projectString = [
        {"John Lennon", "Love is the flower you've got to let grow."},
        {"John Lennon", "As usual, there is a great woman behind every idiot."},
        {"Julien Leloup", "Great minds think alike"},
        {"Ralph Waldo Emerson", "We must be our own before we can be another's"},
        {"Winston Churchill", "am fond of pigs. Dogs look up to us. Cats look down on us. Pigs treat us as equals."}
      ]
      if(projectString) {
        return angular.fromJson(projectString);
      }
      return [];
    }
  }

});
