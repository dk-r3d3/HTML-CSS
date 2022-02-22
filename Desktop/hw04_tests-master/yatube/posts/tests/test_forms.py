from django.test import TestCase, Client, override_settings
from django.urls import reverse

from ..models import Post, Group, User


@override_settings()
class PostCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='UserName')
        cls.group = Group.objects.create(
            title='Тестовый заголовок',
            slug='test-slug',
            description='Тестовый текст',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            group=cls.group,
            text='Тестовый заголовок',
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_form_create(self):
        """Валидная форма создает пост."""
        post_count = Post.objects.count()
        form_data = {
            'text': self.post.text,
            'group': self.group.id,
        }
        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response, reverse(
            'posts:profile', kwargs={'username': self.user.username}))
        self.assertEqual(Post.objects.count(), post_count + 1)
        current_post = Post.objects.latest('pub_date')
        self.assertEqual(
            current_post.text, form_data['text']
        )
        self.assertEqual(
            current_post.group, self.group
        )
        self.assertEqual(
            current_post.author, self.user
        )

    def test_post_edit(self):
        """При отправке валидной формы пост редактируется."""
        text_edit = 'Отредактированный текст'
        form_data = {
            'text': text_edit,
            'group': self.group.id,
        }
        response_1 = self.authorized_client.post(
            reverse('posts:post_edit',
                    kwargs={'post_id': self.post.id}),
            data=form_data,
            follow=True
        )
        self.assertRedirects(response_1, reverse(
            'posts:post_detail', kwargs={
                'post_id': self.post.id
            }),
        )

        current_post = Post.objects.latest('pub_date')
        self.assertEqual(
            current_post.text, form_data['text']
        )
        self.assertEqual(
            current_post.group, self.group
        )
        self.assertEqual(
            current_post.author, self.user
        )

    def test_guest_can_not_create_new_post(self):
        """неавторизованный пользователь не может создать пост"""
        posts_count = Post.objects.count()
        response = self.guest_client.post(
            reverse('posts:post_create'),
            follow=True)
        self.assertRedirects(response, '/auth/login/?next=/create/')
        self.assertEqual(posts_count, Post.objects.count())