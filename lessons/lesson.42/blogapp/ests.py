from django.test import TestCase
from .models import Post, Author
from django.urls import reverse

# Create your tests here.

class TestBlogapp(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='test_author',
            age=20,
            email='test@mail.ru',
            bio='test bio'
        )

    def test_post_create(self):
        """
        Test post create
        :return:
        """
        post_data = {
            'title': 'test_title',
            'content': 'test_content',
            'author': self.author,
            'category': 'test_category',
            'is_published': True,
            'published_date': '2022-01-01',
        }

        response = self.client.post(reverse('post_create'), data=post_data)
        #
        self.assertEqual(response.status_code, 200)
        #
        # self.assertEqual(Post.objects.count(), 5)



        # self.post = Post.objects.create(
        #     title='test_title',
        #     content='test_content',
        #     author=self.author,
        #     category='test_category',
        #     is_published=True,
        #     published_date='2022-01-01'
        # )
        #
        # self.post_2 = Post.objects.create(
        #     title='test_title2',
        #     content='test_content2',
        #     author=self.author,
        #     category='test_category2',
        #     is_published=True,
        #     published_date='2022-01-11'
        # )


    # def tearDown(self):
    #     Post.objects.all().delete()
    #     Author.objects.all().delete()


class PostListViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='test_author',
            age=20,
            email='test@mail.ru',
            bio='test bio'
        )

        self.post = Post.objects.create(
            title='test_title',
            content='test_content',
            author=self.author,
            category='test_category',
            is_published=True,
            published_date='2022-01-01'
        )

        self.post_2 = Post.objects.create(
            title='test_title2',
            content='test_content2',
            author=self.author,
            category='test_category2',
            is_published=True,
            published_date='2022-01-11'
        )


    def test_post_list_view(self):
        """
        Test post list view
        :return:
        """
        response = self.client.get(reverse('post_list'))
        #
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'blogapp/post_list.html')

        self.assertIn('posts', response.context)

        self.assertEqual(len(response.context['posts']), Post.objects.count())


        #
        # self.assertEqual(Post.objects.count(), 5)

    # def tearDown(self):
    #     Post.objects.all().delete()
    #     Author.objects.all().delete()

