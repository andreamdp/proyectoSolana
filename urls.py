from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
from clientes.models import Cliente
#from django.contrib.auth.views import login, logout
#from solanaABM import views
#from django.conf import settings
#from filebrowser.sites import site
from reportes.views import v_ListadoClientes,v_ListadoObras,v_ListadoCobros, v_ListadoCostos
#from clientes.views import detail, index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solanaABM010.views.home', name='home'),
    # url(r'^solanaABM010/', include('solanaABM010.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^reporteClientes/',v_ListadoClientes),
    url(r'^reporteObras/',v_ListadoObras),
    url(r'^reporteCobros/',v_ListadoCobros),
    url(r'^reporteCostos/',v_ListadoCostos),
    # Uncomment the next line to enable the admin:
    #url('^/$', redirect_to, {'url': '/admin', 'permanent': False}),
   # url(r'/$', include(admin.site.urls)),
   # url(r'^admin/treemenus/', include('treemenus.admin_urls')), 
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^login/', include(auth.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
   # url(r'^admin/filebrowser/', include(site.urls)),
   
)

    
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )



urlpatterns += patterns('',
    (r'^grappelli/', include('grappelli.urls')),
)

