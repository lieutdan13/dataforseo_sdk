=====
Usage
=====

To use DataForSEO SDK in a project:

Note: These instructions assume that you are using GitBash in Windows.

#####################
Environment Variables
#####################

Start by setting environment variables to set your API credentials and location for saving API responses::

    #!/bin/env bash
    # Required
    export DFS_API_USERNAME="<Insert your Data for SEO API username>"
    export DFS_API_PASSWORD="<Insert your Data for SEO API password>"

    # Optional
    export DFS_DATA_DIR="C:\seo-data"  # Default is to store the data in the "_data" directory in the package itself
    export DFS_LOCALE="en_us"  # Default is "en_us"
    export DFS_API_DOMAIN="sandbox.dataforseo.com"  # Default is "api.dataforseo.com"

########
Services
########

Now import and use the available services.

*********************************
Locations, Locales, and Languages
*********************************

::

    >>> from dataforseo_sdk.locations.location_service import LocationService
    >>> ls = LocationService()
    >>> print(ls.locales)
    {'fr_dz': (2012, 'fr', 'DZ'), 'ar_dz': (2012, 'ar', 'DZ'), ... 'en_us': (2840, 'en', 'US'), ... 'es_ve': (2862, 'es', 'VE')}

******************
Competitor Service
******************

The Competitor Service can retrieve SEO competitors for a target domain::

    from dataforseo_sdk.competitors.competitor_service import CompetitorService
    cs = CompetitorService()
    print(cs.domain_competitors('example.com'))

***************
Keyword Service
***************

The Keyword Service can retrieve ranked keywords for a target domain::

    from dataforseo_sdk.keywords.keyword_service import KeywordService
    ks = KeywordService()
    print(ks.ranked_keywords('example.com'))