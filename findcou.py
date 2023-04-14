import cv2 as cv
import numpy as np
import tifffile
import os
path1 = r"D:\DOWN\jqc\dataset_rna_0823\img_1024"
path2 = r"D:\DOWN\jqc\dataset_rna_0823\aug\mask"
path3 = r"D:\DOWN\jqc\dataset_rna_0823\aug\img"
path4 = r"D:\DOWN\jqc\dataset_rna_0823\mask2"
path5 = r"D:\DOWN\jqc\dataset_rna_0823\txt"
imgs = os.listdir(path3)
imgs2 = os.listdir(path2)
imgs.sort()
imgs2.sort()
# print(imgs)
# print(imgs2)
# for i in imgs2:
#     if i.replace("_tissue_cut.tif",".tif") not in imgs:
#         print(i)
#         os.remove(path2 + "/" + i)


for i, j in zip(imgs, imgs2):
    img = cv.imread(path3 + "/" + i,0)
    img = cv.resize(img, (1024,1024))
    img2 = cv.imread(path2 + "/" + j,0)
    img2 = cv.resize(img2, (1024, 1024))
    contours, _ = cv.findContours(img2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    # cv.imwrite(r"D:\DOWN\jqc\dataset_rna_0823\aug" + "/" + i,img)
    # cv.imwrite(path4 + "/" + i.replace("_tissue_cut.tif", ".png"), img2)
    with open(r"D:\DOWN\jqc\dataset_rna_0823\aug\txt" + "/" + j.replace(".png", ".txt"), "w") as file1:
        for w in contours:
            a = w/1024
            b = a.flatten()
            fan = ""
            for k in b:
                fan = fan + str(k) + " "
            text = "0 " + fan + "\n"
            file1.writelines(text)
            # print(str(b).replace("[","").replace("]",""))