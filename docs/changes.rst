Changes & News
--------------

0.3.2
~~~~~

* Limited display of request querystring in admin screen to 50 characters

0.3.1
~~~~~

* Fixed 250 character limitation for querystring in Recorded Request 
  (`issue #2 <http://bitbucket.org/yvandermeer/django-http-proxy/issue/2/>`_)
* Added new Request Parameter model; requires ``./manage.py reset httpproxy && ./manage.py syncdb``

0.3
~~~

* Fixed Python 2.5 support by removing use of ``__package__``
* Implemented request path "normalization", fixing record and playback if the
  proxy is URL-configured anywhere other than directly in the root.
* Added experimental ``PROXY_REWRITE_RESPONSES`` settings to fix paths to
  resources (images, javascript, etc) on the same domain if ``httproxy`` is
  not configured at the root.

0.2.2
~~~~~

* Removed print statement I accidentally left behind.

0.2.1
~~~~~

* Fixed `issue #1 <http://bitbucket.org/yvandermeer/django-http-proxy/issue/1/>`_;
  Unsupported content types are now silently ignored.
* Added ``PROXY_IGNORE_UNSUPPORTED`` setting to control the behavior for
  handling unsupported responses (see :doc:`settings`).

0.2
~~~

* Added recording and playback functionality (see the new :ref:`setting-proxy-mode` setting)
* Improved handling of ``httpproxy``-specific settings
* Started using Sphinx for documentation

0.1
~~~

* Initial release
* Basic HTTP proxy functionality based on `a blog post by Will Larson <http://lethain.com/entry/2008/sep/30/suffer-less-by-using-django-dev-server-as-a-proxy/>`_
