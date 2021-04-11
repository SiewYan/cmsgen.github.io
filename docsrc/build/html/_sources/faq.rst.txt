FAQ
===

.. contents::
   :local:

Are there plans for an @app.route decorator like in Flask?
----------------------------------------------------------

As of aiohttp 2.3, :class:`~aiohttp.web.RouteTableDef` provides an API
similar to Flask's ``@app.route``. See
:ref:`aiohttp-web-alternative-routes-definition`.

Unlike Flask's ``@app.route``, :class:`~aiohttp.web.RouteTableDef`
does not require an ``app`` in the module namespace (which often leads
to circular imports).

Instead, a :class:`~aiohttp.web.RouteTableDef` is decoupled from an application instance::

   routes = web.RouteTableDef()

   @routes.get('/get')
   async def handle_get(request):
       ...


   @routes.post('/post')
   async def handle_post(request):
       ...

   app.router.add_routes(routes)


Does aiohttp have a concept like Flask's "blueprint" or Django's "app"?
-----------------------------------------------------------------------

If you're writing a large application, you may want to consider
using :ref:`nested applications <aiohttp-web-nested-applications>`, which
are similar to Flask's "blueprints" or Django's "apps".

See: :ref:`aiohttp-web-nested-applications`.


How do I create a route that matches urls with a given prefix?
--------------------------------------------------------------

You can do something like the following: ::

    app.router.add_route('*', '/path/to/{tail:.+}', sink_handler)

The first argument, ``*``,  matches any HTTP method
(*GET, POST, OPTIONS*, etc). The second argument matches URLS with the desired prefix.
The third argument is the handler function.


Where do I put my database connection so handlers can access it?
----------------------------------------------------------------

:class:`aiohttp.web.Application` object supports the :class:`dict`
interface and provides a place to store your database connections or any
other resource you want to share between handlers.
::

    async def go(request):
        db = request.app['db']
        cursor = await db.cursor()
        await cursor.execute('SELECT 42')
        # ...
        return web.Response(status=200, text='ok')


    async def init_app(loop):
        app = Application(loop=loop)
        db = await create_connection(user='user', password='123')
        app['db'] = db
        app.router.add_get('/', go)
        return app
