from peewee import SqliteDatabase, Model, IntegerField, TextField
from playhouse.migrate import SqliteMigrator


connection = SqliteDatabase('girl_sms_bot.sqlite')
migrator = SqliteMigrator(connection)


class BaseModel(Model):
    class Meta:
        database = connection


class User(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    user_id = IntegerField(column_name='user_id', unique=True)
    user_step = IntegerField(column_name='user_step')

    @staticmethod
    def add_new_user(user_id: int) -> None:
        User.insert(user_id=user_id)

    @staticmethod
    def get_all_users_ids() -> list:
        return [user_id['user_id'] for user_id in User.select(User.user_id).dicts().execute()]

    class Meta:
        table_name = 'User'


class Phrases(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    phrase = TextField(column_name='phrase')

    @staticmethod
    def delete_phrase(phrase_id: int) -> None:
        Phrases.delete_by_id(phrase_id)

    @staticmethod
    def add_phrase(phrase_text: str) -> None:
        Phrases.insert(phrase=phrase_text)

    @staticmethod
    def get_all_phrases(only_phrase: bool = False) -> list:
        if only_phrase:
            return [phrase_obj.phrase for phrase_obj in Phrases.select()]
        else:
            return [(phrase_obj.id, phrase_obj.phrase) for phrase_obj in Phrases.select()]

    @staticmethod
    def format_all_phrases(phrases: list) -> str:
        return ''.join([f'*{phrase[0]}. {phrase[1]}*\n' for phrase in phrases])+'\n'


connection.create_tables([User, Phrases])
print('Database is ready to use')
