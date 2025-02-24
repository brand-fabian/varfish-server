.. _admin_config:

====================
System Configuration
====================

This section describes how to configure the ``varfish-docker-compose`` setup.
When running with the ``varfish-docker-compose`` files and the provided database files, VarFish comes preconfigured with sensible default settings and also contains some example datasets to try out.
There are a few things that you might want to tweak.
Please note that there might be more settings that you can change when exploring the VarFish source code but right now their use is not supported for external users.

.. _admin_config_tls:

-----------------------
TLS / SSL Configuration
-----------------------

In the ``docker-compose.yml`` file you will find sections starting with ``# BEGIN`` and are followed by a token, e.g., ``settings:testing``, ``settings:production-provide-certificate``, and ``settings:production-letsencrypt``.
You will have to decide for one of the following and make sure that the lines for your choice are not commented out while all the others should be (in the case of ``OR`` leave the section in for all ``OR``-ed settings).

The ``varfish-docker-compose`` setup uses `traefik <https://traefik.io/>`__ as a reverse proxy and must be reconfigured if you want to change the default behaviour of using self-signed certificates.

``settings:testing``
    By default (and as a fallback), traefik will use self-signed certificates that are recreated at every startup.
    These are probably fine for a test environment but you might want to change this to one of the below.
``settings:production-provide-certificate``
    You can provide your own certificates by placing them into ````config/traefik/tls/server.crt`` and ``server.key``.
    Make sure to provide the full certificate chain if needed (e.g., for DFN issued certificates).
