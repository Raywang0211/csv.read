import os
import csv
import numpy as np

#
# #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VL 可見光黑較白較擷取的程式片段
IN_dirPath = r"C:\Users\Raywang\Desktop\new" #校正的file的檔案路徑

#資料夾路徑
files=os.listdir(IN_dirPath)
#獲取資料夾內所有的檔名
print(files)
IN_my_array = np.zeros((1344, len(files)), float) #儲存黑校白校的矩陣 要改矩陣大小
for i in range(len(files)):
    num = 0
    f=open(os.path.join(IN_dirPath,files[i]),'r',encoding="utf-8") #開啟檔案(path.join(合成路徑+檔名))
    print(os.path.join(IN_dirPath,files[i]))
    print('*' * 30, 'Currently working space=> ', os.path.join(IN_dirPath, files[i]), '*' * 30)
    reader = csv.reader(f)

    for line in reader: #讀取特定某一行後面所有的資料
        num += 1
        if num >20:

            for row, rowValue in enumerate(reader):
                # print('ROW {:<5} I {:<5}'.format(row,i))

                IN_my_array[row][i] = float(rowValue[1])
    print("CAPTURE FINISH")


f.close()
# print(IN_my_array)
np.savetxt('base_Light.csv', IN_my_array, delimiter=',') #轉存成.CSV檔<<要將校正的檔案分成兩個檔案dark light---因為csv.read一次只能執行一次，結束無法重複>> 要改檔案名稱


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// VL 資料讀取轉換程式
#
# dirPath = r"C:\Users\Raywang\Desktop\tomato\20190417(VL)fungus\sick\12"  #VL 資料讀取並且轉成 excel的來源路徑
# INN_dirPath = r"C:\Users\Raywang\Desktop\tomato\20190417(VL)fungus\base" #校正的file的檔案路徑
#
# files=os.listdir(dirPath)                                   #資料來源個數
# INN_files = os.listdir(INN_dirPath)                         #校正資料來源個數
#
# #因為資料夾裡面有一個 windows系統檔 所以要事先篩選掉
# CSV_File = []
# for i in files:
#     if i.endswith('.csv'):
#         CSV_File.append(i)
#
# print(len(CSV_File))
#
# IN_my_array = np.zeros((1323, 2), float)                    #創建一個矩陣放入 黑校正、白校正 以便計算
# N=0  #為了將輸入excel存入矩陣而設N為<排>
# for IN_Files_No in range(len(INN_files)):
#     IN_f = open(os.path.join(INN_dirPath,INN_files[IN_Files_No]),'r',encoding='utf-8')
#     IN_reader=csv.reader(IN_f)
#     print('*' * 30, 'Currently working space=> ', os.path.join(INN_dirPath, INN_files[IN_Files_No]), '*' * 30)
#     for row,line in enumerate(IN_reader):
#         IN_my_array[row][N] = float(line[0])
#     N+=1
#
# print("IN_my_array==",IN_my_array)
# IN_f.close()
# VL_my_array = np.zeros((1323, len(CSV_File)), float) #宣告 VL 資料儲存矩陣
# # print(len(CSV_File))
# # print(CSV_File)
# for i in range(len(CSV_File)):
#     num = 0
#     print('*'*30, 'Currently working space=> ', os.path.join(dirPath,CSV_File[i]), '*'*30)
#     f = open(os.path.join(dirPath,CSV_File[i]),'r',encoding='utf-8') #開啟檔案(path.join(合成路徑+檔名)) encoding='gbk'<可以讀取文字>
#     reader=csv.reader(f)
#     for line in reader: #讀取特定某一行後面所有的資料
#         num += 1
#
#         if num >20:
#
#             for row, rowValue in enumerate(reader):
#
#                 VL_my_array[row][i] = (float(rowValue[2])-IN_my_array[row][0])/(IN_my_array[row][1]-IN_my_array[row][0])
#                 # print((float(rowValue[2])-IN_my_array[row][0])/(IN_my_array[row][1]-IN_my_array[row][0]))
#
#
#     f.close()
# # print(VL_my_array)
# my_array_name = np.array(CSV_File)
# c = np.vstack((my_array_name,VL_my_array))
# print("=========",c)
# # print(type(c[5][0]))
# np.savetxt('20190417(VL)fungus_sick_12.csv', c,fmt='%s', delimiter=',') #輸出成csv檔
# print('*'*30,"SAVE FINISH",'*'*30)
# #
#




