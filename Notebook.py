class Note(object):
    def __init__(self,content=None):
        self.content=content

    def write_content(self,content):
        self.content=content

    def remove_all(self):
        self.content=""

    def __add__(self, other):
        return self.content+other.content

    def __str__(self):
        return self.content

class NoteBook(object):
    def __init__(self,title):
        self.title=title
        self.page_number=1
        self.notes={}

    def add_note(self,note,page=0):
        if self.page_number<300:
            if page==0:
                self.notes[self.page_number]=note
                self.page_number+=1
            else:
                self.notes={page:note}
                self.page_number+=1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다")

    def get_number_of_pages(self):
        return len(self.notes.keys())

my_notebook=NoteBook("팀랩 강의노트")
new_note=Note("아 수업하기 싫다")
new_note2=Note("파이썬 강의")
my_notebook.add_note(new_note)
my_notebook.add_note(new_note2,100)

print(my_notebook.get_number_of_pages())
print(my_notebook.notes[100])

my_notebook.notes[2]=Note("안녕")
print(my_notebook.notes[2])
