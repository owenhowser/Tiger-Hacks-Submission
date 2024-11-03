#first lines are the questions
corn = int(input("How much, in percent, do you want in corn? (for percent, use 40, not .40 for percentage <3)" ))
corn2=(100-corn)
print("You have", (corn2), " percent remaining")
wheat = int(input("How much, in percent, do you want in wheat?" ))
wheat2=(100-corn-wheat)
print("You have", (wheat2), " percent remaining")
rice = int(input("How much, in percent, do you want in rice?" ))
rice2=(100-corn-wheat-rice)
print("You have", (rice2), "percent remaining")
peanut = int(input("How much, in percent, do you want in peanuts?"))
peanut2=(100-corn-wheat-rice-peanut)
print("You have", (peanut2), "percent remaining")
cotton= int(input("How much, in percent, do you want in cotton?"))
cotton2=(100-corn-wheat-rice-peanut-cotton)
print("You have", (cotton2), "percent remaining")
soybeans= int(input("How much, in percent, do you want in soybeans?"))
land = int(input("How many acres of land do you have or wanting to use?"))
if (corn+wheat+peanut+cotton+soybeans+rice)!=100:
    print("These do not equal 100 percent")    
    exit(0)
#next lines are the equations
dollarsmade = (land*((corn*911)+(rice*1243)+(wheat*431)+(peanut*1199)+(cotton*876))+(soybeans*621))/100
newcorn=(land*corn*911)/100
newwheat=(land*wheat*431)/100
newrice=(land*rice*1243)/100
newpeanut=(land*peanut*1199)/100
newcotton=(land*cotton*876)/100
newsoybeans=(land*soybeans*621)/100
#these lines are the equations giving totals
print("You can make", (dollarsmade), "dollars total from farming.")
print("You can make", (newcorn), "dollars total from wheat.")
print("You can make", (newwheat), "dollars total from wheat.")
print("You can make", (newrice), "dollars total from rice.")
print("You can make", (newpeanut), "dollars total from peanut.")
print("You can make", (newcotton), "dollars total from cotton.")
print("You can make", (newsoybeans), "dollars total from soybeans.")