#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// NIL 資料讀取轉換程式片段
#
# dirPath = r"C:\Users\Raywang\Desktop\tomato\20190417(NIL)fungus\sick\12"  # NIL 讀取檔案來源
#
# #資料夾路徑
# files=os.listdir(dirPath)
# #獲取資料夾內所有的檔名
# print(files)
# print(type(files))
#
# my_array = np.zeros((228, len(files)),float)         #宣告一個矩陣準備放入NIL 所有資料
# print(len(files))
# for i in range(len(files)):
#     num = 0
#     print('*'*30, 'Currently working space=> ', os.path.join(dirPath,files[i]), '*'*30)
#     f=open(os.path.join(dirPath,files[i]),'r') #開啟檔案(path.join(合成路徑+檔名))
#     reader=csv.reader(f)
#     for line in reader: #讀取特定某一行後面所有的資料
#         num += 1
#         # my_array[0][i] = files[i]
#         if num >9:      #從第9行開始讀取
#             for row, rowValue in enumerate(reader):         #enumerate()蝶代<類似for只是前面宣告兩個變數第一個變數為計數器>
#                 # print('ROW {:<5} I {:<5}'.format(row,i))
#                 my_array[row][i] = float(rowValue[2]) / 100#將數值去掉100%
#             # if sizeOfRows !=228:
#             #     print('File {:<9} rows {:<4}'.format(files[i], sizeOfRows))
#
#
#
# f.close()
# my_array_name = np.array(files)
# # print(my_array_name)
# c = np.vstack((my_array_name,my_array))
# print(type(c[5][0]))
# np.savetxt('20190417(NIL)fungus_sick_12.csv', c,fmt='%s', delimiter=',') #輸出成csv檔
#
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#xlsx 轉 csv
#
#
# IN_dirPath = r"C:\Users\Raywang\Desktop\tomato\20190417(VL)fungus\sick"   #輸入檔案路徑
# # OUT_dirPath = r"C:\Users\Raywang\Desktop\123"   #輸出檔案路徑
# FILES_NAME=os.listdir(IN_dirPath)
# print(FILES_NAME)
# csv="csv"
# for i in range(len(FILES_NAME)):
#     data_xls = pd.read_excel(os.path.join(IN_dirPath,FILES_NAME[i]), index_col=None) #讀取excel
#     print("123")
#     if FILES_NAME[i].__len__()==18:  #刪除字串中的.xlsx  字串長度==18
#         FILES_NAME[i]=FILES_NAME[i][:13]+FILES_NAME[i][18:]
#         print("---------1")
#     elif FILES_NAME[i].__len__()==19: #刪除字串中的.xlsx  字串長度==19
#         FILES_NAME[i] = FILES_NAME[i][:14] + FILES_NAME[i][19:]
#         print("---------2")
#     elif FILES_NAME[i].__len__()==10:
#         FILES_NAME[i] = FILES_NAME[i][:6] + FILES_NAME[i][11:]
#         FILES_NAME[i] = FILES_NAME[i] + csv
#         print("---------10.csv")
#     elif FILES_NAME[i].__len__()==11:
#         FILES_NAME[i] = FILES_NAME[i][:7] + FILES_NAME[i][12:]
#         FILES_NAME[i] = FILES_NAME[i] + csv
#         print("---------11.csv")
#     elif FILES_NAME[i].__len__()==20:#刪除字串中的.xlsx  字串長度==20
#         FILES_NAME[i] = FILES_NAME[i][:12] + FILES_NAME[i][20:]
#         FILES_NAME[i] = FILES_NAME[i] + csv
#         print("---------12.csv")
#     elif FILES_NAME[i].__len__()==21:#刪除字串中的.xlsx  字串長度==21
#         FILES_NAME[i] = FILES_NAME[i][:13] + FILES_NAME[i][21:]
#         FILES_NAME[i] = FILES_NAME[i] + csv
#         print("---------13.csv")
#     else:                       #刪除字串中的.xlsx  字串長度==17
#         FILES_NAME[i] = FILES_NAME[i][:12] + FILES_NAME[i][17:]
#         print("---------3")
#     data_xls.to_csv(os.path.join(OUT_dirPath,FILES_NAME[i]),encoding='utf-8')       #轉檔成.cvs
