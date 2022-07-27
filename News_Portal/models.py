from django.db import models
from django.contrib.auth.models import User

article = 'AR'
news = 'NW'

TYPE_POST = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0,  db_column='rating')

    def update_rating(self):
        self.rating = 0
        for post in self.post_set.all():
            self.author_rating += post.post_rating * 3
            for other_comment in post.comment_set.exclude(user__username=self.user.username):
                self.author_rating += other_comment.comment_rating
        for comment in self.user.comment_set.all():
            self.author_rating += comment.comment_rating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=50, unique = True)


class Post(models.Model):
    type_post = models.CharField(max_length=2, choices=TYPE_POST)
    title_post = models.CharField(max_length=50)
    post = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    time_create = models.DateTimeField('time_create', auto_now_add=True)
    post_rating = models.IntegerField(default=0,  db_column='rating')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0, db_column='rating')

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()