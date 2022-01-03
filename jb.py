# import os
# import pyautogui as pg
# import time
# import datetime as dt
# import tkinter.messagebox as tsmg
# import os


# def greet():

#     tsmg.showinfo("Your exam is starting soon, be ready")
#     time.sleep(1)
#     os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

#     time.sleep(3)
#     pg.keyDown('w')
#     pg.keyDown('enter')
#     pg.leftClick()

para = '''Once, there was a boy who became bored when he watched over the village sheep grazing on the hillside. To entertain himself, he sang out, “Wolf! Wolf! The wolf is chasing the sheep!”
When the villagers heard the cry, they came running up the hill to drive the wolf away. But, when they arrived, they saw no wolf. The boy was amused when seeing their angry faces.
Dont scream wolf, boy,” warned the villagers, “when there is no wolf!” They angrily went back down the hill.
Later, the shepherd boy cried out once again, “Wolf! Wolf! The wolf is chasing the sheep!” To his amusement, he looked on as the villagers came running up the hill to scare the wolf away.
As they saw there was no wolf, they said strictly, “Save your frightened cry for when there really is a wolf! when there is no wolf!” But the boy grinned at their words while they walked grumbling down the hill once more.
Later, the boy saw a real wolf sneaking around his flock. Alarmed, he jumped on his feet and cried out as loud as he could, “Wolf! Wolf!” But the villagers thought he was fooling them again, and so they didn’t come to help.
At sunset, the villagers went looking for the boy who  returned with their sheep. When they went up the hill, they found him weeping.
“There really was a wolf here! The flock is gone! I cried out'''

para = para.lower()
para = para.replace(',', '')
para = para.replace('“','')
para = para.replace('!', '')
para= para.replace('.', '')
para = para.replace('”','')
# para = para.replace('i', '')
print(para)




        


