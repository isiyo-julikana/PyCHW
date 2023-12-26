import file_handler
import Note
import note_builder

min_size = 3


def add():
    note = note_builder.create_note(min_size)
    array = file_handler.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_handler.write_file(array, 'a')
    print('Заметка успешно добавлена')


def show(text):
    logic = True
    array = file_handler.read_file()
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.info(notes))

        elif text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

        elif text == 'date':
            logic = False
            print('Дата создания: ' + Note.Note.get_date(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

    if logic == True:
        print('Сохраните новую заметку!')


def id_rewrite():
    id = input(
        'Выберете ID  заметки, которую Вы хотите перезаписать (ВНИМАНИЕ! прежняя информация в этой заметке сохранена не будет!): ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = note_builder.create_note(min_size)
            Note.Note.set_name(notes, note.get_name())
            Note.Note.set_content(notes, note.get_content())
            Note.Note.set_date(notes)
            print('Изменения в заметке успешно сохранены')
    if logic == True:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')


def id_delete():
    id = input('Введите ID заметки, которую хотите удалить (заметка не подлежит восстановлению): ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            prov = input('Подтвердите удаление заметки (y или n): ').strip().lower()
            if prov == 'y':
                array.remove(notes)
                print('Заметка успешно удалена')
            elif prov == 'n':
                print('Операция удаления заметки отменена')
    if logic == True:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')


def id_show():
    id = input('Введите ID необходимой заметки: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')


def date_show():
    date = input('Введите дату и время последнего редактирования: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if date == Note.Note.get_date(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')