inp1.info()
inp1.loc[inp1['09-12-2013']== 'Removed',"09-12-2013"] = np.NaN

inp1.loc[inp1['14-09-2013']== 'removed',"14-09-2013"] = np.NaN

inp1.loc[inp1['16-09-2013']== 'removed',"16-09-2013"] = np.NaN

inp1.loc[inp1['18-09-2013']== 'removed',"18-09-2013"] = np.NaN

inp1.loc[inp1['20-09-2013']== 'removed',"20-09-2013"] = np.NaN

inp1.loc[inp1['22-09-2013']== 'Orders',"22-09-2013"] = np.NaN
inp1= inp1.drop(["26-09-2013"] , axis= 1)

inp1= inp1.drop(["30-09-2013"] , axis= 1)

inp1= inp1.drop(["10-02-2013"] , axis= 1)

inp1= inp1.drop(["10-04-2013"] , axis= 1)

inp1= inp1.drop(["10-08-2013"] , axis= 1)
# group
inp1["24-09-2013"]=inp1["24-09-2013"].apply(lambda x: float(x))
inp1["Summer"]=inp1["29-08-2013"]+inp1["31-08-2013"]+inp1["09-08-2013"]+inp1["10-06-2013"]+inp1["09-06-2013"]
inp1["Autumn"]=inp1["09-10-2013"]+inp1["16-09-2013"]+inp1["14-09-2013"]+inp1["18-09-2013"]+inp1["20-09-2013"]+inp1["22-09-2013"]+inp1["24-09-2013"]+inp1["28-09-2013"]
inp1["Winter"]=inp1["10-12-2013"]+inp1["09-12-2013"]+inp1["09-02-2013"]
inp1["Spring"]=inp1["09-04-2013"]


#irrgegular
inp0.Season= inp0.Season.replace('Automn', "Autumn")

inp0.Season= inp0.Season.replace('spring', "Spring")

inp0.Season= inp0.Season.replace('winter', "Winter")

#irregular 2
inp0.SleeveLength= inp0.SleeveLength.replace(['cap-sleeves', 'capsleeves'], "cap sleeves")

inp0.SleeveLength= inp0.SleeveLength.replace('full', "full sleeves")

inp0.SleeveLength= inp0.SleeveLength.replace(['half','halfsleeve'], "half sleeves")

inp0.SleeveLength= inp0.SleeveLength.replace(['sleevless', 'sleeevless', 'sleeveless', 'sleveless'], "sleeve less")

inp0.SleeveLength= inp0.SleeveLength.replace(['threequarter','threequater', 'thressqatar'], "three quater")

inp0.SleeveLength= inp0.SleeveLength.replace(['turndowncollor','urndowncollor'], "turn down collar")
