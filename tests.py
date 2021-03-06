from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from captcha.conf import settings

from blog.models import BlogEntry

# Unit tests for Starcross Django Blog


class BlogTests(TestCase):

    test_title = "My new blog entry"
    test_entry = "<p>Welcome to my blog</p>"

    comment_name = "Mr nobody"
    comment_email = "foo@bar.com"
    comment_text = "<p>A great post!</p>"

    def setUp(self):
        self.blogentry = BlogEntry.objects.create(
            title=self.test_title,
            entry_text=self.test_entry,
            publication_status='published',
            date_published=timezone.now()
        )

    def test_blogentry_list(self):

        response = self.client.get(reverse('blog:blogentry_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_title)
        self.assertContains(response, self.test_entry)

    def test_blogentry_detail(self):
        response = self.client.get(reverse('blog:blogentry', kwargs={
            'pk': self.blogentry.pk,
            'slug': self.blogentry.title
        }))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_title)
        self.assertContains(response, self.test_entry)

    def test_entry_comment_form(self):

        settings.CAPTCHA_TEST_MODE = True

        response = self.client.post(
            reverse('blog:comment_form'), {
                'name': self.comment_name,
                'email': self.comment_email,
                'comment_text': self.comment_text,
                'entry': self.blogentry.pk,
                'captcha_0': 'abc',
                'captcha_1': 'passed'},
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.comment_name)
        self.assertContains(response, self.comment_text)
