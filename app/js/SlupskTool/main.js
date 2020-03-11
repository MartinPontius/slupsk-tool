define(['wq/app', './removeattachment', './instruction', './filter', './preselect', 'wq/map', 'wq/patterns', 'wq/locate',
        './config', 'leaflet.draw', 'leaflet.markercluster'],
function(app, removeattachment, instruction, filter, preselect, map, patterns, locate, config) {

app.use(removeattachment);
app.use(instruction);
app.use(filter);
app.use(preselect);
app.use(map);
app.use(patterns);
app.use(locate);

//  Add new map icon
map.createIcon("producer", {'iconUrl': "/images/producer.png", 'iconSize': [30, 30]});
map.createIcon("kindergarten", {'iconUrl': "/images/kindergarten.png", 'iconSize': [40, 40]});
map.createIcon("shop", {'iconUrl': "/images/shop.png", 'iconSize': [30, 30]});

config.presync = presync;
config.postsync = postsync;
var ready = app.init(config).then(function() {
    app.jqmInit();
    app.prefetchAll();
});

// Sync UI
function presync() {
    $('button.sync').html("Syncing...");
    $('li a.ui-icon-minus, li a.ui-icon-alert')
       .removeClass('ui-icon-minus')
       .removeClass('ui-icon-alert')
       .addClass('ui-icon-refresh');
}

function postsync(items) {
    $('button.sync').html("Sync Now");
    app.syncRefresh(items);
}

return ready;

});
