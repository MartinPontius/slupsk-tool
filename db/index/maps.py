from django.conf import settings

basemaps = [
    {
        'name': "Stamen Terrain",
        'type': 'tile',
        'url': '//stamen-tiles-{s}.a.ssl.fastly.net/{layer}/{z}/{x}/{y}.jpg',
        'layer': 'terrain',
        'attribution': 'Map tiles by Stamen Design ...'
    }
];

index_map = [{
    'autoZoom' : False,
    'layers': [{
        'name': 'Kindergartens',
        'type': 'geojson',
        'url': 'kindergartens.geojson',
        'popup': 'kindergarten',
        'cluster' : True,
        'icon': 'kindergarten',
    },
    {
        'name': 'Shops',
        'type': 'geojson',
        'url': 'shops.geojson',
        'popup': 'shop',
        'cluster' : True,
        'icon' : 'shop',
    },
    {
    'name': 'Producers',
    'type': 'geojson',
    'url': 'producers.geojson',
    'popup': 'producer',
    'cluster' : True,
    'icon' : 'producer',
    }]
}]
