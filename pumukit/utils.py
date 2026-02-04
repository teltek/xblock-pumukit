# -*- coding: utf-8 -*-
#

from datetime import datetime
import settings
import hashlib

from urllib.parse import quote

def get_hash(email, password, domain):
    """ Get hash of Pumukit user."""
    date = datetime.now().strftime('%d/%m/%Y')
    m = hashlib.md5("{email}{password}{date}{domain}".format(email=email, password=password, date=date, domain=domain))

    return m.hexdigest()


def get_manager_url(username, email):
    """ Get Pumukit Media Manager URL."""
    base_url = settings.BASE_URL
    sso_uri = settings.SSO_URI
    manager_uri = settings.MANAGER_URI

    password = settings.PASSWORD
    domain = settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{manager_uri}?hash={pumukit_hash}&username={username}&email={email}'.format(base_url=base_url, sso_uri=sso_uri, manager_uri=manager_uri, pumukit_hash=pumukit_hash, username=username, email=quote(email))

def get_iframe_url(video_id):
    """ Get Pumukit Iframe URL."""
    base_url = settings.BASE_URL
    iframe_uri = settings.IFRAME_URI
    password = settings.PASSWORD
    domain = settings.DOMAIN
    pumukit_hash = get_hash('', password, domain)
    if not video_id and settings.DEFAULT_VIDEO_ID:
        video_id = settings.DEFAULT_VIDEO_ID
    if not video_id:
        return False

    return '{base_url}/{iframe_uri}/?id={video_id}&hash={ph}'.format(base_url=base_url, iframe_uri=iframe_uri, video_id=video_id, ph=pumukit_hash)

def get_api_video_url(username, video_id):
    """ Get Pumukit API Video URL."""
    base_url = settings.BASE_URL
    sso_uri = settings.SSO_URI
    video_uri = settings.VIDEO_URI

    password = settings.PASSWORD
    domain = settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{video_id}/{video_uri}?hash={pumukit_hash}&username={username}'.format(base_url=base_url, sso_uri=sso_uri, video_id=video_id, video_uri=video_uri, pumukit_hash=pumukit_hash, username=username)

def get_personal_recorder_url(username, email):
    """ Get Pumukit Personal Recorder URL."""
    base_url = settings.BASE_URL
    sso_uri = settings.SSO_URI
    recorder_uri = settings.PERSONAL_RECORDER_URI

    password = settings.PASSWORD
    domain = settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{recorder_uri}?hash={pumukit_hash}&username={username}&email={email}'.format(base_url=base_url, sso_uri=sso_uri, recorder_uri=recorder_uri, pumukit_hash=pumukit_hash, username=username, email=quote(email))

def get_upload_url(username, email, lang):
    """ Get Pumukit Wizard Simple Upload URL."""
    base_url = settings.BASE_URL
    sso_uri = settings.SSO_URI
    upload_uri = settings.UPLOAD_URI

    password = settings.PASSWORD
    domain = settings.DOMAIN
    pumukit_hash = get_hash(username, password, domain)

    return '{base_url}/{sso_uri}/{upload_uri}?hash={pumukit_hash}&username={username}&email={email}&lang={lang}'.format(base_url=base_url, sso_uri=sso_uri, upload_uri=upload_uri, pumukit_hash=pumukit_hash, username=username, email=quote(email), lang=lang)
