# coding: utf-8
"""
    Spittler Application Tests
"""
import os
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django_webtest import WebTest
from TestTask.apps.spittler.models import Spittle
from TestTask.settings import PROJECT_DIR


class SpittlerTest(WebTest):
    fixtures = [u'spittles.json']

    def testListSpittle(self):
        """ Test spittle listing page functionality """

        response = self.app.get(reverse('list_spittles'))

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

        page = self.app.get(reverse('add_spittle'))

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

        result_page = self.app.get(reverse('list_spittles'))

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

        response = self.app.get(reverse('list_spittles'))

        self.assertEqual(response.context['spittle_count'], self.count)
        assert self.count in response

        response = self.app.get(reverse('add_spittle'))

        self.assertEqual(response.context['spittle_count'], self.count)
        assert self.count in response

        spittle = Spittle()
        spittle.title = u'Title'
        spittle.message = u'New short spittle!'
        Spittle.save(spittle)

        response = self.app.get(reverse('list_spittles'))

        self.assertEqual(response.context['spittle_count'], self.count + 1)
        assert self.count + 1 in response


class WidgetTest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        self.spittle = Spittle.objects.all()

    def testDownload(self):
        """ Test widget download functionality """

        response = self.app.get(reverse('download_widget'))

        self.assertEqual(response.status_code, 200, msg=u'Download is not OK')
        self.assertTrue(len(response.content) > 0)

    def testWidget(self):
        """ Test widget functionality """

        response = self.app.get(reverse('get_widget'))

        self.assertTrue(self.spittle[0].title in response
                        or self.spittle[1].title in response)

        response = self.app.get(reverse('add_spittle'))

        self.assertTrue(self.spittle[0].title in response
                        or self.spittle[1].title in response)


class RestAPITest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        self.spittle = Spittle.objects.all()

    def testRandomSpittleCall(self):
        """ Test REST get random spittle functionality """

        response = self.app.get(reverse('rest_api'))

        self.assertEqual(response.status_code, 200, msg=u'REST spittle FAIL')
        self.assertTrue(len(response.content) > 0)
        self.assertTrue(self.spittle[0].title in response or
                        self.spittle[1].title in response)
        self.assertTrue(self.spittle[0].message in response or
                        self.spittle[1].message in response)


class ImageAttachmentTest(WebTest):
    fixtures = [u'spittles.json']

    def setUp(self):
        Spittle.objects.all().delete()

    def testImageAttached(self):
        """ Testing image to message attachment functionality """

        page = self.app.get(reverse('add_spittle'))

        add_form = page.form
        add_form['subject'] = 'Testing image'
        add_form['message'] = 'image attachment'
        add_form['file'] = [os.path.join(PROJECT_DIR,
                            'media/fbook_logo.png', )]

        add_form.submit()

        spittle = Spittle.objects.all()[0]
        result_page = page = self.app.get(reverse('list_spittles'))

        assert  spittle.identity in result_page

    def testNotImageAttached(self):
        """ Testing when attached file is not image functionality """

        page = self.app.get(reverse('add_spittle'))

        add_form = page.form
        add_form['subject'] = 'Testing image'
        add_form['message'] = 'image attachment'
        add_form['file'] = [os.path.join(PROJECT_DIR,
                            'media/not_an_image.txt', )]

        add_form.submit()

        spittle = Spittle.objects.all()
        result_page = page = self.app.get(reverse('list_spittles'))

        assert spittle.count() == 1
        assert  spittle[0].identity not in result_page







