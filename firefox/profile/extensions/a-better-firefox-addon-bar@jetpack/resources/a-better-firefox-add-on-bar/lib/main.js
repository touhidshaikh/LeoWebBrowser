var self = require("self");
var us = require("userstyles");

exports.main = function() {
  var url = self.data.url("style.css");
  us.load(url);
};