``settings:production-letsencrypt``
      If your site is reachable from the internet then you can also use ``settings:production-letsencrypt`` which will use [letsencrypt](https://letsencrypt.org/) to obtain the certificates.
      NB: if you make your site reachable from the internet then you should be aware of the implications.
      VarFish is MIT licensed software which means that it comes "without any warranty of any kind", see the ``LICENSE`` file for details.

After changing the configuration, restart the site (e.g., with ``docker-compose down && docker-compose up -d`` if it is running in detached mode).

------------------
LDAP Configuration
------------------

VarFish can be configured to use up to two upstream LDAP servers (e.g., OpenLDAP or Microsoft Active Directory).
For this, you have to set the following environment variables in the file ``.env`` in your ``varfish-docker-compose`` checkout and restart the site.
The variables are given with their default values.

``ENABLE_LDAP=0``
    Enable primary LDAP authentication server (values: ``0``, ``1``).
``AUTH_LDAP_SERVER_URI=``
    URI for primary LDAP server (e.g., ``ldap://ldap.example.com:port`` or ``ldaps://...``).
``AUTH_LDAP_BIND_DN=``
    Distinguished name (DN) to use for binding to the LDAP server.
``AUTH_LDAP_BIND_PASSWORD=``
    Password to use for binding to the LDAP server.
``AUTH_LDAP_USER_SEARCH_BASE=``
    DN to use for the search base, e.g., ``DC=com,DC=example,DC=ldap``
``AUTH_LDAP_USERNAME_DOMAIN=``
    Domain to use for user names, e.g. with ``EXAMPLE`` users from this domain can login with ``user@EXAMPLE``.
``AUTH_LDAP_DOMAIN_PRINTABLE=${AUTH_LDAP_USERNAME_DOMAIN}``
    Domain used for printing the user name.

If you have the first LDAP configured then you can also enable the second one and configure it.

``ENABLE_LDAP_SECONDARY=0``
    Enable secondary LDAP authentication server (values: ``0``, ``1``).

The remaining variable names are derived from the ones of the primary server but using the prefix ``AUTH_LDAP2`` instead of ``AUTH_LDAP``.

-----------------
Sending of Emails
-----------------

You can configure VarFish to send out emails, e.g., when permissions are granted to users.

``PROJECTROLES_SEND_EMAIL=0``
    Enable sending of emails.
``EMAIL_SENDER=``
    String to use for the sender, e.g., ``noreply@varfish.example.com``.
``EMAIL_SUBJECT_PREFIX=``
    Prefix to use for email subjects, e.g., ``[VarFish]``.
``EMAIL_URL=``
    URL to the SMTP server to use, e.g., ``smtp://user:password@mail.example.com:1234``.

------------------------
External Postgres Server
------------------------

In some setups, it might make sense to run your own Postgres server.
The most common use case would be that you want to run VarFish in a setting where fast disks are not available (virtual machines or in a "cloud" setting).
You might still have a dedicated, fast Postgres server running (or available as a service from your cloud provider).
In this case, you can configure the database connection settings as follows.

``DATABASE_URL=postgresql://postgres:password@postgres/varfish``
    Adjust to the credentials, server, and database name that you want to use.

The default settings do not make for secure settings in the general case.
However, Docker Compose will create a private network that is only available to the Docker containers.
In the default ``docker-compose`` setup, postgres server is thus not exposed to the outside and only reachable by the VarFish web server and queue workers.

.. _admin_config_misc:

---------------------------
Miscellaneous Configuration
---------------------------

``VARFISH_LOGIN_PAGE_TEXT=``
    Text to display on the login page.
``FIELD_ENCRYPTION_KEY``
    Key to use for encrypting secrets in the database (such as saved public keys for the Beacon Site feature).
    You can generate such a key with the following command: ``python -c 'import os, base64; print(base64.urlsafe_b64encode(os.urandom(32)))'``.

--------------------
Sentry Configuration
--------------------

`Sentry <https://sentry.io/welcome/>`__ is a service for monitoring web apps.
Their open source version can be installed on premise.
You can configure sentry support as follows

``ENABLE_SENTRY=0``
    Enable Sentry support.
``SENTRY_DSN=``
    A sentry DSN to report to.
    See Sentry documentation for details.

----------------------------------
System and Docker (Compose) Tweaks
----------------------------------

A number of customizations customizations of the installation can be done using Docker or Docker Compose.
Other customizations have to be done on the system level.
This section lists those that the authors are aware of but in particular network-related settings can be done on many levels.

Using Non-Default HTTP(S) Ports
===============================

If you want to use non-standard HTTP and HTTPS ports (defaults are 80 and 443) then you can tweak this in the ``traefik`` container section.
You have to adjust two parts.

.. code-block:: yaml

    ports:
      - "80:80"
      - "443:443"

To listen on ports ``8080`` and ``8443`` instead, adjust this to:

    ports:
      - "8080:80"
      - "8443:443"

Also, you have to change the command line arguments to traefik for the ``web`` (HTTP) and ``websecure`` (HTTPS) entrypoints.

.. code-block:: yaml

    - "--entrypoints.web.address=:80"
    - "--entrypoints.websecure.address=:443"

Change the lines to read:

.. code-block:: yaml

    - "--entrypoints.web.address=:8080"
    - "--entrypoints.websecure.address=:8443"

Then, restart by calling ``docker-compose up -d`` in the directory with the ``docker-compose.yml`` file.

Listing on Specific IPs
=======================

By default, the ``traefik`` container will listen on all IPs and interfaces of the host machine.

You can change this by prefixing the ``ports`` list with the IPs to listen on.
Change following lines to read:

.. code-block:: yaml

    ports:
      - "80:80"
      - "443:443"

To the following to only listen on ``10.0.0.1``.

.. code-block:: yaml

    ports:
      - "10.0.0.1:80:80"
      - "10.0.0.1:443:443"

More details can be found in the `corresponding section of the Docker Compose manual <https://docs.docker.com/compose/compose-file/compose-file-v3/#ports>`_.
Of course, you can combine this with adjusting the ports, e.g., to ``10.0.0.1:8080:80`` etc.

Limit Incoming Traffic
======================

In some settings you might want to limit incoming traffic to certain networks / IP ranges.
In principle, this is possible with adjusting the Traefik load balancer/reverse proxy.
However, we would recommend you to use the firewall of your operating system or your overall network for this purpose.
Consult the corresponding manual (e.g., of ``firewalld`` for CentOS/Red Hat or of ``ufw`` for Debian/Ubuntu) for instructions.
We remark that in most cases it is better to perform an actual separation of networks and place each (virtual) machine into one network only.

---------------------
Understanding Volumes
---------------------

The ``volumes`` sub directory of the ``varfish-docker-compose`` directory contains the data for the containers.
These are as follows.

``cadd-rest-api``
    Databases for variant annotation with CADD (large).

``exomiser``
    Databases for variant prioritization (medium)

``jannovar``
    Transcript databases for annotation (small).

``minio``
    Storage for files uploaded from client via REST API (big).

``postgres``
    PostgreSQL databases (very big).

``redis``
    Storage for the work queues (small).

``traefik``
    Configuration and certificates for load balancer (very small).

In principle, you can put these on different storages systems (e.g., some over the network and some on directly attached disks).
The main motivation is that fast storage is expensive.
Putting the small and medium sized directories on slower, cheaper storage will have little or no effect on storage efficiency.
At the same time, access to ``redis`` and ``exomiser`` directories should be fast.
As for ``postgres``, this storage is accessed most heavily and should be on storage as fast as you can afford.
``cadd-rest-api`` should also be on fast storage but it is accessed almost only read-only.
You can put the ``minio`` folder on slower storage to shave off some storage costs from your VarFish installation.

To summarize:

- You can put ``minio`` on cheaper storage.
- As for ``cadd-rest-api``, you can probably get away to put this on cheaper storage.
- Put everything else, in particular ``postgres`` on storage as fast as you can afford.

As described in the section :ref:`admin_tuning`, the authors recommend using an advanced file system such as ZFS on multiple SSDs for large, fast storage and enabling compression.
You will get excellent performance and can expect storage saving of 50%.

--------------------------
Beacon Site (Experimental)
--------------------------

An experimental support for the GA4GH beacon protocol.

``VARFISH_ENABLE_BEACON_SITE=``
    Whether or not to enable experimental beacon site support.

--------------------------
Undocumented Configuration
--------------------------

The following list remains a points to implement with Docker Compose and document.

- Kiosk Mode
- Updating Extras Data
