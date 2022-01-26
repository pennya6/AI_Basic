import os
# os.mkdir("test")

try:
    os.mkdir("test")
except FileExistsError as e:
    print("Already created")

#shutil.copy : 파일 복사 함수
#기존에 내가 파일처리 하던 방식대로 하면 안된다. 문제가 있을수 있으니 리룩스를 통해서 관리해야함
import shutil
source="data/i_have_a_dream2.txt"
dest=os.path.join("test","sunghucl.txt")
print(dest)
shutil.copy(source,dest)