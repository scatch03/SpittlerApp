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


class AddSpittleTestCase(WebTest):
    fixtures = [u'spittlers.json']

    def testAddSpittle(self):
        """ Test spittle adding functionality """

        page = self.app.get('/add/')

        add_form = page.form
        add_form['subject'] = ''
        add_form['message'] = ''
        result_page = add_form.submit()
        assert u'is required' in result_page

        add_form = page.form
        add_form['subject'] = 'test_case_subject'
        add_form['message'] = 'Short'
        result_page = add_form.submit()
        assert u'at least 10' in result_page
        assert u'is required' not in result_page

        add_form = page.form
        add_form['subject'] = 'test_case_subject'
        add_form['message'] = 'Long enough'
        result_page = add_form.submit().follow()
        assert u'at least 10' not in result_page
        assert u'required' not in result_page
        assert u'test_case_subject' in result_page
        assert u'Long enough' in result_page

