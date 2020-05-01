define(['wq/store'], function (ds) { 'use strict';

var i18n = {
    name: 'i18n'
};

var $;

i18n.init = function (config) {
    $ = config && config.jQuery || window.jQuery;

    this.language = 'english';

    this.dict = {
      'english': {
        'instruction1_part1': 'We all love food. We make sure our children eat healthily. We are paying more and more attention to what we eat and what we buy. What we eat affects not only us, but also the environment and our immediate surroundings. With this application, we will try to provide you with information about food in Słupsk. Moreover, by answering some questions in this application you can help us to better understand the food nexus. Using the map you can:'
      },
      'polish': {
        'instruction1_part1': 'Cześć'
      }
    };

};


i18n.context = function(context, routeInfo) {
    return this.dict[this.language];
};


i18n.run = function ($page, routeInfo) {

  var parent = this;

  $page.on('change', 'select[class="language"]', function(evt) {
    parent.language = $(evt.target).val();
    // TODO: rerender page/elements
  });

  $page.ready( function() {
    $('select[class="language"]').val(parent.language).change();
  });

};

return i18n;

});
