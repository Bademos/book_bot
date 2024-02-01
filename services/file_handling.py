import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер

def _get_part_text(text:str, start:int, page_size:int) -> tuple[str, int]:
    signs = [',' ,'.', '?', '!', ':', ';']
    pre_text = text[start:start + page_size]
    dct = {}
    lst = 0
    for sg in signs:
        dct[sg] = pre_text.rfind(sg)
        if dct[sg] > lst:
            lst = dct[sg]
    
    if (text[lst + 2] in signs) or (text[lst + 1] in signs):
        pre_text = pre_text[:lst-1]
        lst = 0
        for sg in signs:
            dct[sg] = pre_text.rfind(sg)
            if dct[sg] > lst:
                lst = dct[sg]
    
    pre_text = pre_text[:lst+1]
            
    
    return (pre_text, len(pre_text))

# Функция, формирующая словарь книги

def prepare_book(path: str) -> None:
    text = ""
    with open(path, "r" ,encoding="utf-8") as f:
        text = f.read()
    cnt = 1
    start = 0
    while cnt < (len(text)/PAGE_SIZE + 1):
        temp = _get_part_text(text,start,PAGE_SIZE)
        start = start + temp[1]
        string = temp[0].lstrip()
        #print(string)
        book[cnt]= string
        cnt += 1
        

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))