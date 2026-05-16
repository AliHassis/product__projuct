import random
coderandom=random.randint(1000,9999)    

code=int(input("enter a 4 digit PIN codz:\n"))

if len(str(code))!=4:
    print("enter 4 gigit!")    
elif code==coderandom:
    print("nice")    
else:
    print("PIN code did not match")
    print(f"the computer generated thi PIN : {coderandom}")
    # بنفعش تقلو فوق عند اول شرط اذا الكود يساوي اربعة اظهر رسالة الرقم ليس صحيح الكومبيوتر ادخل هذا الكود لانو في هاي الحالة حتى لو المستخدم ادخل الكود الصح 
    # راح تظهر نفس الرسالة لانو تحقق الشرط انه ادخل اربع ارقام مش راح يشوف الحالة الثانية الي تحت الي تحقق فيها الشرط الي ادخل فيها كود مطابق 