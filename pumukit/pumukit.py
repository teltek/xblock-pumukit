"""Xblock for Pumukit integration"""

from importlib.resources import files

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope

from django.conf import settings

from .utils import get_manager_url, get_iframe_url, get_api_video_url, get_personal_recorder_url, get_upload_url
from .connections import get_json_response
from .render_utils import render_template

from . import settings as pmk_settings

import logging

log = logging.getLogger(__name__)

@XBlock.needs("user")
class PumukitXBlock(XBlock):
    """
    Xblock for Pumukit integration
    """

    display_name = String(
        display_name="Display Name",
        help="Display name for this module in case the source video doesn't have any.",
        default="Pumukit module",
        scope=Scope.settings
    )

    video_id = String(
        display_name="Video ID",
        help="Video ID of the Pumukit Multimedia Object.",
        default="",
        scope=Scope.settings
    )

    video_title = String(
        display_name="Video Title",
        help="Video Title of the Pumukit Multimedia Object.",
        default="",
        scope=Scope.settings
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return files(__package__).joinpath(path).read_text(encoding="utf-8")

    def student_view(self, context=None):
        """
        The primary view of the PumukitXBlock, shown to students
        when viewing courses.
        """
        try:
            pumukit_url = get_iframe_url(self.video_id)
            content = render_template('static/html/pumukit.html', {
                'self': self,
                'pumukit_url': pumukit_url,
            })
            frag = Fragment(content)
            frag.add_css(self.resource_string("static/css/pumukit.css"))
            frag.add_javascript(self.resource_string("static/js/src/pumukit.js"))
            frag.initialize_js('PumukitXBlock')
        except Exception as exc:
            html = self.resource_string("static/html/pumukit_error.html")
            error_message = "{}".format(exc)
            frag = Fragment(html.format(error_message=error_message))

        return frag

    def studio_view(self, context):
        """
        Editing view in Studio
        """
        try:
            user = self._get_logged_in_user()
            username = user.opt_attrs['edx-platform.username']
            email = user.emails[0]

            language = settings.LANGUAGE_CODE
            lang = language[:2]

            upload_url = get_upload_url(username, email, lang)
            recorder_url = get_personal_recorder_url(username, email)
            pumukit_url = get_manager_url(username, email)

            show_url_tab = pmk_settings.SHOW_URL_TAB
            show_upload_tab = pmk_settings.SHOW_UPLOAD_TAB
            show_recorder_tab = pmk_settings.SHOW_RECORDER_TAB
            show_library_tab = pmk_settings.SHOW_LIBRARY_TAB

            content = render_template('static/html/pumukit_edit.html', {
                'self': self,
                'upload_url': upload_url,
                'recorder_url': recorder_url,
                'pumukit_url': pumukit_url,
                'show_url_tab': show_url_tab,
                'show_upload_tab': show_upload_tab,
                'show_recorder_tab': show_recorder_tab,
                'show_library_tab': show_library_tab,
            })
            frag = Fragment(content)
            frag.add_css(self.resource_string("static/css/pumukit_edit.css"))
            frag.add_css(self.resource_string("static/css/pumukit_select.css"))
            frag.add_javascript(self.resource_string("static/js/src/pumukit_edit.js"))
            frag.initialize_js('PumukitEdit')
        except Exception as exc:
            html = self.resource_string("static/html/pumukit_error.html")
            error_message = "{}".format(exc)
            frag = Fragment(html.format(error_message=error_message))

        return frag

    def _get_logged_in_user(self):
        user_service = self.runtime.service(self, 'user')
        user = user_service.get_current_user()

        return user

    @XBlock.json_handler
    def submit(self, data):
        """
        Submits all data to pumukit server
        """
        video_id = data['video_id']
        if video_id == self.video_id:
            return {
                'result': 'success',
            }

        try:
            self.video_id = video_id
            self.video_title = ''
        except Exception as exc:
            log.error('Exception: {}'.format(exc))
            return {
                'result': 'error',
                'message': 'error on saving data',
            }

        try:
            user = self._get_logged_in_user()
            username = user.opt_attrs['edx-platform.username']
            email = user.emails[0]

            username = self._get_logged_in_user()
            pumukit_url = get_api_video_url(username, video_id)

            language = settings.LANGUAGE_CODE
            lang = language[:2]

            response = get_json_response(pumukit_url)
            self.video_title = response.get('title').get(lang)
        except Exception as exc:
            log.error('Exception: {}'.format(exc))
            self.video_title = ''

        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PumukitXBlock",
             """<pumukit/>
             """),
        ]
