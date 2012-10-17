# coding: utf-8
"""
    Spittler Application Tests
"""

from django_webtest import WebTest


class SpittlerTest(WebTest):
    fixtures = [u'spittlers.json']

    def test_list_spittles(self):
        """ Test spittles listing page functionality """

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200, msg=u'Response is not OK')
        self.assertTemplateUsed(response, u'spittles.html')
        assert u'first spittle' in response
        assert u'second spittle' in response

