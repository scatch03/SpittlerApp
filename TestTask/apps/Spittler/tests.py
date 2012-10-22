# coding: utf-8
"""
    Spittler Application Tests
"""

from django.template import Template, Context
from django_webtest import WebTest
from TestTask.apps.Spittler.models import Spittle


class SpittlerTest(WebTest):
    fixtures = [u'spittles.json']

    def testListSpittle(self):
        """ Test spittle listing page functionality """

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200, msg=u'Response is not OK')
        self.assertTemplateUsed(response, u'spittles.html')
        assert u'first spittle' in response
        assert u'second spittle' in response


class TemplateTagsTestCase(WebTest):
    fixtures = [u'spittles.json']

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
    fixtures = [u'spittles.json']

    def setUp(self):
        self.count = Spittle.objects.all().count()

    def testAddSpittle(self):
        """ Test spittle adding functionality """

        page = self.app.get('/add/')

        add_form = page.form
        add_form['subject'] = ''
        add_form['message'] = ''
        result_page = add_form.submit()
        assert u'is required' in result_page

        add_form = page.form
        add_form['subject'] = 'Test case subject'
        add_form['message'] = 'Short'
        result_page = add_form.submit()
        assert u'at least 10' in result_page
        assert u'is required' not in result_page

        add_form = page.form
        add_form['subject'] = 'Test case subject'
        add_form['message'] = 'Long enough'
        result_page = add_form.submit()

        assert Spittle.objects.all().count() - self.count == 1

        result_page = self.app.get('/')

        assert u'at least 10' not in result_page
        assert u'required' not in result_page
        assert u'Test case subject' in result_page
        assert u'Long enough' in result_page


class CountContextProcessorTest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        self.count = Spittle.objects.all().count()

    def testCountSpittle(self):
        """ Test spittle count functionality """

        response = self.app.get('/')

        self.assertEqual(response.context['spittle_count'], self.count)
        assert self.count in response

        response = self.app.get('/add/')

        self.assertEqual(response.context['spittle_count'], self.count)
        assert self.count in response

        spittle = Spittle()
        spittle.title = u'Title'
        spittle.message = u'New short spittle!'
        Spittle.save(spittle)

        response = self.app.get('/')

        self.assertEqual(response.context['spittle_count'], self.count + 1)
        assert self.count + 1 in response


class WidgetTest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        self.spittle = Spittle.objects.all()

    def testDownload(self):
        """ Test widget download functionality """

        response = self.app.get('/download/')

        self.assertEqual(response.status_code, 200, msg=u'Download is not OK')
        self.assertTrue(len(response.content) > 0)

    def testWidget(self):
        """ Test widget functionality """

        response = self.app.get('/widget/')

        self.assertTrue(self.spittle[0].title in response
                        or self.spittle[1].title in response)

        response = self.app.get('/add/')

        self.assertTrue(self.spittle[0].title in response
                        or self.spittle[1].title in response)


class RestAPITest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        self.spittle = Spittle.objects.all()

    def testRandomSpittleCall(self):
        """ Test REST get random spittle functionality """

        response = self.app.get('/rest/spittle/')

        self.assertEqual(response.status_code, 200, msg=u'REST spittle FAIL')
        self.assertTrue(len(response.content) > 0)
        self.assertTrue(self.spittle[0].title in response or
                        self.spittle[1].title in response)
        self.assertTrue(self.spittle[0].message in response or
                        self.spittle[1].message in response)









