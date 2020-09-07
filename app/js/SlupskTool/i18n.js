define(['wq/store', 'wq/router'], function (ds, router) { 'use strict';

// from https://stackoverflow.com/questions/5639346/what-is-the-shortest-function-for-reading-a-cookie-by-name-in-javascript
function getCookieValue(a) {
    var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
    return b ? b.pop() : '';
}

var dict = {
  'en': {
    'instruction1_part1': 'We all love food. We make sure our children eat healthily. We are paying more and more attention to what we eat and what we buy. What we eat affects not only us, but also the environment and our immediate surroundings. With this application, we will try to provide you with information about food in Słupsk. Moreover, by answering some questions in this application you can help us to better understand the food nexus. Using the map you can:'
  },
  'pl': {
    'instruction1_part1': 'Cześć'
  }
};


var i18n = {
    name: 'i18n'
};

var $;

i18n.init = function (config) {
    $ = config && config.jQuery || window.jQuery;

    this.dict = dict;

    // Set language
    var lang = getCookieValue('django_language');  // cookie language preference

    if (!lang) {
      if (navigator.language == 'en' || navigator.language == 'pl') {
        this.language = navigator.language;       // browser language preference
      } else {
        this.language = 'en';                     // fall-back language, should be equal to LANGUAGE_CODE in base.py for consistency
      }
    } else {
      this.language = lang;
    }

    // Set language in select menu
    // if language was changed to polish but cookie is not set, this will
    $('select[class="language"]').val(this.language).change();

    // Use cookie also here?
    ds.set('wq-language', this.language);

};


i18n.context = function(context, routeInfo) {
    return this.dict[this.language];
};


i18n.run = function ($page, routeInfo) {

  var parent = this;

  $page.on('change', 'select[class="language"]', function(evt) {

    // Set language taken from widget
    parent.language = $(evt.target).val();

    // Set cookie to be used by django.middleware.locale.LocaleMiddleware
    document.cookie = "django_language=".concat(parent.language).concat(";SameSite=Lax") ;

    // Reload page once
    // Use cookie also here?
    ds.get('wq-language').then(function(language) {

      if( language != parent.language ) {
        ds.set('wq-language', parent.language);
        window.location.reload();
      }

    });

  });

  $page.ready( function() {
    $('select[class="language"]').val(parent.language).change();
  });


};

return i18n;

});
