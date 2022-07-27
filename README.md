
#Создать двух пользователей (с помощью метода User.objects.create_user('username')).

User.objects.create_user('Иванов Петр Сидорович')
User.objects.create_user('Николаев Олег Владимирович')


#Создать два объекта модели Author, связанные с пользователями.

Author.objects.create(user_id=1)
Author.objects.create(user_id=2)

# Добавить 4 категории в модель Category.

Category.objects.create(category='Интересное')
Category.objects.create(category='Наука')
Category.objects.create(category='События')
Category.objects.create(category='Люди')

# Добавить 2 статьи и 1 новость

Post.objects.create(type_post='AR',title_post='Изобретен робот-мойщик посуды',post='Изобретен робот-мойщик посуды', author_id=1)
Post.objects.create(type_post='AR',title_post='Илья Муромец',post='Прозаические рассказы об Илье Муромце, записанные в виде русских народных сказок и перешедшие к некоторым неславянским народам (финнам), не знают о киевских былинных отношениях Ильи Муромца, не упоминают князя Владимира, заменяя его безымянным королём; содержат они почти исключительно похождение Ильи Муромца с Соловьём-разбойником, иногда и с Идолищем, называемым Обжорой, и приписывают иногда Илье Муромцу освобождение царевны от змея', author_id=2)
Post.objects.create(type_post='NW',title_post='Парад победы',post='9 мая на Дворцовой площади пройдет парад, посвященный победе в ВОВ', author_id=1)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий)

PostCategory.objects.create(post_id=1,category_id=1)
PostCategory.objects.create(post_id=1,category_id=2)
PostCategory.objects.create(post_id=2,category_id=4)
PostCategory.objects.create(post_id=3,category_id=3)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

Comment.objects.create(post_id=1, user_id=2, comment='Брехня!')
Comment.objects.create(post_id=1, user_id=1, comment='Чистая правда! Я уже себе купил!')
Comment.objects.create(post_id=2, user_id=1, comment='Вот больше писать не о чем!')
Comment.objects.create(post_id=3, user_id=2, comment='Как обычно! Все стандартно!')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

p=Post.objects.get(pk=1)
p.like() - 3 times
p.post_rating

p=Post.objects.get(pk=2)
p.like() - 5 times
p.dislike() - 2 times
p.post_rating

p=Post.objects.get(pk=3)
p.like() - 10 times
p.dislike() - 4 times
p.post_rating

c=Comment.objects.get(pk=1)
c.like() - 12 times
c.comment_rating

c=Comment.objects.get(pk=2)
c.like() - 7 times
c.dislike()
c.comment_rating

c=Comment.objects.get(pk=3)
c.like() - 4 times
c.dislike() - 2 times
c.comment_rating

c=Comment.objects.get(pk=4)
c.like() - 6 times
c.dislike() - 3 times
c.comment_rating

# Обновить рейтинги пользователей.

auth = Author.objects.get(pk=1)
auth.update_rating()
auth.author_rating

auth = Author.objects.get(pk=2)
auth.update_rating()
auth.author_rating

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).

Author.objects.all().order_by('-author_rating').values('user__username', 'author_rating').first()

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

Post.objects.all().order_by('-post_rating')
ps=Post.objects.get(pk=3)
Post.objects.all().values('time_create','author__user__username', 'post_rating', 'title_post')
ps.preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

Comment.objects.filter(post__id=3).values('date_create', 'user', 'comment_rating', 'comment')
