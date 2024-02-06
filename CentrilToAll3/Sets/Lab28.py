#Few more important operations in sets

# isdisjoint()returns the boolean values based on the provided inputs. If no common elements in the sets then output is True, else False
set1={"Struggle","Sacrifice","Hardwork","Failures","Passion","Patience"}
set2={"Frustration","Depression","Realisation","Justification"}
print(set1.isdisjoint(set2))
#Adding list to set
print(set1.isdisjoint(["Sacrifice","Transition","Recession"]))


# issubset() returns the boolean values based on the provided inputs. If no similar elements in the sets then the output is False, else True
set3={"Struggle","Sacrifice","Hardwork","Failures","Passion","Patience"}
print(set3.issubset(set1))
print(set2.issubset(set3))
#Same operation can be done in the way
print(set3<=set1)
#Adding list to set
print(set3.issubset(["Sacrifice","Health","wealth","Failures","Passion","Patience"]))


# issuperset()returns the boolean values based on the provided inputs. If  common elements in the sets then output is True, else False
set4={"Frustration","Justification",}
print(set2.issuperset(set4))
#Same operation using different method
print(set2>=set4)