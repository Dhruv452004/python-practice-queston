'''
 Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.
'''

name = "lloohaadon"


for naam in name:
    if(name.count(naam)==1): # ==1 ka mtlb h ki ye sirf vo character print krega jo 1 baar aya h
        print(naam)
        break 
        # break use krne se jo sabse phele non-repeat character hoga vo print krega aur loop rok dega

