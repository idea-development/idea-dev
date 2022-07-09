# zinc
# idea-dev


#Heroku update stack
### heroku stack:set heroku-22 -a


##Debugging
If collectstatic failed during a build, a traceback was provided that will be helpful in diagnosing the problem. If you need additional information about the environment collectstatic was run in, use the DEBUG_COLLECTSTATIC configuration.

heroku config:set DEBUG_COLLECTSTATIC=1
This will display in your build output all of the environment variables that were available to Python when the collectstatic command was executed.

##Disabling Collectstatic
Sometimes, you may not want Heroku to run collectstatic on your behalf. You can disable the collectstatic build step with the DISABLE_COLLECTSTATIC configuration:

heroku config:set DISABLE_COLLECTSTATIC=1
This will fully disable the collectstatic step of the build.

###Specifying a Python version
By default, newly created Python apps use the python-3.10.5 runtime. You can also specify a different supported Python version.

Supported runtimes