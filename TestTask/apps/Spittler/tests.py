# coding: utf-8
"""
    Spittler Application Tests
"""

from django.template import Template, Context
from django_webtest import WebTest
from TestTask.apps.Spittler.models import Spittle


class SpittlerTest(WebTest):
    fixtures = [u'spittlers.json']

    def test_list_spittles(self):
        """ Test spittles listing page functionality """

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200, msg=u'Response is not OK')
        self.assertTemplateUsed(response, u'spittles.html')
        assert u'first spittle' in response
        assert u'second spittle' in response


class TemplateTagsTestCase(WebTest):
    fixtures = [u'spittlers.json']

    def setUp(self):
        self.spittles = Spittle.objects.all()

    def testRenderSpittle(self):
        """ Test custom spittle rendering tag functionality """

        t = Template('{% load render_spittle %}{% render_spittle identity %}')

        for spittle in self.spittles:
            c = Context({"identity": spittle.identity})
            value = t.render(c)

            assert spittle.title in value
            assert spittle.message in value



