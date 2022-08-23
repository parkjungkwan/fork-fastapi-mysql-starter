from app.models import Book, User
from app.database import SessionLocal

db = SessionLocal()


def seed():
    book_titles = [
        '딥러닝 기초',
        '텐서플로 튜토리얼',
        '파이토치 개론'
    ]
    books = [Book(title=title) for title in book_titles]

    user = User(username='hong-gildong')
    user.books = books

    db.add(user)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
