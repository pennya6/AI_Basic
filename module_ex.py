# import fah_converter
#Alias 설정 - 모듈명을 별칭으로 써서 사용
import fah_converter as fah

if __name__=="__main__":
    print("Enter a celcius value : ")
    celcius=float(input())
    fah=fah.convert_c_to_f(celcius)
    print("That's {0} degreees ".format(fah))