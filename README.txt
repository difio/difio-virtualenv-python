monupco.com registration agent for stand-alone Python virtualenv
applications.

It compiles a list of locally installed Python packages and sends it to
monupco.com.


Installing inside your virtualenv
---------------------------------

Create an account at <http://monupco.com>

Activate your virtualenv

::

    workon myapp

Install this package

::

    pip install monupco-virtualenv-python

Configure `$VIRTUAL_ENV/bin/postactivate` hook to contain
your Monupco userID (https://monupco-otb.rhcloud.com/profiles/mine/),
unique identifier for this application and a call to the registration script.

::

    echo "export MONUPCO_USER_ID=YourUserID"          >> $VIRTUAL_ENV/bin/postactivate
    echo "export MONUPCO_UUID=`uuidgen`"              >> $VIRTUAL_ENV/bin/postactivate
    echo "\$VIRTUAL_ENV/bin/monupco-virtualenv-python" >> $VIRTUAL_ENV/bin/postactivate

Activate your virtualenv again so that changes take place.

::

    workon myapp

If everything goes well you should see something like:

::

    Monupco: Success, registered/updated application with id 49


That's it, you can now check your application statistics at
<http://monupco.com>
