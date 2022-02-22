from django.test import Client, TestCase
from django.urls import reverse

from ..forms import PostForm
from ..models import Post, Group, User
from ..views import PAGE_COUNT

PAGE = 14


class PostPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            group=cls.group,
            text='Текст'
        )

    def setUp(self):
        # Создаём неавторизованный клиент
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(PostPagesTests.user)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_pages_names = {
            reverse('posts:index'): 'posts/index.html',
            reverse(
                'posts:group_list', kwargs={'slug': self.group.slug}
            ): 'posts/group_list.html',
            reverse(
                'posts:profile', kwargs={'username': self.user.username}
            ): 'posts/profile.html',
            reverse(
                'posts:post_detail', kwargs={'post_id': self.post.id}
            ): 'posts/post_detail.html',
            reverse(
                'posts:post_edit', kwargs={'post_id': self.post.id}
            ): 'posts/create.html',
            reverse('posts:post_create'): 'posts/create.html'
        }
        for reverse_name, template in templates_pages_names.items():
            with self.subTest(template=template):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_index_correct_context(self):
        """Шаблон home сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse('posts:index'))
        self.assertIn('page_obj', response.context)
        object = response.context['page_obj'][0]
        self.assertEqual(object, self.post)

    def test_group_list_correct_context(self):
        """Шаблон group_list сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse(
            'posts:group_list', kwargs={'slug': self.group.slug})
        )
        self.assertIn('group', response.context)
        object = response.context['group']
        text = response.context['page_obj'][0].text
        group = response.context['page_obj'][0].group.title
        self.assertEqual(object, self.group)
        self.assertEqual(text, self.post.text)
        self.assertEqual(group, self.group.title)

    def test_profile_correct_context(self):
        """Шаблон profile сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse(
            'posts:profile', kwargs={'username': self.user.username})
        )
        object = response.context['author']
        self.assertEqual(object, self.post.author)

    def test_post_detail_correct_context(self):
        """Шаблон post_detail сформирован с правильным контекстом."""
        response = (self.authorized_client.get(reverse(
            'posts:post_detail', kwargs={'post_id': self.post.pk}))
        )
        post = response.context['post']
        author = self.post.author
        group = self.group
        text = self.post.text
        self.assertEqual(author, post.author)
        self.assertEqual(text, post.text)
        self.assertEqual(group, post.group)

    def test_create_correct_context(self):
        """Шаблон create сформирован с правильным контекстом."""
        response = (self.authorized_client.get(reverse('posts:post_create')))
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertIsInstance(form, PostForm)

    def test_post_edit_correct_context(self):
        """Шаблон post_edit сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse(
            'posts:post_edit', kwargs={'post_id': self.post.pk}))
        object = response.context['form'].initial['text']
        self.assertEqual(object, self.post.text)


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        for i in range(1, PAGE):
            cls.post = Post.objects.create(
                author=cls.user,
                text=f'{i} Тестовый пост',
                group=cls.group,
            )

    def test_index_first_page(self):
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(len(response.context['page_obj']), PAGE_COUNT)

    def test_index_second_page(self):
        response = self.client.get(reverse('posts:index') + '?page=2')
        second_page = Post.objects.count() % PAGE_COUNT
        self.assertEqual(len(response.context['page_obj']), second_page)

    def test_group_list_first_page(self):
        response = self.client.get(
            reverse('posts:group_list', kwargs={'slug': 'test-slug'})
        )
        self.assertEqual(len(response.context['page_obj']), PAGE_COUNT)

    def test_group_list_second_page(self):
        response = self.client.get(reverse(
            'posts:group_list', kwargs={'slug': 'test-slug'}) + '?page=2')
        second_page = Post.objects.count() % PAGE_COUNT
        self.assertEqual(len(response.context['page_obj']), second_page)

    def test_profile_first_page(self):
        response = self.client.get(
            reverse('posts:profile', kwargs={'username': self.user.username})
        )
        self.assertEqual(len(response.context['page_obj']), PAGE_COUNT)

    def test_profile_second_page(self):
        response = self.client.get(reverse(
            'posts:profile', kwargs={'username': self.user.username}
        ) + '?page=2')
        second_page = Post.objects.count() % PAGE_COUNT
        self.assertEqual(len(response.context['page_obj']), second_page)
