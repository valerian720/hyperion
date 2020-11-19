class ConsoleMacrosProcessor(object):
    service_mode = True
    # выставляется в положение "истина" путем определения ключевого слова
    # при значении "истина": 
    # - выводит дебаг информацию
    # - позволяет запустить утилиты для ручного редактирования знаний (mem[]) (?)
    def __init__(self, *args):
        super(ConsoleMacrosProcessor, self).__init__(*args))
        