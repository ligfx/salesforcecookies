# codec: utf-8

import browsercookie
import logging
import re

_logger = logging.getLogger(__name__)

def get_instance_url_and_session():
    cookies = browsercookie.chrome()
    sids = [c for c in cookies if c.name == 'sid' and re.search(r'salesforce.com', c.domain)]
    if len(sids) == 0:
        raise Exception("Couldn't find any `sid` cookie for a `salesforce.com` domain; please log in to Salesforce with Chrome, and wait up to 30 seconds.")
    if len(sids) > 1:
        raise Exception("Found multiple `sid` cookies:" + "".join("\n{} {}".format(c.domain, c.value) for c in sids))
    instance_url = 'https://' + sids[0].domain
    session_id = sids[0].value
    _logger.info("Found instance_url ({}) and session_id".format(instance_url, session_id))
    return (instance_url, session_id)

