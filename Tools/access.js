// "In fact what I would like to see is thousands of computer scientists let
//  loose to do whatever they want. That's what really advances the field."
//  - Donald Knuth

var UserAccess = function (pat) {
    this._pat = pat;
};

UserAccess.prototype.get = function(cacheId) {
    // body...
};

UserAccess.prototype.edit = function(cacheId, newContent) {
    // body...
};

UserAccess.prototype.create = function() {
    return ""
};

UserAccess.prototype.delete = function(cacheId) {
    // body...
};
